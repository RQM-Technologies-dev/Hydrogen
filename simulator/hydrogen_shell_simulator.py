import math
from typing import Dict, List

RYDBERG_EV = 13.605693122994
PLANCK = 6.62607015e-34
LIGHT_SPEED = 299792458.0
EV_TO_J = 1.602176634e-19
RYDBERG_J = RYDBERG_EV * EV_TO_J


def shell_table(n_max: int) -> List[Dict[str, float]]:
    """Return rows: n, K, s2, s, degeneracy, energy_eV."""
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


def angular_states(n: int):
    """Return all (ℓ, m) pairs allowed for principal quantum number n."""
    if n < 1:
        raise ValueError("n must be >= 1")
    states = []
    for ell in range(0, n):
        for m in range(-ell, ell + 1):
            states.append((ell, m))
    return states


def _wavelength_for_transition(n_i: int, n_f: int) -> float:
    delta = (1.0 / (n_f**2)) - (1.0 / (n_i**2))
    if delta <= 0:
        raise ValueError("Require n_i > n_f for emission")
    return (PLANCK * LIGHT_SPEED) / (RYDBERG_J * delta)


def transitions(n_max: int):
    """Return all allowed dipole transition channels up to n_max."""
    if n_max < 2:
        return []
    out = []
    for n_i in range(2, n_max + 1):
        for n_f in range(1, n_i):
            lam = _wavelength_for_transition(n_i, n_f)
            for dl in (-1, 1):
                out.append({"n_i": n_i, "n_f": n_f, "dl": dl, "lam": lam})
    return out
