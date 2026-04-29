# Layer separation: benchmark vs native bridge

## 1) Standard hydrogen benchmark layer

These are standard physics formulas/data used for validation and calibration in v1:

- Rydberg shell energy formula E_n = -Ry/n^2.
- Known Lyman/Balmer/Paschen comparison values (reference dataset under data/).
- Standard electric-dipole selection rules.
- Leading fine-structure correction formula.
- H-alpha benchmark components.

These ingredients are used as calibration/validation targets and should not be read as uniquely native derivations.

## 2) Native RQM/QSG bridge layer

These are the v1 native bridge structures:

- State space M = S^3 × R_s.
- Shell-number operator Nhat = sqrt(-Delta_S3 + 1).
- Shell-locking condition Nhat = s^2 / 2.
- Native spectral energy operator H_C = -Ry / Nhat^2.
- S^3 degeneracy n^2.
- S^3 -> S^2 angular projection/decomposition.
- Numerical shell-locking validation.

Honesty boundary: v1's native contribution is a unified shell architecture and falsifiable bridge implementation, not an independent native derivation of every constant/correction.
