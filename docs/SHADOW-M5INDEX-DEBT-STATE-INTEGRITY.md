# SHADOW M5Index — Debt State Integrity & Collection-Chain Provenance

**Status:** Proposed public-commons specification  
**Module:** SHADOW M5Index  
**Repository:** `TitleChain-Foundation/M5-AI-Sovereign-Commons`  
**Suggested path:** `docs/SHADOW-M5INDEX-DEBT-STATE-INTEGRITY.md`

---

## Purpose

Debt should not outlive its evidence.

SHADOW M5Index should not treat a debt as a single balance carried forward from one system to another. A debt has a history:

- an originating obligation;
- an original creditor;
- one or more servicers;
- payments;
- modifications;
- assignments;
- settlements;
- releases;
- cancellations;
- disputes;
- notices;
- collection activity;
- litigation or reporting events;
- and, sometimes, unresolved gaps in the chain.

The purpose of this specification is to make that history inspectable.

SHADOW should connect the parties and services that act on a debt claim so researchers, asset owners, consumers, communities, and authorized institutions can distinguish:

1. **the existence of an original obligation;**
2. **the present state of that obligation;**
3. **the current owner of the claim;**
4. **the authority of a servicer or collector to act;**
5. **the amount claimed and how it was calculated;**
6. **material events that may have changed the obligation;**
7. **the notices, disputes, and evidence associated with collection activity;**
8. **what remains unresolved.**

This is an evidence and provenance framework. It is not a determination that a debt is valid, invalid, enforceable, unenforceable, collectible, or uncollectible under any particular law.

---

# Canonical principle

## THE CLAIM TRAVELS WITH ITS PROOF

Ownership may change.

Servicers may change.

Collectors may change.

The evidence chain should not disappear.

SHADOW should preserve the history of the claim and make missing links visible.

---

# Why this matters

A current collection demand may be only the last visible event in a much longer chain.

A legacy obligation can move through:

```text
ORIGINAL OBLIGATION
        ↓
ORIGINAL CREDITOR
        ↓
SERVICER
        ↓
MODIFICATION / CHARGE-OFF / SETTLEMENT EVENT
        ↓
ASSIGNMENT
        ↓
DEBT BUYER
        ↓
SUBSEQUENT ASSIGNMENTS
        ↓
COLLECTION AGENCY
        ↓
COLLECTION LAW FIRM
        ↓
CREDIT REPORTING / COURT / OTHER ACTION
```

A public or private record may expose only fragments of this chain.

SHADOW should make the gaps explicit.

Example:

```text
2007 ORIGINATION
→ 2009 SERVICER CHANGE
→ 2011 ASSIGNMENT
→ 2013 SETTLEMENT EVENT
→ ??? CHAIN GAP ???
→ 2022 DEBT BUYER
→ 2026 COLLECTION DEMAND
```

A chain gap does not automatically invalidate a claim.

It means:

> **the provenance necessary to understand the current claim is incomplete in the available evidence.**

---

# 1. TitleChain Debt State

Add a machine-readable state envelope parallel to **TitleChain Asset State**.

## `debt_state`

```text
debt_state
├── obligation_identity
├── originating_instrument
├── original_creditor
├── current_claim_owner
├── current_servicer
├── authorized_collector
├── assignment_chain
├── principal_state
├── interest_state
├── fee_state
├── payment_state
├── modification_state
├── settlement_state
├── release_state
├── cancellation_state
├── discharge_state
├── limitation_state
├── dispute_state
├── notice_state
├── collection_authority_state
├── litigation_state
├── reporting_state
├── verification_state
└── evidence_state
```

The current debt state must be derived from events and evidence.

Do not overwrite history.

---

# 2. DSI — Debt State Integrity

Create a new SHADOW M5Index measure:

# **DSI — Debt State Integrity**

Question:

> **How complete, current, internally consistent, and evidentially supported is the known state of this debt?**

DSI should evaluate dimensions such as:

- original obligation identified;
- originating instrument located;
- current claim owner resolved;
- assignment chain completeness;
- current servicer resolved;
- principal reconciled;
- interest provenance resolved;
- fee provenance resolved;
- payment history reconciled;
- modifications captured;
- settlements captured;
- releases captured;
- cancellation/discharge events captured;
- limitation status reviewed where applicable;
- dispute history captured;
- notice history captured;
- litigation/reporting state captured;
- evidence freshness;
- unresolved contradictions.

Suggested scale:

```text
80–100  HIGH INTEGRITY
60–79   SUBSTANTIALLY RESOLVED
40–59   MATERIAL GAPS
20–39   LOW INTEGRITY
0–19    SEVERELY UNRESOLVED
```

A high DSI is not a legal ruling that the claim is enforceable.

A low DSI is not a legal ruling that the claim is invalid.

It measures the integrity of the known evidence chain.

---

# 3. CCI-DC — Collection Chain Integrity

Do not reuse the existing `CCI` acronym, which SHADOW uses for **Capital Concentration Index**.

Create:

# **CCI-DC — Collection Chain Integrity**

Question:

> **How well supported is the current collector's authority and collection chain?**

Suggested dimensions:

- collector identity verified;
- current claim owner verified;
- collector-to-owner relationship documented;
- applicable authority/license/registration evidence captured where relevant;
- assignment continuity;
- balance reconciliation;
- notice evidence;
- dispute history;
- litigation consistency;
- reporting consistency;
- stale-data indicators;
- duplicate-claim indicators.

Example status:

```text
CCI-DC: 42 / 100
STATUS: MATERIAL GAPS

Current owner: PARTIAL
Collector authority: UNRESOLVED
Assignment continuity: GAP
Balance reconciliation: PARTIAL
Notice evidence: SOURCE LOCATED
Dispute state: OPEN
```

---

# 4. Proof Before Collection

Add the following public operating principle:

# **PROOF BEFORE COLLECTION**

Before SHADOW represents a collection claim as **validated**, the evidence record should be capable of resolving, where relevant:

1. the original obligation;
2. the originating instrument;
3. the current claim owner;
4. the chain of assignments;
5. the present servicer;
6. the collector's authority to act;
7. the current principal;
8. interest and fee provenance;
9. material payment history;
10. modifications;
11. settlements;
12. releases;
13. cancellation or discharge events;
14. applicable time/limitation status where relevant;
15. required notices and available delivery evidence;
16. disputes and responses;
17. litigation or reporting activity;
18. jurisdiction.

If the required evidence is absent, use:

```text
COLLECTION_AUTHORITY_STATE:
UNRESOLVED
```

Do not silently promote a collection demand to a verified obligation.

---

# 5. Debt event model

Every material change should be represented as an event.

Example event types:

```text
DEBT_ORIGINATED
SERVICER_APPOINTED
SERVICER_CHANGED
PAYMENT_POSTED
PAYMENT_REVERSED
INTEREST_ACCRUED
FEE_ADDED
MODIFICATION_EXECUTED
FORBEARANCE_EXECUTED
SETTLEMENT_EXECUTED
SETTLEMENT_COMPLETED
RELEASE_EXECUTED
CLAIM_CANCELLED
CLAIM_DISCHARGED
CHARGE_OFF_RECORDED
ASSIGNMENT_RECORDED
CLAIM_OWNER_CHANGED
COLLECTOR_APPOINTED
NOTICE_ISSUED
NOTICE_DELIVERY_RECORDED
NOTICE_RETURNED
DISPUTE_RECEIVED
DISPUTE_RESPONSE_ISSUED
CREDIT_REPORTING_EVENT
LITIGATION_FILED
JUDGMENT_ENTERED
LIEN_RECORDED
LIEN_RELEASED
COLLECTION_CLOSED
```

Each event should support:

```text
event_id
debt_id
event_type
effective_at
recorded_at
actor
actor_role
authority_reference
jurisdiction
amount_before
amount_delta
amount_after
source_id
evidence_digest
confidence
claim_state
supersedes
```

---

# 6. Notice state and machine-native due process

A collection system should distinguish:

```text
NOTICE_CREATED
NOTICE_ISSUED
NOTICE_SENT
NOTICE_DELIVERED
NOTICE_RETURNED
NOTICE_ACKNOWLEDGED
NOTICE_DISPUTED
NOTICE_RESPONSE_ISSUED
```

Do not collapse all of these into:

```text
SENT = TRUE
```

For M5-enabled notice flows, support a verifiable event chain such as:

```text
AUTHORIZED ACTOR
→ issues notice
→ notice receives event ID
→ debt/asset reference attached
→ jurisdiction attached
→ actor credential attached
→ delivery channel recorded
→ delivery status recorded
→ recipient-side receipt recorded where available
→ acknowledgment/dispute linked
→ subsequent state updated
```

Example:

```text
NOTICE_ID:
M5-NOTICE-81F2

ISSUER:
ABC Servicing

AUTHORITY_STATE:
VERIFIED

DEBT_ID:
TC-DEBT-4928

JURISDICTION:
STATE / FEDERAL CONTEXT

ISSUED_AT:
2026-09-14T10:32:17

DELIVERY_STATE:
DELIVERED

RECIPIENT_EVENT:
DISPUTED

COLLECTION_STATE:
REVIEW_REQUIRED
```

A receipt event is evidence of a recorded delivery/interaction state within the system.

It does not replace any legal service, notice, or proof requirement imposed by governing law.

---

# 7. Orbitalys threat vectors

Orbitalys should map threat paths across the debt and collection graph.

Initial threat classes:

```text
assignment_chain_gap
collector_authority_unverified
claim_owner_unresolved
balance_reconciliation_failure
interest_provenance_gap
fee_provenance_gap
duplicate_collection_claim
released_debt_reasserted
settled_debt_reasserted
discharged_debt_reasserted
stale_servicing_data
notice_delivery_unverified
wrong_party_collection
successor_servicer_data_loss
dispute_not_propagated
credit_reporting_mismatch
litigation_state_mismatch
identity_mismatch
document_tampering
evidence_suppression
```

Example threat path:

```text
STALE SERVICING RECORD
        ↓
ASSIGNMENT GAP
        ↓
NEW DEBT BUYER
        ↓
UNRECONCILED BALANCE
        ↓
COLLECTION DEMAND
        ↓
CREDIT REPORTING / LITIGATION
```

Orbitalys identifies the threat path.

M5Canon evaluates authority and policy.

SHADOW records the evidence and public-safe intelligence.

---

# 8. M5Canon integration

M5Canon should be able to evaluate a debt-related action using current state.

Conceptually:

```text
debt_action_context
├── principal
├── debt_id
├── current_claim_owner
├── collector
├── collector_authority_state
├── assignment_chain_state
├── debt_state_integrity
├── notice_state
├── dispute_state
├── jurisdiction
├── credential_state
└── evidence_state
```

Example policy question:

> **Does this actor have current, evidenced authority to perform this requested action against this debt in this jurisdiction?**

M5Canon must not infer authority solely from:

- possession of an account number;
- possession of an old statement;
- a current collection demand;
- an unverified spreadsheet entry;
- a model prediction.

Missing authority must fail closed for consequential automated actions.

---

# 9. Public SHADOW versus private M5POD

Individual consumer financial records must not become a public debt dossier.

## Public SHADOW M5Index may publish or aggregate:

- debt buyers;
- servicing companies;
- collection companies;
- public corporate relationships;
- publicly recorded liens;
- public assignments;
- public court records where lawful and appropriate;
- public enforcement actions;
- documented entity-level patterns;
- commercial debt chains;
- public-asset debt chains;
- aggregate dispute and provenance-gap statistics.

## Private M5POD may hold:

- personal statements;
- account numbers;
- notices;
- payment records;
- settlement documents;
- dispute documents;
- private correspondence;
- receipts;
- private legal/financial records.

Public outputs should use minimization, aggregation, and privacy-preserving identifiers.

---

# 10. SHADOW public capability

Add to the SHADOW M5Index public description:

## FOLLOW THE DEBT

> SHADOW connects creditors, servicers, debt buyers, collectors, liens, assignments, settlements, releases, and collection actions into one provenance graph so a claim cannot silently shed its history as it moves between institutions.

Short form:

> **Debt should not outlive its evidence.**

---

# 11. Report capability callout

Suggested report section:

# WHEN DEBT LOSES ITS MEMORY

### Why provenance matters as much as balance

A debt is not simply a number.

It has an origin, an owner, a servicing history, a chain of assignments, payments, modifications, notices, disputes, settlements, releases, and legal conditions.

When those records live across disconnected institutions, the balance may survive while the history disappears.

**SHADOW M5Index is designed to preserve the history with the claim.**

Suggested visual:

```text
ORIGINAL CREDITOR
      ↓
   SERVICER
      ↓
  ASSIGNMENT
      ↓
  DEBT BUYER
      ↓
 COLLECTION
      ↓
 LAW FIRM
      ↓
 CREDIT / COURT

      ↑
??? CHAIN GAP ???
```

Callout:

> **SHADOW asks for the evidence chain.**

---

# 12. Required schema additions

Suggested new schemas:

```text
shadow-m5index/schemas/debt-state.schema.json
shadow-m5index/schemas/debt-event.schema.json
shadow-m5index/schemas/assignment.schema.json
shadow-m5index/schemas/collector-authority.schema.json
shadow-m5index/schemas/notice-event.schema.json
shadow-m5index/schemas/dispute-event.schema.json
shadow-m5index/schemas/debt-integrity-score.schema.json
shadow-m5index/schemas/collection-chain-integrity.schema.json
```

Suggested relationships:

```text
ORIGINATED_BY
OWNED_BY
ASSIGNED_TO
SERVICED_BY
COLLECTED_BY
AUTHORIZED_BY
SECURED_BY
DISPUTED_BY
SETTLED_BY
RELEASED_BY
REPORTED_BY
LITIGATED_BY
EVIDENCED_BY
SUPERSEDES
CORRECTS
```

---

# 13. Required SHADOW M5Index fields

Add to the debt table:

```text
Debt_ID
Asset_ID
Obligation_Type
Originating_Instrument_ID
Original_Creditor
Current_Claim_Owner
Current_Servicer
Current_Collector
Collector_Authority_State
Assignment_Chain_State
Principal_State
Interest_State
Fee_State
Payment_State
Modification_State
Settlement_State
Release_State
Cancellation_State
Discharge_State
Limitation_State
Notice_State
Dispute_State
Litigation_State
Reporting_State
DSI_Score
CCI_DC_Score
Evidence_State
Last_Verified
```

---

# 14. Evidence states

Reuse the SHADOW evidence model:

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

Important:

```text
COLLECTION DEMAND RECEIVED
```

is evidence that a demand was made.

It is not, by itself, evidence that every underlying element of the claim has been validated.

---

# 15. Tests

Add tests that establish:

1. a current collector does not automatically equal the current claim owner;
2. a claim owner does not automatically authorize every collector action;
3. an assignment gap remains unresolved;
4. a charge-off is not automatically treated as a release;
5. a cancellation event is not automatically treated as a legal discharge;
6. a settlement is not treated as completed until its completion evidence exists;
7. a release does not disappear after a later assignment import;
8. a dispute remains linked to successor servicers/collectors;
9. a notice marked sent is not automatically marked delivered;
10. delivery state and legal sufficiency remain distinct;
11. duplicate debt claims can be flagged;
12. amount changes require provenance;
13. fees and interest require event/source lineage;
14. public SHADOW output excludes private M5POD records;
15. DSI and CCI-DC cannot create legal authority;
16. M5Canon fails closed when required collection authority is unresolved;
17. corrections preserve the prior event history.

---

# 16. Contributor questions

Public contributors should be able to help answer:

- Who originated the obligation?
- Who currently owns the claim?
- What assignments connect the two?
- Who services the account?
- Who is attempting collection?
- What evidence establishes that authority?
- Has the balance been reconciled?
- What interest and fees were added?
- Was the obligation modified?
- Was it settled?
- Was a release recorded?
- Was a discharge or cancellation event recorded?
- What notices are evidenced?
- Was a dispute submitted?
- Did the dispute travel to successor parties?
- Is there litigation or credit reporting?
- Which links remain unresolved?

---

# 17. Canonical public language

Use:

> **SHADOW M5Index follows the debt as closely as it follows the asset. It connects the original obligation, creditor, servicers, assignments, claim owners, collectors, disputes, notices, settlements, releases, and public actions into an evidence-backed provenance chain.**

And:

> **The claim travels with its proof.**

And:

> **Debt should not outlive its evidence.**

---

# 18. Relationship to existing SHADOW indices

The SHADOW M5Index family becomes:

```text
TSI      Title State Integrity
DSI      Debt State Integrity
ASI      Asset Stress Index
DPI      Debt Pressure Index
OOI      Ownership Opacity Index
CCI      Capital Concentration Index
CCI-DC   Collection Chain Integrity
PVMI     Public Value Migration Index
PBOI     Public Benefit Opportunity Index
```

These measures answer different questions.

- **TSI:** What is the integrity of the title/right state?
- **DSI:** What is the integrity of the debt state?
- **DPI:** How much financing pressure exists?
- **CCI-DC:** How complete is the current collection-authority chain?

Do not collapse them into one score.

---

# 19. Engineering implementation order

## Phase 1 — State model
Implement debt, assignment, notice, dispute, settlement, release, and collector-authority schemas.

## Phase 2 — Event chain
Make debt state event-derived and append-only.

## Phase 3 — Evidence
Connect every material state to source evidence, confidence, and correction history.

## Phase 4 — DSI
Implement Debt State Integrity using versioned deterministic formulas.

## Phase 5 — CCI-DC
Implement Collection Chain Integrity.

## Phase 6 — Orbitalys
Map debt/collection threat vectors.

## Phase 7 — M5Canon
Add debt-action authority context and fail-closed conditions.

## Phase 8 — Public/private separation
Publish entity-level and public-record intelligence while keeping personal financial evidence in M5POD.

## Phase 9 — Public interface
Render:

```text
Debt timeline
Assignment chain
Current claim owner
Current servicer
Current collector
Collection authority state
Balance provenance
Notice state
Dispute state
Settlement/release state
DSI
CCI-DC
Orbitalys threats
Evidence panel
```

---

# 20. Definition of success

A SHADOW user examining a debt claim should be able to ask:

> What created this obligation?

> Who owns it now?

> How did ownership get from the original creditor to the current owner?

> Who is authorized to service or collect it?

> What amount is actually supported by the evidence?

> What payments, modifications, settlements, releases, cancellations, or disputes changed its state?

> What notices are evidenced?

> What links are missing?

> What is private, and what can be responsibly published?

If SHADOW cannot answer one of those questions, the correct state is:

# **UNRESOLVED**

—not an invented answer.

---

## Canonical principle

**Evidence before collection state.  
Provenance before automation.  
Authority before action.  
The claim travels with its proof.**
