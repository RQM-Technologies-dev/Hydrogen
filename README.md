[![Hydrogen Bridge v1 CI](https://github.com/RQM-Technologies-dev/Hydrogen/actions/workflows/ci.yml/badge.svg)](https://github.com/RQM-Technologies-dev/Hydrogen/actions/workflows/ci.yml)

# Hydrogen Bridge v1

This repository implements a **calibrated bridge** for hydrogen on the RQM/QSG state space
\(M=S^3\times\mathbb R_s\). It is designed as a reproducible package for shell energies,
degeneracy, angular states, transition channels, numerical validation of shell locking,
and a fine-structure H-alpha benchmark.

## Central public claim

Hydrogen bound-state shell architecture is naturally represented by scalar harmonics on S³.

- \(-\Delta_{S^3}Y_K = K(K+2)Y_K\)
- \(\hat N = \sqrt{-\Delta_{S^3}+1}\)
- \(\hat N\,Y_K = (K+1)Y_K\)
- \(n = K+1\)
- \(\dim\mathcal H_K(S^3)=(K+1)^2=n^2\)
- \(H_C = -\mathrm{Ry}/\hat N^2\)
- \(E_n=-\mathrm{Ry}/n^2\)

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
python scripts/generate_plots.py
```

## What it generates

Running `python scripts/generate_reports.py` creates:

- `reports/shell_table.csv`
- `reports/angular_state_counts.csv`
- `reports/series_comparison.csv`
- `reports/shell_locking_validation.csv`
- `reports/h_alpha_fine_structure.csv`
- `reports/HYDROGEN_BRIDGE_V1_REPORT.md`
- `reports/hopf_projection_statistics.csv`
- `reports/hopf_flux_scaling.csv`

These artifacts provide a benchmark against hydrogen spectral architecture for Hydrogen Bridge v1.

Generated artifacts under `reports/` are produced locally and may not be committed in every branch or clone.


## Technical notes

- `notes/hydrogen_bridge_v1.md` — main Hydrogen Bridge v1 technical note.
- `notes/appendix_coulomb_action_to_s3_operator.md` — expanded derivation from Coulomb action to the native S³ spectral hydrogen operator.
- `notes/appendix_b_closure_geometry_inverse_square_action.md` — closure-action derivation showing how quaternionic closure plus central flux equilibrium supports the inverse-square Coulomb action law.
- `notes/appendix_c_hopf_flux_projection_and_coulomb_field.md` — Hopf-projected quaternionic flux support layer showing how conserved projected $S^2$ flux gives $E(r)\sim 1/r^2$ and $V(r)\sim -1/r$.


## Reviewer map

- `notes/hydrogen_bridge_v1.md`
- `notes/s3_scalar_harmonic_shell_architecture.md` — public-facing anchor note for hydrogen shell architecture as scalar harmonics on S³.
- `notes/appendix_coulomb_action_to_s3_operator.md`
- `notes/angular_projection_s3_to_s2.md`
- `docs/math_references.md`
- `data/hydrogen_reference_lines_provenance.md`
- `notes/layer_separation.md`
- `notes/appendix_b_closure_geometry_inverse_square_action.md`
- `notes/appendix_c_hopf_flux_projection_and_coulomb_field.md`
- `docs/claims_matrix.md`

## Plot generation

Run `python scripts/generate_plots.py` to generate deterministic visual diagnostics under `reports/plots/`.
