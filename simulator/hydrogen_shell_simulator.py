import math

RYDBERG_EV = 13.605693122994
HC_EV_NM = 1239.8419843320026
PLANCK = 6.62607015e-34
LIGHT_SPEED = 299792458.0
EV_TO_J = 1.602176634e-19


def shell_table(n_max: int) -> list[dict]:
    if n_max < 1:
        raise ValueError("n_max must be >= 1")
    rows = []
    for n in range(1, n_max + 1):
        s2 = 2 * n
        rows.append(
            {
                "n": n,
                "K": n - 1,
                "s2": float(s2),
                "s": math.sqrt(s2),
                "degeneracy": n**2,
                "energy_eV": -RYDBERG_EV / (n**2),
            }
        )
    return rows


def angular_states(n: int) -> list[dict]:
    if n < 1:
        raise ValueError("n must be >= 1")
    K = n - 1
    states = []
    for ell in range(0, n):
        for m in range(-ell, ell + 1):
            states.append({"n": n, "K": K, "ell": ell, "m": m})
    return states


def allowed_dipole_channels(n_i: int, n_f: int) -> list[dict]:
    if n_i <= n_f:
        raise ValueError("Require n_i > n_f for emission channels")

    channels = []
    for state_i in angular_states(n_i):
        for state_f in angular_states(n_f):
            delta_ell = state_f["ell"] - state_i["ell"]
            delta_m = state_f["m"] - state_i["m"]
            if delta_ell in (-1, 1) and delta_m in (-1, 0, 1):
                channels.append(
                    {
                        "ell_i": state_i["ell"],
                        "m_i": state_i["m"],
                        "ell_f": state_f["ell"],
                        "m_f": state_f["m"],
                        "delta_ell": delta_ell,
                        "delta_m": delta_m,
                    }
                )
    return channels


def transition_energy_eV(n_i: int, n_f: int) -> float:
    if n_i <= n_f:
        raise ValueError("Require n_i > n_f")
    return RYDBERG_EV * ((1.0 / (n_f**2)) - (1.0 / (n_i**2)))


def transition_wavelength_nm(n_i: int, n_f: int) -> float:
    return HC_EV_NM / transition_energy_eV(n_i, n_f)


def transition_summary(n_i: int, n_f: int) -> dict:
    channels = allowed_dipole_channels(n_i, n_f)
    return {
        "n_i": n_i,
        "n_f": n_f,
        "K_i": n_i - 1,
        "K_f": n_f - 1,
        "s2_i": float(2 * n_i),
        "s2_f": float(2 * n_f),
        "energy_eV": transition_energy_eV(n_i, n_f),
        "wavelength_nm": transition_wavelength_nm(n_i, n_f),
        "angular_channel_count": len(channels),
    }
