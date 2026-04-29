# fine_structure.py
#
# Adds relativistic fine-structure corrections:
#
#   E_{n,j} = -Ry/n² + (m_e c² α⁴)/(2n³) [3/(4n) - 1/(j + 1/2)]
#
# and enumerates fine-structure components for the H-alpha line (3 → 2).
#
# Scaffold — implementation to be filled in.

def energy_fine_structure(n: int, j: float) -> float:
    """Return E_{n,j} in eV."""
    raise NotImplementedError


def h_alpha_components():
    """
    Return the six allowed fine-structure channels for H-alpha (3 → 2).

    Each entry is a dict with keys:
        label    (str)   : transition label, e.g. '3s_1/2 -> 2p_1/2'
        delta_E  (float) : energy difference in eV
        lam      (float) : wavelength in metres

    Channels:
      3s_{1/2} → 2p_{1/2}
      3p_{1/2} → 2s_{1/2}
      3p_{3/2} → 2s_{1/2}
      3d_{3/2} → 2p_{1/2}
      3d_{3/2} → 2p_{3/2}
      3d_{5/2} → 2p_{3/2}
    """
    raise NotImplementedError
