"""Dependency-free Clebsch-Gordan coefficients using doubled quantum numbers."""

from __future__ import annotations

import math


def validate_doubled_quantum_number(j2: int, m2: int) -> bool:
    """Validate doubled (j,m) values.

    Requires integer j2>=0, integer m2 with |m2|<=j2 and same parity as j2.
    """
    if not isinstance(j2, int) or not isinstance(m2, int):
        return False
    if j2 < 0 or abs(m2) > j2:
        return False
    return (j2 - m2) % 2 == 0


def m_values_for_j2(j2: int) -> list[int]:
    """Return allowed doubled m-values for fixed doubled j."""
    if not isinstance(j2, int) or j2 < 0:
        raise ValueError("j2 must be a non-negative integer")
    return list(range(-j2, j2 + 1, 2))


def _fact_halfint(x2: int) -> float:
    if x2 < 0:
        return 0.0
    return math.gamma((x2 / 2.0) + 1.0)


def clebsch_gordan(j1_2: int, m1_2: int, j2_2: int, m2_2: int, J_2: int, M_2: int) -> float:
    """Return <j1,m1;j2,m2|J,M> in Condon-Shortley convention.

    All arguments are doubled integers.
    Invalid combinations return 0.0.
    """
    if not all(isinstance(x, int) for x in [j1_2, m1_2, j2_2, m2_2, J_2, M_2]):
        return 0.0
    if not validate_doubled_quantum_number(j1_2, m1_2):
        return 0.0
    if not validate_doubled_quantum_number(j2_2, m2_2):
        return 0.0
    if not validate_doubled_quantum_number(J_2, M_2):
        return 0.0
    if M_2 != m1_2 + m2_2:
        return 0.0
    if J_2 < abs(j1_2 - j2_2) or J_2 > (j1_2 + j2_2):
        return 0.0

    p1 = _fact_halfint(j1_2 + j2_2 - J_2)
    p2 = _fact_halfint(j1_2 - j2_2 + J_2)
    p3 = _fact_halfint(-j1_2 + j2_2 + J_2)
    p4 = _fact_halfint(j1_2 + j2_2 + J_2 + 2)
    if p4 == 0.0:
        return 0.0
    pref_triangle = math.sqrt((2.0 * (J_2 / 2.0) + 1.0) * p1 * p2 * p3 / p4)

    pref_m = math.sqrt(
        _fact_halfint(j1_2 + m1_2)
        * _fact_halfint(j1_2 - m1_2)
        * _fact_halfint(j2_2 + m2_2)
        * _fact_halfint(j2_2 - m2_2)
        * _fact_halfint(J_2 + M_2)
        * _fact_halfint(J_2 - M_2)
    )

    phase_exp = (j1_2 - j2_2 + M_2) // 2
    phase = -1.0 if (phase_exp % 2) else 1.0

    # k-bounds from nonnegative factorial arguments
    k_min = max(
        0,
        (j2_2 - J_2 - m1_2 + 1) // 2,
        (j1_2 - J_2 + m2_2 + 1) // 2,
    )
    k_max = min(
        (j1_2 + j2_2 - J_2) // 2,
        (j1_2 - m1_2) // 2,
        (j2_2 + m2_2) // 2,
    )

    total = 0.0
    for k in range(k_min, k_max + 1):
        args2 = [
            2 * k,
            j1_2 + j2_2 - J_2 - 2 * k,
            j1_2 - m1_2 - 2 * k,
            j2_2 + m2_2 - 2 * k,
            J_2 - j2_2 + m1_2 + 2 * k,
            J_2 - j1_2 - m2_2 + 2 * k,
        ]
        if any(a < 0 for a in args2):
            continue
        denom = 1.0
        for a2 in args2:
            denom *= _fact_halfint(a2)
        term = (-1.0 if (k % 2) else 1.0) / denom
        total += term

    return phase * pref_triangle * pref_m * total
