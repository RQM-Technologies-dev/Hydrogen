# Appendix A — From Coulomb Action to the S³ Spectral Hydrogen Operator

## 1. Motivation: why the \(s^{-4}\) term looked inserted

For the clean standalone S^3 spectral equation, see `notes/native_s3_spectral_hydrogen_equation.md`. This appendix explains one calibrated action-law route to that operator and should be read as supporting derivation, not the core first-read statement.

The term

\[
E(s) = -\frac{4\mathrm{Ry}}{s^4}
\]

works immediately once the shell relation \(s^2 = 2n\) is imposed. Taken alone, however, it can appear to be a fitted profile placed directly on the slice coordinate. This appendix shows the opposite: in the calibrated bridge it follows from the Coulomb action law plus the RQM/QSG slice-action identification, and can then be rewritten as a native S³ spectral energy operator.

## 2. Coulomb energy as an action law

Start from the Coulomb action-energy relation:

\[
E(J) = -\frac{\mu\kappa^2}{2J^2},
\qquad
\kappa = \frac{e^2}{4\pi\varepsilon_0}.
\]

For hydrogen-like bound shells, with \(J_n = n\hbar\),

\[
E_n = -\frac{\mu\kappa^2}{2(n\hbar)^2}
    = -\frac{\mathrm{Ry}}{n^2},
\]

where

\[
\mathrm{Ry} = \frac{\mu\kappa^2}{2\hbar^2}.
\]

In Hydrogen Bridge v1, \(\mathrm{Ry}\) is used as a calibration constant in a calibrated bridge for numerical validation; it is not presented as an independently derived constant from RQM/QSG.

## 3. Slice-action identification

Use the bridge relation

\[
s^2 = 2n,
\]

so that

\[
J(s) = \hbar n = \frac{\hbar s^2}{2}.
\]

Substitute into the Coulomb action law:

\[
\begin{aligned}
E(s)
&= -\frac{\mu\kappa^2}{2J(s)^2} \\
&= -\frac{\mu\kappa^2}{2(\hbar s^2/2)^2} \\
&= -\frac{2\mu\kappa^2}{\hbar^2s^4} \\
&= -\frac{4\mathrm{Ry}}{s^4}.
\end{aligned}
\]

Hence the \(s^{-4}\) energy law follows from Coulomb action plus slice-action identification; it is not an inserted potential term.

## 4. Shell locking and the S³ shell-number operator

On \(S^3\),

\[
-\Delta_{S^3}Y_K = K(K+2)Y_K.
\]

Define the shell-number operator

\[
\hat N = \sqrt{-\Delta_{S^3}+1},
\]

which gives

\[
\hat N Y_K = (K+1)Y_K.
\]

Impose the shell-locking condition:

\[
\hat N = \frac{s^2}{2}.
\]

Therefore,

\[
K+1 = n = \frac{s^2}{2}.
\]

## 5. Native S³ spectral energy operator

The same energy law is written spectrally as

\[
H_C = -\frac{\mathrm{Ry}}{\hat N^2}
    = -\frac{\mathrm{Ry}}{-\Delta_{S^3}+1}.
\]

Acting on \(Y_K\):

\[
H_CY_K = -\frac{\mathrm{Ry}}{(K+1)^2}Y_K.
\]

With \(K+1=n\):

\[
H_CY_{n-1} = -\frac{\mathrm{Ry}}{n^2}Y_{n-1}.
\]

## 6. Why this formulation is stronger

The energy law is no longer merely placed on the slice coordinate. It is encoded as the spectral function

\[
(-\Delta_{S^3}+1)^{-1}.
\]

This ties together, in one operator language:

- energy denominator,
- S³ shell number,
- hydrogen principal shell,
- degeneracy,
- slice-action position.

Compactly,

\[
\hat N = \sqrt{-\Delta_{S^3}+1}
       = \frac{s^2}{2}
       = n,
\]

\[
H_C = -\frac{\mathrm{Ry}}{\hat N^2}.
\]

This is the native S³ spectral energy operator used in the benchmark against hydrogen spectral architecture.

## 7. Degeneracy and interpretation

\[
\dim \mathcal H_K(S^3) = (K+1)^2 = n^2.
\]

The same shell number \(n\) controls
\(E_n \sim -1/n^2\),
\(\dim\mathcal H_n \sim n^2\),
and \(s^2 = 2n\).

Hydrogen bound states are S³ spectral shells whose shell-number operator simultaneously determines energy, degeneracy, and slice-action position.

## 8. Transition-energy form

\[
\Delta E
=
\mathrm{Ry}
\left(
  \frac{1}{(K_f+1)^2}
  -
  \frac{1}{(K_i+1)^2}
\right).
\]

Since \(n_i = K_i+1\), \(n_f = K_f+1\):

\[
\Delta E
=
\mathrm{Ry}
\left(
  \frac{1}{n_f^2}
  -
  \frac{1}{n_i^2}
\right).
\]

Selection rules remain projection rules:
\(\Delta \ell = \pm 1\), \(\Delta m = 0,\pm 1\).

## 9. Optional modeling scaffold

\[
H_{\mathrm{RQM-H}}
=
-\frac{\mathrm{Ry}}{-\Delta_{S^3}+1}
+ H_{\mathrm{lock}}
+ H_s
+ H_{\mathrm{FS}}.
\]

with

\[
H_{\mathrm{lock}}
=
\gamma
\left(
  \sqrt{-\Delta_{S^3}+1}
  -
  \frac{s^2}{2}
\right)^2,
\]

\[
H_s
=
-\frac{\hbar^2}{2\mu}\partial_s^2
+
\beta\sin^2\!\left(\frac{\pi s^2}{2}\right),
\]

\[
H_{\mathrm{FS}}
=
H_{\mathrm{rel}} + H_{\mathrm{SO}} + H_D.
\]

Section 9 is an optional modeling summary; the clean spectral core is \(H_C=-\mathrm{Ry}/(-\Delta_{S^3}+1)\).

Final caution: Hydrogen Bridge v1 uses \(\mathrm{Ry}\) as a calibration constant and does not claim an independent first-principles derivation of the Rydberg constant. The emphasis is numerical validation under the shell-locking condition within a calibrated bridge.
