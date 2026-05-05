# Π_K^ang — Clean angular bridge from S^3 shells to hydrogen angular states

## 1. Clean statement

This note specifies an operator-level angular bridge at fixed shell index \(K\):

\[
\Pi_K^{\mathrm{ang}}:\mathcal H_K(S^3)\to\bigoplus_{\ell=0}^{K}\mathcal H_\ell(S^2).
\]

The goal is to make the shell-wise angular branching statement explicit while keeping implementation limits clear.

## 2. Bridge table

At fixed S^3 shell \(K\), the angular content of the shell is identified with the direct sum of ordinary \(S^2\) angular momentum sectors:

\[
\mathcal H_K(S^3)\to\bigoplus_{\ell=0}^{K}\mathcal H_\ell(S^2).
\]

\(\Pi_K^{\mathrm{ang}}\) is the operator-level version of this bridge. It sends each normalized coupled shell basis state \(\Phi^K_{\ell m}\) to the corresponding spherical harmonic \(Y_{\ell m}\).

| S^3 shell object | Hydrogen angular object |
|---|---|
| \(\mathcal H_K(S^3)\) | \(n\)-shell angular content |
| \(K\) | \(n-1\) |
| \(\Phi^K_{\ell m}\) | \(Y_{\ell m}\) |
| \(\ell=0,\dots,K\) | \(\ell=0,\dots,n-1\) |
| \(m=-\ell,\dots,\ell\) | magnetic label \(m\) |

## 3. Why counting is not enough

The identity

\[
\sum_{\ell=0}^{K}(2\ell+1)=(K+1)^2
\]

is necessary but not sufficient for a strong bridge statement.

A stronger claim requires a map that preserves:

1. basis labels \((\ell,m)\),
2. normalization/orthogonality,
3. angular momentum operator action.

## 4. Technical construction

### 4.1 \(S^3\) as \(SU(2)\)

Use the standard identification \(S^3\cong SU(2)\). Scalar harmonics on \(S^3\) can be organized shell-by-shell with Wigner \(D\)-matrix elements.

### 4.2 Fixed shell \(K\) and representation identification

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

### 4.3 Branching rule

Under diagonal \(SU(2)\)/\(SO(3)\) action,

\[
V_j\otimes V_j^*\cong\bigoplus_{\ell=0}^{2j}V_\ell.
\]

Since \(2j=K\):

\[
\mathcal H_K(S^3)\cong\bigoplus_{\ell=0}^{K}V_\ell
\cong\bigoplus_{\ell=0}^{K}\mathcal H_\ell(S^2).
\]

### 4.4 Definition of \(\Pi_K^{\mathrm{ang}}\)

In a coupled basis, one may write

\[
\Phi^K_{\ell m}(g)=\sum_{a,b}C^{\ell m}_{j a, j b}\,D^j_{ab}(g),
\]

or equivalently as normalized Clebsch-Gordan coupling of shell-wise Wigner-\(D\) basis elements.

Set

\[
\Pi_K^{\mathrm{ang}}\big(\Phi^K_{\ell m}\big)=Y_{\ell m},
\]

and extend linearly.

## 5. Normalization and isometry target

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

## 6. Angular momentum compatibility

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

## 7. Hopf-map warning

\(\Pi_K^{\mathrm{ang}}\) is not merely the Hopf point map \(q\mapsto qkq^{-1}\); it is a shell-level angular branching map.

## 8. Hydrogen identification

With \(K=n-1\):

\[
\mathcal H_{n-1}(S^3)\to\bigoplus_{\ell=0}^{n-1}\mathcal H_\ell(S^2),
\]

recovering standard hydrogen angular labels:

- \(\ell=0,\dots,n-1\),
- \(m=-\ell,\dots,\ell\).

## 9. Technical next steps

- numerical Clebsch-Gordan implementation,
- orthonormality tests,
- angular momentum label tests,
- dipole-transition compatibility.

## 10. Honesty boundary

This note strengthens the angular representation bridge by specifying an operator-level target.

It does **not** derive:

- radial Coulomb eigenfunctions,
- fine structure,
- the Rydberg constant,
- or the full Schrödinger-Coulomb solution.


## Numerical validation status

Status: **Low-K numerical construction implemented** (Gate 1).

- K range tested: K=0..5.
- Numerical Clebsch-Gordan coupling implemented with doubled quantum numbers and Condon-Shortley convention.
- Π_K^ang matrix orthonormality validated numerically (row/column checks near machine precision).
- L_z label compatibility validated under the dual convention m_source=a-b.
- L^2 compatibility implemented via pulled-back source Casimir \(L^2_{\text{source}}=P^\top L^2_{\text{target}}P\) with machine-precision intertwining diagnostics.
- Dipole compatibility validated at label level against existing hydrogen channel enumeration.
- Angular-only rank-1 transition operator implemented on target side and pulled back to S^3 with low-K intertwining diagnostics.

Remaining work:
- Explicit source-side generator construction \(L_x,L_y,L_z\) as an independent Casimir build (beyond pulled-back baseline).
- Native physical transition operator beyond the angular-only pulled-back skeleton.
- Radial amplitudes and oscillator strengths.
- Higher-K stability and conditioning analysis.

Honesty boundary: this is a validated low-K numerical bridge construction, not yet a full physical unitary projection/intertwiner for all K.
