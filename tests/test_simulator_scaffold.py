from pathlib import Path
import csv
import subprocess
import sys

import pytest

from simulator.fine_structure import h_alpha_components
from simulator.hydrogen_shell_simulator import (
    RYDBERG_EV,
    allowed_dipole_channels,
    angular_states,
    shell_table,
)
from simulator.shell_locking_test import run_shell_locking_test
from simulator.spectral_comparison import balmer_series, load_reference_wavelengths


def test_shell_table_values():
    rows = shell_table(5)
    for row in rows:
        n = row["n"]
        assert row["K"] == n - 1
        assert row["s2"] == 2 * n
        assert row["degeneracy"] == n**2
        assert abs(row["energy_eV"] - (-RYDBERG_EV / (n**2))) < 1e-12


def test_reference_csv_exists_and_schema_valid():
    p = Path("data/hydrogen_reference_lines.csv")
    assert p.exists()
    with p.open("r", encoding="utf-8", newline="") as f:
        r = csv.DictReader(f)
        expected = {"series", "transition", "n_i", "n_f", "wavelength_nm", "medium", "source", "source_version_or_access_date", "notes"}
        assert expected.issubset(set(r.fieldnames or []))
        rows = list(r)
        assert rows
        assert all(row["medium"] for row in rows)
        assert all(row["source"] for row in rows)


def test_spectral_comparison_loads_from_csv_and_missing_graceful():
    refs = load_reference_wavelengths()
    assert (3, 2) in refs
    rows = balmer_series(n_max=8)
    row_8_2 = [r for r in rows if r["transition"] == "8->2"][0]
    assert row_8_2["reference_nm"] is None
    assert row_8_2["error_nm"] is None


def test_angular_states_count():
    for n in range(1, 7):
        assert len(angular_states(n)) == n**2


def test_allowed_dipole_channels_3_to_2():
    channels = allowed_dipole_channels(3, 2)
    tuples = {(c["ell_i"], c["ell_f"]) for c in channels}
    assert (0, 1) in tuples
    assert (1, 0) in tuples
    assert (2, 1) in tuples


def test_balmer_alpha_near_656nm():
    rows = balmer_series(n_max=3)
    assert abs(rows[0]["predicted_nm"] - 656.0) < 1.0


def test_shell_locking_expectation_close():
    rows = run_shell_locking_test(K_max=3)
    for row in rows:
        assert abs(row["error"]) < 0.1


def test_h_alpha_components_sorted_nonempty():
    rows = h_alpha_components()
    assert rows
    wavelengths = [r["wavelength_nm"] for r in rows]
    assert wavelengths == sorted(wavelengths)


def test_doc_integrity_notes_and_claims_matrix():
    ap = Path("notes/angular_projection_s3_to_s2.md").read_text(encoding="utf-8")
    for token in ["S^3", "S^2", "H_K", "n^2", "angular projection"]:
        assert token in ap

    ls = Path("notes/layer_separation.md").read_text(encoding="utf-8")
    assert "Standard hydrogen benchmark layer" in ls
    assert "Native RQM/QSG bridge layer" in ls

    cm = Path("docs/claims_matrix.md").read_text(encoding="utf-8")
    assert "Native derivation of Rydberg constant" in cm
    assert "Heavier element extension" in cm


def test_report_generation_runs():
    subprocess.run([sys.executable, "scripts/generate_reports.py"], check=True)
    assert Path("reports/HYDROGEN_BRIDGE_V1_REPORT.md").exists()


def test_plot_generation_runs_or_skips():
    matplotlib = pytest.importorskip("matplotlib")
    assert matplotlib
    subprocess.run([sys.executable, "scripts/generate_plots.py"], check=True)
    expected = [
        "shell_locking_potential_K0_K5.png",
        "shell_locking_expectation_vs_target.png",
        "shell_locking_error.png",
        "hydrogen_energy_ladder.png",
        "transition_wavelength_comparison.png",
    ]
    for name in expected:
        assert Path("reports/plots") .joinpath(name).exists()
