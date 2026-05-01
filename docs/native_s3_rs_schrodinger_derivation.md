# Native \(S^3\times \mathbb R_s\) Schrödinger-type derivation (initial pass)

## Scope and honesty boundary

This note starts a **theoretical** derivation pathway and should be read as a model-construction document. It is separate from verified spectroscopy data work in `data/hydrogen_reference_lines.csv`.

## 1) Native shell operator on \(S^3\)

On \(L^2(S^3)\), define

\[
\widehat N := \sqrt{-\Delta_{S^3}+1}.
\]

For scalar harmonic shell \(\mathcal H_K(S^3)\):

\[
-\Delta_{S^3} = K(K+2),\qquad
\widehat N=K+1.
\]

Thus principal shell label is naturally

\[
n=K+1.
\]

## 2) Shell-locking postulate in \(s\)-coordinate

Introduce a radial-scale coordinate \(s\in\mathbb R_+\) and impose the shell-locking relation

\[
\sqrt{-\Delta_{S^3}+1}=\frac{s^2}{2}.
\]

On shell \(K\), this gives

\[
K+1 = \frac{s^2}{2}
\quad\Longleftrightarrow\quad
s=\sqrt{2(K+1)}=\sqrt{2n}.
\]

Interpretation: \(s\) is not free inside a fixed shell sector; shell quantization constrains it to discrete values.

## 3) Coulomb-sector operator ansatz

Define the Coulomb-sector Hamiltonian ansatz

\[
H_C := -\frac{\mathrm{Ry}}{-\Delta_{S^3}+1}
      = -\frac{\mathrm{Ry}}{\widehat N^2}.
\]

Hence on \(\mathcal H_K(S^3)\),

\[
E_K = -\frac{\mathrm{Ry}}{(K+1)^2}
    = -\frac{\mathrm{Ry}}{n^2},
\]

recovering the hydrogenic \(n\)-dependence at the level of shell energies.

## 4) Schrödinger-type evolution on \(S^3\times\mathbb R_s\)

A minimal coupled equation template is

\[
i\hbar\,\partial_t\Psi
=\Big(T_s + V_{\mathrm{lock}}(s,\widehat N) - \frac{\mathrm{Ry}}{\widehat N^2}\Big)\Psi,
\]

with

- \(T_s\): chosen kinetic operator in \(s\),
- \(V_{\mathrm{lock}}\): strong term enforcing \(\widehat N\approx s^2/2\),
- angular sector controlled by \(\Delta_{S^3}\).

In the strict-locking regime (or projected shell-wise), this reduces to decoupled shell sectors labelled by \(n\).

## 5) Next derivation tasks (not yet claimed complete)

1. Specify a self-adjoint \(T_s\) and domain on \(L^2(\mathbb R_+,w(s)ds)\).
2. Provide an explicit \(V_{\mathrm{lock}}\) (penalty or constraint) and prove convergence to shell projectors.
3. Construct the intertwiner/projection to \(S^2\) states and track \(\ell,m\) multiplicities per shell.
4. Add perturbative structure (fine structure, Lamb-shift-scale corrections) without conflating with core shell spectrum.
5. Keep all spectroscopy claims tied to external verified data tables, not to this derivation text.
