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


## 3) Semiclassical closure-action support layer

This is a semiclassical support layer that strengthens the bridge architecture but is not a full native derivation:

- Quaternionic loop closure count \(N_c=(1/4\pi)\|\oint q^{-1}dq\|\).
- Action conversion \(J=N_c\hbar\).
- Fixed-action central-flux equilibrium \(E_J(r)=J^2/(2\mu r^2)-\kappa/r\).
- Stability result \(E(J)=-\mu\kappa^2/(2J^2)\).

## 4) Projected field-geometry support layer

This layer investigates whether the central field scaling used in the Coulomb action law can be supported by quaternionic projection geometry.

- Hopf-style projection \(q\mapsto q\mathbf kq^{-1}\) maps \(S^3\) orientation states to \(S^2\) directions.
- Conserved projected \(S_r^2\) flux gives \(E(r)\sim 1/r^2\).
- Integrating the radial field gives \(V(r)\sim -1/r\).
- This supports the scaling form used in Appendix B.
- It does not derive charge, \(\kappa\), Maxwell equations, or \(\mathrm{Ry}\).
