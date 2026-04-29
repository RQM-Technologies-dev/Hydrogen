import math


def run_shell_locking_test(K_max: int = 5, grid_points: int = 500, eta: float = 1.0, beta: float = 3.0, gamma: float = 6.0):
    """Numerical shell-locking proxy using weighted low-energy localization on an s-grid."""
    if K_max < 0:
        raise ValueError("K_max must be >= 0")
    if grid_points < 50:
        raise ValueError("grid_points should be >= 50")

    s_max = math.sqrt(2 * (K_max + 2.0)) + 2.0
    ds = s_max / (grid_points - 1)
    s_values = [i * ds for i in range(grid_points)]

    rows = []
    for K in range(0, K_max + 1):
        energies = []
        for s in s_values:
            x = 0.5 * s * s
            v = beta * (math.sin(math.pi * x) ** 2) + gamma * ((K + 1 - x) ** 2)
            energies.append(v)

        min_v = min(energies)
        weights = [math.exp(-(v - min_v) / max(eta, 1e-8)) for v in energies]
        z = sum(weights) * ds
        exp_val = sum((0.5 * s * s) * w for s, w in zip(s_values, weights)) * ds / z

        target = float(K + 1)
        rows.append({"K": K, "target": target, "numerical": exp_val, "error": exp_val - target})

    return rows
