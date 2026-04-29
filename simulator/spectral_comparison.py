from simulator.hydrogen_shell_simulator import transition_wavelength_nm

REFERENCE_WAVELENGTH_NM = {
    (2, 1): 121.567,
    (3, 1): 102.572,
    (4, 1): 97.254,
    (5, 1): 94.974,
    (6, 1): 93.780,
    (3, 2): 656.281,
    (4, 2): 486.133,
    (5, 2): 434.047,
    (6, 2): 410.174,
    (7, 2): 397.007,
    (4, 3): 1875.627,
    (5, 3): 1281.807,
    (6, 3): 1093.807,
    (7, 3): 1004.938,
    (8, 3): 954.621,
}


def _series(n_f: int, n_max: int, series_name: str) -> list[dict]:
    rows = []
    for n_i in range(n_f + 1, n_max + 1):
        predicted_nm = transition_wavelength_nm(n_i, n_f)
        reference_nm = REFERENCE_WAVELENGTH_NM.get((n_i, n_f))
        if reference_nm is None:
            error_nm = None
            relative_error_ppm = None
        else:
            error_nm = predicted_nm - reference_nm
            relative_error_ppm = (error_nm / reference_nm) * 1_000_000
        rows.append(
            {
                "series": series_name,
                "transition": f"{n_i}->{n_f}",
                "predicted_nm": predicted_nm,
                "reference_nm": reference_nm,
                "error_nm": error_nm,
                "relative_error_ppm": relative_error_ppm,
            }
        )
    return rows


def lyman_series(n_max: int = 6) -> list[dict]:
    return _series(1, n_max, "Lyman")


def balmer_series(n_max: int = 7) -> list[dict]:
    return _series(2, n_max, "Balmer")


def paschen_series(n_max: int = 8) -> list[dict]:
    return _series(3, n_max, "Paschen")


def all_series_tables() -> list[dict]:
    return lyman_series() + balmer_series() + paschen_series()
