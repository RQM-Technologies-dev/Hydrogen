import csv
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from simulator.fine_structure import h_alpha_components
from simulator.hopf_flux_projection import flux_scaling_diagnostics, projection_statistics
from simulator.hydrogen_shell_simulator import angular_states, shell_table
from simulator.shell_locking_test import run_shell_locking_test
from simulator.spectral_comparison import REFERENCE_DATA_PATH, all_series_tables

REPORTS_DIR = Path("reports")
PLOTS_DIR = REPORTS_DIR / "plots"


def write_csv(path: Path, rows: list[dict]) -> None:
    if not rows:
        return
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def to_markdown_table(rows: list[dict], columns: list[str], float_digits: int = 6) -> list[str]:
    lines = ["| " + " | ".join(columns) + " |", "| " + " | ".join(["---"] * len(columns)) + " |"]
    for row in rows:
        values = []
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
    hopf_stats = [projection_statistics(count=10000, seed=0)]
    hopf_flux = flux_scaling_diagnostics()

    write_csv(REPORTS_DIR / "shell_table.csv", shell_rows)
    write_csv(REPORTS_DIR / "angular_state_counts.csv", angular_counts)
    write_csv(REPORTS_DIR / "series_comparison.csv", series_rows)
    write_csv(REPORTS_DIR / "shell_locking_validation.csv", locking_rows)
    write_csv(REPORTS_DIR / "h_alpha_fine_structure.csv", h_alpha_rows)
    write_csv(REPORTS_DIR / "hopf_projection_statistics.csv", hopf_stats)
    write_csv(REPORTS_DIR / "hopf_flux_scaling.csv", hopf_flux["rows"])

    plots = sorted([p.name for p in PLOTS_DIR.glob("*.png")]) if PLOTS_DIR.exists() else []
    plot_note = [f"- `{name}`" for name in plots] if plots else ["Plots not found. Run `python scripts/generate_plots.py` to generate `reports/plots/*.png`."]

    md = [
        "# HYDROGEN BRIDGE V1 REPORT",
        "",
        "This report summarizes a calibrated bridge, numerical shell-locking validation, and benchmark against hydrogen spectral architecture.",
        "",
        "## Layer separation",
        "Standard benchmark formulas/data are separated from native RQM/QSG bridge structures; see `notes/layer_separation.md`.",
        "",
        "## Reference wavelength provenance",
        f"Reference lines are loaded from `{REFERENCE_DATA_PATH.relative_to(ROOT)}` with medium metadata (air/vacuum) and source fields.",
        "Current dataset values are labeled legacy benchmark rows pending authoritative verification; see `data/hydrogen_reference_lines_provenance.md` for manual NIST ASD replacement steps.",
        "",
        "## Claims matrix",
        "Status and honesty boundaries are tracked in `docs/claims_matrix.md`.",
        "",
        "## 1. Shell table (n=1..8)",
        *to_markdown_table(shell_rows, ["n", "K", "s2", "s", "degeneracy", "energy_eV"]),
        "",
        "## 2. Angular state count table",
        *to_markdown_table(angular_counts, ["n", "state_count", "expected"]),
        "",
        "## 3. Lyman/Balmer/Paschen comparison table",
        *to_markdown_table(series_rows, ["series", "transition", "predicted_nm", "reference_nm", "medium", "source", "error_nm", "relative_error_ppm"]),
        "",
        "## 4. Shell-locking validation table",
        *to_markdown_table(locking_rows, ["K", "target_x", "expectation_x", "error", "variance_x", "eigenvalue_0"]),
        "",
        "## 5. H-alpha fine-structure table",
        *to_markdown_table(h_alpha_rows, ["label", "delta_E_eV", "wavelength_nm"]),
        "",
        "",
        "## 6. Hopf flux projection diagnostics",
        "These diagnostics test the projected-flux scaling layer only; they do not constitute a full derivation of electromagnetism.",
        *to_markdown_table(hopf_stats, ["count", "mean_norm", "max_norm_error", "mean_x", "mean_y", "mean_z", "second_moment_x", "second_moment_y", "second_moment_z"]),
        "",
        f"- Field log-log slope: {hopf_flux['field_slope']:.12f}",
        f"- Potential log-log slope: {hopf_flux['potential_slope']:.12f}",
        f"- Max flux reconstruction error: {hopf_flux['max_flux_error']:.12e}",
        "",
        *to_markdown_table(hopf_flux["rows"], ["r", "area", "field", "potential", "reconstructed_flux"]),
        "## 7. Generated plots",
        *plot_note,
        "",
        "## 8. Limitations",
        "- This implementation is a calibrated bridge and does not claim a first-principles derivation of the Rydberg constant.",
        "- Scope remains hydrogen; heavier elements are out of scope for v1.",
        "- Fine structure is benchmarked with a standard correction formula; native derivation is future work.",
    ]
    (REPORTS_DIR / "HYDROGEN_BRIDGE_V1_REPORT.md").write_text("\n".join(md), encoding="utf-8")


if __name__ == "__main__":
    main()
