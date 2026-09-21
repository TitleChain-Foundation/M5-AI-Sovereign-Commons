# SHADOW M5Index Engineering Epic

**Status:** Proposed implementation roadmap  
**Capability:** Systemic Holdings, Assets, Debt & Ownership Watch  
**Current increment:** PR-1 public research seed using v0.1 source data

## Outcome

Implement a first-class, public-safe asset intelligence capability that represents state, evidence, provenance, title, ownership, capital, debt, rights, obligations, environment, dispositions, threats, scores, and public-benefit review without creating authority or overstating source claims.

## Non-goals

This epic does not create a land registry, title insurer, appraisal, investment product, securities exchange, official CAMELS rating, bid, award, conveyance, funding commitment, or autonomous transaction authority. External authoritative records and accountable institutions remain controlling.

## Invariants

- Unknown facts remain unknown.
- `SUBMITTED` and `SOURCE_VERIFIED` never silently become `CANONICAL`.
- High bid, accepted offer, closing, deed, title state, and ultimate capital are separate claims.
- Title, rights, debt, environment, authority, and transferability are separable.
- Evidence events append; corrections and supersession remain visible.
- Scores cite method and input versions and grant no authority.
- Public data excludes private M5POD, identity, bank, credential, and secret material.
- Every automated or agent action remains explicitly delegated, bounded, attributable, and revocable.

## Delivery sequence

### PR 1 — Public structure and research seed

- Add the `shadow-m5index/` capability landing page.
- Preserve the canonical handoff and imported source workbook by checksum.
- Publish the 36-row asset CSV.
- Generate the requested normalized workbook tabs without inventing records.
- Document methodology and Orbitalys/People’s Trust boundaries.
- Add deterministic integrity and posture tests.

**Exit gate:** required tabs and IDs match; source fingerprints match; seed contains no `CANONICAL` claims; scores remain `NOT SCORED`; CAMEL remains explicitly unofficial; Spring Commons remains unresolved and non-authoritative.

### PR 2 — Versioned schemas and events

Define Draft 2020-12 schemas for asset identity, evidence claim, state event, current-state projection, organization/ownership relation, debt/lien, right/encumbrance, claim/obligation, environmental condition, disposition event, score, threat finding, and public-benefit review.

**Exit gate:** schema/example pairs validate; unknown fields fail as designed; correction and supersession examples retain lineage.

### PR 3 — Deterministic state engine and graph

Implement append-only event ingestion, current-state projection, subject/predicate/object graph output, temporal querying, corrections, disputes, and provenance traversal.

**Exit gate:** replay is deterministic; event ordering and supersession tests pass; source state cannot be promoted by inference.

### PR 4 — M5MST and authority controls

Add the M5 Master Title/State Agent interface for evidence handling and bounded task orchestration. Integrate current authority, jurisdiction, delegation, purpose, and receipt checks.

**Exit gate:** revoked, stale, missing, altered, or out-of-scope authority fails closed; no agent acts as principal.

### PR 5 — Versioned SHADOW scoring

Implement TSI, ASI, DPI, OOI, CCI, PVMI, and PBOI with published formulas, input completeness, confidence, limitations, method version, and reproducible fixtures.

**Exit gate:** deterministic outputs reproduce; incomplete inputs do not become false precision; PBOI is review-only.

### PR 6 — Synthetic SHADOW CAMEL

Publish the public-data C/A/M*/E/L/S* methodology and synthetic institution fixtures before evaluating any real institution.

**Exit gate:** all output says it is not an official CAMELS rating; proxy components and source limitations are visible.

### PR 7 — Orbitalys threat adapter

Connect versioned public-safe state events to a threat graph while preserving the authority boundary.

**Exit gate:** findings cite evidence and affected graph elements; threats cannot mutate evidence or authorize action.

### PR 8 — People’s Trust feasibility workflow

Implement nomination, multi-domain review, accountable reviewer decision, and explicit rights disclaimer.

**Exit gate:** nomination creates no ownership, security, membership, investment, financing, or acquisition right.

### PR 9 — Public aggregate feed and UI

Publish approved aggregate events to the M5 Global Index and add accessible views for search, state history, evidence, ownership paths, debt, rights, environment, score explanations, threats, and research queues.

**Exit gate:** no private evidence is emitted; all assertions link to provenance and display status/limitations.

## Initial backlog

| Priority | Work item | Acceptance evidence |
| --- | --- | --- |
| P0 | Govern evidence promotion | reviewed transition matrix and negative tests |
| P0 | Define event identity/supersession | replay and correction fixtures |
| P0 | Model title/rights/debt/environment independently | schema and projection tests |
| P0 | Map Spring Commons without transaction claims | crosswalk to `PPT-EZ-CA-0001` and `HOLD` posture |
| P1 | Resolve Tranche 1 sources | captured primary records or explicit unresolved state |
| P1 | Investigate Tranche 2 ownership/debt | claim-scoped sources and reviewer attribution |
| P1 | Monitor Tranche 3 dispositions | append-only state changes; no closing shortcut |
| P1 | Publish score methodology | versioned formulas and synthetic fixtures |
| P2 | Add graph/API/UI | provenance-preserving public views |

## Required review roles

- data/provenance reviewer;
- TitleChain/title-state reviewer;
- security and privacy reviewer;
- legal/process subject-matter reviewer for consequential claims;
- methodology reviewer for scores and CAMEL;
- accessibility reviewer for public interfaces; and
- accountable maintainer for releases and evidence-state promotion.

## Definition of done

A milestone is complete only when artifacts, tests, limitations, provenance, authority boundaries, and human-readable documentation agree. Test success proves bounded software behavior—not truth, legal status, compliance, ownership, transfer, funding, or production readiness.

[Open the SHADOW M5Index module](../shadow-m5index/README.md)
