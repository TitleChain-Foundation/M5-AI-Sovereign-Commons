# Spring Commons v0.6 — Push Manifest

## Repository

`TitleChain-Foundation/M5-AI-Sovereign-Commons`

## Target project

`pilots/312-spring-commons`

## Recommended branch

`spring-commons-v0.6-open-entity-source-chain`

## Replace

1. `pilots/312-spring-commons/README.md`
2. `pilots/312-spring-commons/documents/public/00-Master-Index-and-Document-Control.pdf`
3. `pilots/312-spring-commons/documents/public/DOC-05-Investor-Executive-Brief.pdf`
4. `pilots/312-spring-commons/documents/public/DOC-23-Source-of-Funds-Entity-Provenance-Jurisdiction-Chain-and-Public-Transaction-Graph-Standard.pdf`
5. `pilots/312-spring-commons/documents/public/DOC-23-Source-of-Funds-Entity-Provenance-Jurisdiction-Chain-and-Public-Transaction-Graph-Standard.md`
6. `pilots/312-spring-commons/schemas/m5-jurisdictional-capital-provenance.schema.json`
7. `pilots/312-spring-commons/examples/PPT-EZ-CA-0001-jurisdictional-capital-provenance-example.json`
8. `pilots/312-spring-commons/update-notes/M5GLOBAL-CAPITAL-FLOW-INTELLIGENCE-METHODOLOGY.md`
9. `pilots/312-spring-commons/update-notes/PUSH-MANIFEST.md`

## Add / replace coordinated update map

10. `pilots/312-spring-commons/update-notes/V0.6-CROSS-DOCUMENT-UPDATE-MAP.md`

If `V0.5-CROSS-DOCUMENT-UPDATE-MAP.md` exists on the target branch, retain it only as historical release documentation or move it to a release/history area; the active update map should be v0.6.

## Add release and retained historical controls

11. `pilots/312-spring-commons/update-notes/V0.6-RELEASE-NOTES.md`
12. `pilots/312-spring-commons/update-notes/SEC-S7-2026-30-IMPLEMENTATION-CROSSWALK.md`
13. `pilots/312-spring-commons/update-notes/AUTHORITY-AND-PARTICIPANT-REGISTRY-TEMPLATE.md`
14. `pilots/312-spring-commons/update-notes/V0.4-CROSS-DOCUMENT-UPDATE-MAP.md`

Items 12–14 are retained from the previously unpushed v0.4 SEC-alignment update. The v0.6 README, Master Index, and Investor Executive Brief supersede their v0.4 counterparts; these three v0.4 update notes remain as historical implementation and authority controls.

## Important file-selection note

Use the v0.6 `DOC-05-Investor-Executive-Brief.pdf` in this package. It preserves the current photo-based brief, updates the front-page version marker to v0.6, and appends the two-page **Open Entity Grounding, Source-Chain Activation & M5Global Intelligence** addendum. Do not replace it with an older text-only or v0.4/v0.5 PDF.

## v0.6 focus

- OpenData.org as an optional open entity-reference source with dated dataset/coverage metadata.
- Overture Maps / GERS as an optional spatial/place grounding source.
- Canonical M5 entity/location identifier crosswalks across official and reference IDs.
- Explicit `SOURCE_CHAIN_ACTIVATED` evidence gate.
- Separate `DESTINATION_CHAIN_CONFIRMED` state.
- Versioned jurisdiction-path corrections and supersessions.
- Public-sector/intergovernmental capital provenance.
- Cross-border capital/regulatory routing.
- OBSERVED / ESTIMATED / MODELED / SCENARIO / FORECAST analytic labels.
- Public-analytics minimum-cohort, aggregation, delay, banding and suppression controls.
- Dataset license, snapshot, transformation and match-confidence lineage.

## Validation completed

- DOC-23 v0.6 DOCX rendered and visually reviewed; 24-page PDF produced from the verified document.
- DOC-05 v0.6 is 24 pages: the photo-based prior brief plus a two-page v0.6 addendum; the cover version marker was updated to v0.6 and the final PDF re-rendered for review.
- Master Index v0.6 is a four-page 23-document index and was rendered for review; DOC-23 row is kept intact across pages.
- JSON Schema uses Draft 2020-12 and the Spring Commons example validates with zero errors.
- Repo-ready DOC-23 Markdown was regenerated from the v0.6 DOCX so sections 1–36 remain synchronized.

## Legal / architecture boundaries preserved

- `.eth` jurisdiction aliases are technical adapters, not government authority or sovereign recognition.
- BrightQuery, OpenCorporates, OpenData.org and Overture/GERS are optional reference/evidence connectors, not authority roots or mandatory providers.
- Source-chain activation does not itself prove destination receipt, settlement finality, title change, lawful use of proceeds, or investment performance.
- Public / regulator-qualified-assurance / private-protected evidence planes remain separate.
- Official legal, government, regulated, bank/escrow, transfer-agent, professional and executed records remain controlling in their domains.
- M5-GCFI / Opportunity Registry are research/intelligence layers, not a registered exchange, ATS, broker-dealer, transfer agent, custodian, clearing agency, bank, investment adviser, or offering venue.
- Any future regulated activity requires the actual registrations, licenses, approvals, exemptions and authorized operator applicable to that activity.

## Suggested commit

`Spring Commons v0.6: open entity grounding and source-chain activation`

## Suggested PR title

`Spring Commons v0.6 — OpenData/Overture grounding + source-chain capital intelligence`
