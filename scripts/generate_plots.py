import sys
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from simulator.hydrogen_shell_simulator import RYDBERG_EV
from simulator.shell_locking_test import run_shell_locking_test
from simulator.spectral_comparison import all_series_tables


def main() -> None:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    out = Path("reports/plots")
    out.mkdir(parents=True, exist_ok=True)

    s = np.linspace(0.5, 5.5, 500)
    beta, gamma = 2.0, 1.0
    plt.figure(figsize=(8, 5))
    for K in range(6):
        v = beta * np.sin(np.pi * (s**2) / 2.0) ** 2 + gamma * ((K + 1) - (s**2) / 2.0) ** 2
        plt.plot(s, v, label=f"K={K}")
    plt.xlabel("s")
    plt.ylabel("V_K(s)")
    plt.legend()
    plt.tight_layout()
    plt.savefig(out / "shell_locking_potential_K0_K5.png", dpi=300)
    plt.close()

    rows = run_shell_locking_test(K_max=5)
    ks = [r["K"] for r in rows]
    tx = [r["target_x"] for r in rows]
    ex = [r["expectation_x"] for r in rows]
    er = [r["error"] for r in rows]

    plt.figure(figsize=(7, 4))
    plt.plot(ks, tx, "o-", label="target_x")
    plt.plot(ks, ex, "s-", label="expectation_x")
    plt.xlabel("K")
    plt.ylabel("x")
    plt.legend()
    plt.tight_layout()
    plt.savefig(out / "shell_locking_expectation_vs_target.png", dpi=300)
    plt.close()

    plt.figure(figsize=(7, 4))
    plt.axhline(0.0, color="k", linewidth=1)
    plt.plot(ks, er, "o-")
    plt.xlabel("K")
    plt.ylabel("expectation_x - target_x")
    plt.tight_layout()
    plt.savefig(out / "shell_locking_error.png", dpi=300)
    plt.close()

    n = np.arange(1, 9)
    e = -RYDBERG_EV / (n**2)
    plt.figure(figsize=(7, 4))
    plt.plot(n, e, "o-")
    plt.xlabel("n")
    plt.ylabel("E_n (eV)")
    plt.tight_layout()
    plt.savefig(out / "hydrogen_energy_ladder.png", dpi=300)
    plt.close()

    sr = [r for r in all_series_tables() if r["reference_nm"] is not None]
    idx = np.arange(len(sr))
    pred = [r["predicted_nm"] for r in sr]
    ref = [r["reference_nm"] for r in sr]
    labels = [f"{r['series']} {r['transition']}" for r in sr]
    plt.figure(figsize=(12, 4))
    plt.plot(idx, pred, "o", label="predicted")
    plt.plot(idx, ref, "x", label="reference")
    plt.xticks(idx, labels, rotation=75, ha="right", fontsize=7)
    plt.ylabel("wavelength (nm)")
    plt.legend()
    plt.tight_layout()
    plt.savefig(out / "transition_wavelength_comparison.png", dpi=300)
    plt.close()


if __name__ == "__main__":
    main()
