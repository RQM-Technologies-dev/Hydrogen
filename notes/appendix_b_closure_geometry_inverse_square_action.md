# Appendix B — Closure Geometry and the Inverse-Square Action Law

## 1. Motivation

Appendix A starts from the Coulomb action-energy law

\[
E(J)=-\frac{\mu\kappa^2}{2J^2}
\]

and then maps action into the native \(S^3\) shell operator. This appendix fills the prior step: why fixed closed action under central flux geometry naturally produces an inverse-square action-energy relation.

Hydrogen’s inverse-square ladder arises from closed action on \(S^3\) equilibrating against central flux geometry.

Matter is phase-locked closure; hydrogen is inverse-square closure action.

This appendix strengthens the bridge architecture. It does not independently derive \(\mathrm{Ry}\), \(\kappa\), \(\mu\), or the Coulomb interaction from RQM/QSG first principles.

## 2. Quaternionic closure gives the action count

Use the unit quaternion/spinor loop:

\[
q(\phi)=e^{\mathbf u\phi},
\qquad \mathbf u^2=-1.
\]

Then:

\[
dq=\mathbf u e^{\mathbf u\phi}d\phi
\]

and:

\[
q^{-1}dq=\mathbf u\,d\phi.
\]

For spinorial closure over \(0\leq\phi\leq4\pi n\):

\[
\oint q^{-1}dq=4\pi n\mathbf u.
\]

Taking the norm gives:

\[
\left\|\oint q^{-1}dq\right\|=4\pi n.
\]

Define the closure number:

\[
N_c=\frac{1}{4\pi}\left\|\oint q^{-1}dq\right\|=n.
\]

The loop integral is dimensionless and quaternion-valued before taking a norm. It is not equal to \(\hbar\). Instead, \(\hbar\) is the physical scale converting closure count into action:

\[
J=N_c\hbar=n\hbar.
\]

## 3. Closed action creates a radial kinetic cost

For a projected closed bound state with characteristic radius \(r\), fixed action gives:

\[
J\sim pr.
\]

Therefore:

\[
p=\frac{J}{r}.
\]

The kinetic energy is:

\[
T=\frac{p^2}{2\mu}
\]

so:

\[
T(r)=\frac{J^2}{2\mu r^2}.
\]

A tighter closed loop has a larger kinetic cost. This is the radial energetic price of enforcing fixed closure action.

## 4. Central flux gives the \(1/r\) binding form

Use central flux geometry:

\[
\oint_{S^2_r}\mathbf F\cdot d\mathbf A=4\pi\kappa.
\]

Since area scales as:

\[
A=4\pi r^2,
\]

the radial field scales as:

\[
F(r)=\frac{\kappa}{r^2}.
\]

Since:

\[
F(r)=-\frac{dV}{dr},
\]

the potential scales as:

\[
V(r)=-\frac{\kappa}{r}.
\]

This is standard central-field geometry, used here as a semiclassical closure-action support layer.

## 5. Fixed-action energy and stability

Combine the closure kinetic cost and central binding:

\[
E_J(r)=\frac{J^2}{2\mu r^2}-\frac{\kappa}{r}.
\]

A stable closed state satisfies:

\[
\frac{dE_J}{dr}=0.
\]

Compute:

\[
\frac{dE_J}{dr}
=
-\frac{J^2}{\mu r^3}
+
\frac{\kappa}{r^2}.
\]

Set to zero:

\[
-\frac{J^2}{\mu r^3}
+
\frac{\kappa}{r^2}=0.
\]

Therefore:

\[
r_J=\frac{J^2}{\mu\kappa}.
\]

This gives the key scaling:

\[
r_J\sim J^2.
\]

Since \(J=n\hbar\),

\[
r_n\sim n^2.
\]

## 6. Energy at the stable closure radius

Substitute

\[
r_J=\frac{J^2}{\mu\kappa}
\]

into

\[
E_J(r)=\frac{J^2}{2\mu r^2}-\frac{\kappa}{r}.
\]

Then

\[
\frac{J^2}{2\mu r_J^2}
=
\frac{\mu\kappa^2}{2J^2}
\]

and

\[
-\frac{\kappa}{r_J}
=
-\frac{\mu\kappa^2}{J^2}.
\]

Therefore:

\[
E_J
=
-\frac{\mu\kappa^2}{2J^2}.
\]

Using \(J=n\hbar\):

\[
E_n
=
-\frac{\mu\kappa^2}{2n^2\hbar^2}.
\]

With

\[
\mathrm{Ry}=\frac{\mu\kappa^2}{2\hbar^2},
\]

recover:

\[
E_n=-\frac{\mathrm{Ry}}{n^2}.
\]

## 7. Relation to the \(S^3\) shell operator

Connect to the existing Hydrogen Bridge v1 operator:

\[
\hat N=\sqrt{-\Delta_{S^3}+1}.
\]

On \(S^3\):

\[
-\Delta_{S^3}Y_K=K(K+2)Y_K,
\]

so:

\[
\hat NY_K=(K+1)Y_K.
\]

Identify:

\[
n=K+1=N_c.
\]

Therefore:

\[
J=\hbar\hat N.
\]

The Coulomb closure-action law becomes:

\[
H_C
=
-\frac{\mu\kappa^2}{2\hbar^2\hat N^2}
=
-\frac{\mathrm{Ry}}{\hat N^2}.
\]

This is the same native spectral energy operator already used in Hydrogen Bridge v1.

## 8. Relation to slice-action locking

Connect to the slice relation:

\[
s^2=2n,
\qquad
n=\frac{s^2}{2}.
\]

Then the shell-locking condition is:

\[
\hat N=\frac{s^2}{2}.
\]

The same integer \(n\) appears as:

- quaternionic closure count \(N_c\),
- action quantum \(J=n\hbar\),
- \(S^3\) shell number \(K+1\),
- slice-action value \(s^2/2\),
- hydrogen energy denominator \(E_n=-\mathrm{Ry}/n^2\).

## 9. What this strengthens

Previously, the bridge flow was:

\[
E(J)\rightarrow J(s)\rightarrow H_C.
\]

Appendix B adds:

\[
\text{closure}\rightarrow J\rightarrow E(J)\rightarrow J(s)\rightarrow H_C.
\]

This strengthens the conceptual spine without changing the calibrated v1 implementation.

## 10. Honesty boundary

This appendix does not claim:

- an independent native derivation of \(\mathrm{Ry}\),
- a first-principles derivation of \(\kappa=e^2/(4\pi\varepsilon_0)\),
- a replacement of the Schrödinger solution,
- a full derivation of Coulomb eigenfunctions,
- extension beyond hydrogen.

It claims:

- quaternionic closure provides a natural integer action count,
- fixed-action central-flux equilibrium produces \(E(J)\sim -1/J^2\),
- this supports the existing \(S^3\) operator form \(H_C=-\mathrm{Ry}/\hat N^2\).
