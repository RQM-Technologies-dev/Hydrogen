from simulator.hydrogen_shell_simulator import transitions

KNOWN_WAVELENGTH_M = {
    (2, 1): 121.567e-9,
    (3, 1): 102.572e-9,
    (4, 1): 97.254e-9,
    (5, 1): 94.974e-9,
    (6, 1): 93.780e-9,
    (3, 2): 656.281e-9,
    (4, 2): 486.133e-9,
    (5, 2): 434.047e-9,
    (6, 2): 410.174e-9,
    (7, 2): 397.007e-9,
    (4, 3): 1875.627e-9,
    (5, 3): 1281.807e-9,
    (6, 3): 1093.807e-9,
    (7, 3): 1004.938e-9,
    (8, 3): 954.621e-9,
}


def _series(n_f: int, n_max: int, series_name: str):
    rows = []
    all_transitions = transitions(n_max)
    seen = set()
    for row in all_transitions:
        if row["n_f"] != n_f:
            continue
        key = (row["n_i"], row["n_f"])
        if key in seen:
            continue
        seen.add(key)
        pred = row["lam"]
        known = KNOWN_WAVELENGTH_M.get(key)
        err = None if known is None else pred - known
        rows.append(
            {
                "series": series_name,
                "transition": f"{row['n_i']}->{row['n_f']}",
                "predicted_m": pred,
                "known_m": known,
                "error_m": err,
            }
        )
    return rows


def lyman_series(n_max: int = 6):
    return _series(1, n_max, "Lyman")


def balmer_series(n_max: int = 7):
    return _series(2, n_max, "Balmer")


def paschen_series(n_max: int = 8):
    return _series(3, n_max, "Paschen")
