# Hydrogen Bound-State Shell Architecture as Scalar Harmonics on S³

## 1. Core claim

Hydrogen bound-state shell architecture is naturally represented by scalar harmonics on the three-sphere:

\[
S^3 \cong SU(2).
\]

The central observation is that scalar harmonic shells on \(S^3\) carry exactly the same principal shell counting and pre-spin angular degeneracy structure that appears in the hydrogen atom.

In Hydrogen Bridge v1, this is not presented as a complete first-principles replacement for the Schrödinger-Coulomb solution. It is presented as a compact spectral representation of hydrogen's shell architecture.

## 2. Scalar harmonics on S³

Let \(Y_{K,\alpha}\) denote scalar harmonics on \(S^3\), where

\[
K=0,1,2,\ldots
\]

labels the \(S^3\) shell and \(\alpha\) labels the states within that shell.

The scalar Laplacian spectrum on the unit three-sphere is

\[
-\Delta_{S^3}Y_{K,\alpha}=K(K+2)Y_{K,\alpha}.
\]

Therefore

\[
(-\Delta_{S^3}+1)Y_{K,\alpha}=(K+1)^2Y_{K,\alpha}.
\]

This motivates the shifted shell-number operator

\[
\hat N=\sqrt{-\Delta_{S^3}+1}.
\]

Acting on scalar harmonics,

\[
\hat N Y_{K,\alpha}=(K+1)Y_{K,\alpha}.
\]

## 3. Principal shell identification

Hydrogen Bridge v1 identifies the hydrogen principal shell number with the shifted \(S^3\) shell number:

\[
n=K+1.
\]

Equivalently,

\[
K=n-1.
\]

This is the bridge's central structural move. It allows hydrogen shell architecture to be represented by the compact spectral ladder of \(S^3\).

## 4. Degeneracy

The dimension of the scalar harmonic shell \(\mathcal H_K(S^3)\) is

\[
\dim\mathcal H_K(S^3)=(K+1)^2.
\]

Using \(n=K+1\), this becomes

\[
\dim\mathcal H_{n-1}(S^3)=n^2.
\]

This reproduces the familiar pre-spin hydrogen shell degeneracy.

That is the first major reason the \(S^3\) representation is worth pursuing: the degeneracy is not added by hand. It is already present in the scalar harmonic structure of \(S^3\).

## 5. Native shell-energy operator

Using the shell-number operator, define the spectral hydrogen shell operator

\[
H_C=-\frac{\mathrm{Ry}}{\hat N^2}.
\]

Since

\[
\hat N^2=-\Delta_{S^3}+1,
\]

this can also be written as

\[
H_C=-\frac{\mathrm{Ry}}{-\Delta_{S^3}+1}.
\]

Acting on a scalar harmonic shell,

\[
H_CY_{K,\alpha}
=-\frac{\mathrm{Ry}}{(K+1)^2}Y_{K,\alpha}.
\]

With \(n=K+1\),

\[
H_CY_{n-1,\alpha}
=-\frac{\mathrm{Ry}}{n^2}Y_{n-1,\alpha}.
\]

Thus the same \(S^3\) shell-number operator determines both the hydrogen energy denominator and the shell degeneracy.

## 6. Angular projection to ordinary hydrogen labels

The standard hydrogen angular labels are recovered through the decomposition

\[
\mathcal H_K(S^3)
\rightarrow
\bigoplus_{\ell=0}^{K}\mathcal H_\ell(S^2).
\]

With \(K=n-1\), this becomes

\[
\mathcal H_{n-1}(S^3)
\rightarrow
\bigoplus_{\ell=0}^{n-1}\mathcal H_\ell(S^2).
\]

Each \(S^2\) angular sector has dimension

\[
\dim\mathcal H_\ell(S^2)=2\ell+1.
\]

Therefore

\[
\sum_{\ell=0}^{n-1}(2\ell+1)=n^2.
\]

This matches

\[
\dim\mathcal H_{n-1}(S^3)=n^2.
\]

The \(S^3\) shell therefore packages the full pre-spin angular content of a hydrogen principal shell.

## 7. Why this matters

The bridge ties together three hydrogen facts that are usually introduced separately:

1. the principal shell number \(n\),
2. the energy denominator \(1/n^2\),
3. the angular degeneracy \(n^2\).

In the \(S^3\) representation, they arise from one compact spectral object:

\[
\hat N=\sqrt{-\Delta_{S^3}+1}.
\]

The core relationship is

\[
\boxed{
\hat N Y_{K,\alpha}=(K+1)Y_{K,\alpha}=nY_{K,\alpha}
}
\]

and therefore

\[
\boxed{
H_C=-\frac{\mathrm{Ry}}{\hat N^2}
}
\]

with

\[
\boxed{
\dim\mathcal H_{n-1}(S^3)=n^2.
}
\]

This is the mathematical center of Hydrogen Bridge v1.

## 8. Relation to shell locking

Hydrogen Bridge v1 also introduces a slice coordinate \(s\in\mathbb R_s\) and the shell-locking condition

\[
\hat N=\frac{s^2}{2}.
\]

Since \(\hat N=n\) on shell,

\[
n=\frac{s^2}{2}.
\]

This gives

\[
s^2=2n.
\]

The slice coordinate is therefore used as an action-shell coordinate, while the compact \(S^3\) harmonic shell carries the angular and spectral structure.

The central public claim should not depend on tuning the shell-locking potential. The strongest claim is simpler: scalar harmonics on \(S^3\) already encode the hydrogen shell number and pre-spin degeneracy.

## 9. What is native, calibrated, and still future work

### Native in the current bridge

- \(S^3\cong SU(2)\) as compact orientation/state geometry.
- Scalar harmonic spectrum \(-\Delta_{S^3}Y_K=K(K+2)Y_K\).
- Shifted shell-number operator \(\hat N=\sqrt{-\Delta_{S^3}+1}\).
- Principal shell identification \(n=K+1\).
- Degeneracy \(\dim\mathcal H_K(S^3)=(K+1)^2=n^2\).
- Spectral shell operator \(H_C=-\mathrm{Ry}/\hat N^2\).

### Calibrated in the current bridge

- The value of \(\mathrm{Ry}\).
- Numerical comparisons to known spectral lines.
- Fine-structure benchmark formulas.

### Future work

- Derive or constrain \(\mathrm{Ry}\), \(\kappa\), and physical coupling constants from deeper geometry.
- Upgrade the angular projection into a full operator-intertwiner statement.
- Derive the native \(S^3\times\mathbb R_s\) Schrödinger-type equation.
- Extend beyond shell architecture toward radial eigenfunctions, spin coupling, fine structure, and multi-electron atoms.

## 10. Public-facing summary

Hydrogen Bridge v1 proposes that the bound-state shell architecture of hydrogen has a natural representation in scalar harmonics on \(S^3\). The shifted \(S^3\) shell-number operator

\[
\hat N=\sqrt{-\Delta_{S^3}+1}
\]

has eigenvalues \(K+1\), which are identified with the hydrogen principal shell number \(n\). The same shell has dimension \((K+1)^2=n^2\), reproducing the pre-spin hydrogen angular degeneracy. With the calibrated spectral operator

\[
H_C=-\frac{\mathrm{Ry}}{\hat N^2},
\]

the standard hydrogen energy ladder \(E_n=-\mathrm{Ry}/n^2\) follows on each \(S^3\) shell.

This makes \(S^3\) not an arbitrary higher-dimensional embellishment, but a compact spectral space where hydrogen's principal energy ladder and angular shell degeneracy are represented by one operator structure.
