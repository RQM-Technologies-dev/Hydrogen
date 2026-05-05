import numpy as np

from simulator.angular_operators import (
    l2_compatibility_diagnostics,
    rank1_allowed_label_pairs,
    rank1_target_operator,
    rank1_transition_diagnostics,
    target_l2_diagonal,
)
from simulator.hydrogen_shell_simulator import allowed_dipole_channels
from simulator.s3_s2_intertwiner import coupled_angular_labels


def test_l2_compatibility_low_k() -> None:
    for K in range(6):
        d = l2_compatibility_diagnostics(K)
        assert d["l2_intertwining_error"] < 1e-10
        assert d["l2_source_symmetry_error"] < 1e-10


def test_l2_target_labels() -> None:
    for K in range(6):
        labels = coupled_angular_labels(K)
        diag = target_l2_diagonal(K)
        assert len(labels) == len(diag)
        for i, (ell, _m) in enumerate(labels):
            assert np.isclose(diag[i], ell * (ell + 1))


def test_rank1_target_operator_selection_rules() -> None:
    for K_i, K_f in [(2, 1), (3, 1), (3, 2)]:
        labels_i = coupled_angular_labels(K_i)
        labels_f = coupled_angular_labels(K_f)
        for q in (-1, 0, 1):
            op = rank1_target_operator(K_i, K_f, q)
            for row, col in np.argwhere(np.abs(op) > 0.0):
                ell_f, m_f = labels_f[int(row)]
                ell_i, m_i = labels_i[int(col)]
                assert (m_f - m_i) == q
                assert (ell_f - ell_i) in (-1, 1)


def test_rank1_s3_intertwining_low_k() -> None:
    for K_i, K_f in [(2, 1), (3, 2), (4, 3)]:
        rows = rank1_transition_diagnostics(K_i, K_f)
        for row in rows:
            assert row["intertwining_error"] < 1e-10


def test_rank1_allowed_labels_match_existing_dipole_channels() -> None:
    for n_i, n_f in [(3, 2), (4, 2), (4, 3)]:
        K_i = n_i - 1
        K_f = n_f - 1
        got = rank1_allowed_label_pairs(K_i, K_f)
        expected = {
            (c["ell_i"], c["m_i"], c["ell_f"], c["m_f"])
            for c in allowed_dipole_channels(n_i, n_f)
        }
        assert got == expected


def test_report_diagnostics_fields() -> None:
    row = rank1_transition_diagnostics(2, 1)[0]
    for key in ["K_i", "K_f", "q", "intertwining_error", "target_nonzero_count"]:
        assert key in row
