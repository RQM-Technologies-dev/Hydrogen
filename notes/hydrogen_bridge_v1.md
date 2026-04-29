# Hydrogen as an S³ Spectral Shell: A Quaternionic Shell-Locking Bridge for RQM/QSG

## Abstract
This note defines a falsifiable Hydrogen Bridge v1 linking an RQM/QSG shell picture to standard hydrogen observables. The bridge is built around one operator,
\(\hat N = \sqrt{-\Delta_{S^3}+1}\), one lock relation, \(\hat N=s^2/2\), and one Coulomb-energy operator, \(H_C=-\mathrm{Ry}/\hat N^2\). With these ingredients, the framework reproduces principal-shell energies, \(n^2\) degeneracy, angular-state decomposition, and electric-dipole selection rules. A minimal simulator package provides benchmark tables and numerical shell-locking checks.

## 1. State space
We take
\[
M=S^3\times\mathbb R_s,
\]
where \(S^3\) carries compact harmonic structure and \(s\in\mathbb R\) is the shell coordinate used for locking.

## 2. \(S^3\) harmonic spectrum
For \(K=0,1,2,\dots\), the spherical harmonics on \(S^3\) satisfy
\[
-\Delta_{S^3}Y_K=K(K+2)Y_K.
\]
Hence \(-\Delta_{S^3}+1\) has eigenvalues \((K+1)^2\).

## 3. Shell-number operator
Define
\[
\hat N=\sqrt{-\Delta_{S^3}+1}.
\]
On the \(K\)-eigenspace, \(\hat N\) has eigenvalue \(K+1\equiv n\), identifying the principal quantum number.

## 4. Shell-locking condition
Impose
\[
\hat N=\frac{s^2}{2}.
\]
At the expectation-value level in sector \(K\), this predicts
\[
\left\langle\frac{s^2}{2}\right\rangle\approx K+1.
\]
A reduced one-dimensional locking Hamiltonian is used for falsification:
\[
H_K=-\eta\frac{d^2}{ds^2}+\beta\sin^2\!\left(\frac{\pi s^2}{2}\right)+\gamma\left(K+1-\frac{s^2}{2}\right)^2.
\]

## 5. Hydrogen energy operator
Define
\[
H_C=-\frac{\mathrm{Ry}}{\hat N^2}.
\]
Thus on shell \(n\):
\[
E_n=-\frac{\mathrm{Ry}}{n^2},
\]
matching the gross hydrogen spectrum.

## 6. Degeneracy
The \(S^3\) harmonic-space dimension is
\[
\dim\mathcal H_K(S^3)=(K+1)^2=n^2,
\]
which reproduces hydrogen's \(n^2\) degeneracy before spin/fine corrections.

## 7. Angular projection
The shell space projects as
\[
\mathcal H_{n-1}(S^3)\rightarrow\bigoplus_{\ell=0}^{n-1}\mathcal H_\ell(S^2),
\]
with magnetic sublevels \(m=-\ell,\dots,\ell\).

## 8. Transition rules
Electric-dipole channels use the standard rules:
\[
\Delta \ell=\pm 1,\qquad \Delta m=0,\pm1.
\]
Wavelengths are computed from
\[
\lambda=\frac{hc}{\mathrm{Ry}(1/n_f^2-1/n_i^2)}\quad (n_i>n_f).
\]

## 9. Fine structure as next correction
Next-order relativistic splitting is included via
\[
E_{n,j}=-\frac{\mathrm{Ry}}{n^2}+\frac{m_ec^2\alpha^4}{2n^3}\left[\frac{3}{4n}-\frac{1}{j+\frac12}\right].
\]
Hydrogen Bridge v1 reports fine-structure components for H-\(\alpha\) (\(3\to2\)) as a spectroscopy benchmark.

## 10. Falsifiability checklist
A v1 implementation is considered successful only if it reproducibly outputs:
1. Shell table \((n,K,s^2,s,n^2,E_n)\).
2. Angular states \((\ell,m)\) per shell.
3. Dipole-allowed transition channels with wavelengths.
4. Lyman/Balmer/Paschen comparison tables.
5. Numerical locking results with \(\langle s^2/2\rangle\approx K+1\) across \(K\)-sectors.
6. Fine-structure decomposition for H-\(\alpha\).
