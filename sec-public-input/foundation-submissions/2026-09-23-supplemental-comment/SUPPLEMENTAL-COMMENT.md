# Supplemental Comment of TitleChain Foundation

> **© 2026 TitleChain Foundation.** Part of the Foundation's written submission
> to the SEC on File No. S7-2026-30 (emailed September 23, 2026; pending SEC
> posting). Licensed under CC-BY-4.0 with required attribution. TitleChain
> Foundation, M5 and related marks are not licensed, and no patent rights are
> granted. See [NOTICE](NOTICE.md). *This notice is added by the repository and
> is not part of the submitted text.*

**Re:** File No. S7-2026-30; Release No. 34-106246 - Transfer Agent Rules\
**Title:** Authority, Evidence, Record Continuity, and Regulator-Ready Routing in Tokenized Securities\
**Source cutoff:** 2026-09-24

## Executive summary

TitleChain Foundation submits this supplemental technical comment to build on its September 5, 2026 comment concerning credential-bound authority, machine-readable restrictions, bounded automation, preservation of underlying rights, and regulator-ready evidence.

The Commission's proposed amendments expressly ask how transfer-agent records should work across physical, digital, distributed-ledger, onchain, and offchain environments, including Questions 80-89. The Foundation's public reference implementation now demonstrates a broader answer: consequential electronic records should preserve not only technical execution, but the accountable authority, legal context, evidence, and authoritative resulting record that make the execution meaningful.

The Foundation recommends a technology-neutral separation:

**CONTROL != TITLE STATE != AUTHORITY != NOTICE/CLAIMS != EVIDENCE**

Technical control can prove that a key, wallet, account, service, or system executed an action. It does not by itself establish that the actor had legal or organizational authority to change the authoritative record.

The Foundation further recommends that modern recordkeeping support:

1. authority chains from accountable entity and human to bounded execution;
2. explicit authoritative-record hierarchy and reconciliation;
3. provenance and lifecycle state for attestations;
4. fail-closed handling of missing, expired, revoked, disputed, or out-of-scope authority;
5. successor-provider and cryptographic migration without loss of authoritative history;
6. regulator-ready evidence receipts for consequential machine actions; and
7. machine-readable classification and routing that identifies potentially applicable authorities and required evidence without allowing an internal label to manufacture a legal conclusion.

## 1. Direct response to Questions 80-89

### Q80 - all forms and types of records
Yes, electronic rules should be technology-neutral, but the record set should include the authority and evidence that caused a consequential state transition. A blockchain transaction alone is not a complete regulatory record when the legal effect depends on issuer authority, transfer restrictions, approvals, credentials, or external records.

### Q81 - flexibility across business models and systems
Use outcome-based requirements. A small transfer agent and a large technology platform may use different infrastructure while producing the same minimum reconstruction package: accountable actor, authority source, instruction, approvals, execution event, authoritative record update, exceptions, corrections, and evidence.

### Q82 - access and production of DLT records
DLT records should be producible in an examiner-readable export that preserves native identifiers while resolving them to the relevant human/entity, authority, transaction, authoritative record, and evidence. The export should remain usable if the original chain, provider, wallet, or cryptographic dependency is replaced.

### Q83 - onchain/offchain association
The Foundation supports explicit linkage without collapsing the two domains. Wallet address, token quantity, and issue date may be associated with offchain holder identity and authoritative records, but the linkage should also preserve who was authorized to establish or change the association, its jurisdiction and scope, and its revocation/supersession state.

### Q84 - records on networks not exclusively controlled by the transfer agent
The transfer agent's responsibility should be separated from exclusive technical ownership of every underlying network component. The recordkeeping transfer agent should retain exclusive responsibility for the authoritative master securityholder file even when linked systems are distributed. External network events should be treated as evidence or constituent records subject to reconciliation, not as self-executing legal authority.

### Q85 - timing granularity
Where operationally material, timestamps should support sufficient granularity to reconstruct ordering, latency, approval, rejection, correction, and posting. Systems should preserve clock/source provenance where ordering matters.

### Q86 - written appointment and authority records
Written appointment records are especially important in automated systems because they anchor the authority graph. Machine-readable representations may supplement but should not silently replace controlling legal instruments.

### Q87 - transfer journal
A transfer journal should be mandatory for consequential changes and should preserve rejected, held, corrected, reversed, and superseded events as well as successful transfers. A journal is valuable precisely because the current authoritative state alone cannot explain how that state was reached.

### Q88 - master securityholder file, control book, and transfer journal on DLT
The three records should remain logically distinguishable even if implemented across linked systems or a shared technical substrate. The authoritative current owner record, aggregate authorization/issuance control, and historical transaction journal perform different functions and should be reconcilable.

### Q89 - non-routine items
Non-routine records should include the evidence supporting classification, authority, exception handling, human review, and resulting disposition. In tokenized or agentic systems, unique categories include stale/revoked credentials, conflicting onchain/offchain state, compromised keys, disputed attestations, provider migration, chain migration, cryptographic deprecation, and attempts by automation to exceed delegated authority.

## 2. Authoritative records must survive their technology

The master securityholder file is the authoritative record of registered ownership under the Commission's proposal. The Foundation recommends a companion continuity principle:

> **The authoritative securityholder record must survive the technology used to represent it.**

A key compromise, algorithm deprecation, smart-contract defect, provider failure, chain migration, wallet replacement, or transfer-agent succession should not erase the history necessary to establish the prior authoritative state or silently change title, authority, restrictions, or claims.

## 3. Authority must be reconstructable

For consequential actions, the system should be able to reconstruct:

**accountable entity -> accountable human -> capacity -> credential/appointment -> jurisdiction -> authority source -> scope -> instruction -> required approvals -> deterministic policy -> bounded execution -> authoritative record update -> evidence receipt**

If a required link is missing, stale, revoked, disputed, mismatched, or out of scope, the appropriate machine state is **HOLD** or **REJECT**, not inference from technical control.

## 4. M5 classification as regulator-ready routing, not regulatory determination

The M5 reference architecture separates internal asset/economic classification from external legal classification. Its purpose is to make the asset/right, transaction/event, actor/capacity, jurisdiction, and evidence machine-readable so that potentially applicable regulatory pathways can be identified before execution.

The routing layer may identify, depending on the facts and activity, securities, commodities/derivatives, banking/payment, AML/BSA, tax, state/local property, recorder, licensing, public-asset disposition, or other authorities and regulated functions.

An M5 label does **not** determine that the SEC, CFTC, FinCEN, a banking regulator, a state, a county, or another authority has jurisdiction. External law and authoritative agency determinations remain controlling. Ambiguity produces **REGULATORY_HOLD / LEGAL_REVIEW_REQUIRED**.

## 5. Public reference implementation

The Foundation's public Commons includes three progressively broader simulations:

1. **312 Spring Commons / PPT-EZ-CA-0001** - government-to-public real estate, title, authority, blended capital, structured debt, transfer-agent boundaries, settlement, productive assets, and lifecycle evidence.
2. **People's Trust Farmland** - repeatable title, stewardship, operator, economic-right, regulated-recordkeeping, correction, and successor-portability controls.
3. **Global UN Commons** - international interoperability and jurisdiction-profile testing without representing any nation, UN body, or government as activated or participating.

The Commons also includes **SHADOW M5Index**, a public-research layer connecting real-world asset state, title provenance, ownership, capital, debt, rights, obligations, environmental conditions, disposition activity, threats, and public-benefit feasibility.

The published **SHADOW CAMEL Report - Q3 2026** is a first-edition public-research release using public sources. It is expressly not an official CAMELS rating, confidential supervisory rating, bank examination, regulator finding, investment recommendation, credit rating, or legal conclusion.

## 6. Activating the edge without manufacturing authority

The public-ingestion model is intended to let title companies, county recorders and clerks, notaries, assessors, regulated intermediaries, professionals, researchers, and citizens contribute source-linked public evidence for governed review.

A contribution does not become authoritative merely because it is uploaded. Evidence states preserve the distinction among discovery, submission, source verification, authority verification, canonical adoption where appropriate, dispute, correction, and supersession.

This architecture is intended to let existing authoritative actors continue performing the functions assigned to them by law while giving people and communities portable tools to discover, contribute, verify, challenge, and trace public evidence.

## 7. Industry input and the unresolved layer

Recent Crypto Task Force submissions illustrate related concerns. Plume describes tokenized vault infrastructure, transfer-agent modernization, programmable compliance, and DLT wallet-address treatment. Ceres Coin TA emphasizes an authoritative regulated register for holder-rights parity. NeuFin emphasizes material-change revalidation and records connecting prior state, authority boundaries, and outcomes. Gene Deyev emphasizes sourced, timestamped, evidence-typed issuance records and preservation of prior versions.

These are submitter positions, not Commission findings. They are useful because they independently surface the need to distinguish technical infrastructure from authoritative records, authority, provenance, revalidation, and continuity.

## 8. Requested Commission consideration

The Foundation respectfully recommends that the Commission consider technology-neutral expectations that:

- distinguish technical control from authority and authoritative record state;
- preserve an authority chain for consequential record changes;
- require provenance and lifecycle state for material attestations;
- preserve logical distinctions among master securityholder file, control book, and transfer journal;
- require reconciliation and exception handling across linked onchain/offchain systems;
- support successor-provider and cryptographic migration;
- preserve machine-readable receipts for consequential actions; and
- permit machine-readable regulatory routing while making clear that internal classifications do not create governmental jurisdiction or approval.

These recommendations do not ask the Commission to mandate TitleChain, M5, ICSN, any blockchain, wallet, namespace, identity provider, registry, or vendor.

## Exhibits

- Exhibit A - End-to-End 312 Spring Commons Reference Transaction
- Exhibit B - Repository and Contract Architecture Crosswalk
- Exhibit C - M5 Classification to Regulatory Authority Routing
- Exhibit D - Government Authority and Approval Matrix
- Exhibit E - Capital, Debt, Securities and Settlement Architecture
- Exhibit F - Public Evidence and Edge Participation Network
- Exhibit G - SHADOW M5Index and SHADOW CAMEL Public-Data Pipeline
- Exhibit H - Industry Architecture Crosswalk
- Exhibit I - Failure, Recovery and Successor-State Tests
- Exhibit J - Demonstrated / Built / Pipeline / External / Not Yet Demonstrated

## Status boundary

This supplement and its exhibits describe Foundation research, public standards work, reference implementations, and simulations. They do not establish government authorization, agency participation, completed title transfer, live settlement, regulated-provider appointment, legal compliance, investment suitability, or independent validation unless corresponding evidence is explicitly identified.

## Commenter

**Pamela Norton**\
Founder & Executive Director, TitleChain Foundation\
Sovereign Chief Architect, TitleChain Registry\
Email: p_norton@titlechain.world

Submitted on behalf of TitleChain Foundation as public-interest technical input. The Foundation does not request Commission endorsement of TitleChain, M5, ICSN, any blockchain, vendor, namespace, or implementation.
