# Hydrogen reference line provenance (public-readiness)

## Status

The current `data/hydrogen_reference_lines.csv` rows are **legacy benchmark values pending authoritative verification**.
They are retained for continuity of Hydrogen Bridge v1 report generation, but they are not yet presented as a finalized public authoritative spectroscopy table.

## Intended authoritative source

- Primary source: NIST Atomic Spectra Database (ASD), Lines Data for Hydrogen (H I).
- URL: https://physics.nist.gov/asd
- Recommended retrieval mode:
  - Species: H I
  - Data type: Lines
  - Output fields: observed/ritz wavelength, uncertainty (if available), transition designation, lower/upper levels
  - Medium handling: explicitly capture whether each wavelength is in air or vacuum

## Why this file exists

Automated extraction from NIST ASD can be brittle across query/UI updates. For public release honesty, this repo now records:

1. exact provenance fields in CSV rows,
2. explicit medium (`air` or `vacuum`), and
3. a reproducible manual verification/update procedure.

## Manual update procedure (authoritative replacement path)

1. Open NIST ASD lines interface from https://physics.nist.gov/asd.
2. Query Hydrogen (H I) line data for the target transitions used in this repo:
   - Lyman: 2->1, 3->1, 4->1, 5->1, 6->1
   - Balmer: 3->2, 4->2, 5->2, 6->2, 7->2
   - Paschen: 4->3, 5->3, 6->3, 7->3, 8->3
3. For each transition, record:
   - wavelength (nm),
   - medium basis (air/vacuum),
   - source URL/query details,
   - access date,
   - table/query label used.
4. Replace legacy benchmark rows in `data/hydrogen_reference_lines.csv` with verified values.
5. Update row `notes` to remove "legacy benchmark" language once verified.
6. Run:
   - `pytest`
   - `python scripts/generate_reports.py`
   - `python scripts/generate_plots.py`
7. Confirm `reports/series_comparison.csv` and `reports/HYDROGEN_BRIDGE_V1_REPORT.md` render the updated provenance fields.

## Honesty boundary

Until step 4 is completed with verified NIST ASD extraction, this repository should describe the reference-line table as **partially complete for public release**: provenance schema and update path are in place; authoritative row replacement is still pending.
