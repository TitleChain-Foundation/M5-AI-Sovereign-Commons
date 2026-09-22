# Simulated Transaction Completion Matrix

> **SIMULATION CONTROL DOCUMENT.** A checked simulation box confirms only that the repository identifies or models the artifact. The authoritative column is the transaction truth. No external requirement below is marked satisfied.

## 1. Completion rule

A requirement is transaction-complete only when:

`artifact exists + correct party has authority + required reviews occurred + authorized signatures/decisions exist + conditions are met + authoritative system records the event`

Repository publication satisfies only the first element.

## 2. GSA/NPS conveyance and real-property title

| ID | Required artifact/action | Primary party/system of record | Simulation | Authoritative status |
| --- | --- | --- | --- | --- |
| FED-01 | Property status and controlling disposition-path confirmation | GSA | ☑ Modeled request | `PENDING_EXTERNAL` |
| FED-02 | Current notice, instructions, timeline, and federal contacts | GSA/NPS | ☑ Checklist | `PENDING_EXTERNAL` |
| FED-03 | Eligible public applicant selected | Public governing body | ☑ Placeholder | `PENDING_EXTERNAL` |
| FED-04 | Applicant eligibility/legal-capacity opinion | Applicant counsel | ☑ Requirement | `PENDING_EXTERNAL` |
| FED-05 | Governing resolution and signer authority | Applicant governing body/clerk | ☑ Requirement | `PENDING_EXTERNAL` |
| FED-06 | Expression of interest | Applicant/GSA record | ☑ EOI-01 simulation | `PENDING_EXTERNAL` |
| FED-07 | GSA invitation/referral to develop formal application | GSA | ☑ Process step | `PENDING_EXTERNAL` |
| FED-08 | Official application cover/certifications | Applicant/NPS | ☑ APP-01 simulation | `PENDING_EXTERNAL` |
| FED-09 | Program of Preservation and Utilization | Applicant/NPS | ☑ PPU-01 simulation | `PENDING_EXTERNAL` |
| FED-10 | Preservation plan and historic baseline | Applicant preservation team/NPS | ☑ Structure | `PENDING_EXTERNAL` |
| FED-11 | Use/public-benefit plan | Applicant/community/NPS | ☑ Structure | `PENDING_EXTERNAL` |
| FED-12 | Financial/perpetual-maintenance plan | Applicant financial officer/NPS | ☑ Structure | `PENDING_EXTERNAL` |
| FED-13 | Deferred-maintenance and repair plan | Licensed professionals/NPS | ☑ Structure | `PENDING_EXTERNAL` |
| FED-14 | Proposed rehabilitative changes | Design team/NPS | ☑ Structure | `PENDING_EXTERNAL` |
| FED-15 | Revenue/accounting/excess-income procedures | Applicant/NPS | ☑ Structure | `PENDING_EXTERNAL` |
| FED-16 | Operator/lease proposal and approval path | Applicant/NPS | ☑ DOC-03/04 crosswalk | `PENDING_EXTERNAL` |
| FED-17 | Environmental/Section 106/SHPO/tribal process as applicable | Federal lead/consulting parties | ☑ Requirement | `PENDING_EXTERNAL` |
| FED-18 | NPS application review and recommendation | NPS official record | ☑ Process step | `PENDING_EXTERNAL` |
| FED-19 | GSA acceptance/award decision | GSA official record | ☑ Process step | `PENDING_EXTERNAL` |
| FED-20 | Deed terms, restrictions, reversion, and closing statement | GSA/applicant counsel | ☑ Requirement | `PENDING_EXTERNAL` |
| FED-21 | Applicant acceptance and closing authorization | Public governing body | ☑ Requirement | `PENDING_EXTERNAL` |
| FED-22 | Executed federal deed | GSA and public grantee | ☑ Requirement | `PENDING_EXTERNAL` |
| FED-23 | Recorder acceptance and official real-property record | County recorder/authoritative land records | ☑ Requirement | `PENDING_EXTERNAL` |
| FED-24 | Post-transfer NPS monitoring/reporting record | Public grantee/NPS | ☑ Framework | `PENDING_EXTERNAL` |

## 3. Property, preservation, environmental, and construction diligence

| ID | Required artifact/action | Responsible party | Simulation | Authoritative status |
| --- | --- | --- | --- | --- |
| DUE-01 | Title report, legal description, survey, easements, retained interests | GSA/title professionals/counsel | ☑ Index requirement | `PENDING_EXTERNAL` |
| DUE-02 | Historic designation and character-defining-features record | Preservation professional/NPS | ☑ Index requirement | `PENDING_EXTERNAL` |
| DUE-03 | Building condition/historic structure report | Qualified team | ☑ Scope | `PENDING_EXTERNAL` |
| DUE-04 | Structural/seismic assessment | Licensed engineer | ☑ Scope | `PENDING_EXTERNAL` |
| DUE-05 | MEP/fire/life-safety/code assessment | Licensed professionals/AHJ | ☑ Scope | `PENDING_EXTERNAL` |
| DUE-06 | Accessibility assessment | Qualified professional/AHJ | ☑ Scope | `PENDING_EXTERNAL` |
| DUE-07 | Environmental/hazardous-material assessment | Qualified environmental team | ☑ Scope | `PENDING_EXTERNAL` |
| DUE-08 | Utility/interconnection and productive-engine feasibility | Utilities/licensed specialists | ☑ Scope | `PENDING_EXTERNAL` |
| DUE-09 | Space program/demand and operations validation | Applicant/operator/community | ☑ Scope | `PENDING_EXTERNAL` |
| DUE-10 | Drawings, specifications, preservation review, permits | Design team/NPS/AHJs | ☑ Requirement | `PENDING_EXTERNAL` |
| DUE-11 | Independent cost estimate, schedule, contingency | Independent estimator/team | ☑ Requirement | `PENDING_EXTERNAL` |
| DUE-12 | Insurance, bonding, procurement, contractor qualification | Applicant/insurers/procurement | ☑ Requirement | `PENDING_EXTERNAL` |
| DUE-13 | Commissioning, certificates, closeout, warranties | Professionals/AHJs/public owner | ☑ Requirement | `PENDING_EXTERNAL` |

## 4. Governance, community, operator, and public accountability

| ID | Required artifact/action | Responsible party | Simulation | Authoritative status |
| --- | --- | --- | --- | --- |
| GOV-01 | Accountable sponsor charter and project budget | Public sponsor | ☑ Milestone | `PENDING_EXTERNAL` |
| GOV-02 | Authority and participant registry populated with active evidence | Each appointing authority | ☑ Template | `PENDING_EXTERNAL` |
| GOV-03 | Stakeholder/affected-community map | Public sponsor/community process | ☑ Requirement | `PENDING_EXTERNAL` |
| GOV-04 | Accessible engagement plan and public record | Public sponsor/community body | ☑ Requirement | `PENDING_EXTERNAL` |
| GOV-05 | Community priorities, benefits, and response-to-comments | Public sponsor/community body | ☑ DOC-19/22 concepts | `PENDING_EXTERNAL` |
| GOV-06 | Governance charter/reserved-power matrix | Public owner/community body | ☑ Draft concepts | `PENDING_EXTERNAL` |
| GOV-07 | Operator procurement, diligence, selection, and approval | Public owner | ☑ Requirement | `PENDING_EXTERNAL` |
| GOV-08 | Executed operator lease/agreement | Public owner/operator/NPS as required | ☑ DOC-04 draft | `PENDING_EXTERNAL` |
| GOV-09 | Conflicts, procurement, records, audit, grievance, appeal policies | Public owner/operator | ☑ Framework | `PENDING_EXTERNAL` |
| GOV-10 | Worker/employment/procurement protections | Employer/public owner | ☑ DOC-14 draft | `PENDING_EXTERNAL` |
| GOV-11 | Privacy, security, accessibility, continuity controls | Public owner/operator | ☑ Framework | `PENDING_EXTERNAL` |

## 5. Financing, escrow, and any securities process

| ID | Required artifact/action | Authoritative party/system | Simulation | Authoritative status |
| --- | --- | --- | --- | --- |
| FIN-01 | Approved scope-linked sources and uses | Applicant/project entity | ☑ Illustrative model | `PENDING_EXTERNAL` |
| FIN-02 | Operating pro forma and downside cases | Applicant/advisers | ☑ Requirement | `PENDING_EXTERNAL` |
| FIN-03 | Preservation/maintenance reserve policy | Public owner/NPS | ☑ Requirement | `PENDING_EXTERNAL` |
| FIN-04 | $25M provider identified and diligenced | Project entity/advisers | ☑ Synthetic provider | `PENDING_EXTERNAL` |
| FIN-05 | Instrument and definitive economics selected | Authorized issuer/borrower/counsel | ☑ Draft alternatives | `PENDING_EXTERNAL` |
| FIN-06 | Legal, tax, public-finance, securities, procurement analysis | Qualified counsel/advisers | ☑ Requirement | `PENDING_EXTERNAL` |
| FIN-07 | Binding commitment executed by authorized parties | Provider/project entity | ☑ DOC-02 draft only | `PENDING_EXTERNAL` |
| FIN-08 | Proof of funds/capacity and source provenance verified | Qualified verifier/provider | ☑ Evidence rule | `PENDING_EXTERNAL` |
| FIN-09 | Bank/escrow selected and agreements executed | Regulated provider | ☑ DOC-06 draft | `PENDING_EXTERNAL` |
| FIN-10 | Funds deposited/reserved | Bank/escrow ledger | ☑ State modeled | `PENDING_EXTERNAL` |
| FIN-11 | Closing conditions certified | Counsel/fiduciaries/professionals | ☑ Gate modeled | `PENDING_EXTERNAL` |
| FIN-12 | Authorized draw and settlement | Bank/escrow ledger | ☑ Fail-closed simulation | `PENDING_EXTERNAL` |
| FIN-13 | Offering/subscription documents if securities route used | Issuer/counsel/investors | ☑ DOC-11/12 drafts | `NOT_APPLICABLE_UNTIL_PATH_CONFIRMED` |
| FIN-14 | Transfer agent/custody/registry arrangements if legally required | Qualified provider/official books | ☑ Requirement distinguished | `NOT_APPLICABLE_UNTIL_PATH_CONFIRMED` |
| FIN-15 | HTC/NMTC/grant/PRI closing records if used | Applicable parties/systems | ☑ DOC-08/09/13 drafts | `NOT_APPLICABLE_UNTIL_PATH_CONFIRMED` |

**Current capital evidence state:** `ILLUSTRATIVE`, not `CONDITIONALLY_COMMITTED`, `FUNDS_VERIFIED`, or `ESCROW_RESERVED`.

## 6. Existing DOC-01 through DOC-23 crosswalk

All documents below exist as public draft references. None is represented as negotiated, approved, executed, effective, or accepted by a counterparty.

| ID | Existing draft | Process contribution | Authoritative status |
| --- | --- | --- | --- |
| DOC-01 | Master Deal Term Sheet | Transaction framework/conditions | `PENDING_EXTERNAL` |
| DOC-02 | Conditional Capital Commitment Letter | Future capital evidence | `PENDING_EXTERNAL` |
| DOC-03 | Public Grantee MOU | Public-grantee relationship | `PENDING_EXTERNAL` |
| DOC-04 | Master Lease Term Sheet | Operator/lease structure | `PENDING_EXTERNAL` |
| DOC-05 | Investor Executive Brief | Orientation only | `DRAFT_REFERENCE_ONLY` |
| DOC-06 | Capital Escrow and Draw Agreement | Escrow/draw controls | `PENDING_EXTERNAL` |
| DOC-07 | Rehabilitation and Development Agreement | Delivery and work controls | `PENDING_EXTERNAL` |
| DOC-08 | Historic Tax Credit Investor Term Sheet | Conditional HTC lane | `NOT_APPLICABLE_UNTIL_PATH_CONFIRMED` |
| DOC-09 | NMTC CDE Transaction Term Sheet | Conditional NMTC lane | `NOT_APPLICABLE_UNTIL_PATH_CONFIRMED` |
| DOC-10 | TitleChain Evidence and Digital Records Schedule | Parallel evidence controls | `DRAFT_REFERENCE_ONLY` |
| DOC-11 | Private Offering PPM Framework | Potential securities route | `NOT_APPLICABLE_UNTIL_PATH_CONFIRMED` |
| DOC-12 | Subscription Agreement/Questionnaire | Potential investor onboarding | `NOT_APPLICABLE_UNTIL_PATH_CONFIRMED` |
| DOC-13 | Philanthropic Grant and PRI Agreement | Conditional funding lane | `NOT_APPLICABLE_UNTIL_PATH_CONFIRMED` |
| DOC-14 | Worker and Cooperative Participation Agreement | Worker/right separation | `PENDING_EXTERNAL` |
| DOC-15 | Master Risk Factors and Disclosure Schedule | Risk controls | `DRAFT_REFERENCE_ONLY` |
| DOC-16 | M5Canon Master Ricardian and Machine Policy Standard | Deterministic policy | `DRAFT_REFERENCE_ONLY` |
| DOC-17 | Authority Jurisdiction and Source of Truth Matrix | Authority mapping | `PENDING_EXTERNAL` active evidence |
| DOC-18 | CER UCC Article 12/9 Rights Schedule | Digital/legal-right separation | `NOT_APPLICABLE_UNTIL_PATH_CONFIRMED` |
| DOC-19 | Federated Registry and Governance Agreement | Governance architecture | `PENDING_EXTERNAL` |
| DOC-20 | Credential Privacy and ZK Requirements | Privacy/credential controls | `DRAFT_REFERENCE_ONLY` |
| DOC-21 | Benchmark and Performance Methodology | Targets/measurement | `PENDING_EXTERNAL` baselines/adoption |
| DOC-22 | State-to-Entity Due Process Standard | Notice/appeal controls | `DRAFT_REFERENCE_ONLY` |
| DOC-23 | Source-of-Funds/Provenance/Public Graph Standard | Capital provenance | `DRAFT_REFERENCE_ONLY` |

## 7. Party completion ledger

| Party/class | Required role | Selection | Authority | Required evidence/decision |
| --- | --- | --- | --- | --- |
| GSA | Federal disposal authority/conveying agency | Statutory role; property contact TBD | `PENDING_EXTERNAL` | Status, path, instructions, award, deed |
| NPS/Interior | Historic-surplus review, recommendation, oversight | Statutory/program role; contact TBD | `PENDING_EXTERNAL` | Suitability, application review, approvals, monitoring |
| Eligible public grantee | Applicant and restricted fee-title holder | `TBD` | `PENDING_EXTERNAL` | Eligibility, resolution, signer, acceptance, performance |
| Community governance body | Defined public-benefit participation/oversight | `TBD` | `PENDING_EXTERNAL` | Representative formation, charter, reserved powers |
| Public Trust of America | Potential supporting/operator role only | Proposed, not selected | `PENDING_EXTERNAL` | Legal role, procurement/approval, contract; not title eligibility substitute |
| Operator/developer | Rehabilitation and operations | `TBD` | `PENDING_EXTERNAL` | Selection, capacity, contract, lease, insurance |
| Preservation/design team | Professional plans/certifications | `TBD` | `PENDING_EXTERNAL` | Licensure, scope, reports, approvals |
| Engineers/environmental/code professionals | Diligence/design/certification | `TBD` | `PENDING_EXTERNAL` | Licensure, reports, permits/certifications |
| Public real-estate/preservation counsel | Eligibility, authority, deed/application advice | `TBD` | `PENDING_EXTERNAL` | Engagement and written advice |
| Finance/securities/tax counsel and advisers | Capital-route analysis | `TBD` | `PENDING_EXTERNAL` | Engagement, classification, opinions/advice |
| Capital provider(s) | Project funding | Synthetic/TBD | `PENDING_EXTERNAL` | Diligence, authority, definitive commitment, funds |
| Bank/escrow | Custody and settlement | `TBD` | `PENDING_EXTERNAL` | Regulated status, account, agreement, ledger |
| Transfer agent/custodian, if required | Official securities ownership/transfer records | `TBD` | `NOT_APPLICABLE_UNTIL_PATH_CONFIRMED` | Legal requirement, appointment, official books |
| County recorder/title professionals | Real-property recording/title evidence | Official/professional roles TBD | `PENDING_EXTERNAL` | Accepted deed and authoritative land record |
| Tax-credit/CDE/grant parties, if used | Conditional capital lanes | `TBD` | `NOT_APPLICABLE_UNTIL_PATH_CONFIRMED` | Approvals and definitive closings |
| Insurers/sureties/contractors | Delivery risk and work | `TBD` | `PENDING_EXTERNAL` | Procurement, policies/bonds, contracts |
| TitleChain/M5 | Parallel evidence, policy, and receipt layer | Repository demonstrator | `NONE` for legal authority | Never substitutes for deed, agency, bank, court, or regulated records |

## 8. Separation of title and transfer-agent records

1. **Federal real-property transfer:** GSA conveyance, public-grantee acceptance, deed, restrictions, and county recording establish real-property title.
2. **Project agreements:** leases, development agreements, financing documents, and approved governance records establish contractual rights and duties.
3. **Securities ownership/transfer:** if a final capital instrument is a security and requires transfer-agent services, the appointed qualified provider's official books govern those records.
4. **TitleChain/M5 evidence:** records provenance, status, restrictions, approvals, and reconciliation only; it does not transfer fee title or independently settle a security.

## 9. Overall status

- Simulation document coverage: `SIMULATED_PASS`.
- External authority satisfaction: `PENDING_EXTERNAL`.
- Financial movement: `false`.
- Network write: `false`.
- Authority effect: `NONE`.
- Execution authorized: `false`.
- Transaction decision: `HOLD`.
