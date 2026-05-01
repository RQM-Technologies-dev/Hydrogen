# Hydrogen reference line provenance (public-readiness)

## Status

`data/hydrogen_reference_lines.csv` now contains manually verified NIST ASD H I Ritz wavelengths for the currently tracked:

- Lyman transitions: 2->1 through 6->1
- Balmer transitions: 3->2 through 7->2
- Paschen transitions: 4->3 through 8->3

## Authoritative source

- Primary source: NIST Atomic Spectra Database (ASD), Lines Data for Hydrogen (H I)
- URL: https://physics.nist.gov/asd
- Retrieval framing used for this dataset:
  - Species: H I
  - Data type: Lines
  - Value basis: Ritz wavelength
  - Medium labels copied by ASD output convention (air/vacuum)

## Medium convention used in CSV

This repository does not remap media independently. The `medium` column records the medium corresponding to the NIST ASD line output convention for each listed transition.

For the currently included transitions this yields:

- Lyman rows: `vacuum`
- Balmer rows: `air`
- Paschen rows: `air`

## Maintenance procedure

For future updates or added transitions:

1. Query NIST ASD H I Lines Data.
2. Record Ritz wavelength and ASD medium basis for each transition.
3. Keep provenance columns (`source`, `source_url`, `source_access_date`, `source_table_or_query`, `notes`) populated.
4. Re-run project checks and report generation.

## Honesty boundary

- Verified spectroscopy claims should be made from the CSV/provenance tables.
- Theoretical S^3/R_s derivation notes are model-side documents and are not spectroscopy measurement sources.
