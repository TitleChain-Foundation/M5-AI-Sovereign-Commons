# M5POD Living Documentation — Review and synchronization contract v0.3

**Implementation artifact:** M5POD_Documentation_Activation_v0_3.zip (local review package, not yet deployed).

## Source precedence (preserve, do not rewrite)
1. User-supplied `M5_Capital_Domain_Portfolio_OFFICIAL_2026-01-08.docx`, source authority for the **original portfolio with declared total 183**. Extraction currently yields 139 unique explicitly listed names; do not invent remaining rows or supplant this source with 326/351 estimates from other snapshots.
2. `M5Capital_FreedomOffice_OpenAPI_Partners_Revised_2026-10-23.xlsx`: 24 Freedom Office tool records and 25 featured M5-OpenAPI provider records.
3. `satonakaoshimoto/M5Ecosystem` canonical source for M5Canon/ICSN and active technical implementations, not an override for the historical source portfolio.
4. `TitleChain-Foundation/M5-AI-Sovereign-Commons`: reviewed public publication target.

## Living-document event contract
Each update records: source repository/path, source commit or immutable file digest, original author/provenance, steward, classification, document kind, affected canonical record IDs, change summary, policy version, reviewer and authorization receipt, publication SHA, and rollback reference. Editing the document index must never silently alter the immutable original or private M5POD contents.

## Safe synchronization
- Read-only authenticated ingestion from source repositories; fail closed on missing permissions, stale evidence or ambiguous mappings.
- Stage differences in a review branch; do not bidirectionally sync or write directly to default branches.
- Require designated human approval and the corresponding M5Canon/M5-CV gate before making public changes.
- Export only approved, nonprivate document and namespace metadata to the Commons. Never put registrar keys, private ownership evidence, private POD contents or member account details in static files.
- Validate source provenance, public-visibility decisions, freshness, broken routes and service claims.
- A domain or partner appearing in a workbook is not proof of DNS/ENS registration, signed agreement, service availability or governmental authority.
- Keep M5POD, Foundation standards and M5Ecosystem implementations discoverable through a single documentation interface; preserve their distinct owners and approval controls.

## Acceptance outstanding
- [x] Generate local review explorer, source-digest manifest and public-safe draft data feed.
- [x] Include official table names and both revised service catalogs with explicit verification unknowns.
- [x] Pass review-feed structural and status checks.
- [ ] Import approved static explorer into `site/` and link existing Commons navigation after human public-disclosure review.
- [ ] Configure authenticated canonical source ingest and digest-based drift checks.
- [ ] Implement reviewed PR publication and approved TitleChain event receipts.
- [ ] Verify actual Freedom Office endpoints and M5-OpenAPI connector activation.
- [ ] Verify DNS/ENS mappings, InLine mirrors and rollback.
- [ ] Complete GitHub Pages/TLS/DNS deployment and end-to-end checks.

**No live DNS, ENS, GitHub Pages, TitleChain issuance or M5POD permissions were changed by this documentation update.**
