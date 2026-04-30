# Appendix C — Hopf Flux Projection and the Coulomb Field

*Toward hydrogen as a projected quaternionic field-closure system*

## 1. Motivation

Appendix B strengthens the closure-action side of the bridge while still assuming a central flux field with potential scaling \(V(r)\sim -1/r\). Appendix C asks the prior geometric question:

Can a Coulomb-like central field scaling emerge from projecting quaternionic orientation geometry on \(S^3\) onto observable \(S^2\) spatial shells?

This appendix demonstrates a projection/scaling mechanism. It does not derive electric charge, \(\kappa\), Maxwell equations, or \(\mathrm{Ry}\) from first principles.

\[
\text{quaternionic orientation on }S^3
\rightarrow
\text{Hopf-projected direction on }S^2
\rightarrow
\text{conserved projected flux}
\rightarrow
E(r)\sim r^{-2}
\rightarrow
V(r)\sim r^{-1}.
\]

## 2. Unit quaternions and observable directions

Let

\[
q=a+b\mathbf i+c\mathbf j+d\mathbf k,
\qquad
a^2+b^2+c^2+d^2=1.
\]

Use the Hopf-style projection

\[
\mathbf n(q)=q\mathbf kq^{-1}.
\]

Then \(\mathbf n(q)\) is a pure imaginary unit quaternion, naturally identified with a direction on \(S^2\):

\[
\mathbf n(q)\in S^2.
\]

Interpretation: the internal quaternionic orientation \(q\in S^3\) projects to an observable spatial direction \(\mathbf n\in S^2\).

## 3. Why this matters for Coulomb structure

A full \(S^3\) volume spreading law would not directly give the ordinary Coulomb \(1/r^2\) field. The observed central field is measured across ordinary spatial \(S_r^2\) shells. Therefore the relevant object is not full \(S^3\) volume dilution, but projected \(S^2\) flux.

\[
\Phi=\int_{S_r^2}\mathbf E\cdot d\mathbf A.
\]

For spherical symmetry,

\[
\mathbf E(r)=E(r)\hat{\mathbf r}.
\]

Hence

\[
\Phi=E(r)4\pi r^2,
\qquad
E(r)=\frac{\Phi}{4\pi r^2}.
\]

This is the inverse-square field scaling.

Coulomb structure may be the \(S^2\)-projected flux law of quaternionic orientation geometry on \(S^3\).

## 4. Potential scaling

Using

\[
\mathbf E=-\nabla V,
\]

and for a radial field,

\[
E(r)=-\frac{dV}{dr}.
\]

If

\[
E(r)=\frac{\Phi}{4\pi r^2},
\]

then

\[
V(r)=-\frac{\Phi}{4\pi r}+C
\]

up to sign convention and reference potential.

For attractive hydrogen binding, the effective potential is written

\[
V(r)=-\frac{\kappa}{r}.
\]

Appendix C supports the scaling form, not the independent value of \(\kappa\).

## 5. Relation to Appendix B

Appendix B used

\[
E_J(r)=\frac{J^2}{2\mu r^2}-\frac{\kappa}{r}.
\]

Appendix C supplies geometric support for the \(1/r\) central potential scaling used there.

\[
S^3\text{ quaternionic orientation}
\rightarrow
S^2\text{ Hopf-projected flux}
\rightarrow
V(r)\sim -1/r
\rightarrow
J\text{-closure equilibrium}
\rightarrow
E(J)\sim -1/J^2
\rightarrow
J=n\hbar
\rightarrow
H_C=-\mathrm{Ry}/\hat N^2.
\]

Hydrogen’s Coulomb field, action quantization, energy ladder, degeneracy, and shell-locking may be different projections of one quaternionic closure geometry.

## 6. Relation to the \(S^3\) shell operator

Hydrogen Bridge v1 uses

\[
\hat N=\sqrt{-\Delta_{S^3}+1}.
\]

Appendix C does not change the shell operator. It provides a projected-field support layer for the central potential scaling used upstream of the shell-energy law.

## 7. Numerical diagnostics implemented in the repo

The simulator/test layer now provides reproducible diagnostics:

- sample unit quaternions \(q\in S^3\),
- compute \(\mathbf n(q)=q\mathbf kq^{-1}\),
- verify \(\|\mathbf n(q)\|\approx 1\),
- verify approximate isotropy on \(S^2\),
- compute an inverse-square flux table,
- fit a log-log slope for \(E(r)\), expecting \(-2\),
- fit a log-log slope for \(|V(r)|\), expecting \(-1\).

## 8. Honesty boundary

This appendix does not claim:

- a complete derivation of electromagnetism,
- a derivation of electric charge,
- a derivation of \(\kappa=e^2/(4\pi\epsilon_0)\),
- a derivation of Maxwell equations,
- a derivation of \(\mathrm{Ry}\),
- a replacement for the Schrödinger-Coulomb solution.

It claims:

- Hopf-style quaternionic orientation projection naturally maps \(S^3\) orientations to \(S^2\) directions,
- conserved projected \(S_r^2\) flux gives \(E(r)\sim 1/r^2\),
- integrating the field gives \(V(r)\sim -1/r\),
- this supports the Coulomb scaling used by Appendix B and the Hydrogen Bridge v1 operator chain.

Hydrogen as a projected quaternionic field-closure system remains a research program, but Appendix C supplies the first reproducible field-projection step.
