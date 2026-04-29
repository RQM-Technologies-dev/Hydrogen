# HYDROGEN BRIDGE V1 REPORT

This report summarizes a calibrated bridge, numerical shell-locking validation, and benchmark against hydrogen spectral architecture.

## Layer separation
Standard benchmark formulas/data are separated from native RQM/QSG bridge structures; see `notes/layer_separation.md`.

## Reference wavelength provenance
Reference lines are loaded from `data/hydrogen_reference_lines.csv` with medium metadata (air/vacuum) and source fields.
Current dataset values are legacy benchmark rows pending replacement by a fully cited authoritative spectroscopy dataset.

## Claims matrix
Status and honesty boundaries are tracked in `docs/claims_matrix.md`.

## 1. Shell table (n=1..8)
| n | K | s2 | s | degeneracy | energy_eV |
| --- | --- | --- | --- | --- | --- |
| 1 | 0 | 2.000000 | 1.414214 | 1 | -13.605693 |
| 2 | 1 | 4.000000 | 2.000000 | 4 | -3.401423 |
| 3 | 2 | 6.000000 | 2.449490 | 9 | -1.511744 |
| 4 | 3 | 8.000000 | 2.828427 | 16 | -0.850356 |
| 5 | 4 | 10.000000 | 3.162278 | 25 | -0.544228 |
| 6 | 5 | 12.000000 | 3.464102 | 36 | -0.377936 |
| 7 | 6 | 14.000000 | 3.741657 | 49 | -0.277667 |
| 8 | 7 | 16.000000 | 4.000000 | 64 | -0.212589 |

## 2. Angular state count table
| n | state_count | expected |
| --- | --- | --- |
| 1 | 1 | 1 |
| 2 | 4 | 4 |
| 3 | 9 | 9 |
| 4 | 16 | 16 |
| 5 | 25 | 25 |
| 6 | 36 | 36 |
| 7 | 49 | 49 |
| 8 | 64 | 64 |

## 3. Lyman/Balmer/Paschen comparison table
| series | transition | predicted_nm | reference_nm | medium | source | error_nm | relative_error_ppm |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Lyman | 2->1 | 121.502273 | 121.567000 | vacuum | Hydrogen Bridge v1 legacy benchmark | -0.064727 | -532.435521 |
| Lyman | 3->1 | 102.517543 | 102.572000 | vacuum | Hydrogen Bridge v1 legacy benchmark | -0.054457 | -530.913012 |
| Lyman | 4->1 | 97.201819 | 97.254000 | vacuum | Hydrogen Bridge v1 legacy benchmark | -0.052181 | -536.546273 |
| Lyman | 5->1 | 94.923651 | 94.974000 | vacuum | Hydrogen Bridge v1 legacy benchmark | -0.050349 | -530.133486 |
| Lyman | 6->1 | 93.730325 | 93.780000 | vacuum | Hydrogen Bridge v1 legacy benchmark | -0.049675 | -529.695001 |
| Balmer | 3->2 | 656.112276 | 656.281000 | air | Hydrogen Bridge v1 legacy benchmark | -0.168724 | -257.090455 |
| Balmer | 4->2 | 486.009094 | 486.133000 | air | Hydrogen Bridge v1 legacy benchmark | -0.123906 | -254.881598 |
| Balmer | 5->2 | 433.936691 | 434.047000 | air | Hydrogen Bridge v1 legacy benchmark | -0.110309 | -254.141248 |
| Balmer | 6->2 | 410.070173 | 410.174000 | air | Hydrogen Bridge v1 legacy benchmark | -0.103827 | -253.129740 |
| Balmer | 7->2 | 396.907426 | 397.007000 | air | Hydrogen Bridge v1 legacy benchmark | -0.099574 | -250.810500 |
| Paschen | 4->3 | 1874.606504 | 1875.627000 | air | Hydrogen Bridge v1 legacy benchmark | -1.020496 | -544.082563 |
| Paschen | 5->3 | 1281.469290 | 1281.807000 | air | Hydrogen Bridge v1 legacy benchmark | -0.337710 | -263.464093 |
| Paschen | 6->3 | 1093.520461 | 1093.807000 | air | Hydrogen Bridge v1 legacy benchmark | -0.286539 | -261.965137 |
| Paschen | 7->3 | 1004.671923 | 1004.938000 | air | Hydrogen Bridge v1 legacy benchmark | -0.266077 | -264.769302 |
| Paschen | 8->3 | 954.345129 | 954.621000 | air | Hydrogen Bridge v1 legacy benchmark | -0.275871 | -288.984490 |

## 4. Shell-locking validation table
| K | target_x | expectation_x | error | variance_x | eigenvalue_0 |
| --- | --- | --- | --- | --- | --- |
| 0 | 1.000000 | 0.998125 | -0.001875 | 0.003883 | 5.180950 |
| 1 | 2.000000 | 1.998686 | -0.001314 | 0.005545 | 7.280423 |
| 2 | 3.000000 | 2.998935 | -0.001065 | 0.006837 | 8.867456 |
| 3 | 4.000000 | 3.999083 | -0.000917 | 0.007935 | 10.188378 |
| 4 | 5.000000 | 4.999185 | -0.000815 | 0.008909 | 11.338442 |
| 5 | 6.000000 | 5.999261 | -0.000739 | 0.009793 | 12.366492 |

## 5. H-alpha fine-structure table
| label | delta_E_eV | wavelength_nm |
| --- | --- | --- |
| 3p_3/2 -> 2s_1/2 | 1.889729 | 656.094953 |
| 3d_3/2 -> 2p_1/2 | 1.889729 | 656.094953 |
| 3s_1/2 -> 2p_1/2 | 1.889716 | 656.099611 |
| 3p_1/2 -> 2s_1/2 | 1.889716 | 656.099611 |
| 3d_5/2 -> 2p_3/2 | 1.889689 | 656.109122 |
| 3d_3/2 -> 2p_3/2 | 1.889684 | 656.110675 |
| 3s_1/2 -> 2p_3/2 | 1.889671 | 656.115334 |

## 6. Generated plots
Plots not found. Run `python scripts/generate_plots.py` to generate `reports/plots/*.png`.

## 7. Limitations
- This implementation is a calibrated bridge and does not claim a first-principles derivation of the Rydberg constant.
- Scope remains hydrogen; heavier elements are out of scope for v1.
- Fine structure is benchmarked with a standard correction formula; native derivation is future work.