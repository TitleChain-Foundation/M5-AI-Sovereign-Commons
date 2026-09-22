# SHADOW M5Index — Repo Implementation Notes

This patch is designed to merge into:

`TitleChain-Foundation/M5-AI-Sovereign-Commons`

It creates a new `shadow-m5index/` module plus SHADOW-specific issue forms, workflows and docs.

## Current seed

- 36 Q3 2026 SHADOW assets
- permanent `SHD-###` IDs
- JSON, JSONL and CSV registry
- Government / CRE / Farmland generated views
- permanent property QR codes
- evidence submission contracts
- debt-state / collection-chain specification
- Q3 2026 report release

## Important correction

The working `v0.2_enriched.xlsx` created during research contained a row-offset enrichment error in two sheets. This repo patch does **not** publish that workbook.

`SHADOW_M5Index_Master_Dataset_v0.3_repo_ready.xlsx` was rebuilt from the intact v0.1 dataset and enrichment was re-applied by `Asset_ID`.

## Merge rule

Treat seed research as public research data with its stated evidence/confidence status. Do not promote a conversational or unresolved claim merely because it appears in the seed dataset.

## Public contribution

The first launch can use GitHub Issue Forms. A later website/API can post the same schema while preserving the repo as the auditable technical source of truth.
