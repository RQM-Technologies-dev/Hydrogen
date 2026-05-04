# Hydrogen reference line provenance (public-readiness)

## Status

The `data/hydrogen_reference_lines.csv` benchmark rows are now populated from verified NIST ASD H I line entries for the repo's Lyman, Balmer, and Paschen transition subset.

## Authoritative source

- Source: NIST Atomic Spectra Database (ASD), Lines Data for neutral hydrogen (H I)
- URL: https://physics.nist.gov/asd
- Access date for current table values: 2026-05-04

## Query method used

1. Open NIST ASD Lines Data interface from https://physics.nist.gov/asd.
2. Select spectrum `H I`.
3. Use line output with Ritz wavelengths enabled/preferred.
4. Match the transition subset used by this repository using lower/upper principal shells (`n_i -> n_f`):
   - Lyman: 2->1, 3->1, 4->1, 5->1, 6->1
   - Balmer: 3->2, 4->2, 5->2, 6->2, 7->2
   - Paschen: 4->3, 5->3, 6->3, 7->3, 8->3
5. Record wavelengths in nm together with the wavelength medium exactly as returned by NIST ASD.

## Ritz vs observed policy

This dataset uses Ritz wavelengths for the benchmark rows (where NIST provides Ritz values), consistent with ASD guidance that Ritz values are typically preferred for precision line references.

## Air/vacuum handling

- The `medium` column is explicit per row.
- UV Lyman rows are recorded as `vacuum`.
- Optical/IR Balmer and Paschen rows are recorded as `air`.
- No unmarked air/vacuum mixing is allowed.

## Reviewer note (scope boundary)

This update upgrades benchmark/reference data provenance and row authority only. It does **not** broaden or change native RQM/QSG theory claims, derivation status, or the Hydrogen Bridge v1 architectural boundaries.
