"""Symbolic S^3 spectral hydrogen helper identities."""

RYDBERG_EV = 13.605693122994


def s3_laplacian_eigenvalue(K: int) -> int:
    return K * (K + 2)


def shifted_shell_operator_eigenvalue(K: int) -> int:
    return (K + 1) ** 2


def shell_number_from_K(K: int) -> int:
    return K + 1


def hydrogen_energy_from_K(K: int, rydberg_ev: float = RYDBERG_EV) -> float:
    return -rydberg_ev / (K + 1) ** 2


def hydrogen_energy_from_n(n: int, rydberg_ev: float = RYDBERG_EV) -> float:
    return -rydberg_ev / n**2
