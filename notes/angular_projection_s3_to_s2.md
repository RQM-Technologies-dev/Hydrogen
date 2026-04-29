# S^3 to S^2 angular projection note

This note records the angular projection/decomposition used in Hydrogen Bridge v1.

## Statement

For scalar shell harmonics on S^3 (with shell label H_K), the bridge uses:

H_K(S^3) -> ⊕_{ell=0}^{K} H_ell(S^2)

and for K=n-1:

H_{n-1}(S^3) -> ⊕_{ell=0}^{n-1} H_ell(S^2).

## Why this is the relevant structure

- S^3 ≅ SU(2), so harmonic sectors on S^3 carry a compact representation structure.
- Scalar harmonics on S^3 at shell K have dimension (K+1)^2.
- The projected S^2 angular labels are the standard hydrogen labels ell,m with m=-ell,...,+ell.

State-count check:

sum_{ell=0}^{n-1} (2ell+1) = n^2.

This matches dim H_{n-1}(S^3)=n^2 and therefore recovers the standard hydrogen angular counting before spin/fine corrections.

## Caveat / honesty boundary

This angular projection is a bridge/decomposition argument for mapping shell spaces to standard angular sectors.
It is not, in v1, a full first-principles derivation of all Coulomb eigenfunctions from native RQM/QSG dynamics.
