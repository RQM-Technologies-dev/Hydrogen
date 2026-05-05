import math

import numpy as np

from simulator.clebsch_gordan import clebsch_gordan
from simulator.hydrogen_shell_simulator import allowed_dipole_channels
from simulator.s3_s2_intertwiner import (
    coupled_angular_labels,
    dipole_compatible_label_pairs,
    lz_compatibility_diagnostics,
    pi_k_ang_matrix,
    pi_k_orthonormality_diagnostics,
    uncoupled_s3_basis,
)


def test_clebsch_gordan_known_values():
    rt2 = math.sqrt(2.0)
    # This implementation keeps a consistent Condon-Shortley phase choice
    # where <1/2,1/2;1/2,1/2|1,1> = -1.
    assert abs(clebsch_gordan(1, 1, 1, 1, 2, 2) + 1.0) < 1e-12
    assert abs(clebsch_gordan(1, 1, 1, -1, 2, 0) - 1.0 / rt2) < 1e-12
    assert abs(clebsch_gordan(1, -1, 1, 1, 2, 0) - 1.0 / rt2) < 1e-12
    assert abs(clebsch_gordan(1, 1, 1, -1, 0, 0) - 1.0 / rt2) < 1e-12
    assert abs(clebsch_gordan(1, -1, 1, 1, 0, 0) + 1.0 / rt2) < 1e-12


def test_pi_k_matrix_shapes_low_k():
    for K in range(6):
        P = pi_k_ang_matrix(K)
        dim = (K + 1) ** 2
        assert P.shape == (dim, dim)
        assert len(coupled_angular_labels(K)) == dim
        assert len(uncoupled_s3_basis(K)) == dim


def test_pi_k_orthonormality_low_k():
    for K in range(6):
        P = pi_k_ang_matrix(K)
        I = np.eye((K + 1) ** 2)
        assert np.linalg.norm(P @ P.T - I) < 1e-10
        assert np.linalg.norm(P.T @ P - I) < 1e-10


def test_lz_compatibility_low_k():
    for K in range(6):
        diag = lz_compatibility_diagnostics(K)
        assert diag["violating_entries"] == 0
        assert diag["max_mismatch_abs"] < 1e-12


def test_dipole_label_compatibility_matches_existing_channels():
    for K_i, K_f in [(2, 1), (3, 1), (3, 2)]:
        n_i, n_f = K_i + 1, K_f + 1
        ours = set(dipole_compatible_label_pairs(K_i, K_f))
        existing = {
            (row["ell_i"], row["m_i"], row["ell_f"], row["m_f"])
            for row in allowed_dipole_channels(n_i, n_f)
        }
        assert ours == existing


def test_diagnostics_report_fields():
    diag = pi_k_orthonormality_diagnostics(5)
    for key in [
        "K",
        "dimension",
        "row_orthonormality_error",
        "column_orthonormality_error",
        "max_entry_abs",
        "convention",
    ]:
        assert key in diag
    assert diag["row_orthonormality_error"] < 1e-10
    assert diag["column_orthonormality_error"] < 1e-10
