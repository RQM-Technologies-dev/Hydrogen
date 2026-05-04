# Pi_K^ang operator-level angular branching target

## 1. Purpose

This note upgrades the existing S^3->S^2 dimension-counting bridge into an **operator-level target** for angular decomposition at fixed shell index \(K\).

The goal is to specify the map

\[
\Pi_K^{\mathrm{ang}}:\mathcal H_K(S^3)\to\bigoplus_{\ell=0}^{K}\mathcal H_\ell(S^2)
\]

as a normalized angular-momentum branching/intertwiner target, while keeping current implementation limits explicit.

## 2. Why counting is not enough

The identity

\[
\sum_{\ell=0}^{K}(2\ell+1)=(K+1)^2
\]

is necessary, but not sufficient, for a strong bridge statement.

A stronger claim requires a map that preserves:

1. basis labels \((\ell,m)\),
2. normalization/orthogonality,
3. angular momentum operator action.

## 3. \(S^3\) as \(SU(2)\)

Use the standard identification \(S^3\cong SU(2)\). Scalar harmonics on \(S^3\) can be organized shell-by-shell using Wigner \(D\)-matrix elements (Peter-Weyl harmonic organization).

## 4. Fixed shell \(K\) and representation identification

At fixed shell \(K\), define

\[
j=\frac K2,
\qquad
\mathcal H_K(S^3)\cong V_j\otimes V_j^*.
\]

Dimension check:

\[
\dim(V_j\otimes V_j^*)=(2j+1)^2=(K+1)^2.
\]

## 5. Branching rule

Under diagonal \(SU(2)\)/\(SO(3)\) angular momentum action,

\[
V_j\otimes V_j^*\cong\bigoplus_{\ell=0}^{2j}V_\ell.
\]

Since \(2j=K\), this becomes

\[
\mathcal H_K(S^3)\cong\bigoplus_{\ell=0}^{K}V_\ell.
\]

Identify each \(V_\ell\) with \(\mathcal H_\ell(S^2)\), yielding

\[
\mathcal H_K(S^3)\cong\bigoplus_{\ell=0}^{K}\mathcal H_\ell(S^2).
\]

## 6. Definition of \(\Pi_K^{\mathrm{ang}}\)

Define the target branching map

\[
\Pi_K^{\mathrm{ang}}:\mathcal H_K(S^3)\to\bigoplus_{\ell=0}^{K}\mathcal H_\ell(S^2).
\]

Interpret \(\Pi_K^{\mathrm{ang}}\) as a **basis-changing angular decomposition operator**, not a crude pointwise projection.

In a coupled basis, one may write

\[
\Phi^K_{\ell m}(g)=\sum_{a,b}C^{\ell m}_{j a, j b}\,D^j_{ab}(g),
\]

or, with convention details deferred,

\[
\Phi^K_{\ell m}(g)=\text{normalized Clebsch-Gordan coupling of Wigner-}D\text{ shell basis elements}.
\]

Then set

\[
\Pi_K^{\mathrm{ang}}\big(\Phi^K_{\ell m}\big)=Y_{\ell m},
\]

and extend linearly.

## 7. Normalization and isometry target

Desired shell-wise normalization:

\[
\langle\Phi^K_{\ell m},\Phi^K_{\ell' m'}\rangle_{S^3}=\delta_{\ell\ell'}\delta_{mm'},
\]
\[
\langle Y_{\ell m},Y_{\ell' m'}\rangle_{S^2}=\delta_{\ell\ell'}\delta_{mm'}.
\]

Target isometry statement within fixed \(K\):

\[
\langle F,G\rangle_{S^3}=\langle\Pi_K^{\mathrm{ang}}F,\Pi_K^{\mathrm{ang}}G\rangle_{\oplus S^2}.
\]

## 8. Angular momentum compatibility

Intertwining target:

\[
\Pi_K^{\mathrm{ang}}L^2_{\mathrm{diag},S^3}=L^2_{S^2}\Pi_K^{\mathrm{ang}},
\]
\[
\Pi_K^{\mathrm{ang}}L_{z,\mathrm{diag},S^3}=L_{z,S^2}\Pi_K^{\mathrm{ang}}.
\]

So eigen-labels are preserved:

\[
L^2\Phi^K_{\ell m}=\ell(\ell+1)\Phi^K_{\ell m}
\quad\mapsto\quad
L^2Y_{\ell m}=\ell(\ell+1)Y_{\ell m},
\]

and similarly for \(m\).

## 9. Dipole transition compatibility as future work

After constructing \(\Pi_K^{\mathrm{ang}}\) numerically, next work is to define a rank-1 transition operator \(T^{(1)}\) on the \(S^3\)-shell side and test whether standard selection rules

\[
\Delta\ell=\pm1,
\qquad
\Delta m=0,\pm1
\]

emerge or are preserved under the map.

This is not complete yet.

## 10. Distinction from the Hopf map

Warning: the Hopf-style point map \(q\mapsto qkq^{-1}\) from \(S^3\) to \(S^2\) is geometrically important, but \(\Pi_K^{\mathrm{ang}}\) is **not** merely that point map.

\(\Pi_K^{\mathrm{ang}}\) is an operator-level shell decomposition / angular branching map.

## 11. Hydrogen identification

With \(K=n-1\):

\[
\mathcal H_{n-1}(S^3)\to\bigoplus_{\ell=0}^{n-1}\mathcal H_\ell(S^2),
\]

recovering standard hydrogen angular labels:

- \(\ell=0,\dots,n-1\),
- \(m=-\ell,\dots,\ell\).

## 12. Honesty boundary

This note strengthens the angular representation bridge by specifying an operator-level target.

It does **not** derive:

- radial Coulomb eigenfunctions,
- fine structure,
- the Rydberg constant,
- or the full Schrodinger-Coulomb solution.
