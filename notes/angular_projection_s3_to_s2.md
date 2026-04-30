# S^3 to S^2 angular projection / decomposition bridge note

This note strengthens the Hydrogen Bridge v1 angular bridge statement while keeping calibrated-bridge honesty boundaries explicit.

## Bridge statement

At shell index \(K\), Hydrogen Bridge v1 uses the representation-theoretic decomposition intuition

\[
\mathcal H_K(S^3) \;\to\; \bigoplus_{\ell=0}^{K} \mathcal H_\ell(S^2),
\]

with hydrogen identification \(K=n-1\):

\[
\mathcal H_{n-1}(S^3) \;\to\; \bigoplus_{\ell=0}^{n-1} \mathcal H_\ell(S^2).
\]

## Why this is structurally plausible

1. **S^3 as SU(2):** S^3 is diffeomorphic to SU(2), so scalar harmonic shells on S^3 carry compact-group harmonic structure.
2. **Shell dimension on S^3:**
   \[
   \dim \mathcal H_K(S^3)=(K+1)^2.
   \]
3. **Ordinary S^2 angular sectors:**
   \[
   \dim \mathcal H_\ell(S^2)=2\ell+1.
   \]
4. **Dimension identity:**
   \[
   \sum_{\ell=0}^{K}(2\ell+1)=(K+1)^2,
   \]
   so the S^2-sector counting exactly matches the S^3 shell count.

This recovers the standard angular counting pattern used for hydrogen labels:

- \(\ell=0,\dots,n-1\),
- \(m=-\ell,\dots,+\ell\),
- total count \(n^2\).

## Intertwiner language (careful use)

In v1, the repo uses the above as a **decomposition/projection bridge statement** at the level of representation content and counting.

It does **not** yet present a fully constructed physical unitary projection operator with complete normalization and dynamics attached.

A precise future statement should define an explicit operator/intertwiner \(\Pi_K\) and validate it directly.

## Honesty boundary

This note supports angular-shell architecture and counting consistency only.

It does **not** yet derive the full Coulomb radial eigenfunctions or the full Schrödinger-Coulomb solution.

## Next operator-level upgrade

Target object:

\[
\Pi_K : \mathcal H_K(S^3) \to \bigoplus_{\ell=0}^{K} \mathcal H_\ell(S^2).
\]

Desired properties for a stronger future bridge:

1. linearity,
2. dimension preservation,
3. orthogonality/isometry or controlled normalization,
4. compatibility with angular-momentum labels \((\ell,m)\),
5. compatibility with dipole transition operators,
6. recovery of standard \(\ell,m\) counting in explicit basis form.

Until this operator-level program is completed, Hydrogen Bridge v1 should be read as a calibrated spectral representation bridge centered on S^3 scalar harmonic shell architecture.
