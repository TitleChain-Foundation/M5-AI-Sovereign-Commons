# SHADOW M5Index
## Canonical Engineering Agent Handoff

**Repository:** `TitleChain-Foundation/M5-AI-Sovereign-Commons`

**Status:** Proposed public-commons module for implementation and public review.

---

# 1. Canonical name

## SHADOW M5Index

### SHADOW =
**Systemic Holdings, Assets, Debt & Ownership Watch**

SHADOW M5Index is the public intelligence and transition layer for tracking real-world assets, debt, ownership, rights, risk, value migration, disposition activity, and potential public-benefit acquisition opportunities.

Its job is to:

> **Watch the old-world holdings. Follow the deal flow. Trace the debt. Resolve the ownership. Establish the state of title. Map the threats. Follow the value. Identify what may move into the edge economy.**

---

# 2. Common-language definitions

## S — Systemic

Look at the asset as part of a connected system.

Common question:

> **What else is this connected to?**

---

## H — Holdings

Assets, rights, interests, loans, liens, securities, land, buildings, or other positions an entity holds or controls.

Common question:

> **What does this person or entity actually hold?**

---

## A — Assets

The thing of legal or economic value.

Examples:

- land;
- buildings;
- farms;
- infrastructure;
- housing;
- businesses;
- mineral rights;
- water rights;
- financial instruments.

Common question:

> **What is the thing of value?**

---

## D — Debt

Financial obligations attached to an asset or entity.

Common question:

> **Who is owed money, how much, and when does it matter?**

---

## O — Ownership

Legal and economic control of an asset.

Distinguish:

**recorded owner**

from

**ultimate economic owner.**

Common question:

> **Who ultimately controls and benefits from this asset?**

---

## W — Watch

Continuous monitoring of changes in:

- ownership;
- debt;
- title;
- liens;
- disposition;
- maturity;
- foreclosure;
- redevelopment;
- refinancing;
- public-benefit eligibility.

Common question:

> **What is changing now?**

---

# 3. What M5 means here

## M5 is the shift from user to issuer.

The architecture starts with the accountable principal.

Not:

```text
platform
→ account
→ user
```

But:

```text
principal
→ identity
→ authority
→ jurisdiction
→ records
→ assets
→ delegated capability
```

Public framing:

> **Your identity.  
> Your assets.  
> Your agents.  
> Your wallet.  
> Your vault.  
> Your records.**

The principal has standing before the platform.

---

# 4. Canonical architecture

```text
M5HUM / accountable principal
        ↓
M5IAM
        ↓
TCID
        ↓
private M5POD evidence
        ↓
M5-CV / SOPHIA credentials
        ↓
jurisdiction + policy + delegation
        ↓
M5Canon
deterministic authority decision
        ↓
M5AGT
bounded delegated action
        ↓
TitleChain
asset + title + rights + debt provenance
        ↓
TitleChain Asset State
current state of title, rights, claims, obligations,
encumbrances, environment and transferability
        ↓
Orbitalys
threat-vector graph
        ↓
SHADOW M5Index
public intelligence + scores + transition monitoring
        ↓
People's Trust
public-benefit feasibility / acquisition review
        ↓
chained asset events
        ↓
M5 Global Index and Exchange
privacy-preserving real-world economic signals
```

---

# 5. Architectural boundaries

## M5

Provides:

- principal identity;
- credentials;
- private evidence;
- authority;
- delegation;
- wallet/vault;
- bounded agents;
- deterministic policy.

---

## TitleChain

Provides:

- asset identity;
- authoritative-record linkage;
- title provenance;
- rights;
- liens;
- debt;
- jurisdiction;
- transfer history;
- asset-state events.

---

## Orbitalys

Provides:

- threat-vector graph;
- risk relationships;
- attack/failure paths;
- risk propagation.

Orbitalys does not create legal authority.

---

## SHADOW M5Index

Provides:

- public intelligence;
- asset/debt/ownership graph;
- scores;
- trend analysis;
- disposition watch;
- deal-flow discovery;
- public-benefit opportunity analysis.

---

## People's Trust

Provides:

- feasibility review;
- stewardship pathway;
- capital-structure analysis;
- public-benefit acquisition review.

---

## M5 Global Index and Exchange

Receives aggregated, public-safe, provenance-aware economic signals from real-world asset-state events.

It is an economic-intelligence/index layer.

It is not a securities exchange.

---

# 6. The critical missing layer: TitleChain Asset State

Do not treat:

```text
deed found
```

as equivalent to:

```text
asset ready for transfer
```

Every asset must have a current machine-readable:

# TitleChain Asset State

The state answers:

> **What is legally, economically, operationally, and evidentially true about this titled asset right now?**

---

# 7. Required Asset State fields

```text
asset_state
├── asset_identity
├── jurisdiction
├── provenance
├── title_state
├── rights_state
├── encumbrance_state
├── claims_state
├── obligations_state
├── environmental_state
├── authority_state
├── transfer_state
├── dispute_state
├── verification_state
└── evidence_state
```

---

# 8. Asset identity

Record:

- TitleChain asset ID;
- parcel ID;
- legal description;
- deed/record ID;
- jurisdiction;
- asset class;
- coordinates where appropriate;
- authoritative registry.

Question:

> **What exactly is this asset?**

---

# 9. Provenance

Track:

```text
origination
→ prior state
→ conveyance
→ assignment
→ subdivision
→ consolidation
→ new rights
→ current state
```

Each event requires:

```text
event_id
event_type
effective_date
recorded_date
authority
jurisdiction
source
evidence_digest
predecessor_state
successor_state
```

Never overwrite provenance.

Append new events.

---

# 10. Title verification

Never use only:

```text
verified = true
```

Use:

```text
title_verification
├── status
├── authoritative_source
├── source_record_id
├── jurisdiction
├── verified_by
├── verifier_credential
├── verification_method
├── verified_at
├── record_effective_at
├── evidence_digest
├── freshness
└── limitations
```

Possible states:

```text
UNVERIFIED
SOURCE_LOCATED
RECORD_MATCHED
TITLE_VERIFIED
TITLE_VERIFIED_WITH_EXCEPTIONS
TITLE_DISPUTED
TITLE_STALE
TITLE_SUPERSEDED
```

---

# 11. Rights state

Track rights separately.

Examples:

```text
surface_rights
subsurface_rights
mineral_rights
oil_gas_rights
water_rights
air_rights
development_rights
timber_rights
access_rights
easement_rights
leasehold_rights
utility_rights
pipeline_rights
beneficial_interests
```

Every right should carry:

```text
holder
grantor
scope
jurisdiction
effective_date
expiration
transferability
recording_reference
restrictions
evidence
```

Important principle:

> **Owning the land does not necessarily mean owning every economic right connected to the land.**

---

# 12. Encumbrance state

Track:

```text
MORTGAGE
DEED_OF_TRUST
TAX_LIEN
MECHANICS_LIEN
JUDGMENT_LIEN
EASEMENT
RIGHT_OF_WAY
LEASE
UTILITY_RIGHT
PIPELINE_RIGHT
COVENANT
RESTRICTION
OPTION
PURCHASE_RIGHT
ENVIRONMENTAL_LIEN
OTHER_RECORDED_INTEREST
```

Each requires:

```text
encumbrance_id
type
holder
priority
recorded_date
effective_date
amount
scope
release_conditions
expiration
status
source
evidence
```

Do not use the phrase:

```text
clean title
```

as a machine state.

Use explicit state.

---

# 13. Claims state

Track claims even before final validation.

Possible states:

```text
ASSERTED
RECORDED
DISPUTED
VALIDATED
REJECTED
SATISFIED
RELEASED
UNRESOLVED
```

A claim does not automatically become an established right.

---

# 14. Obligations state

Track obligations attached to the asset.

Examples:

- remediation;
- maintenance;
- restoration;
- decommissioning;
- pipeline abandonment;
- plugging;
- hazardous-material handling;
- preservation;
- tenant obligations;
- tax obligations;
- utility obligations;
- public-benefit covenants.

Each obligation requires:

```text
obligation_id
obligor
authority_or_beneficiary
type
trigger
due_date
estimated_cost
successor_liability
transferability
status
evidence
```

This is essential to understanding acquisition economics.

---

# 15. Environmental state

Track:

```text
known_contamination
suspected_contamination
hazardous_materials
underground_infrastructure
abandoned_infrastructure
remediation_order
cleanup_status
monitoring_requirement
environmental_lien
responsible_party
successor_liability
estimated_remediation_cost
regulatory_authority
```

Example states:

```text
NO_KNOWN_CONDITION
REVIEW_REQUIRED
KNOWN_CONDITION
ACTIVE_REMEDIATION
REMEDIATION_COMPLETE_UNVERIFIED
REMEDIATION_VERIFIED
RESPONSIBLE_PARTY_UNRESOLVED
```

---

# 16. Pipeline / abandoned infrastructure example

A parcel may appear inexpensive but actually have:

```text
SURFACE TITLE
VERIFIED

PIPELINE RIGHT-OF-WAY
ACTIVE

PIPELINE OPERATOR
UNKNOWN

ABANDONMENT STATUS
UNRESOLVED

DECOMMISSIONING RECORD
NOT FOUND

ENVIRONMENTAL CONDITION
REVIEW REQUIRED

REMEDIATION RESPONSIBILITY
UNRESOLVED
```

That is materially different from:

```text
PIPELINE RIGHT-OF-WAY
RELEASED

DECOMMISSIONING
VERIFIED COMPLETE

ENVIRONMENTAL RELEASE
RECORDED
```

SHADOW must preserve this distinction.

---

# 17. Authority state

Track who is currently authorized to affect the asset.

Examples:

```text
owner_authority
signer_authority
manager_authority
trustee_authority
lender_consent
governmental_approval
transfer_agent_authority
court_authority
regulatory_authority
```

Each actor:

```text
actor
role
credential
issuer
scope
standing
effective_date
expiration
revocation_status
jurisdiction
```

This connects to M5-CV and M5Canon.

---

# 18. Transfer state

Possible states:

```text
NOT_TRANSFERABLE
TRANSFER_RESTRICTED
CONSENT_REQUIRED
REGULATORY_APPROVAL_REQUIRED
LIEN_RELEASE_REQUIRED
CLAIM_RESOLUTION_REQUIRED
TITLE_CURE_REQUIRED
TRANSFER_ELIGIBLE
TRANSFER_AUTHORIZED
TRANSFER_PENDING
TRANSFER_RECORDED
```

This feeds M5MST Transfer Authority.

---

# 19. M5MST

Use the canonical:

# M5MST

**Origination  
Minting  
Sovereign Registration  
Transfer Authority**

M5MST answers:

> **Where is the asset in the M5 lifecycle?**

TitleChain Asset State answers:

> **What is currently true about the asset?**

Both are required.

---

# 20. Event-chain architecture

Never overwrite asset state.

Append state events.

Example:

```text
TITLE_VERIFIED

LIEN_RECORDED

PIPELINE_EASEMENT_DISCOVERED

ENVIRONMENTAL_REVIEW_REQUIRED

LIEN_SATISFIED

LIEN_RELEASE_RECORDED

TRANSFER_AUTHORITY_GRANTED
```

The current asset state is computed from chained events.

This gives:

# state + history + provenance

---

# 21. State confidence

Confidence belongs at the claim/state-element level.

Example:

```text
title:
  VERIFIED
  confidence: A

pipeline_right:
  ACTIVE
  confidence: A

pipeline_operator:
  UNRESOLVED
  confidence: C

remediation_obligation:
  POSSIBLE
  confidence: C
```

A verified deed must not make every other property condition appear verified.

---

# 22. SHADOW M5Index measures

Canonical index family:

## TSI — Title State Integrity

Question:

> **How complete, current, verified, and transferable is the asset's known title-and-rights state?**

Inputs:

- title verification;
- provenance completeness;
- rights resolution;
- encumbrance resolution;
- claims resolution;
- obligations resolution;
- environmental resolution;
- authority verification;
- transfer readiness;
- evidence freshness.

---

## ASI — Asset Stress Index

Question:

> **How much pressure is the asset itself under?**

---

## DPI — Debt Pressure Index

Question:

> **How much pressure is coming from financing?**

---

## OOI — Ownership Opacity Index

Question:

> **How difficult is it to determine ultimate control and economic ownership?**

High opacity is not an accusation.

It means ownership resolution remains incomplete.

---

## CCI — Capital Concentration Index

Question:

> **Where is acquisition and ownership capital concentrating?**

Track:

```text
PUBLIC
NONPROFIT
LOCAL_PRIVATE
DEVELOPER
FAMILY_OFFICE
PRIVATE_EQUITY
PRIVATE_CREDIT
REIT
BANK
TECH_INFRASTRUCTURE
SPE_UNRESOLVED
OTHER
```

Calculate:

- by transaction count;
- by dollar value.

---

## PVMI — Public Value Migration Index

Question:

> **Where did economic value move after public disposition or restructuring?**

Track:

```text
public investment
→ maintenance
→ disposition
→ acquisition
→ redevelopment
→ incentives
→ refinance
→ resale/current value
→ ultimate economic ownership
```

---

## PBOI — Public Benefit Opportunity Index

Question:

> **Does the asset warrant deeper People's Trust feasibility review?**

High score means:

> **review**

not:

> **buy.**

---

# 23. SHADOW CAMEL

Public-data banking-condition methodology.

Components:

```text
C — Capital
A — Asset Quality
M* — Public Management-Risk Proxy
E — Earnings
L — Liquidity
S* — Publicly Inferred Sensitivity
```

Initial weighting:

```text
C   20%
A   25%
M*  10%
E   15%
L   15%
S*  15%
```

Scale:

```text
1 strong
2 stable/watch
3 elevated
4 high risk
5 severe observable risk
```

SHADOW CAMEL must never claim to be an official regulatory CAMELS rating.

---

# 24. Core graph

Ownership:

```text
PROPERTY
→ PARCEL
→ TITLE
→ LEGAL OWNER
→ SPE
→ PRINCIPALS
→ SPONSOR
→ PARENT
→ FUND / FAMILY OFFICE / PUBLIC ENTITY
→ ULTIMATE CAPITAL
```

Debt:

```text
PROPERTY
→ LOAN
→ LIEN
→ ORIGINAL LENDER
→ CURRENT LENDER
→ SERVICER
→ SPECIAL SERVICER
→ MATURITY
→ MODIFICATION
→ FORECLOSURE / NOTE SALE
```

Rights:

```text
ASSET
→ TITLE
→ RIGHTS
→ RESTRICTIONS
→ OBLIGATIONS
→ JURISDICTION
→ TRANSFER AUTHORITY
```

---

# 25. Orbitalys threat graph

Create adapter:

```text
shadow-m5index/reference/orbitalys-adapter/
```

Initial vectors:

```text
authority_escalation
credential_compromise
principal_confusion
agent_self_authorization
title_document_tampering
wallet_substitution
beneficial_owner_opacity
stale_credentials
debt_data_poisoning
valuation_data_poisoning
jurisdiction_bypass
transfer_policy_bypass
audit_evidence_suppression
provider_tool_substitution
```

Orbitalys answers:

> **What can go wrong, and through what path?**

M5Canon answers:

> **Is the actor authorized?**

Keep these functions separate.

---

# 26. Disposition states

Public transition:

```text
P0 IDENTIFIED
P1 REVIEW
P2 MARKETED
P3 BIDDING
P4 HIGH_BIDDER
P5 UNDER_CONTRACT
P6 CLOSED
P7 REDEVELOPMENT
P8 REFINANCE_OR_RESALE
```

Transaction proof:

```text
S0 LISTED
S1 AUCTION_COMPLETED
S2 AWARD_ANNOUNCED
S3 CLOSING_CONFIRMED
S4 DEED_CONFIRMED
```

Ownership resolution:

```text
O0 BUYER_UNDISCLOSED
O1 GRANTEE_IDENTIFIED
O2 PRINCIPALS_IDENTIFIED
O3 SPONSOR_IDENTIFIED
O4 LENDER_IDENTIFIED
O5 ULTIMATE_CAPITAL_RESOLVED
```

Critical rules:

> **Winning bid ≠ completed sale.**

> **Completed sale ≠ ultimate ownership resolved.**

---

# 27. Deal-flow feed

SHADOW M5Index should continuously ingest observable events such as:

```text
GSA disposition
county deed
mortgage assignment
bank Call Report
CRE maturity
CMBS servicing event
foreclosure
auction
note sale
development entitlement
refinance
public acquisition
private acquisition
People's Trust nomination
```

Every event must link back to evidence.

---

# 28. Legacy Holdings → Edge Economy

Canonical transition model:

```text
LEGACY HOLDINGS
        ↓
SHADOW DISCOVERY
        ↓
TITLECHAIN PROVENANCE
        ↓
TITLECHAIN ASSET STATE
        ↓
ORBITALYS THREAT GRAPH
        ↓
SHADOW M5INDEX
        ↓
PEOPLE'S TRUST REVIEW
        ↓
M5 ACTIVATION
        ↓
EDGE ECONOMY
```

---

# 29. People's Trust path

Conventional path:

```text
asset
→ acquisition SPE
→ private equity/debt
→ redevelopment
→ refinance/sale
→ residual private ownership
```

People's Trust research path:

```text
asset
→ TitleChain state review
→ jurisdiction-specific public-benefit structure
→ People's Trust stewardship
→ structured outside capital
→ rehabilitation
→ productive operating revenue
→ repayment
→ defined residual economics
→ enduring public-benefit stewardship
```

The question is not:

> investors or no investors?

The question is:

> **Who owns the productive asset and residual economic value after capital obligations are satisfied?**

---

# 30. People's Trust nomination

Workflow:

```text
DISCOVERED
→ NOMINATED
→ EVIDENCE REVIEW
→ TITLE STATE REVIEW
→ DEBT / LIENS
→ RIGHTS / OBLIGATIONS
→ ENVIRONMENTAL REVIEW
→ PUBLIC-BENEFIT ELIGIBILITY
→ CAPITAL FEASIBILITY
→ COMMUNITY REVIEW
→ ADVANCE / HOLD / DECLINE / NEED MORE EVIDENCE
```

Nomination creates no:

- ownership right;
- security;
- investment right;
- membership;
- financing commitment.

---

# 31. M5 Global Index and Exchange integration

Do not send private title files into M5 Global.

Send public-safe state events and aggregates.

Possible signals:

```text
TITLE_VERIFIED
LIEN_ADDED
LIEN_RELEASED
RIGHT_RESERVED
DEBT_REFINANCED
ENVIRONMENTAL_OBLIGATION_IDENTIFIED
TRANSFER_AUTHORIZED
TRANSFER_RECORDED
REMEDIATION_COMPLETE
ASSET_RETURNED_TO_PRODUCTIVE_USE
```

Aggregated examples:

```text
number of assets entering disposition

value of assets changing ownership

acreage carrying unresolved rights

CRE debt nearing maturity

environmental obligations identified

assets returned to productive use

public-benefit transfers completed
```

This becomes real-time economic intelligence from actual asset-state change.

---

# 32. Repository structure

Create:

```text
shadow-m5index/
├── README.md
├── methodology/
├── schemas/
├── data/
│   ├── assets/
│   ├── institutions/
│   ├── dispositions/
│   ├── rights/
│   ├── obligations/
│   ├── jurisdictions/
│   └── sources/
├── reports/
├── examples/
├── visuals/
├── reference/
│   ├── graph/
│   ├── scoring/
│   ├── titlechain-adapter/
│   ├── orbitalys-adapter/
│   ├── camel/
│   └── people-trust-review/
└── tests/
```

Also create:

```text
docs/SHADOW-M5INDEX-ENGINEERING-EPIC.md
```

---

# 33. Root README

Add SHADOW M5Index to the root README as a first-class Commons capability.

Include:

- name and acronym;
- common-language definitions;
- M5 user → issuer;
- TitleChain Asset State;
- Orbitalys;
- index family;
- SHADOW CAMEL;
- People’s Trust;
- M5 Global connection;
- public contribution CTA.

Start-here row:

> **I want to understand real-world assets, title state, debt, ownership, banking risk, deal flow, and People's Trust opportunities → SHADOW M5Index**

---

# 34. Required schemas

Create at minimum:

```text
asset.schema.json
asset-state.schema.json
asset-state-event.schema.json
entity.schema.json
ownership-relationship.schema.json
title-verification.schema.json
right.schema.json
encumbrance.schema.json
claim.schema.json
obligation.schema.json
environmental-state.schema.json
authority-state.schema.json
transfer-state.schema.json
debt.schema.json
lien.schema.json
deed.schema.json
disposition.schema.json
evidence.schema.json
threat-vector.schema.json
shadow-index.schema.json
shadow-camel.schema.json
people-trust-nomination.schema.json
people-trust-review.schema.json
```

---

# 35. Evidence model

Every material claim requires:

```text
claim_id
subject_id
predicate
object
source_id
source_type
jurisdiction
observed_date
effective_date
confidence
claim_state
contributor
reviewer
created_at
updated_at
supersedes
```

Evidence states:

```text
SUBMITTED
SOURCE_VERIFIED
CORROBORATED
CANONICAL
DISPUTED
UNRESOLVED
REJECTED
CORRECTED
SUPERSEDED
```

Unknown remains unknown.

---

# 36. Public contribution model

Support:

**Inspect it.**

**Challenge it.**

**Add evidence.**

**Resolve an owner.**

**Trace a lender.**

**Follow a deed.**

**Map a threat.**

**Correct the record.**

**Download the data.**

**Build from it.**

**Nominate an asset.**

Submissions do not automatically become canonical.

---

# 37. Seed data

Use the existing SHADOW research tranches.

## Tranche 1

Resolved/substantially resolved buyer/capital provenance.

## Tranche 2

Unresolved buyers, title rights, lender, beneficial ownership.

## Tranche 3

Active federal dispositions before transfer.

All conversational research must be revalidated before becoming canonical repo data.

---

# 38. First reference asset

Use:

# PPT-EZ-CA-0001

Spring Street Courthouse, Los Angeles.

This should demonstrate:

```text
asset
→ authoritative title
→ TitleChain Asset State
→ rights
→ obligations
→ debt
→ jurisdiction
→ disposition
→ Orbitalys threats
→ SHADOW scores
→ People's Trust review
```

Do not imply completed acquisition.

---

# 39. Public property page

Every asset view should begin with:

# ASSET STATE

Then display:

```text
Asset Identity

Title State

Verified By / When

Provenance

Rights

Encumbrances

Claims

Obligations

Environmental State

Authority State

Transfer State

M5MST

TSI

Ownership

Debt

Orbitalys Threat Graph

SHADOW Scores

Disposition State

People's Trust Review

Evidence

Corrections / History
```

---

# 40. Engineer implementation order

## PR 1 — Structure + README

Create module structure.

Add root README section.

Create engineering epic.

---

## PR 2 — Asset State schemas

Implement:

```text
asset
title
provenance
rights
encumbrances
claims
obligations
environment
authority
transfer
```

---

## PR 3 — Evidence + event chain

Implement:

```text
evidence
confidence
claim state
correction
supersession
asset-state events
```

No destructive history edits.

---

## PR 4 — Graph engine

Implement:

```text
asset
→ owner
→ capital
→ debt
→ rights
→ obligations
→ jurisdiction
```

---

## PR 5 — M5MST integration

Link lifecycle state to current TitleChain Asset State.

Do not merge them.

---

## PR 6 — SHADOW indices

Implement:

```text
TSI
ASI
DPI
OOI
CCI
PVMI
PBOI
```

Every formula versioned.

---

## PR 7 — SHADOW CAMEL

Implement:

```text
C
A
M*
E
L
S*
composite
trend
confidence
```

Start with synthetic institutions.

---

## PR 8 — Orbitalys

Build adapter and graph mapping.

Threats never create authority.

---

## PR 9 — People's Trust

Implement nomination and feasibility states.

---

## PR 10 — M5 Global event feed

Generate public-safe event output.

Do not publish private title documents or M5POD evidence.

---

## PR 11 — Seed research

Convert Tranches 1–3.

Revalidate every source.

---

## PR 12 — Public interface

Build:

```text
asset page
state timeline
ownership graph
debt graph
rights graph
Orbitalys graph
score cards
evidence panel
download
contribute
nominate asset
```

---

# 41. Required tests

At minimum:

1. schemas validate;
2. IDs are unique;
3. evidence is required for canonical claims;
4. unknown stays unknown;
5. disputed evidence remains visible;
6. asset state is event-derived;
7. previous states are preserved;
8. deed verification does not imply no encumbrances;
9. verified title does not imply environmental clearance;
10. rights can be separated from surface ownership;
11. pipeline/mineral/water rights can have independent holders;
12. unresolved remediation remains unresolved;
13. title verification records verifier + timestamp;
14. M5MST remains separate from external legal state;
15. auction result does not equal deed transfer;
16. SPE ownership does not equal ultimate-capital resolution;
17. Orbitalys does not grant authority;
18. SHADOW CAMEL is never labeled official CAMELS;
19. M* and S* are explicitly inferred;
20. M5AGT cannot exceed principal authority;
21. revoked credentials invalidate authority;
22. private M5POD data cannot leak into public SHADOW;
23. People’s Trust nomination creates no legal/economic right;
24. M5 Global feed contains only approved public-safe events;
25. scoring is deterministic and versioned.

---

# 42. V0.1 definition of done

SHADOW M5Index v0.1 is complete when:

- root README contains canonical SHADOW section;
- common-language glossary exists;
- `shadow-m5index/README.md` exists;
- engineering epic exists;
- TitleChain Asset State schemas exist;
- event-chain state engine works;
- TSI exists;
- all SHADOW indices validate;
- synthetic SHADOW CAMEL validates;
- Orbitalys adapter exists;
- People’s Trust workflow exists;
- M5 Global public event format exists;
- at least 10 source-backed assets validate;
- at least 3 resolve through sponsor/capital;
- at least 1 remains explicitly unresolved;
- at least 1 asset demonstrates environmental/rights complexity;
- PPT-EZ-CA-0001 demonstrates end-to-end state;
- JSON / JSONL / CSV export works;
- all tests pass.

---

# 43. Canonical public statement

> **SHADOW M5Index makes visible what sits between the public record and the real economy: the state of the title, who owns the asset, who holds the debt, what rights and obligations travel with it, who finances the transfer, where risk sits in the chain, where value moves, and where communities may still have an opportunity to act.**

---

# 44. Canonical operating principles

## Evidence before inference.

Do not infer where a record can be verified.

## State before scoring.

Do not score an asset until its known state is represented.

## Provenance before automation.

Every consequential state needs evidence lineage.

## Authority before action.

No agent or score creates authority.

## Unknown means unknown.

Never fill evidentiary gaps with model confidence.

## Events, not overwrites.

Preserve the historical state chain.

## Rights are separable.

Surface ownership does not imply control of every right.

## Obligations travel too.

Do not track upside while ignoring remediation, decommissioning, liens, or successor liability.

## Public and private stay separated.

Private M5POD evidence remains outside the public Commons.

---

# 45. Final engineer directive

Build SHADOW M5Index as the **real-world asset intelligence and transition layer of the M5 Commons**.

The system must connect:

```text
identity
authority
title
state
rights
debt
ownership
obligations
risk
deal flow
public-benefit opportunity
economic transition
```

Do not begin by building a dashboard.

Begin with:

# state + evidence + provenance.

Then graph.

Then scoring.

Then threats.

Then deal flow.

Then People's Trust.

Then M5 Global signals.

Then the public interface.

The most important question in the system is not:

> **What is this asset worth?**

It is:

> **What exactly is this asset, what state is it in, who has rights or claims against it, who has authority over it, what obligations travel with it, and what evidence proves each answer?**

Everything else follows from that.