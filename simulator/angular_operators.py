"""Angular operator diagnostics for the S^3->S^2 bridge.

This module implements Gate 1B/1C diagnostics:
- L^2 compatibility for Π_K^ang.
- Angular-only rank-1 transition operators on the target side and pulled back to S^3.

These operators are angular compatibility operators only. They do not include
radial matrix elements, oscillator strengths, or a full physical dipole model.
"""

from __future__ import annotations

import numpy as np

from simulator.clebsch_gordan import clebsch_gordan
from simulator.s3_s2_intertwiner import coupled_angular_labels, pi_k_ang_matrix


def target_l2_diagonal(K: int) -> np.ndarray:
    """Return diagonal L^2 eigenvalues over coupled target labels (ell, m)."""
    return np.array([ell * (ell + 1) for ell, _ in coupled_angular_labels(K)], dtype=float)


def l2_compatibility_diagnostics(K: int) -> dict[str, float | int | str]:
    """Compute Π_K^ang L^2_source ≈ L^2_target Π_K^ang diagnostics.

    Uses pulled-back source representation L^2_source = P^T L^2_target P.
    TODO: add explicit source-side generator construction (Lx, Ly, Lz) for an
    independent native-source cross-check.
    """
    P = pi_k_ang_matrix(K)
    l2_target_diag = target_l2_diagonal(K)
    l2_target = np.diag(l2_target_diag)
    l2_source = P.T @ l2_target @ P
    intertwining_error = float(np.linalg.norm(P @ l2_source - l2_target @ P, ord=np.inf))
    symmetry_error = float(np.linalg.norm(l2_source - l2_source.T, ord=np.inf))
    source_evals = np.linalg.eigvalsh(l2_source)
    target_evals = np.linalg.eigvalsh(l2_target)
    eval_error = float(np.max(np.abs(np.sort(source_evals) - np.sort(target_evals))))
    return {
        "K": K,
        "dimension": int(P.shape[0]),
        "l2_intertwining_error": intertwining_error,
        "l2_source_symmetry_error": symmetry_error,
        "max_l2_eigenvalue_error": eval_error,
        "convention": "pulled-back source Casimir via Π_K^ang (dual convention)",
    }


def rank1_target_operator(K_i: int, K_f: int, q: int) -> np.ndarray:
    """Build angular-only normalized rank-1 target operator matrix.

    This is not a full physical dipole amplitude: radial matrix elements and
    oscillator strengths are intentionally excluded.
    """
    if q not in (-1, 0, 1):
        raise ValueError("q must be one of -1, 0, +1")
    labels_i = coupled_angular_labels(K_i)
    labels_f = coupled_angular_labels(K_f)
    out = np.zeros((len(labels_f), len(labels_i)), dtype=float)
    for row, (ell_f, m_f) in enumerate(labels_f):
        for col, (ell_i, m_i) in enumerate(labels_i):
            if (ell_f - ell_i) not in (-1, 1) or (m_f - m_i) != q:
                continue
            out[row, col] = clebsch_gordan(2 * ell_i, 2 * m_i, 2, 2 * q, 2 * ell_f, 2 * m_f)
    return out


def rank1_s3_operator(K_i: int, K_f: int, q: int) -> np.ndarray:
    """Pull back the target angular rank-1 operator to the S^3 shell basis."""
    P_i = pi_k_ang_matrix(K_i)
    P_f = pi_k_ang_matrix(K_f)
    T_target = rank1_target_operator(K_i, K_f, q)
    return P_f.T @ T_target @ P_i


def rank1_transition_diagnostics(K_i: int, K_f: int) -> list[dict[str, float | int]]:
    """Return intertwining diagnostics for q=-1,0,+1."""
    P_i = pi_k_ang_matrix(K_i)
    P_f = pi_k_ang_matrix(K_f)
    rows = []
    for q in (-1, 0, 1):
        T_target = rank1_target_operator(K_i, K_f, q)
        T_s3 = P_f.T @ T_target @ P_i
        err = float(np.linalg.norm(P_f @ T_s3 - T_target @ P_i, ord=np.inf))
        rows.append(
            {
                "K_i": K_i,
                "K_f": K_f,
                "q": q,
                "target_nonzero_count": int(np.count_nonzero(np.abs(T_target) > 0.0)),
                "s3_nonzero_count": int(np.count_nonzero(np.abs(T_s3) > 1e-15)),
                "intertwining_error": err,
                "max_target_entry_abs": float(np.max(np.abs(T_target))) if T_target.size else 0.0,
                "max_s3_entry_abs": float(np.max(np.abs(T_s3))) if T_s3.size else 0.0,
            }
        )
    return rows


def rank1_allowed_label_pairs(K_i: int, K_f: int) -> set[tuple[int, int, int, int]]:
    """Return all nonzero (ell_i, m_i, ell_f, m_f) labels across q=-1,0,+1."""
    labels_i = coupled_angular_labels(K_i)
    labels_f = coupled_angular_labels(K_f)
    out: set[tuple[int, int, int, int]] = set()
    for q in (-1, 0, 1):
        T = rank1_target_operator(K_i, K_f, q)
        nz = np.argwhere(np.abs(T) > 0.0)
        for row, col in nz:
            ell_f, m_f = labels_f[int(row)]
            ell_i, m_i = labels_i[int(col)]
            out.add((ell_i, m_i, ell_f, m_f))

    return out
