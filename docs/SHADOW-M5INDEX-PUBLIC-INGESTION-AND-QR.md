# SHADOW M5Index — Public Ingestion and QR Architecture

**Status:** Reviewed implementation proposal for public comment. The routes, forms, registries, receipts, and QR files described here are not live unless a linked repository artifact says otherwise.

**Source artifact:** `SHADOW-M5INDEX-PUBLIC-INGESTION-AND-QR.md`
**Source SHA-256:** `2fb4cfefed9f1b4a2099ac4e1f6055c5e0e56dbc3fd5ca20e045fa69a550f91b`

This document records the public-ingestion boundary proposed for SHADOW M5Index. It does not promote a submitted record to canonical evidence, establish title, create authority, or announce a deployed service.

## Public purpose

The proposed public workflow lets a contributor:

1. discover or nominate a public-research asset;
2. choose Government Buildings & Land, Commercial Real Estate, or Farmland;
3. add a public source or challenge a field;
4. receive submission and evidence identifiers;
5. track review without directly editing the canonical record; and
6. help resolve title, ownership, debt, rights, environmental, and disposition questions.

> **The public does not edit the truth. The public contributes evidence to the record.**

The repository remains the inspectable technical and evidence layer. A future website may provide the public interface, but no future route is represented as live by this specification.

## Authority and publication boundary

A submission, score, nomination, QR code, model output, or steward role creates no ownership, investment, financing, membership, acquisition, title, or decision authority.

Public submissions may enter as `SUBMITTED` or `SOURCE_LOCATED`. They must not become `CANONICAL` without the governed verification policy. Unknown remains unknown, and contradictory or superseded evidence remains visible.

Do not publish private M5POD records, credentials, keys, wallet data, private member information, confidential title files, bank records, or production endpoints.

## Stable identifiers

Assets use stable opaque identifiers such as `SHD-029`. Category, jurisdiction, owner, name, and status may change; the identifier must not.

Proposed submissions and evidence use separate identifiers:

```text
SUB-2026-000001
EVD-2026-000001
```

A submission identifier is a receipt for review, not proof that its claim is true.

## Permanent URLs and QR rules

A future canonical asset URL may follow this pattern:

```text
https://titlechainfoundation.org/shadow/assets/SHD-029
```

This is a proposed route, not a declaration that the route is deployed.

Each QR code must encode only the permanent public asset URL. It must not encode ownership data, personal data, deed text, wallet addresses, scores, or temporary report URLs. Campaign parameters may request an action, but they cannot alter the underlying asset identity or authority state.

QR generation must be deterministic, with a registry recording at minimum:

```json
{
  "asset_id": "SHD-029",
  "canonical_url": "https://titlechainfoundation.org/shadow/assets/SHD-029",
  "qr_svg": "qr/SHD-029.svg",
  "qr_png": "qr/SHD-029.png",
  "status": "proposed"
}
```

Do not generate or publish production QR codes until the canonical domain, routes, redirect policy, ownership, and long-term maintenance process are verified.

## Proposed repository surfaces

```text
shadow-m5index/
├── registry/
│   ├── assets.jsonl
│   ├── asset-index.csv
│   ├── asset-index.json
│   └── qr-registry.json
├── data/
│   ├── canonical/{government,cre,farmland}/
│   ├── submissions/{new-assets,evidence}/
│   └── archived/
├── evidence/{metadata,manifests}/
├── schemas/
├── qr/
├── scripts/
├── public/{government,cre,farmland}/
└── tests/
```

This tree is a build target. Empty or proposed paths are not evidence that the corresponding service exists.

## Common record model

Every sector record should share asset identity, location, jurisdiction, parcel or legal-description references, recorded owner and grantee fields, ownership-resolution state, disposition and transaction-proof state, title verification, rights, encumbrances, claims, obligations, environmental state, debt, M5MST state, versioned SHADOW scores, evidence state, verification date, completeness, and open questions.

Sector extensions may add:

- **Government:** agency, public-benefit window, disposition authority and method, preservation restrictions, reversionary interests, vacancy, and maintenance.
- **CRE:** property and occupancy metrics, borrower/lender/servicer state, maturity, modification, default, foreclosure, receivership, and REO state.
- **Farmland:** acreage classes, operator and lease state, crop/use, soil, water/mineral/pipeline rights, easements, conservation restrictions, mortgage, and agricultural ownership restrictions.

## Public actions

The first public forms should be limited to:

1. add a new asset;
2. add evidence to an existing asset;
3. challenge or correct an existing field; and
4. nominate an asset for People's Trust review.

A nomination creates no ownership, financing, investment, membership, eligibility, or acquisition right.

Before a native application exists, reviewed GitHub Issue Forms may provide a temporary interface. Contributors should not need to edit JSON or open a pull request.

## Evidence workflow

```text
SUBMITTED
→ SOURCE_VERIFIED
→ CORROBORATED
→ CANONICAL
```

Also preserve:

```text
UNRESOLVED
DISPUTED
REJECTED
CORRECTED
SUPERSEDED
```

No public form writes directly to `CANONICAL`.

Canonical evidence metadata should include the evidence and asset identifiers, scoped claim, source office or agency, source URL, source type, jurisdiction, observed and effective dates, instrument number where applicable, retrieval date, digest, evidence state, limitations, contributor, reviewer, and correction/supersession lineage.

Large binaries should normally remain in approved public archives or object storage; the repository retains provenance metadata, stable references, and digests where licensing permits.

## Steward boundary

A contributor may help maintain an asset's public research record as a local, title, debt, environmental, rights, capital, farmland, or historic steward. Stewardship of a research record does not convey control or authority over the underlying asset.

## Completeness is not a SHADOW score

A public page may display research completeness for identity, title, ownership, debt, rights, environment, disposition, and evidence. Completeness only measures populated and reviewed research surfaces. It is not TSI, an appraisal, a title opinion, a risk rating, or proof of transfer readiness.

## Ingestion pipeline

Initial flow:

```text
public form or reviewed Issue Form
→ submission JSON
→ schema validation
→ submission and evidence receipts
→ review queue
→ bounded extraction
→ human/source verification
→ pull request to canonical data
→ attributable review and merge
→ index rebuild
```

Later automated connectors may locate government, recorder, assessor, regulator, banking, servicing, agriculture, water, mineral, conservation, planning, and zoning sources. Automated ingestion may create `SOURCE_LOCATED` or `SUBMITTED`; it must not manufacture `CANONICAL` evidence.

## Required validation

Validation must fail closed for:

- duplicate asset, submission, or evidence identifiers;
- missing source and jurisdiction fields;
- invalid state values or broken cross-record references;
- private or security-sensitive fields;
- canonical claims without governed evidence;
- incomplete QR registry entries;
- QR destinations outside the approved canonical host;
- redirects to unapproved hosts;
- formula, macro, or external-workbook-link injection in public datasets; and
- any inference that a score, nomination, key, wallet, model, or QR creates authority.

## Report links

A future SHADOW report may link to verified public sector indexes and permanent asset pages. Ordinary readers should receive an accessible public interface rather than raw data alone, while the repository remains the audit layer.

No report cover or visual is itself a report, evidence source, official CAMELS rating, or proof that sector pages are live. Report publication requires a dated dataset version, methodology version, source and correction notes, accessibility text, and working destinations.

## Build order

1. closed schemas and validation;
2. reviewed seed conversion to canonical JSON/JSONL;
3. Government, CRE, and Farmland indexes;
4. evidence submission schema and Issue Forms;
5. generated asset detail records;
6. verified stable routes and QR registry;
7. deterministic QR generation;
8. completeness and public research queues;
9. CI validation;
10. website integration; and
11. automated source connectors only after manual ingestion is stable.

## Launch gate

Public ingestion is ready only when a contributor can browse a sector, open a stable asset record, distinguish known from unknown, choose a missing research task, submit a public authoritative source, receive a receipt, observe review state, and later see verified evidence incorporated without losing provenance or contradictory history.

Until those gates pass, links must be labeled as repository research or proposed architecture rather than a live public ingestion service.
