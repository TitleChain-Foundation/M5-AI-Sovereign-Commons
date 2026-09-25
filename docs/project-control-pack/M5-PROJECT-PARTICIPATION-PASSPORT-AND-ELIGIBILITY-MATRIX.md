# M5 Project Participation Passport & Eligibility Matrix

**Status:** Informative architecture / public-review standard\
**Version:** 0.1\
**Date:** September 24, 2026

## Core idea

M5-CV should answer:

> **What has this person or entity proved about identity, capability, standing,
> experience, qualification and authority?**

A **Project Participation Passport** should answer a different question:

> **For this project, in this jurisdiction, for this instrument or role, what is
> this person or entity currently permitted to do?**

M5-CV is therefore reusable evidence.

The Project Participation Passport is project-specific permission.

Neither one creates a legal right merely by existing.

## Participation resolver

```text
M5HUM / verified human
        ↓
IAM / TCID
        ↓
M5-CV capability + credential evidence
        ↓
PROJECT REQUIREMENTS
        +
JURISDICTION
        +
INSTRUMENT CLASSIFICATION
        +
CURRENT STANDING / REVOCATION
        ↓
DISCLOSURES + CONSENTS + PROJECT ADMISSION
        ↓
PROJECT PARTICIPATION PASSPORT
        ↓
PURPOSE-BOUND CAPABILITY
        ↓
ACTION
        ↓
AUTHORITATIVE RESULT + RECEIPT
```

Every consequential action rechecks current authority/standing.

## Do not use one word — “owner” — for everyone

The project must distinguish:

| Status | What it means | What it does NOT automatically mean |
| --- | --- | --- |
| **Public participant / supporter** | Can learn, review, contribute feedback or support permitted public work | No title, vote or investment right |
| **Member / steward** | Admitted under adopted trust/cooperative/governance documents | No automatic land title or project economic right |
| **Project member** | Admitted to a specific project under its governing rules | No automatic right in other projects |
| **Title owner / grantee** | Holds the legally recognized property/title right | No automatic operating or investor role |
| **Operator** | Has contractual operating authority | No automatic title, governance or investor right |
| **Economic-right holder / investor** | Holds rights under a specific lawful instrument | No automatic title or trust governance right |
| **Lender / creditor** | Holds debt/credit rights | No automatic ownership/governance right |
| **Donor / grantor** | Supplies philanthropic/restricted support | No automatic investment or title right |
| **Worker / contractor / vendor** | Provides labor or services | No automatic member/investor/title right |
| **Trustee / fiduciary** | Holds specifically appointed fiduciary powers | No powers outside governing instrument/law |
| **Professional / regulated provider** | Performs licensed/registered role within scope | No general project control |
| **Authorized signatory** | May bind the specific entity/matter within documented scope | No authority outside delegation |

One person may hold multiple statuses, but each status requires its own evidence,
instrument, admission and authority.

## Project participation classes

The Passport can expose simple capability classes.

### P0 — Public Review

Possible capabilities:

- `VIEW_PUBLIC`
- `COMMENT_PUBLIC`
- `REVIEW_STANDARD`
- `SUBMIT_PUBLIC_EVIDENCE`

No private project information, ownership, vote or financial participation.

### P1 — Contributor / Builder

Additional evidence may include skill, training, portfolio, insurance,
background/engagement requirements, project NDA/privacy controls or professional
standing where applicable.

Possible capabilities:

- `CONTRIBUTE_RESEARCH`
- `BUILD`
- `DESIGN`
- `ANALYZE`
- `PROVIDE_SERVICE`

### P2 — Worker / Vendor / Operator

Requires project-specific engagement and current authority.

Possible capabilities:

- `WORK`
- `VENDOR`
- `OPERATE`
- `REQUEST_DRAW`
- `RECEIVE_PROJECT_PAYMENT`

A skill credential alone does not create a contract.

### P3 — Member / Steward / Governance Participant

Requires adopted governing structure, eligibility, affirmative consent and
recorded admission.

Possible capabilities:

- `MEMBER`
- `STEWARD`
- `PROPOSE`
- `VOTE` only where the governing instrument grants it
- `GOVERNANCE_REVIEW`

A member credential does not create title or investment rights.

### P4 — Donor / Grant / Mission Supporter

Project policy determines what support may be accepted.

Possible capabilities:

- `DONATE`
- `GRANT`
- `SPONSOR`
- `PRI_INTEREST` only after separate instrument classification

### P5 — Lender / Capital Provider

Requires the actual financing instrument, authority, source-of-funds and
jurisdictional checks.

Possible capabilities:

- `LEND`
- `COMMIT_CAPITAL`
- `FUND_ESCROW`

No investment capability should be inferred from wealth or identity alone.

### P6 — Investor / Economic-Right Participant

This class is always **instrument-specific**.

The Passport should never issue a generic `CAN_INVEST_IN_ANY_PROJECT`
credential.

Examples of narrow eligibility claims include:

- `US_REG_D_ACCREDITED_STATUS_VERIFIED`
- `US_OFFERING_ELIGIBILITY_VERIFIED:<offering_id>`
- `STATE_OFFERING_ELIGIBILITY_VERIFIED:<state>:<offering_id>`
- `INSTITUTIONAL_ELIGIBILITY_VERIFIED:<instrument_id>`
- `PROJECT_INVESTOR_ADMITTED:<project_id>:<instrument_id>`

An accredited-investor status may be relevant to some exempt securities
offerings, but it is not universal eligibility for every investment.

The credential should preserve:

- verifier;
- authoritative/supporting evidence source;
- verification method;
- scope;
- jurisdiction;
- instrument/offering ID;
- effective date;
- expiration/reverification date;
- revocation/supersession state; and
- minimum-necessary disclosure.

Do not place raw wealth, income, bank or identity evidence in the public record.

### P7 — Commodity / Hedging Participant

Only when the project actually uses futures, options, swaps, commodity pools or
other commodity-interest structures.

Possible narrow claims:

- `COMMERCIAL_HEDGE_ROLE`
- `ECP_STATUS_VERIFIED_IF_REQUIRED`
- `CPO_STATUS_CURRENT_IF_REQUIRED`
- `CTA_STATUS_CURRENT_IF_REQUIRED`
- `FCM_STATUS_CURRENT_IF_REQUIRED`

These claims are transaction-specific and do not create land/title rights.

### P8 — Fiduciary / Regulated Professional

Examples:

- `TRUSTEE_APPOINTMENT_CURRENT`
- `FIDUCIARY_SCOPE_CURRENT`
- `TRANSFER_AGENT_STATUS_CURRENT`
- `BROKER_DEALER_STATUS_CURRENT`
- `ESCROW_AUTHORITY_CURRENT`
- `ATTORNEY_LICENSE_CURRENT`
- `CPA_LICENSE_CURRENT`
- `REAL_ESTATE_LICENSE_CURRENT`
- `NOTARY_STATUS_CURRENT`
- `PROFESSIONAL_LICENSE_CURRENT`

A status credential proves only the defined current claim.

### P9 — Signatory / Approver

Purpose-bound authority examples:

- `AUTHORITY_TO_SIGN:<entity>:<matter>`
- `ESCROW_RELEASE_APPROVER:<account>`
- `DRAW_APPROVER:<budget>:<limit>`
- `TRANSFER_APPROVER:<instrument>`
- `GOVERNING_BODY_APPROVAL:<resolution>`

These should be short-lived or tightly scoped where possible.


## Work, Opportunity & Support Matching

M5-CV should not stop at identity or capability verification. It should help a
person discover **where their verified skills, experience, credentials,
availability and interests can actually be used**.

A participant should be able to ask:

> **What work can I do, what can I apply for, where can I contribute, and how
> can I support a Commons project today?**

The matching layer can compare the person's current M5-CV evidence against the
machine-readable requirements published by each project.

### You can work

A project may publish opportunities such as:

- paid employment;
- contract work;
- professional services;
- apprenticeships;
- project-based assignments;
- farm or property operations;
- research;
- engineering;
- accounting;
- title and records work;
- design;
- software development;
- legal/compliance support where properly qualified;
- construction/trades;
- procurement;
- community engagement;
- education/training;
- stewardship; and
- other project-specific work.

The opportunity should state:

- project ID;
- role ID;
- work type;
- required skills;
- required credentials/licenses;
- jurisdiction;
- location/remote status;
- compensation basis where public;
- engagement type;
- application requirements;
- decision authority;
- opening/closing dates if applicable; and
- status.

M5-CV can pre-fill or reuse already verified evidence so the person does not
have to repeatedly prove the same capability.

### You can apply or be considered

The platform should support distinct states:

```text
OPPORTUNITY_DISCOVERED
        ↓
MATCHED_TO_M5CV
        ↓
INTEREST_EXPRESSED
        ↓
APPLICATION_SUBMITTED
        ↓
UNDER_CONSIDERATION
        ↓
ADDITIONAL_EVIDENCE_REQUIRED
        ↓
SHORTLISTED
        ↓
SELECTED / NOT_SELECTED
        ↓
ENGAGEMENT_EXECUTED
        ↓
WORK_CAPABILITY_ACTIVATED
```

A match is not a job offer.

A credential is not a hiring decision.

A project remains responsible for its own lawful selection, employment,
contracting, procurement, professional-licensing and conflict processes.

### You can contribute time

Projects may publish non-investment contribution opportunities such as:

- volunteer research;
- public review;
- mentoring;
- community service;
- standards review;
- translation;
- testing;
- documentation;
- education;
- local stewardship;
- events; and
- other approved volunteer/community work.

Use a clear contribution record such as:

`TIME_CONTRIBUTION:<project_id>:<role_id>`

where useful for recognition or project accounting.

A time contribution does not automatically create employment, membership,
ownership, voting or investment rights.

### You can contribute talent

A participant may make verified skills or professional capability available to a
project.

Examples:

- accountant;
- architect;
- farmer/grower;
- engineer;
- software developer;
- title professional;
- surveyor;
- attorney;
- CPA;
- notary;
- contractor;
- project manager;
- educator;
- researcher;
- designer; or
- community organizer.

M5-CV can make the capability discoverable while the Project Participation
Passport controls whether the person is actually admitted to perform that role.

### You can support

Projects may accept different forms of **support**, subject to the project's
governing documents, payment policy, jurisdiction, tax treatment, financial
controls and applicable law.

Support can include:

**Time · Talent · Tokens · Approved cryptographic / sovereign digital currency**

Possible support paths include:

- **donation**;
- **grant**;
- **sponsorship**;
- approved in-kind contribution;
- restricted project support;
- philanthropic support;
- mission support;
- approved project token contribution where lawfully structured; and
- approved cryptographic or sovereign digital currency where the project
  lawfully accepts that payment form.

Support must remain separate from an investment unless a separate instrument
expressly creates an investment or economic right.

A donation, grant, sponsorship, token contribution or digital-currency payment
does **not** automatically create:

- land title;
- project ownership;
- an investment return;
- a security;
- voting rights;
- membership;
- profit-sharing;
- transfer rights; or
- governance authority.

If support is intended to create an economic or investment right, route it
through the Financial Instrument + Regulatory Routing Matrix first.

### Support capability examples

Possible narrowly scoped claims/capabilities include:

- `CAN_VOLUNTEER:<project_id>:<role_id>`
- `CAN_APPLY_FOR_WORK:<project_id>:<role_id>`
- `WORK_APPLICATION_SUBMITTED:<project_id>:<role_id>`
- `UNDER_CONSIDERATION:<project_id>:<role_id>`
- `VENDOR_ELIGIBLE:<project_id>:<service_class>`
- `PROFESSIONAL_ROLE_VERIFIED:<credential_type>`
- `CAN_DONATE:<project_id>`
- `CAN_SPONSOR:<project_id>:<sponsorship_class>`
- `GRANT_PROVIDER_VERIFIED:<entity_id>`
- `APPROVED_SUPPORT_RAIL:<project_id>:<currency_or_rail>`
- `PROJECT_SUPPORT_RECEIVED:<project_id>:<support_type>`

These claims should be purpose-bound and should not imply a broader legal right.

### Opportunity matching result

A useful participant-facing result might read:

```text
YOU CAN WORK
✓ Apply for Farm Operations Analyst — M5-CV match 8/10
✓ Apply for Public Records Researcher — requirements satisfied
○ Licensed Surveyor — additional state license verification required

YOU CAN CONTRIBUTE
✓ Public standards review
✓ Volunteer title-source research
✓ Mentor a project cohort

YOU CAN SUPPORT
✓ Donation
✓ Sponsorship
✓ Grant support
✓ Approved in-kind contribution
○ Approved cryptographic / sovereign digital currency
  — available only where the project has activated that payment rail

YOU MAY QUALIFY FOR
○ Lender participation — additional project underwriting required
○ Investment Instrument ND-FARM-M4-001 — offering-specific eligibility required
```

The UI must always distinguish **support** from **investment** and **matching**
from **authorization**.

## Project Opportunity Matching

A participant should be able to ask:

> **What can I do in the Commons today?**

The system can match the person's current credentials against public project
requirements and return opportunities such as:

- open public review;
- research or build task;
- qualified professional need;
- vendor opportunity;
- operator opportunity;
- volunteer/community role;
- member/steward admission window;
- donation/grant opportunity;
- debt/capital opportunity;
- investment opportunity for which the person appears eligible;
- commodity/hedging role;
- trustee/fiduciary/regulated-service role.

The response must distinguish:

`DISCOVERABLE`
from
`POTENTIALLY_ELIGIBLE`
from
`VERIFIED_ELIGIBLE`
from
`ADMITTED`
from
`AUTHORIZED_TO_ACT`.

Discovery is not authorization.

## Eligibility state machine

```text
DISCOVERABLE
        ↓
REQUIREMENTS_VIEWED
        ↓
EVIDENCE_SUBMITTED / REUSED
        ↓
EVIDENCE_VERIFIED
        ↓
PROJECT_ELIGIBILITY_CONFIRMED
        ↓
DISCLOSURES / CONSENTS
        ↓
PROJECT_ADMISSION
        ↓
CAPABILITY_ISSUED
        ↓
ACTION-TIME RECHECK
        ↓
AUTHORIZED ACTION
        ↓
RECEIPT / AUTHORITATIVE RESULT
```

Possible failure states:

- `NOT_ELIGIBLE`
- `EVIDENCE_STALE`
- `CREDENTIAL_REVOKED`
- `PROJECT_CLOSED`
- `JURISDICTION_NOT_SUPPORTED`
- `INSTRUMENT_NOT_AVAILABLE`
- `CONFLICT_REVIEW_REQUIRED`
- `ADDITIONAL_DISCLOSURE_REQUIRED`
- `REGULATED_PROVIDER_REQUIRED`

## Cross-project portability

The reusable part should be the evidence, not the right.

For example:

- identity can be reused;
- professional license status can be reused until it expires;
- entity-good-standing evidence can be reused subject to freshness rules;
- accredited-investor evidence can be reused only within its lawful verification
  scope and freshness policy;
- project membership cannot simply be copied into another project;
- voting rights cannot be copied;
- investment admission cannot be copied;
- trustee/signatory authority cannot be copied.

This preserves portability without creating “one credential rules everything.”

## Public view

For privacy, a public project may show:

`P6 — VERIFIED FOR INSTRUMENT X`

without showing the person's income, net worth, bank statement, tax return,
beneficial-owner file or other protected evidence.

The verifier, claim type, status, scope, date and revocation reference can be
available at the appropriate evidence plane.

## Project-specific implementation

Every project should publish a Participant Matrix answering:

| Role | Required M5-CV evidence | Additional project evidence | Admission authority | Capability granted | Expiry/recheck |
| --- | --- | --- | --- | --- | --- |
| Public reviewer | verified account optional/public policy | none/minimal | project policy | view/comment | session/policy |
| Builder | skill/capability | engagement terms | project lead | contribute | engagement |
| Operator | skill/experience/entity | contract, insurance, licenses | steward/title owner | operate | current contract |
| Member/steward | identity + eligibility | consent/governance admission | governing body | governance | membership state |
| Investor | identity + offering-specific eligibility | subscription + disclosures + funds | issuer/authorized intermediary | instrument rights | instrument terms |
| Lender | entity/authority | credit/loan docs + funds | borrower/lender | debt rights | loan terms |
| Trustee/fiduciary | identity + status | appointment | governing instrument | fiduciary acts | appointment |
| Transfer agent | entity + registration/status | engagement | issuer | transfer-agent function | engagement/status |
| Commodity intermediary | registration/status where required | mandate/engagement | project/instrument | derivatives function | status/engagement |
| Signatory | identity + office/role | authority source | entity/governing body | defined signature | delegation |

## Boundary

This architecture does not itself determine that a person is legally permitted
to invest, lend, hedge, vote, operate or act as a fiduciary. It defines how the
Commons can reuse evidence and make project-specific decisions auditable while
leaving the legal determination and authoritative records with the responsible
people and institutions.
