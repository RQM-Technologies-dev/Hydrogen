# Clean native S^3 spectral hydrogen equation

## 1. Purpose

This note states the clean native S^3 spectral eigenvalue equation used in Hydrogen Bridge v1.

It is important to separate the clean shell-energy equation from the longer modeling stack:

- The clean equation is **not** the full stacked modeling Hamiltonian.
- The clean equation is the spectral shell equation

\[
H_C\Psi = E\Psi,
\qquad
H_C = -\frac{\mathrm{Ry}}{-\Delta_{S^3}+1}.
\]

## 2. The usual problem

In standard quantum mechanics, hydrogen is usually written in \(\mathbb R^3\) with a Coulomb potential and radial/angular separation.

Hydrogen Bridge v1 does not replace that theory. It uses a bridge representation focused on shell architecture after lifting to \(S^3\), where shell index, degeneracy, and shell-energy denominator are captured spectrally.

## 3. S^3 shell spectrum

For shell eigenfunctions \(Y_K\) on \(S^3\):

\[
-\Delta_{S^3}Y_K = K(K+2)Y_K.
\]

Therefore:

\[
(-\Delta_{S^3}+1)Y_K = (K+1)^2Y_K.
\]

Define:

\[
\hat N = \sqrt{-\Delta_{S^3}+1}.
\]

Then:

\[
\hat N Y_K = (K+1)Y_K.
\]

## 4. Native spectral hydrogen operator

Define the spectral Coulomb shell operator:

\[
H_C = -\frac{\mathrm{Ry}}{\hat N^2} = -\frac{\mathrm{Ry}}{-\Delta_{S^3}+1}.
\]

Core eigenvalue equation:

\[
\left(-\frac{\mathrm{Ry}}{-\Delta_{S^3}+1}\right)\Psi = E\Psi.
\]

For \(\Psi=Y_K\):

\[
H_CY_K = -\frac{\mathrm{Ry}}{(K+1)^2}Y_K,
\qquad
E_K = -\frac{\mathrm{Ry}}{(K+1)^2}.
\]

With hydrogen identification \(n=K+1\):

\[
E_n = -\frac{\mathrm{Ry}}{n^2}.
\]

This is the precise sense in which the repo treats hydrogen shell structure as an S^3 resonance: the shell eigenvalue of the shifted S^3 Laplacian determines the principal shell and calibrated energy denominator.

## 5. Why this is cleaner

The radial Coulomb shell law is encoded as a spectral function of the \(S^3\) Laplacian:

\[
(-\Delta_{S^3}+1)^{-1}.
\]

This single operator perspective ties together:

- principal shell number \(n\),
- \(S^3\) shell index \(K\),
- energy denominator \(n^2\),
- degeneracy \(n^2\),
- slice-action position \(s^2 = 2n\).

## 6. Relation to the s-coordinate

The \(s\)-coordinate is not required to write the clean spectral equation.

It enters as a shell-action coordinate through the shell-locking relation:

\[
\hat N = \frac{s^2}{2}.
\]

Hence:

\[
s^2 = 2n.
\]

This is used as a shell-locking condition, not as a required complicated dynamical term in the clean equation.

## 7. Relation to \(\Pi_K^{\mathrm{ang}}\)

Once shell \(K\) is fixed, the angular bridge map is:

\[
\mathcal H_K(S^3) \to \bigoplus_{\ell=0}^{K}\mathcal H_\ell(S^2).
\]

With \(K=n-1\):

\[
\mathcal H_{n-1}(S^3) \to \bigoplus_{\ell=0}^{n-1}\mathcal H_\ell(S^2).
\]

This recovers standard hydrogen angular labels:

- \(\ell = 0,\dots,n-1\),
- \(m = -\ell,\dots,+\ell\).

See: `notes/pi_k_angular_intertwiner.md`.

## 8. Optional modeling Hamiltonian

A longer modeling/scaffolding expression is sometimes used:

\[
H_{\mathrm{RQM-H}} = H_C + H_{\mathrm{lock}} + H_s + H_{\mathrm{FS}}.
\]

This is optional modeling structure, not the clean native equation headline.

Roles:

- \(H_C\): clean spectral hydrogen core,
- \(H_{\mathrm{lock}}\): optional penalty enforcing \(\hat N=s^2/2\),
- \(H_s\): optional numerical slice dynamics,
- \(H_{\mathrm{FS}}\): future/benchmark fine-structure extension.

## 9. Honesty boundary

This note does **not** derive:

- \(\mathrm{Ry}\) from first principles,
- \(\kappa\) or electric charge,
- Maxwell equations,
- full Coulomb radial eigenfunctions,
- fine structure,
- the complete Schrödinger-Coulomb solution.

It provides a clean calibrated S^3 spectral eigenvalue equation that reproduces the hydrogen shell-energy law.
