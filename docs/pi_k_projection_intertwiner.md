# Native \(S^3\) spectral projector \(\Pi_K\), character kernel, and \(S^3\to S^2\) branching

## Scope and status

This note is a **theoretical derivation document** for the Hydrogen program's native \(S^3\) harmonic architecture. It is not a spectroscopy measurement source. Experimental/observational line data remain tracked separately in `data/hydrogen_reference_lines.csv`.

## 1) Harmonic shell decomposition on \(S^3\cong SU(2)\)

Let \(\mathcal H = L^2(S^3)\) with Laplace--Beltrami operator \(\Delta_{S^3}\). The scalar harmonic decomposition is

\[
\mathcal H = \widehat\bigoplus_{K=0}^{\infty} \mathcal H_K(S^3),
\]

where each eigenspace satisfies

\[
-\Delta_{S^3} f = K(K+2)f,\qquad f\in\mathcal H_K(S^3),
\]

with multiplicity \((K+1)^2\).

Define the native shell number operator

\[
\widehat N := \sqrt{-\Delta_{S^3}+1}.
\]

Then on \(\mathcal H_K(S^3)\),

\[
\widehat N f = (K+1) f.
\]

So shell label \(n\) is naturally identified by

\[
n = K+1 \quad\Longleftrightarrow\quad K=n-1.
\]

## 2) Spectral projector \(\Pi_K\)

The orthogonal projector onto \(\mathcal H_K(S^3)\) is

\[
\Pi_K = \mathbf 1_{\{K(K+2)\}}(-\Delta_{S^3})
      = \mathbf 1_{\{K+1\}}(\widehat N).
\]

For any \(f\in L^2(S^3)\),

\[
(\Pi_K f)(u) = \int_{S^3} \mathcal K_K(u,v) f(v)\,d\mu(v),
\]

with reproducing kernel \(\mathcal K_K\).

## 3) Character-kernel form on \(SU(2)\)

Using \(S^3\cong SU(2)\), Peter--Weyl gives a bi-invariant kernel expressed by the spin-\(j\) character (with \(j=K/2\)):

\[
\mathcal K_K(u,v) = (K+1)\,\chi_{K/2}(u v^{-1}),
\]

where \(\chi_{K/2}\) is the irreducible \(SU(2)\) character. In class-angle form \(\theta\in[0,\pi]\),

\[
\chi_{K/2}(\theta) = \frac{\sin((K+1)\theta)}{\sin\theta},
\]

so \(\mathcal K_K\) is a zonal kernel depending only on geodesic separation.

Equivalent matrix-coefficient form:

\[
\mathcal K_K(u,v)=\sum_{m,m'=-K/2}^{K/2} D^{K/2}_{m m'}(u)\,\overline{D^{K/2}_{m m'}(v)}.
\]

## 4) Branching/intertwiner to \(S^2\)

Under the Hopf fibration \(S^3\to S^2\), each \(\mathcal H_K(S^3)\) branches into ordinary \(S^2\) harmonics up to degree \(\ell=K\):

\[
\mathcal H_K(S^3) \xrightarrow{\ \mathfrak I_K\ } \bigoplus_{\ell=0}^{K} \mathcal H_\ell(S^2).
\]

Here \(\mathfrak I_K\) denotes an intertwiner compatible with the symmetry action used in the chosen projection model (e.g., fiber averaging / weighted pushforward in program notes). The key counting identity is

\[
\sum_{\ell=0}^{K}(2\ell+1)=(K+1)^2=\dim\mathcal H_K(S^3),
\]

matching the \(S^3\) shell multiplicity.

## 5) Hydrogen-shell connection

Because \(\widehat N\vert_{\mathcal H_K}=K+1\), identifying principal shell index by \(n=K+1\) yields

\[
K=n-1,
\]

and the internal \(\ell\)-content of shell \(n\) appears as

\[
\ell=0,1,\dots,n-1.
\]

This document states the representation-theoretic scaffold only. It does **not** itself validate physical spectroscopy; that must come from external data sources (NIST ASD rows in this repo's data tables).
