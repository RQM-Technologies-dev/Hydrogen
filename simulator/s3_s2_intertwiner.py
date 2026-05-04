"""Symbolic bookkeeping for the S^3->S^2 angular branching target.

This module does not implement the full numerical Clebsch-Gordan operator.
It provides shell/label bookkeeping that supports an operator-level target note
for Pi_K^ang and associated low-K consistency tests.
"""


def shell_j(K: int) -> float:
    """Return j=K/2 for shell index K."""
    if K < 0:
        raise ValueError("K must be non-negative")
    return K / 2


def angular_sectors_for_K(K: int) -> list[tuple[int, int]]:
    """Return symbolic (ell, m) sectors with ell=0..K and m=-ell..ell."""
    if K < 0:
        raise ValueError("K must be non-negative")
    return [(ell, m) for ell in range(K + 1) for m in range(-ell, ell + 1)]


def s3_shell_dimension(K: int) -> int:
    """Dimension of H_K(S^3): (K+1)^2."""
    if K < 0:
        raise ValueError("K must be non-negative")
    return (K + 1) ** 2


def s2_branch_dimension(K: int) -> int:
    """Dimension of direct sum_{ell=0..K} H_ell(S^2): sum(2ell+1)."""
    if K < 0:
        raise ValueError("K must be non-negative")
    return sum(2 * ell + 1 for ell in range(K + 1))


def validate_branching_dimension(K: int) -> bool:
    """Check the dimension identity for the shell/branch bridge at fixed K."""
    return s3_shell_dimension(K) == s2_branch_dimension(K)


def pi_k_label_map(K: int) -> list[dict[str, object]]:
    """Return symbolic rows Phi^K_{ell,m} -> Y_{ell,m}.

    This is label-level bookkeeping only, not a numeric intertwiner matrix.
    """
    rows = []
    for ell, m in angular_sectors_for_K(K):
        rows.append(
            {
                "K": K,
                "ell": ell,
                "m": m,
                "source": f"Phi^{K}_{{{ell},{m}}}",
                "target": f"Y_{{{ell},{m}}}",
            }
        )
    return rows
