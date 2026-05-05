import csv
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from simulator.fine_structure import h_alpha_components
from simulator.hopf_flux_projection import flux_scaling_diagnostics, projection_statistics
from simulator.angular_operators import l2_compatibility_diagnostics, rank1_transition_diagnostics
from simulator.hydrogen_shell_simulator import angular_states, shell_table
from simulator.shell_locking_test import run_shell_locking_test
from simulator.s3_s2_intertwiner import lz_compatibility_diagnostics, pi_k_orthonormality_diagnostics
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
    pi_k_rows = []
    l2_rows = []
    for K in range(6):
        ortho = pi_k_orthonormality_diagnostics(K)
        lz = lz_compatibility_diagnostics(K)
        l2 = l2_compatibility_diagnostics(K)
        pi_k_rows.append(
            {
                "K": K,
                "dimension": ortho["dimension"],
                "row_orthonormality_error": ortho["row_orthonormality_error"],
                "column_orthonormality_error": ortho["column_orthonormality_error"],
                "lz_mismatch_error": lz["max_mismatch_abs"],
            }
        )
        l2_rows.append(
            {
                "K": K,
                "dimension": l2["dimension"],
                "l2_intertwining_error": l2["l2_intertwining_error"],
                "l2_source_symmetry_error": l2["l2_source_symmetry_error"],
            }
        )
    rank1_rows = []
    for K_i, K_f in [(2, 1), (3, 2), (4, 3)]:
        rank1_rows.extend(rank1_transition_diagnostics(K_i, K_f))

    write_csv(REPORTS_DIR / "shell_table.csv", shell_rows)
    write_csv(REPORTS_DIR / "angular_state_counts.csv", angular_counts)
    write_csv(REPORTS_DIR / "series_comparison.csv", series_rows)
    write_csv(REPORTS_DIR / "shell_locking_validation.csv", locking_rows)
    write_csv(REPORTS_DIR / "h_alpha_fine_structure.csv", h_alpha_rows)
    write_csv(REPORTS_DIR / "hopf_projection_statistics.csv", hopf_stats)
    write_csv(REPORTS_DIR / "hopf_flux_scaling.csv", hopf_flux["rows"])
    write_csv(REPORTS_DIR / "pi_k_ang_diagnostics.csv", pi_k_rows)
    write_csv(REPORTS_DIR / "pi_k_l2_diagnostics.csv", l2_rows)
    write_csv(REPORTS_DIR / "rank1_transition_diagnostics.csv", rank1_rows)

    plots = sorted([p.name for p in PLOTS_DIR.glob("*.png")]) if PLOTS_DIR.exists() else []
    plot_note = [f"- `{name}`" for name in plots] if plots else ["Plots not found. Run `python scripts/generate_plots.py` to generate `reports/plots/*.png`."]

    md = [
        "# HYDROGEN BRIDGE V1 REPORT",
        "",
        "This report summarizes the core S^3 spectral bridge, validation artifacts, and support diagnostics.",
        "",
        "## Core S^3 spectral result",
        "H_C = -Ry/(-Delta_{S^3}+1)",
        "",
        "E_n = -Ry/n^2",
        "",
        "dim H_{n-1}(S^3)=n^2",
        "",
        "Status and honesty boundaries are tracked in `docs/claims_matrix.md`.",
        "Layer separation is documented in `notes/layer_separation.md`.",
        "",
        "## Core validation tables",
        "Reference lines are loaded from `" + str(REFERENCE_DATA_PATH.relative_to(ROOT)) + "` with medium metadata (air/vacuum) and source fields.",
        "Reference wavelengths are sourced from NIST ASD H I Lines Data for the current Lyman/Balmer/Paschen subset, with explicit air/vacuum medium metadata and access-date provenance. Future work may add uncertainty columns, exact level labels, and broader line coverage.",
        "",
        "### 1. Shell table",
        *to_markdown_table(shell_rows, ["n", "K", "s2", "s", "degeneracy", "energy_eV"]),
        "",
        "### 2. Angular state count table",
        *to_markdown_table(angular_counts, ["n", "state_count", "expected"]),
        "",
        "The wavelength comparison is a benchmark sanity check for the calibrated shell-energy law; residuals reflect the simplified v1 energy model and are not claimed as precision spectroscopy fits.",
        "",
        "### 3. Lyman/Balmer/Paschen comparison table",
        *to_markdown_table(series_rows, ["series", "transition", "predicted_nm", "reference_nm", "medium", "source", "error_nm", "relative_error_ppm"]),
        "",
        "### 4. Shell-locking validation table",
        *to_markdown_table(locking_rows, ["K", "target_x", "expectation_x", "error", "variance_x", "eigenvalue_0"]),
        "",
        "### 5. Π_K^ang low-K diagnostics",
        *to_markdown_table(pi_k_rows, ["K", "dimension", "row_orthonormality_error", "column_orthonormality_error", "lz_mismatch_error"]),
        "",
        "### Π_K^ang L² compatibility diagnostics",
        *to_markdown_table(l2_rows, ["K", "dimension", "l2_intertwining_error", "l2_source_symmetry_error"]),
        "",
        "### Rank-1 angular transition operator diagnostics",
        "The rank-1 operator here is angular-only and normalized for compatibility testing; it does not include radial matrix elements or oscillator strengths.",
        *to_markdown_table(rank1_rows, ["K_i", "K_f", "q", "target_nonzero_count", "s3_nonzero_count", "intertwining_error"]),
        "",
        "## Benchmark/support tables",
        "",
        "### H-alpha fine-structure benchmark",
        "This is a standard benchmark correction, not a native fine-structure derivation.",
        *to_markdown_table(h_alpha_rows, ["label", "delta_E_eV", "wavelength_nm"]),
        "",
        "## Appendix diagnostics",
        "",
        "### Hopf flux projection diagnostics",
        "These diagnostics test a projected-flux support layer only and are not part of the core S^3 spectral claim.",
        *to_markdown_table(hopf_stats, ["count", "mean_norm", "max_norm_error", "mean_x", "mean_y", "mean_z", "second_moment_x", "second_moment_y", "second_moment_z"]),
        "",
        f"- Field log-log slope: {hopf_flux['field_slope']:.12f}",
        f"- Potential log-log slope: {hopf_flux['potential_slope']:.12f}",
        f"- Max flux reconstruction error: {hopf_flux['max_flux_error']:.12e}",
        "",
        *to_markdown_table(hopf_flux["rows"], ["r", "area", "field", "potential", "reconstructed_flux"]),
        "",
        "## Generated plots",
        *plot_note,
        "",
        "## Limitations",
        "- This implementation is a calibrated bridge and does not claim a first-principles derivation of the Rydberg constant.",
        "- Scope remains hydrogen; heavier elements are out of scope for v1.",
        "- Fine structure is benchmarked with a standard correction formula; native derivation is future work.",
    ]
    (REPORTS_DIR / "HYDROGEN_BRIDGE_V1_REPORT.md").write_text("\n".join(md), encoding="utf-8")


if __name__ == "__main__":
    main()
