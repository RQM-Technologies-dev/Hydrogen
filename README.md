# Hydrogen Bridge v1

This repository implements a **calibrated bridge** for hydrogen on the RQM/QSG state space
\(M=S^3\times\mathbb R_s\). It is designed as a reproducible package for shell energies,
degeneracy, angular states, transition channels, numerical validation of shell locking,
and a fine-structure H-alpha benchmark.

Core equations used in the package:

- \(\hat N = \sqrt{-\Delta_{S^3} + 1}\)
- \(\hat N = s^2/2\)
- \(H_C = -\mathrm{Ry}/\hat N^2\)

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
