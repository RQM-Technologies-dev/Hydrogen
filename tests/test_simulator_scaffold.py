# test_simulator_scaffold.py
#
# Smoke tests confirming the simulator scaffold is importable and that each
# public function raises NotImplementedError (i.e. the stub is in place).

import pytest

from simulator.hydrogen_shell_simulator import shell_table, angular_states, transitions
from simulator.spectral_comparison import lyman_series, balmer_series, paschen_series
from simulator.shell_locking_test import run_shell_locking_test
from simulator.fine_structure import energy_fine_structure, h_alpha_components


def test_shell_table_is_stub():
    with pytest.raises(NotImplementedError):
        shell_table(3)


def test_angular_states_is_stub():
    with pytest.raises(NotImplementedError):
        angular_states(2)


def test_transitions_is_stub():
    with pytest.raises(NotImplementedError):
        transitions(3)


def test_lyman_series_is_stub():
    with pytest.raises(NotImplementedError):
        lyman_series()


def test_balmer_series_is_stub():
    with pytest.raises(NotImplementedError):
        balmer_series()


def test_paschen_series_is_stub():
    with pytest.raises(NotImplementedError):
        paschen_series()


def test_shell_locking_test_is_stub():
    with pytest.raises(NotImplementedError):
        run_shell_locking_test(K_max=2)


def test_energy_fine_structure_is_stub():
    with pytest.raises(NotImplementedError):
        energy_fine_structure(n=2, j=0.5)


def test_h_alpha_components_is_stub():
    with pytest.raises(NotImplementedError):
        h_alpha_components()
