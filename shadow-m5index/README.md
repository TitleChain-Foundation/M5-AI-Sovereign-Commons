# SHADOW M5Index

**SHADOW — Systemic Holdings, Assets, Debt & Ownership Watch**

> **Status: PR-1 public research seed using v0.1 source data—not the complete SHADOW M5Index v0.1 release defined by the canonical handoff.** This module is not a title report, appraisal, official regulatory rating, acquisition recommendation, investment product, securities exchange, offer, or evidence that a transaction closed. Unknown remains unknown; authoritative public, land-record, court, bank, regulator, and executed-instrument records control.

SHADOW M5Index is the proposed public intelligence and transition layer for examining real-world assets, ownership, capital, debt, liens, rights, claims, obligations, environmental conditions, disposition activity, and potential public-benefit review.

Its operating question is:

> What exactly is the asset, what state is it in, who has rights or claims against it, who has authority over it, what obligations travel with it, and what evidence proves each answer?

## Start with the data

| Artifact | Purpose |
| --- | --- |
| [Normalized master workbook](data/SHADOW_M5Index_Master_Dataset_v0.1.xlsx) | Seventeen-sheet public research workbook covering the requested SHADOW surfaces |
| [Asset inventory CSV](data/assets/SHADOW_M5Index_Assets_Index_v0.1.csv) | Portable 36-asset seed index spanning research Tranches 1–3 |
| [Data guide](data/README.md) | Provenance, tab map, evidence boundaries, and regeneration instructions |
| [Methodology](methodology/README.md) | State, evidence, scoring, CAMEL, Orbitalys, and People’s Trust rules |
| [SHADOW CAMEL Report — Q3 2026](reports/SHADOW-CAMEL-REPORT-Q3-2026.md) | First-edition PDF and editable Word report, preliminary reading, release provenance, limitations, and public contribution actions |
| [Engineering epic](../docs/SHADOW-M5INDEX-ENGINEERING-EPIC.md) | Incremental implementation order and v0.1 acceptance gates |
| [Public ingestion and QR architecture](../docs/SHADOW-M5INDEX-PUBLIC-INGESTION-AND-QR.md) | Reviewed proposal for public evidence intake, stable identifiers, receipts, and deterministic QR generation |
| [Canonical handoff](reference/SHADOW-M5INDEX-CANONICAL-ENGINEERING-HANDOFF.md) | Preserved source specification supplied for this module |

The ingestion routes, forms, registries, receipts, and QR destinations are
proposed, not deployed. Do not generate production QR codes until the canonical
host, routes, redirects, and long-term maintenance process are verified.

## Architecture

```text
accountable principal and institution
→ verified authority and jurisdiction
→ TitleChain asset identity and event provenance
→ current TitleChain Asset State
→ Orbitalys threat analysis
→ SHADOW public research and versioned scores
→ People’s Trust feasibility review
→ approved public-safe aggregate events
→ M5 Global Index intelligence
```

The layers remain separate:

- **M5** models principal identity, credentials, authority, delegation, and bounded action.
- **TitleChain** links asset identity, authoritative records, provenance, rights, debt, and state events.
- **Orbitalys** maps threats and failure paths through a privately licensed M5 API integration; it grants no authority. The private service is not distributed or sublicensed by this repository.
- **SHADOW M5Index** organizes public research, state, scores, trends, and disposition watch.
- **People’s Trust review** asks whether deeper public-benefit feasibility work is warranted; nomination creates no right.
- **M5 Global Index** may receive approved public-safe aggregates; it is not represented as a securities exchange.

## Dataset status

The seed contains 36 uniquely identified research assets:

- **Tranche 1:** substantially resolved buyer/sponsor research leads;
- **Tranche 2:** unresolved ownership, rights, debt, or environmental research leads; and
- **Tranche 3:** active/recent disposition watch items supported by listed public sources.

`SUBMITTED` and `SOURCE_VERIFIED` are workflow states below `CANONICAL`. Confidence grades do not upgrade evidence. No workbook row currently establishes verified title, complete encumbrances, environmental clearance, ultimate capital, transfer authority, or acquisition readiness.

All SHADOW score rows remain `NOT SCORED`. The SHADOW CAMEL tab is intentionally empty because no synthetic institution methodology fixture is included in this PR; SHADOW CAMEL is not an official CAMELS rating. The schemas, event engine, indices, synthetic CAMEL validation, adapters, and public feed required for the handoff's full v0.1 definition of done remain future milestones.

## Spring Commons alignment

`SHD-029` maps to `PPT-EZ-CA-0001`, 312 N. Spring Street. Its presence on GSA’s accelerated-disposition list supports a disposition research state only. It does not establish:

- an active Historic Monument Public Benefit Conveyance;
- an eligible or authorized public applicant;
- GSA or NPS approval;
- a bid, award, accepted offer, deed, or title transfer;
- a committed or escrowed $25 million tranche; or
- authority for TitleChain, M5, SHADOW, or People’s Trust to transact.

See the [simulated GSA/NPS package](../pilots/312-spring-commons/simulations/gsa-historic-pbc/README.md) for the separate dual-ledger application workflow.

## Contribution rule

Inspect it, challenge it, add evidence, resolve an owner, trace a lender, follow a deed, map a threat, correct the record, or nominate an asset—but never silently promote a research lead.

Every material claim should eventually carry subject, predicate, object, source, jurisdiction, observed/effective dates, confidence, evidence state, contributor/reviewer, and correction/supersession lineage. Private M5POD, KYC/KYB, bank, identity, credential, key, or security-sensitive data does not belong in this public module.

### Help update SHADOW

- [Nominate a government, CRE, or farmland asset](https://github.com/TitleChain-Foundation/M5-AI-Sovereign-Commons/issues/new?template=shadow-new-asset.yml)
- [Add official registry or public-record evidence](https://github.com/TitleChain-Foundation/M5-AI-Sovereign-Commons/issues/new?template=shadow-add-evidence.yml)
- [Challenge or correct an existing record](https://github.com/TitleChain-Foundation/M5-AI-Sovereign-Commons/issues/new?template=shadow-correction.yml)
- [Join the public TitleChain Foundation discussion](https://github.com/orgs/TitleChain-Foundation/discussions/23)

Useful contributions include dated links to recorder, assessor, court,
regulator, agency, SEC EDGAR, FDIC, FFIEC, GSA, USDA, state water/mineral,
conservation, planning, zoning, and similar authoritative public records. A
submission does not become `CANONICAL` until governed verification and
attributable approval are complete.

People who also want to enter the public activation pathway may
[set up the free IAM starting account](https://m5bank.app/) or
[join the public M5POD waitlist](https://m5podactivationdemo.netlify.app/).
Neither action creates a credential, membership, project role, or authority.
