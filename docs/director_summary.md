# Hydrogen Bridge v1 — Director Summary

## Core claim
Hydrogen Bridge v1 is a calibrated spectral-geometric bridge: hydrogen shell architecture is represented by scalar harmonics on \(S^3\), with one shell number controlling principal shell index, degeneracy, and calibrated energy denominator.

## Clean equation
\[
-\Delta_{S^3}Y_K=K(K+2)Y_K,\quad
\hat N=\sqrt{-\Delta_{S^3}+1},\quad
\hat N Y_K=(K+1)Y_K
\]
\[
n=K+1,\quad \dim\mathcal H_K(S^3)=(K+1)^2=n^2
\]
\[
H_C=-\frac{\mathrm{Ry}}{-\Delta_{S^3}+1},\quad
H_C\Psi=E\Psi,\quad
E_n=-\frac{\mathrm{Ry}}{n^2}
\]
\[
\Pi_K^{\mathrm{ang}}:\mathcal H_K(S^3)\to\bigoplus_{\ell=0}^{K}\mathcal H_\ell(S^2)
\]

## What is implemented
- Core S^3 shell spectrum and shell-number operator mapping.
- Shell table/energy helpers and \(n^2\) counting checks.
- Symbolic/operator-target angular bridge \(\Pi_K^{\mathrm{ang}}\).
- NIST ASD line-comparison, shell-locking diagnostics, tests, and generated report artifacts.

## What is not claimed
- No first-principles derivation of Ry, \(\kappa\), charge, or Maxwell equations.
- No full Schrödinger-Coulomb solution derivation.
- No native fine-structure derivation.
- No completed physical unitary \(\Pi_K\) construction yet.

## Why it matters
The bridge yields a compact, falsifiable architecture where shell number, degeneracy, and calibrated energy denominator are unified by a single shifted \(S^3\) Laplacian structure, with executable evidence and explicit honesty boundaries.

## Next technical milestones
1. Numerical low-\(K\) construction/tests for \(\Pi_K^{\mathrm{ang}}\) basis normalization and angular-label compatibility.
2. Expanded NIST ASD coverage with uncertainties and exact level labels.
3. Robustness scans for shell-locking diagnostics and tighter uncertainty reporting.
