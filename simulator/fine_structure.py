from simulator.hydrogen_shell_simulator import PLANCK, LIGHT_SPEED, EV_TO_J, RYDBERG_EV

ALPHA = 7.2973525693e-3
M_E_C2_EV = 510998.95000


def energy_fine_structure(n: int, j: float) -> float:
    if n < 1:
        raise ValueError("n must be >= 1")
    if j <= 0:
        raise ValueError("j must be positive")
    base = -RYDBERG_EV / (n**2)
    correction = (M_E_C2_EV * (ALPHA**4) / (2 * (n**3))) * ((3 / (4 * n)) - (1 / (j + 0.5)))
    return base + correction


def h_alpha_components():
    channels = [
        ("3s_1/2 -> 2p_1/2", (3, 0.5), (2, 0.5)),
        ("3p_1/2 -> 2s_1/2", (3, 0.5), (2, 0.5)),
        ("3p_3/2 -> 2s_1/2", (3, 1.5), (2, 0.5)),
        ("3d_3/2 -> 2p_1/2", (3, 1.5), (2, 0.5)),
        ("3d_3/2 -> 2p_3/2", (3, 1.5), (2, 1.5)),
        ("3d_5/2 -> 2p_3/2", (3, 2.5), (2, 1.5)),
    ]
    rows = []
    for label, upper, lower in channels:
        e_up = energy_fine_structure(*upper)
        e_lo = energy_fine_structure(*lower)
        delta_e = e_up - e_lo
        lam = (PLANCK * LIGHT_SPEED) / (abs(delta_e) * EV_TO_J)
        rows.append({"label": label, "delta_E": delta_e, "lam": lam})
    return rows
