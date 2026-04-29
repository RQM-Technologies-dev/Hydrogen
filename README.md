# Hydrogen

RQM Hydrogen Derivations — Hydrogen Bridge v1

A clean, inspectable, reproducible package demonstrating that RQM/QSG organises
hydrogen into shells, degeneracy, angular states, transitions, and fine structure
via a single central operator N̂ = √(−Δ_{S³} + 1) and one shell-locking condition
N̂ = s²/2.

## Repository layout

```
notes/
  hydrogen_bridge_v1.md       Formal technical note (scaffold)

simulator/
  __init__.py
  hydrogen_shell_simulator.py  Shell table, angular states, dipole transitions
  spectral_comparison.py       Lyman / Balmer / Paschen vs. NIST
  shell_locking_test.py        Numerical validation of the locking potential
  fine_structure.py            Relativistic fine-structure corrections

tests/
  test_simulator_scaffold.py   Smoke tests for the scaffold
```

## Running the tests

```bash
pip install pytest
pytest tests/
```
