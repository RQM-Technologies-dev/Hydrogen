"""Low-K numerical S^3->S^2 angular bridge Π_K^ang.

Implements a first operator-validity gate for K=0..5 using a dependency-free
Clebsch-Gordan implementation and the V_j ⊗ V_j* dual convention.
"""

from __future__ import annotations

import numpy as np

from simulator.clebsch_gordan import clebsch_gordan, m_values_for_j2


def shell_j(K: int) -> float:
    if K < 0:
        raise ValueError("K must be non-negative")
    return K / 2


def angular_sectors_for_K(K: int) -> list[tuple[int, int]]:
    if K < 0:
        raise ValueError("K must be non-negative")
    return [(ell, m) for ell in range(K + 1) for m in range(-ell, ell + 1)]


def s3_shell_dimension(K: int) -> int:
    if K < 0:
        raise ValueError("K must be non-negative")
    return (K + 1) ** 2


def s2_branch_dimension(K: int) -> int:
    if K < 0:
        raise ValueError("K must be non-negative")
    return sum(2 * ell + 1 for ell in range(K + 1))


def validate_branching_dimension(K: int) -> bool:
    return s3_shell_dimension(K) == s2_branch_dimension(K)


def pi_k_label_map(K: int) -> list[dict[str, object]]:
    rows = []
    for ell, m in angular_sectors_for_K(K):
        rows.append({"K": K, "ell": ell, "m": m, "source": f"Phi^{K}_{{{ell},{m}}}", "target": f"Y_{{{ell},{m}}}"})
    return rows


def uncoupled_s3_basis(K: int) -> list[tuple[int, int]]:
    j2 = K
    mvals = m_values_for_j2(j2)
    return [(a2, b2) for a2 in mvals for b2 in mvals]


def coupled_angular_labels(K: int) -> list[tuple[int, int]]:
    return angular_sectors_for_K(K)


def pi_k_ang_matrix(K: int) -> np.ndarray:
    """Construct Π_K^ang with rows (ell,m), cols (a,b).

    Dual convention: |j,b>* = (-1)^(j-b)|j,-b>, so
    Π[(ell,m),(a,b)] = (-1)^(j-b) <j,a; j,-b | ell,m>.
    All internal m-labels use doubled integers.
    """
    j2 = K
    cols = uncoupled_s3_basis(K)
    rows = coupled_angular_labels(K)
    P = np.zeros((len(rows), len(cols)), dtype=float)
    for i, (ell, m) in enumerate(rows):
        ell2 = 2 * ell
        m2 = 2 * m
        for k, (a2, b2) in enumerate(cols):
            phase = -1.0 if ((j2 - b2) // 2) % 2 else 1.0
            P[i, k] = phase * clebsch_gordan(j2, a2, j2, -b2, ell2, m2)
    return P


def pi_k_orthonormality_diagnostics(K: int) -> dict[str, float | int | str]:
    P = pi_k_ang_matrix(K)
    I = np.eye(P.shape[0])
    row_err = float(np.linalg.norm(P @ P.T - I, ord=np.inf))
    col_err = float(np.linalg.norm(P.T @ P - I, ord=np.inf))
    out: dict[str, float | int | str] = {
        "K": K,
        "dimension": int(P.shape[0]),
        "row_orthonormality_error": row_err,
        "column_orthonormality_error": col_err,
        "max_entry_abs": float(np.max(np.abs(P))),
        "convention": "dual index |j,b>* = (-1)^(j-b)|j,-b>; Condon-Shortley CG",
    }
    try:
        out["determinant_abs"] = float(abs(np.linalg.det(P)))
    except np.linalg.LinAlgError:
        pass
    return out


def lz_compatibility_diagnostics(K: int, tol: float = 1e-12) -> dict[str, float | int]:
    P = pi_k_ang_matrix(K)
    rows = coupled_angular_labels(K)
    cols = uncoupled_s3_basis(K)
    mismatch = 0.0
    nonzero = 0
    violating = 0
    for i, (_, m) in enumerate(rows):
        for j, (a2, b2) in enumerate(cols):
            val = abs(P[i, j])
            if val > tol:
                nonzero += 1
                if ((a2 - b2) // 2) != m:
                    violating += 1
                    mismatch = max(mismatch, val)
    return {"K": K, "max_mismatch_abs": mismatch, "violating_entries": violating, "nonzero_entries": nonzero}


def dipole_compatible_label_pairs(K_i: int, K_f: int) -> list[tuple[int, int, int, int]]:
    labels_i = coupled_angular_labels(K_i)
    labels_f = coupled_angular_labels(K_f)
    out = []
    for ell_i, m_i in labels_i:
        for ell_f, m_f in labels_f:
            if (ell_f - ell_i) in (-1, 1) and (m_f - m_i) in (-1, 0, 1):
                out.append((ell_i, m_i, ell_f, m_f))
    return out
