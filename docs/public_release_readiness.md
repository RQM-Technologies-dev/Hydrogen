# Public Release Readiness Checklist

This checklist defines what should be true before making the Hydrogen repository public.

## Public-facing center

The repository should orbit one narrow claim:

> Hydrogen bound-state shell architecture is naturally represented by scalar harmonics on \(S^3\).

The public release should avoid presenting Hydrogen Bridge v1 as a complete replacement for the Schrödinger-Coulomb solution. It should instead present a reproducible spectral-geometric bridge.

## Must be clear before public release

- [ ] README leads with the scalar-harmonic \(S^3\) shell architecture claim.
- [ ] `notes/s3_scalar_harmonic_shell_architecture.md` is the primary conceptual entry point.
- [ ] The repo clearly distinguishes native bridge structures from calibrated benchmark ingredients.
- [ ] `docs/claims_matrix.md` accurately labels what is implemented, calibrated, partial, and future work.
- [ ] All generated reports can be reproduced from a clean checkout using the Quickstart commands.
- [ ] Tests pass locally and in CI.
- [ ] Reference spectral-line data is either cited/versioned or clearly labeled as legacy benchmark data.
- [ ] No text claims a first-principles derivation of \(\mathrm{Ry}\), \(\kappa\), electric charge, Maxwell equations, fine structure, or the full Schrödinger equation.
- [ ] The future-work path is stated plainly: operator-intertwiner projection, native \(S^3\times\mathbb R_s\) Schrödinger-type equation, spin/fine-structure sector, and heavier atoms.

## Strong public claims allowed

The following claims are currently appropriate:

1. Scalar harmonics on \(S^3\) satisfy

\[
-\Delta_{S^3}Y_K=K(K+2)Y_K.
\]

2. The shifted shell-number operator

\[
\hat N=\sqrt{-\Delta_{S^3}+1}
\]

has eigenvalues \(K+1\).

3. Identifying \(n=K+1\) gives the hydrogen principal shell label.

4. The scalar harmonic shell dimension

\[
\dim\mathcal H_K(S^3)=(K+1)^2
\]

becomes the pre-spin hydrogen shell degeneracy \(n^2\).

5. With calibrated \(\mathrm{Ry}\), the spectral operator

\[
H_C=-\frac{\mathrm{Ry}}{\hat N^2}
\]

reproduces the shell energy ladder

\[
E_n=-\frac{\mathrm{Ry}}{n^2}.
\]

6. The repository provides reproducible software tables and diagnostics for this bridge.

## Claims to avoid before more work

The following claims should not be made yet:

- RQM has derived the full hydrogen atom from first principles.
- RQM has replaced the Schrödinger equation.
- RQM has derived \(\mathrm{Ry}\), \(\kappa\), electric charge, or Maxwell equations.
- The Hopf-projected flux model is a complete derivation of electromagnetism.
- The fine-structure benchmark is native rather than imported from standard correction formulas.
- The shell-locking potential is experimentally confirmed.

## Immediate next work before public release

1. Replace or supplement legacy hydrogen reference wavelengths with a cited authoritative dataset.
2. Add a short `docs/math_references.md` file with references for scalar harmonics on \(S^3\), Laplacian eigenvalues, and \(S^3\to S^2\) decomposition.
3. Add a stronger note on the projection/intertwiner relationship

\[
\mathcal H_K(S^3)\to\bigoplus_{\ell=0}^{K}\mathcal H_\ell(S^2).
\]

4. Ensure all public-facing language uses "calibrated bridge," "spectral representation," and "shell architecture" rather than overclaiming a completed theory.

## One-sentence public description

Hydrogen Bridge v1 is a reproducible spectral-geometric bridge showing that hydrogen's principal shell number, pre-spin angular degeneracy, and Rydberg energy denominator are naturally represented by scalar harmonic shells on \(S^3\).
