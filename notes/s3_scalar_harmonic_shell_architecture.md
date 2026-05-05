# S³ scalar harmonic shell architecture for hydrogen

## Public-facing summary

Hydrogen bound-state shell architecture is naturally represented by scalar harmonics on S³.

Hydrogen Bridge v1 proposes that the bound-state shell architecture of hydrogen has a natural representation in scalar harmonics on S³. The shifted S³ shell-number operator \(\hat N = \sqrt{-\Delta_{S^3}+1}\) has eigenvalues \(K+1\), which are identified with the hydrogen principal shell number \(n\). The same shell has dimension \((K+1)^2 = n^2\), reproducing the pre-spin hydrogen angular degeneracy. With the calibrated spectral operator \(H_C = -\mathrm{Ry}/\hat N^2\), the standard hydrogen shell energy ladder \(E_n = -\mathrm{Ry}/n^2\) follows on each S³ shell.

## Core construction

- Geometry/group anchor: \(S^3 \cong \mathrm{SU}(2)\).
- Scalar harmonics on \(S^3\):
  \[
  -\Delta_{S^3}Y_K = K(K+2)Y_K.
  \]
- Shifted shell-number operator:
  \[
  \hat N = \sqrt{-\Delta_{S^3}+1}.
  \]
- Action on scalar harmonic shells:
  \[
  \hat N\,Y_K = (K+1)Y_K.
  \]
- Principal shell identification:
  \[
  n = K+1.
  \]
- Degeneracy:
  \[
  \dim\mathcal H_K(S^3) = (K+1)^2 = n^2.
  \]
- Calibrated spectral hydrogen shell operator:
  \[
  H_C = -\frac{\mathrm{Ry}}{\hat N^2}.
  \]
- Shell energy result:
  \[
  H_CY_{n-1} = -\frac{\mathrm{Ry}}{n^2}Y_{n-1}.
  \]
- S³→S² angular decomposition (bridge statement):
  \[
  \mathcal H_{n-1}(S^3)\;\to\;\bigoplus_{\ell=0}^{n-1}\mathcal H_\ell(S^2).
  \]
- Counting identity:
  \[
  \sum_{\ell=0}^{n-1}(2\ell+1)=n^2.
  \]

## Interpretation

This note is the public anchor for the repository's scalar harmonic shell architecture and spectral representation framing. It captures the exact shell index map and degeneracy structure used by the simulator and documentation, while keeping the calibrated energy-scale boundary explicit.

The resonance interpretation is that each hydrogen shell corresponds to a compact S^3 scalar-harmonic resonance. Ordinary hydrogen labels (n, ell, m) are then read as projected labels of that higher-dimensional shell architecture.

## Honesty boundary

- This is a calibrated spectral-geometric bridge.
- It is not a completed first-principles derivation of the full Schrödinger-Coulomb solution.
- \(\mathrm{Ry}\) is calibrated in v1.
- The explicit S³→S² physical projection/intertwiner remains future work.
- Native fine-structure and coupling-constant derivations remain future work.
