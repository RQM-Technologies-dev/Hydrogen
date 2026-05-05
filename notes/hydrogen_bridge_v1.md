# Hydrogen Bridge v1 Technical Note

## 1. Scope and honesty boundary
Hydrogen Bridge v1 is a calibrated, falsifiable bridge between \(S^3\) spectral structure and hydrogen shell architecture. v1 is focused on hydrogen and uses \(\mathrm{Ry}\) as a calibration constant. It does not claim a first-principles derivation of \(\mathrm{Ry}\), \(\kappa\), charge, Maxwell equations, fine structure, or the full Schrödinger-Coulomb solution.

## 2. S^3 shell spectrum
\[
-\Delta_{S^3}Y_K = K(K+2)Y_K,\qquad K=0,1,2,\ldots
\]
So \((-\Delta_{S^3}+1)\) has eigenvalue \((K+1)^2\).

## 3. Shell-number operator
\[
\hat N = \sqrt{-\Delta_{S^3}+1},\qquad \hat N Y_K=(K+1)Y_K.
\]
Hence principal shell number is identified as
\[
n=K+1.
\]

## 4. Clean spectral operator
\[
H_C=-\frac{\mathrm{Ry}}{-\Delta_{S^3}+1}=-\frac{\mathrm{Ry}}{\hat N^2}.
\]
For shell \(n\):
\[
E_n=-\frac{\mathrm{Ry}}{n^2}.
\]

## 5. Degeneracy
\[
\dim\mathcal H_K(S^3)=(K+1)^2=n^2.
\]
This reproduces hydrogen shell degeneracy before spin/fine corrections.

## 6. Angular bridge
\[
\Pi_K^{\mathrm{ang}}:\mathcal H_K(S^3)\to\bigoplus_{\ell=0}^{K}\mathcal H_\ell(S^2),
\]
with \(K=n-1\), recovering \(\ell=0,\dots,n-1\) and \(m=-\ell,\dots,\ell\).

## 7. Validation layer
- Reproducible shell table and angular state counts.
- Lyman/Balmer/Paschen comparison against NIST ASD H I Lines Data.
- Shell-locking numerical diagnostic and generated reports/tests.

Reference wavelengths are sourced from NIST ASD H I Lines Data for the current Lyman/Balmer/Paschen subset, with explicit air/vacuum medium metadata and access-date provenance. Future work may add uncertainty columns, exact level labels, and broader line coverage.

## 8. Support and validation layers
The following are support/diagnostic layers and not the core first-read statement:
- projected central flux hypothesis (Appendix C),
- Coulomb action relation and closure-action support (Appendices A/B),
- fine-structure benchmark,
- numerical shell-locking finite-difference model details.

For layer ordering and suppression guidance, see `notes/layer_separation.md`.
