# hydrogen_shell_simulator.py
#
# Computes the S³ shell table, allowed (ℓ, m) states, and dipole transitions
# for hydrogen up to a given n_max.
#
# Scaffold — implementation to be filled in.

def shell_table(n_max: int):
    """Return a list of dicts with columns: n, K, s2, s, degeneracy, energy_eV."""
    raise NotImplementedError


def angular_states(n: int):
    """Return all (ℓ, m) pairs allowed for principal quantum number n."""
    raise NotImplementedError


def transitions(n_max: int):
    """Return all allowed dipole transitions (n_i → n_f, Δℓ = ±1) with wavelength λ (m)."""
    raise NotImplementedError
