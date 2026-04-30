import csv
from pathlib import Path

from simulator.hydrogen_shell_simulator import transition_wavelength_nm

REFERENCE_COLUMNS = {
    "series",
    "transition",
    "n_i",
    "n_f",
    "wavelength_nm",
    "medium",
    "source",
    "source_url",
    "source_access_date",
    "source_table_or_query",
    "notes",
}
REFERENCE_DATA_PATH = Path(__file__).resolve().parents[1] / "data" / "hydrogen_reference_lines.csv"


def load_reference_wavelengths(path: Path = REFERENCE_DATA_PATH) -> dict[tuple[int, int], dict]:
    with path.open("r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        if reader.fieldnames is None or not REFERENCE_COLUMNS.issubset(set(reader.fieldnames)):
            missing = REFERENCE_COLUMNS - set(reader.fieldnames or [])
            raise ValueError(f"Missing required reference columns: {sorted(missing)}")

        references: dict[tuple[int, int], dict] = {}
        for row in reader:
            n_i = int(row["n_i"])
            n_f = int(row["n_f"])
            references[(n_i, n_f)] = {
                "wavelength_nm": float(row["wavelength_nm"]),
                "medium": row["medium"],
                "source": row["source"],
                "source_url": row["source_url"],
                "source_access_date": row["source_access_date"],
                "source_table_or_query": row["source_table_or_query"],
                "notes": row["notes"],
                "series": row["series"],
                "transition": row["transition"],
            }
    return references


def _series(n_f: int, n_max: int, series_name: str) -> list[dict]:
    refs = load_reference_wavelengths()
    rows = []
    for n_i in range(n_f + 1, n_max + 1):
        predicted_nm = transition_wavelength_nm(n_i, n_f)
        ref = refs.get((n_i, n_f))
        reference_nm = None if ref is None else ref["wavelength_nm"]
        if reference_nm is None:
            error_nm = None
            relative_error_ppm = None
            medium = None
            source = None
        else:
            error_nm = predicted_nm - reference_nm
            relative_error_ppm = (error_nm / reference_nm) * 1_000_000
            medium = ref["medium"]
            source = ref["source"]
        rows.append(
            {
                "series": series_name,
                "transition": f"{n_i}->{n_f}",
                "predicted_nm": predicted_nm,
                "reference_nm": reference_nm,
                "medium": medium,
                "source": source,
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
