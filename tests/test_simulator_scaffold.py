import math

from simulator.hydrogen_shell_simulator import shell_table, angular_states, transitions
from simulator.spectral_comparison import lyman_series, balmer_series, paschen_series
from simulator.shell_locking_test import run_shell_locking_test
from simulator.fine_structure import energy_fine_structure, h_alpha_components


def test_shell_table_basic():
    rows = shell_table(3)
    assert len(rows) == 3
    assert rows[1]["n"] == 2
    assert rows[1]["degeneracy"] == 4


def test_angular_states_count():
    states = angular_states(3)
    assert len(states) == 9
    assert (2, -2) in states and (2, 2) in states


def test_transitions_nonempty():
    rows = transitions(3)
    assert any(r["n_i"] == 3 and r["n_f"] == 2 for r in rows)


def test_series_tables_populate():
    assert len(lyman_series()) > 0
    assert len(balmer_series()) > 0
    assert len(paschen_series()) > 0


def test_shell_locking_runs():
    rows = run_shell_locking_test(K_max=2, grid_points=120)
    assert len(rows) == 3
    assert all("numerical" in r for r in rows)


def test_energy_fine_structure_runs():
    e = energy_fine_structure(n=2, j=0.5)
    assert e < 0


def test_h_alpha_components():
    rows = h_alpha_components()
    assert len(rows) == 6
    assert all(r["lam"] > 0 for r in rows)
    assert math.isfinite(rows[0]["delta_E"])
