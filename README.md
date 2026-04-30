[![Hydrogen Bridge v1 CI](https://github.com/RQM-Technologies-dev/Hydrogen/actions/workflows/ci.yml/badge.svg)](https://github.com/RQM-Technologies-dev/Hydrogen/actions/workflows/ci.yml)

# Hydrogen Bridge v1

## What this repository is

Hydrogen Bridge v1 is a reproducible research package exploring a calibrated spectral-geometric representation of hydrogen shell architecture on \(S^3 \times \mathbb R_s\). Its central claim is narrow: hydrogen’s principal shell number, pre-spin angular degeneracy, and Rydberg energy denominator are naturally represented by scalar harmonic shells on \(S^3\).

## Central public claim

Hydrogen bound-state shell architecture is naturally represented by scalar harmonics on S³.

Implemented bridge equations and identities used in this package:

- \(-\Delta_{S^3}Y_K = K(K+2)Y_K\)
- \(\hat N = \sqrt{-\Delta_{S^3}+1}\), with \(\hat N\,Y_K = (K+1)Y_K\)
- \(n = K+1\), and \(\dim\mathcal H_K(S^3)=(K+1)^2=n^2\)
- Calibrated energy operator \(H_C = -\mathrm{Ry}/\hat N^2\), giving \(E_n=-\mathrm{Ry}/n^2\)
- Shell-locking relation used in diagnostics: \(\hat N = s^2/2\)

## What this repository is not

- It is not a completed first-principles derivation of the full Schrödinger-Coulomb solution.
- It does not independently derive \(\mathrm{Ry}\), \(\kappa\), electric charge, Maxwell equations, fine structure, or all hydrogen eigenfunctions.
- It does not yet construct the full physical \(S^3\to S^2\) projection/intertwiner operator.
- Spectral-line reference rows are currently legacy benchmark values with provenance fields and an authoritative NIST ASD replacement path.

## Start here

Recommended order:

1. `notes/s3_scalar_harmonic_shell_architecture.md`
2. `notes/hydrogen_bridge_v1.md`
3. `notes/angular_projection_s3_to_s2.md`
4. `docs/claims_matrix.md`
5. `docs/public_release_readiness.md`

## Quickstart

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
pytest
python scripts/generate_reports.py
python scripts/generate_plots.py
```

## What is implemented and generated

Running `python scripts/generate_reports.py` creates:

- `reports/shell_table.csv`
- `reports/angular_state_counts.csv`
- `reports/series_comparison.csv`
- `reports/shell_locking_validation.csv`
- `reports/h_alpha_fine_structure.csv`
- `reports/HYDROGEN_BRIDGE_V1_REPORT.md`
- `reports/hopf_projection_statistics.csv`
- `reports/hopf_flux_scaling.csv`

Run `python scripts/generate_plots.py` to generate deterministic visual diagnostics under `reports/plots/`.

Generated artifacts under `reports/` are produced locally and may not be committed in every branch or clone.

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

## Continuous Integration

The CI workflow runs tests and regenerates reports on pushes to `main` and pull requests targeting `main`.

## License

This repository is licensed under the MIT License. See [`LICENSE`](LICENSE).
