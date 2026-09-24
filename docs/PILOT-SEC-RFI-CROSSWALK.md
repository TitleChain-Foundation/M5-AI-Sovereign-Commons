# Pilot and SEC Transfer-Agent Public-Input Crosswalk

**Status:** Informative Draft for Public Comment\
**Version:** 0.2\
**Reviewed:** September 24, 2026

## Boundary

This crosswalk identifies public-review questions that the Commons simulations
can help examine against the U.S. Securities and Exchange Commission's proposed
Transfer Agent Rules. It does not claim that the SEC has adopted, approved,
requested, certified, or endorsed an M5, TitleChain, People's Trust, Spring
Commons, Public Bank of California, or Global UN Commons design.

The authoritative proposal is:

- U.S. Securities and Exchange Commission, **Transfer Agent Rules**
- Release No. **34-106246**
- File No. **S7-2026-30**
- Federal Register publication date: **September 4, 2026**
- SEC issue date: **September 1, 2026**
- Current SEC comment deadline: **November 3, 2026**

The official SEC proposal and docket control over this summary.

The Foundation's September 5, 2026 public comment is a submitted public position,
not an SEC finding. Repository discussions, Issues, implementation notes and
Open Commons Reviews are Foundation public-review materials and are not
additional SEC submissions unless separately filed through the SEC's official
comment process.

## Commons implementation lanes

The public simulations now provide three differently bounded test environments:

| Development lane | Public simulation | SEC/public-input relevance |
| --- | --- | --- |
| **GSA / CRE** | **312 Spring Commons — California** | Tests separation among public-property title, public authority, project capitalization, bank/escrow records, investment instruments, transfer-agent records, restrictions, and TitleChain evidence. The Public Bank of California is a concept-only financing/public-capital layer within this simulation and is not represented as a chartered bank or regulated intermediary. |
| **FARMLAND / REDEVELOPMENT** | **America's People's Trust Farmland** | Tests title/economic-right separation, local operator authority, stewardship, repeatable project evidence, portability, correction, regulated recordkeeping boundaries, and anti-consolidation questions. |
| **GLOBAL DEVELOPMENT PROJECT** | **Global UN Commons — UN-NY-0001** | Tests jurisdiction-profile and evidence interoperability across borders. It is not a claim that SEC rules govern the UN campus or foreign jurisdictions. U.S. securities/transfer-agent requirements apply only where the actual U.S. legal or regulated function triggers them. |

These are simulations and review environments. They do not evidence a live
offering, completed acquisition, transfer-agent appointment, bank charter,
government authorization, or United Nations endorsement.

## Foundation comment themes carried into implementation

The Foundation's September 5 public comment recommends voluntary,
implementation-neutral open standards around the following themes. The Commons
uses them as public test questions rather than as statements of adopted law.

1. **Credential-bound authority** — identify the accountable institution,
   current authorized human, role, jurisdiction, scope, standing, expiry and
   revocation state before consequential execution.
2. **Known entity → current human authority → bounded automation** — software
   and AI inherit only specifically delegated capability and cannot create
   legal authority.
3. **Machine-readable restrictions** — preserve the legal source, affected
   right, jurisdiction, status, exception/removal authority and change history.
4. **Ricardian representation** — link controlling human-readable terms,
   machine-readable structure and separately bounded executable instructions.
5. **Pre-execution control gates** — identity, authority, jurisdiction,
   deterministic policy, required approval and attributable evidence.
6. **Origination is not later transfer authority** — creation or registration
   of an asset/instrument does not automatically confer transfer, correction,
   freeze, restriction-removal or cancellation powers.
7. **Preserve the underlying right across wrappers and rails** — do not treat
   property title, contract rights, security interests, securities-holder
   records, settlement records, custody records and digital representations as
   interchangeable.
8. **Regulator-ready portability and correction evidence** — preserve the
   authoritative record, event history, exceptions, corrections, successor
   continuity and reconciliation evidence.

## Theme crosswalk

| Proposal and public-review theme | Commons evidence/test surface | Question for reviewers |
| --- | --- | --- |
| Registration, contacts, entity structure, and control | Versioned entity, signer, role, standing, jurisdiction, delegation and revocation records | Which facts must be public, regulator-only or private? |
| Operational capacity and service providers | Dependency/provider inventory with accountable owners and migration controls | Which dependencies are material and how should failures be reported? |
| Electronic instructions and receipt | Distinct draft, submit, receive, accept, reject, execute, post, correct and supersede states | What event creates which legal or operational consequence? |
| Securityholder and wallet association | Verified private identity binding plus public-safe reference | How can association be proved without publishing unnecessary PII? |
| Authoritative master record | Explicit authoritative-record declaration and reconciliation | How should linked ledgers avoid becoming competing masters? |
| Distributed-ledger and electronic records | Signed authority, policy, execution, posting and correction receipts | What evidence is required beyond a chain event? |
| Timestamps, journals, controls and audit | Ordered lifecycle events, source clocks and privacy-filtered views | Which clocks and records control when systems disagree? |
| Retention and corrections | Differentiated retention, append-only correction, supersession and legal hold | What must be retained for the life of an issue? |
| Safeguards and incident response | Separation of duties, recovery, compromised-device, provider-loss and migration tests | Which independent assessments are necessary? |
| Transfer restrictions | Machine-readable restriction linked to authoritative legal source and exception/removal authority | How are ambiguity, change, waiver and removal handled? |
| Portability and successor transfer | Exportable state/evidence package with reconciliation history | What minimum package permits an accountable successor to resume service? |
| Small-entity burden / concentration | Reusable schemas, evidence inventories, proportional test fixtures and transition evidence | Which requirements reduce duplication without creating a false safe harbor or forcing avoidable consolidation? |
| Source of capital and economic rights | Spring Commons M5-JCP-001 capital-provenance path and separate instrument/right records | How can source/use/economic-right evidence be reconstructable without exposing protected data? |
| Bank, escrow and transfer-agent boundaries | Separate authoritative bank/escrow money record, project/title record and transfer-agent/securityholder record | Which institution controls each legally relevant record and how is reconciliation proven? |
| Cross-border interoperability | Jurisdiction profiles, authoritative endpoints, notices, revocation and adjudication routing | Which rules travel with the instrument and which remain jurisdiction-specific? |

## Public Bank of California concept — SEC boundary

The **Public Bank of California** is a research concept within the Spring Commons
simulation. It may be used to model how a public-capital or wholesale
participation layer could interact with community banks, credit unions,
regulated banks/escrow providers, public finance programs and project vehicles.

The concept must not be described as:

- a chartered bank;
- a California agency;
- an FDIC-insured depository institution;
- a registered transfer agent;
- a broker-dealer, exchange, ATS, custodian or clearing agency;
- an approved Spring Commons financing source; or
- an SEC-approved structure.

A future lawful bank or public-finance entity would remain responsible for its
own charter, banking, prudential, consumer, AML/KYC, payment, custody and other
applicable obligations. A transfer agent remains responsible for the
authoritative securities records and regulated functions within its scope.

The simulation should therefore test **interfaces and evidence boundaries**, not
collapse regulated functions into one platform.

## Core demonstration assertions

The Commons asks reviewers to test these propositions:

1. Classification occurs before regulated execution.
2. Wallet or key possession does not create authority.
3. Private credentials do not replace governmental registration or professional standing.
4. The accountable regulated intermediary remains responsible where its regulation applies.
5. One authoritative state can be maintained while linked systems provide evidence and automation.
6. Rejection, exception, correction, reversal and supersession are first-class states.
7. Restrictions preserve their authoritative source and change history.
8. Current state and material history are portable to an authorized successor.
9. Bank/escrow money movement, public-property title, investment rights and
   transfer-agent securityholder records remain distinct but reconcilable.
10. A public-capital concept does not become a bank or regulated securities
    intermediary merely because the Commons models its role.
11. Technical jurisdiction namespaces or aliases do not create governmental authority.
12. Cross-border interoperability does not erase local law or adjudication.

These are proposed control principles and test questions, not descriptions of
current law in every jurisdiction.

## Review questions by audience

### Regulators and transfer agents

1. Which record is authoritative for each legally relevant state?
2. What evidence should bind a wallet/account to a registered holder?
3. Which regulated statuses must be checked before capability is exposed?
4. What information should be public, regulator-only or private?
5. How should rejected, frozen, corrected, court-ordered, reversed and
   superseded events be represented?
6. What conformance tests aid examination without creating a safe harbor?
7. What minimum successor package preserves history and continuity?

### Banks, escrow providers and public-finance reviewers

1. Which money-movement record is authoritative?
2. How should project/escrow evidence reconcile without turning TitleChain into
   the bank ledger?
3. Which public-capital participation structures require separate legal,
   banking, tax, municipal-finance or securities analysis?
4. How should a community/public-finance layer interact with local banks and
   credit unions without implying that it replaces them?
5. Which source-of-funds and use-of-proceeds evidence should be reproducible,
   and which evidence must remain protected?

### States, counties, cities and title professionals

1. Which official record controls each title or severable-right event?
2. Can public-safe filing/fee receipts improve reconciliation without replacing
   the official record?
3. What proves authority to sign, convey, lease, encumber or approve?
4. How should title, lease, crop, water, mineral, easement and operator rights
   remain independently represented?
5. When a federal/public asset is disposed or conveyed, which state/local
   approvals and records become controlling?

### Operators and communities

1. Which decisions require qualified local operational authority?
2. Which operational details must remain confidential?
3. How should succession and continuity be tested?
4. Which stewardship measures are useful and which create unreasonable burden?
5. What public evidence helps communities understand an asset without creating
   an ownership, investment or voting right that does not legally exist?

### Standards and technology reviewers

1. What minimum schemas are needed for authoritative-record declarations,
   identity bindings, restrictions, decisions, corrections and provenance?
2. Which identifiers remain stable across provider, wallet, chain, bank or
   transfer-agent changes?
3. How can credential status be proved without exposing private evidence?
4. Which fixtures and tests are implementation-neutral?
5. How should jurisdiction namespaces bind to authoritative sources without
   pretending that a technical namespace is the jurisdiction itself?

## Submission and publication handling

Public repository comments must use synthetic or already-public evidence.
Private credentials, identity records, privileged analysis, confidential
transaction materials, protected bank/KYC records, security-sensitive topology
and unreported vulnerabilities must use an approved private channel.

GitHub comments and Commons review notes are not submitted to the SEC. A comment
intended for the Commission must use the SEC's official submission channel and
identify File No. S7-2026-30.
