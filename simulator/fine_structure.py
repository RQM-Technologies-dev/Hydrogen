from simulator.hydrogen_shell_simulator import HC_EV_NM, RYDBERG_EV

ALPHA = 7.2973525693e-3
M_E_C2_EV = 510998.95000


def energy_fine_structure(n: int, j: float) -> float:
    if n < 1:
        raise ValueError("n must be >= 1")
    if j <= 0:
        raise ValueError("j must be positive")
    base = -RYDBERG_EV / (n**2)
    correction = (M_E_C2_EV * (ALPHA**4) / (2 * (n**3))) * ((3 / (4 * n)) - (1 / (j + 0.5)))
    return base + correction


def fine_structure_states(n: int) -> list[dict]:
    states = []
    for ell in range(0, n):
        if ell == 0:
            js = [0.5]
        else:
            js = [ell - 0.5, ell + 0.5]
        for j in js:
            states.append({"n": n, "ell": ell, "j": float(j)})
    return states


def allowed_fine_structure_channels(n_i: int, n_f: int) -> list[dict]:
    if n_i <= n_f:
        raise ValueError("Require n_i > n_f")
    channels = []
    for up in fine_structure_states(n_i):
        for lo in fine_structure_states(n_f):
            delta_ell = lo["ell"] - up["ell"]
            delta_j = lo["j"] - up["j"]
            if delta_ell in (-1, 1) and delta_j in (-1.0, 0.0, 1.0) and lo["j"] > 0:
                channels.append(
                    {
                        "n_i": n_i,
                        "ell_i": up["ell"],
                        "j_i": up["j"],
                        "n_f": n_f,
                        "ell_f": lo["ell"],
                        "j_f": lo["j"],
                        "delta_ell": delta_ell,
                        "delta_j": delta_j,
                    }
                )
    return channels


def _format_j(j: float) -> str:
    return f"{int(2*j)}/2"


def h_alpha_components() -> list[dict]:
    rows = []
    for ch in allowed_fine_structure_channels(3, 2):
        e_up = energy_fine_structure(ch["n_i"], ch["j_i"])
        e_lo = energy_fine_structure(ch["n_f"], ch["j_f"])
        delta_e = e_up - e_lo
        wavelength_nm = HC_EV_NM / abs(delta_e)
        label = (
            f"{ch['n_i']}{'spdf'[ch['ell_i']]}_{_format_j(ch['j_i'])} -> "
            f"{ch['n_f']}{'spdf'[ch['ell_f']]}_{_format_j(ch['j_f'])}"
        )
        rows.append(
            {
                "label": label,
                "n_i": ch["n_i"],
                "ell_i": ch["ell_i"],
                "j_i": ch["j_i"],
                "n_f": ch["n_f"],
                "ell_f": ch["ell_f"],
                "j_f": ch["j_f"],
                "delta_E_eV": delta_e,
                "wavelength_nm": wavelength_nm,
            }
        )
    return sorted(rows, key=lambda row: row["wavelength_nm"])
