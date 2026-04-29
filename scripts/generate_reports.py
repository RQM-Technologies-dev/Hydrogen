import csv
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from simulator.fine_structure import h_alpha_components
from simulator.hydrogen_shell_simulator import angular_states, shell_table
from simulator.shell_locking_test import run_shell_locking_test
from simulator.spectral_comparison import all_series_tables

REPORTS_DIR = Path("reports")


def write_csv(path: Path, rows: list[dict]) -> None:
    if not rows:
        return
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def to_markdown_table(rows: list[dict], columns: list[str], float_digits: int = 6) -> list[str]:
    lines = [
        "| " + " | ".join(columns) + " |",
        "| " + " | ".join(["---"] * len(columns)) + " |",
    ]
    for row in rows:
        values: list[str] = []
        for col in columns:
            value = row.get(col)
            if isinstance(value, float):
                values.append(f"{value:.{float_digits}f}")
            elif value is None:
                values.append("")
            else:
                values.append(str(value))
        lines.append("| " + " | ".join(values) + " |")
    return lines


def main() -> None:
    REPORTS_DIR.mkdir(exist_ok=True)

    shell_rows = shell_table(8)
    angular_counts = [{"n": n, "state_count": len(angular_states(n)), "expected": n**2} for n in range(1, 9)]
    series_rows = all_series_tables()
    locking_rows = run_shell_locking_test(K_max=5)
    h_alpha_rows = h_alpha_components()

    write_csv(REPORTS_DIR / "shell_table.csv", shell_rows)
    write_csv(REPORTS_DIR / "angular_state_counts.csv", angular_counts)
    write_csv(REPORTS_DIR / "series_comparison.csv", series_rows)
    write_csv(REPORTS_DIR / "shell_locking_validation.csv", locking_rows)
    write_csv(REPORTS_DIR / "h_alpha_fine_structure.csv", h_alpha_rows)

    md = [
        "# HYDROGEN BRIDGE V1 REPORT",
        "",
        "This report summarizes a calibrated bridge, numerical shell-locking validation, and benchmark against hydrogen spectral architecture.",
        "",
        "## 1. Shell table (n=1..8)",
        *to_markdown_table(shell_rows, ["n", "K", "s2", "s", "degeneracy", "energy_eV"]),
        "",
        "## 2. Angular state count table",
        *to_markdown_table(angular_counts, ["n", "state_count", "expected"]),
        "",
        "## 3. Lyman/Balmer/Paschen comparison table",
        *to_markdown_table(series_rows, ["series", "transition", "predicted_nm", "reference_nm", "error_nm", "relative_error_ppm"]),
        "",
        "Reference wavelengths are hardcoded benchmark values for software validation; future work should replace them with a cited, versioned reference dataset and consistently distinguish air vs vacuum wavelengths.",
        "",
        "## 4. Shell-locking validation table",
        *to_markdown_table(locking_rows, ["K", "target_x", "expectation_x", "error", "variance_x", "eigenvalue_0"]),
        "",
        "## 5. H-alpha fine-structure table",
        *to_markdown_table(h_alpha_rows, ["label", "delta_E_eV", "wavelength_nm"]),
        "",
        "## 6. Limitations",
        "- This implementation is a calibrated bridge and does not claim a first-principles derivation of the Rydberg constant.",
        "- The shell-locking section is a numerical shell-locking validation over finite-difference sectors.",
        "- The spectral comparison is a benchmark against hydrogen spectral architecture, limited to hardcoded benchmark lines.",
    ]
    (REPORTS_DIR / "HYDROGEN_BRIDGE_V1_REPORT.md").write_text("\n".join(md), encoding="utf-8")


if __name__ == "__main__":
    main()
