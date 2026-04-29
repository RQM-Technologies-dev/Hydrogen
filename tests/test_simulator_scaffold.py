from pathlib import Path
import subprocess
import sys

from simulator.fine_structure import h_alpha_components
from simulator.hydrogen_shell_simulator import (
    RYDBERG_EV,
    allowed_dipole_channels,
    angular_states,
    shell_table,
)
from simulator.shell_locking_test import run_shell_locking_test
from simulator.spectral_comparison import balmer_series


def test_shell_table_values():
    rows = shell_table(5)
    for row in rows:
        n = row["n"]
        assert row["K"] == n - 1
        assert row["s2"] == 2 * n
        assert row["degeneracy"] == n**2
        assert abs(row["energy_eV"] - (-RYDBERG_EV / (n**2))) < 1e-12


def test_angular_states_count():
    for n in range(1, 7):
        assert len(angular_states(n)) == n**2


def test_allowed_dipole_channels_3_to_2():
    channels = allowed_dipole_channels(3, 2)
    tuples = {(c["ell_i"], c["ell_f"]) for c in channels}
    assert (0, 1) in tuples
    assert (1, 0) in tuples
    assert (2, 1) in tuples
    assert (0, 0) not in tuples
    assert (2, 0) not in tuples


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
    assert all(650 < w < 660 for w in wavelengths)


def test_report_generation_runs():
    subprocess.run([sys.executable, "scripts/generate_reports.py"], check=True)
    assert Path("reports/HYDROGEN_BRIDGE_V1_REPORT.md").exists()


def test_report_contains_markdown_tables():
    subprocess.run([sys.executable, "scripts/generate_reports.py"], check=True)
    report = Path("reports/HYDROGEN_BRIDGE_V1_REPORT.md").read_text(encoding="utf-8")
    assert "| n | K |" in report
    assert "| series | transition |" in report
    assert "| K | target_x | expectation_x |" in report
    assert "| label |" in report
