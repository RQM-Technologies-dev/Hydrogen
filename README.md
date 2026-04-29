[![Hydrogen Bridge v1 CI](https://github.com/RQM-Technologies-dev/Hydrogen/actions/workflows/ci.yml/badge.svg)](https://github.com/RQM-Technologies-dev/Hydrogen/actions/workflows/ci.yml)

# Hydrogen Bridge v1

This repository implements a **calibrated bridge** for hydrogen on the RQM/QSG state space
\(M=S^3\times\mathbb R_s\). It is designed as a reproducible package for shell energies,
degeneracy, angular states, transition channels, numerical validation of shell locking,
and a fine-structure H-alpha benchmark.

Core equations used in the package:

- \(\hat N = \sqrt{-\Delta_{S^3} + 1}\)
- \(\hat N = s^2/2\)
- \(H_C = -\mathrm{Ry}/\hat N^2\)

## Continuous Integration

The Hydrogen Bridge v1 CI workflow runs tests and regenerates reports on pushes to `main` and pull requests targeting `main`.

Each CI run uploads generated report files as workflow artifacts for inspection and downstream use.

Outputs under `reports/` are generated artifacts and may not be committed in every branch or clone.

## Quickstart

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
pytest
python scripts/generate_reports.py
```

## What it generates

Running `python scripts/generate_reports.py` creates:

- `reports/shell_table.csv`
- `reports/angular_state_counts.csv`
- `reports/series_comparison.csv`
- `reports/shell_locking_validation.csv`
- `reports/h_alpha_fine_structure.csv`
- `reports/HYDROGEN_BRIDGE_V1_REPORT.md`

These artifacts provide a benchmark against hydrogen spectral architecture for Hydrogen Bridge v1.

Generated artifacts under `reports/` are produced locally and may not be committed in every branch or clone.


## Technical notes

- `notes/hydrogen_bridge_v1.md` — main Hydrogen Bridge v1 technical note.
- `notes/appendix_coulomb_action_to_s3_operator.md` — expanded derivation from Coulomb action to the native S³ spectral hydrogen operator.
