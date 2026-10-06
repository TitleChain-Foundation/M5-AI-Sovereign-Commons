# Sovereign Herd Open-Data Registry

This registry records candidate public/open sources for research and reference.

It is intentionally conservative: public availability does not automatically mean unrestricted commercial redistribution.

| Source | Material | Current evidence state | Initial use |
|---|---|---|---|
| Precision Beef — Animal Behaviour Classification, Zenodo 4064802 | 10 Hz collar acceleration + cattle behavior labels | `LICENSE_UNCLEAR` for redistribution in this package | Research/reference; verify terms before copying files |
| University of Strathclyde — Bolus Sensor Acceleration Data With Timestamp and Behavioural Classification | 107 hours, 3-axis acceleration, eating/rumination/other labels | `VERIFIED_ATTRIBUTION_REQUIRED` — CC BY 4.0 on source record | Attributed research/model development |
| University of Strathclyde — Bolus acceleration data 3x | Raw bolus acceleration from three cows | `VERIFIED_ATTRIBUTION_REQUIRED` — CC BY 4.0 on source record | Attributed research |
| BovHEAT | Open-source heat/estrus analysis software | `VERIFIED_PERMISSIVE` — MIT shown on repository | Method/code reference; input-data rights separate |
| MmCows | Multimodal dairy cattle wearable/location/vision research material | `REFERENCE_ONLY` pending source-level license audit | Architecture and research reference |

## Rules

1. Never copy a dataset into this repository solely because it is downloadable.
2. Record the source license and evidence.
3. Distinguish software license from dataset license.
4. Distinguish model-weight license from training-data license.
5. Keep attribution.
6. Mark unresolved terms explicitly.
7. Do not mix private farm-generated data with public training data.
8. Do not publish an individual farm's private telemetry as a benchmark without separate authorization.

Machine-readable entries are in `open-data-registry.json`.
