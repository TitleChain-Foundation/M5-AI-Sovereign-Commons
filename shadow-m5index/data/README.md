# SHADOW M5Index data

## Published artifacts

- `SHADOW_M5Index_Master_Dataset_v0.1.xlsx` — normalized public master workbook.
- `assets/SHADOW_M5Index_Assets_Index_v0.1.csv` — exact portable asset inventory supplied with the source workbook.
- `source/SHADOW_M5Index_Master_Dataset_v0.1.source.xlsx` — immutable imported workbook retained for provenance.

The normalized workbook is generated; do not hand-edit it. Run `tools/build_master_dataset.py` with the source workbook and asset CSV when a reviewed source revision is accepted.

The preserved source workbook contains ten ordinary dashboard formulas. It has
no macros, external workbook links, hidden sheets, or cell comments. Treat it as
provenance input rather than an execution surface. The normalized public
workbook contains no formulas, macros, external links, hidden sheets, comments,
or defined names and is packaged deterministically.

## Workbook tabs

1. `README`
2. `Assets`
3. `Ownership_Capital`
4. `Debt_Liens`
5. `TitleChain_Asset_State`
6. `Rights_Encumbrances`
7. `Claims_Obligations`
8. `Environmental_State`
9. `Dispositions_Deal_Flow`
10. `SHADOW_Scores`
11. `SHADOW_CAMEL`
12. `Orbitalys_Threats`
13. `Peoples_Trust_Review`
14. `Evidence_Sources`
15. `Research_Queue_T1`
16. `Research_Queue_T2`
17. `Research_Queue_T3`

The original workbook combined rights, obligations, and environmental records and omitted a CAMEL sheet. Normalization separates only existing records by `Record_Type`; it does not create missing facts. The CAMEL sheet contains headers only.

## Evidence states

- `SUBMITTED` — a research lead was supplied; revalidation is required.
- `SOURCE_VERIFIED` — the cited public source was located and supports the scoped observation.
- `CORROBORATED` — multiple suitable sources support the scoped claim.
- `CANONICAL` — reserved for the governed acceptance process with sufficient authoritative evidence.
- `DISPUTED`, `UNRESOLVED`, `REJECTED`, `CORRECTED`, `SUPERSEDED` — preserve conflict and history.

Source verification is claim-scoped. A GSA listing can support an asset being listed for disposition; it cannot by itself prove buyer identity, closing, deed transfer, title condition, debt, ultimate capital, environmental clearance, or transferability.

## Public-data boundary

The data is research-oriented and may contain incomplete or outdated public reporting. Names are included only where the supplied research associates them with public transaction or entity reporting. Contributors must attach a source and avoid private personal, identity, bank, credential, or security-sensitive information.

## Regeneration

The generator requires Python and `openpyxl`:

```text
python shadow-m5index/tools/build_master_dataset.py \
  --source-workbook shadow-m5index/data/source/SHADOW_M5Index_Master_Dataset_v0.1.source.xlsx \
  --source-assets-csv shadow-m5index/data/assets/SHADOW_M5Index_Assets_Index_v0.1.csv \
  --output shadow-m5index/data/SHADOW_M5Index_Master_Dataset_v0.1.xlsx
```

Validation checks sheet order, asset parity, ID uniqueness, evidence vocabulary, non-canonical seed status, score boundaries, workbook safety, and the Spring Commons `HOLD` posture.

[Back to SHADOW M5Index](../README.md)
