# PPT-EZ-CA-0001 — SEC S7-2026-30 Implementation Crosswalk

**Project:** 312 Spring Commons / Spring Commons LA  
**SEC filing reference:** TitleChain Foundation public comment filed September 5, 2026  
**SEC File:** S7-2026-30  
**Release:** 34-106246  
**Status:** Project working draft / public-commons implementation test. This project is not represented as SEC-approved, SEC-reviewed, or a regulatory sandbox.

## 1. Why this crosswalk exists

TitleChain Foundation's filed SEC comment recommends voluntary, implementation-neutral open standards that make authority, restrictions, execution and evidence interoperable while leaving legally authoritative records and regulated duties with the responsible institutions.

312 Spring Commons should explicitly identify itself as a proposed real-world implementation test of those recommendations across two separate but linked domains:

1. **physical/public asset transition** — federal disposition, public conveyance, deed restrictions, lease/operating rights, permitting and productive-infrastructure assets; and
2. **capital/investment instruments** — grants, PRIs, debt, project equity, HTC/NMTC structures and any securities or other regulated instruments actually created.

A TitleChain event does not by itself make a physical transfer, securities transfer, permit, payment, professional opinion or government approval legally effective.

## 2. SEC recommendation → project control

| Filed SEC recommendation | Spring Commons control | Primary project documents |
|---|---|---|
| Credential-bound participant identifiers | Resolve accountable principal, current role/credential, jurisdiction, scope, revocation and evidence before consequential action | DOC-01, 05, 10, 12, 17, 20, 22 |
| Known legal entity → current human authority → bounded agent | Entity first, current authorized human second, software/AI delegation third and narrower | DOC-03, 04, 06, 10, 16, 17, 20, 22 |
| Machine-readable restrictive legends / transfer rights | Restrictions point to legal source, affected right, jurisdiction, status, permitted actors, placement/removal authority, effective period and required approvals | DOC-10, 11, 12, 16, 18 |
| Ricardian three-part representation | Human-readable controlling terms + machine-readable structured meaning + separately bounded executable instructions, sharing identifier/version/digest | DOC-01 through DOC-22 as applicable; canonical treatment DOC-16 |
| Six-gate pre-activation controls for automated agents | Identity → current role/credential → jurisdiction/legal context → deterministic policy → required accountable approval → tamper-evident receipt | DOC-06, 10, 16, 17, 20, 22 |
| Origination authority distinct from later transfer/correction/cancellation authority | No role receives later capabilities merely because it created, registered or onboarded the asset/instrument | DOC-10, 16, 17, 18 |
| Underlying right/provenance preserved across wrappers and rails | Physical title/right, leasehold, financial wrapper, securityholder record, settlement rail and digital representation remain distinct but linked | DOC-01, 05, 10, 11, 16, 18 |
| Regulator-ready evidence | Export actor, authority source, instruction, approvals, execution, authoritative result, restrictions, corrections, exceptions and reconciliation in documented formats | DOC-06, 10, 15, 16, 17, 21, 22 |

## 3. Authority + Responsibility Registry

Before execution, the project should maintain a current registry for every consequential participant.

| Field | Required content |
|---|---|
| `entity_id` | Canonical legal entity/institution identifier and authoritative registry/source |
| `role_id` | Exact office, professional, fiduciary, project or regulated function |
| `human_principal` | Current accountable human/signatory when a human action is required |
| `authority_source` | Statute, regulation, deed program, resolution, appointment, license, registration, contract, board action, delegation or other controlling evidence |
| `jurisdiction` | Federal / California / Los Angeles / other applicable jurisdiction |
| `scope` | Asset, instrument, project, matter, amount/resource, action and/or time scope |
| `credential_status` | Current / pending / expired / revoked / suspended / unknown |
| `effective_from` / `effective_to` | Effective window where applicable |
| `revocation_source` | Authoritative revocation/termination source where applicable |
| `approval_threshold` | Single signer, governing body, regulator, transfer agent, lender, counsel or multi-party approval |
| `system_of_record` | Government, bank, transfer-agent, permit, court, corporate, professional or other legally authoritative record |
| `m5_account_context` | M5BOM plus M5BOB/M5BOI/M5BOG role context where used; never treated as the authority source itself |
| `agent_delegation` | Named software/AI agent, purpose, tools, model/version, limits, approvals, expiry and emergency suspension, if any |
| `evidence_receipt` | Proposed / approved / rejected / executed / corrected / reversed state plus timestamp, source references and digest |

## 4. Candidate public-authority onboarding map

**Do not pre-designate an office as a required signer until counsel and the authoritative program/charter/statute establish its role.** The project should earmark candidate institutions for resolution, then activate only the ones legally required by the final pathway.

| Plane | Candidate institutions / roles | Activation rule |
|---|---|---|
| Federal asset disposition | GSA disposition authority | Required if GSA controls the federal disposition path; exact office/person/signing authority verified from current federal records |
| Historic Surplus / preservation | National Park Service Historic Surplus program and preservation/lease-review functions | Required if Historic Surplus pathway proceeds; exact program decisions and signatory authority verified |
| Public fee-title recipient | Qualifying state, county, municipality or similar governmental entity | Required for the current Historic Surplus working model; governing-body approvals and signatory authority verified under applicable law/charter/resolution |
| California state | Secretary of State or other registries for entity/status evidence as applicable | Activate for actual registry/status function |
| California Governor's Office | Candidate oversight/approval participant only if final pathway or law assigns a function | Do not presume approval/signature authority |
| California Attorney General | Candidate charitable/public-interest/fiduciary/oversight participant only if the final entity/trust/pathway triggers jurisdiction | Do not presume approval/signature authority |
| Los Angeles Mayor's Office | Candidate local executive participant if city ownership, approvals or charter/delegation require it | Do not presume approval/signature authority |
| LA City Council / County Board | Candidate governing-body approval for public owner/grantee, lease, financing or other local action | Activate only for actions legally assigned to the body |
| City Attorney / County Counsel | Candidate legal-review/advice role for public entity | Scope and authority defined by engagement/charter/law |
| Planning / building / fire / health / utilities / preservation | Permit, inspection, interconnection and operating approvals | Activate based on final project scope and jurisdiction |

### Historic Surplus title boundary

Under the current working Historic Surplus model, fee title should remain modeled as a conveyance to an eligible public entity. The proposed Public Trust of America may become a stewardship, membership, leasing, operating or program framework only to the extent permitted by the final deed, lease, public-owner approvals and applicable law. Do not describe the federal conveyance as a direct fee-title transfer to the Public Trust unless a separate lawful eligibility pathway is established.

## 5. Regulated capital and market participant map

The project should select participants by function and instrument, not brand.

| Role | Activation rule / authoritative record |
|---|---|
| Issuer / borrower / project vehicle | Definitive entity and governing documents; authorized signers verified |
| Registered transfer agent | If a security requires/uses transfer-agent services, selected registered transfer agent remains accountable for official Master Securityholder File and regulated functions |
| Broker-dealer / placement agent | Activate only if the selected offering/distribution structure requires or uses the role; verify registration, engagement and transaction scope |
| ATS / exchange / other venue | Activate only if lawful secondary transaction pathway actually uses the venue |
| Custodian | Activate if asset/security/cash custody structure uses one; authoritative custody records control |
| DTC / DTCC participant / settlement infrastructure | Activate only if selected security/settlement/custody design uses the infrastructure; do not assume every instrument must use DTC/DTCC |
| Bank / escrow | Authoritative money movement remains with selected regulated bank/escrow systems |
| CPA / auditor | Verify license/firm, engagement, scope and good standing; professional attestation stays attributable to issuer |
| Tax / HTC / NMTC professionals | Verify role and engagement; tax determinations remain with qualified professionals and official program/tax records |
| Trustee / fiduciary / trust agent | Appointment, fiduciary duties and scope arise from governing instrument and law; M5 records status/evidence only |
| Counsel | Legal determinations remain with licensed counsel; engagement and matter scope recorded |
| SEC / regulator | Regulator is not an operator of project stack; project produces regulator-ready evidence exports and preserves official filing/examination records as authoritative |

## 6. Demonstration transaction sequence

```text
FEDERAL ASSET STATE
GSA / federal title / disposition evidence
        ↓
HISTORIC / PUBLIC PATHWAY STATE
NPS + qualifying public grantee + governing-body authority
        ↓
LAWFUL CONVEYANCE / RECORDING
public fee title + restrictions
        ↓
STEWARDSHIP / OPERATING RIGHTS
Public Trust / operator / master lease only as legally approved
        ↓
CAPITAL INSTRUMENT STATE
issuer + investor + instrument + restrictions + regulated providers
        ↓
BANK / ESCROW / DRAW
money remains on regulated authoritative rails
        ↓
PRODUCTIVE ASSET ACTIVATION
energy / water / food / compute / building system asset passports
        ↓
OPERATING + COMPLIANCE STATE
permits + notices + good standing + revenue + reporting
        ↓
TRANSFER / CORRECTION / EXIT
only under governing instrument + responsible public/regulated authority
```

## 7. Regulator-ready evidence bundle

A regulator/examiner export should be able to reproduce, at minimum:

1. controlling human-readable legal instrument and version;
2. machine-readable rights/restriction/policy representation and legal source;
3. accountable entity and current authorized human;
4. role/credential/license/registration/appointment status;
5. jurisdiction, scope, delegation, expiry and revocation evidence;
6. instruction and required approvals;
7. any software/AI involvement and bounded authority;
8. execution event and authoritative system-of-record result;
9. TitleChain provenance/state receipt and reconciliation to the authoritative record;
10. holds, rejections, exceptions, corrections, reversals and superseding events; and
11. documented export suitable for examination, migration and successor-provider continuity.

## 8. Public-commons statement

The use case should be described as an **implementation pilot being built in the public commons**. Publication makes the architecture inspectable and allows regulators, transfer agents, broker-dealers, public agencies, banks, fiduciaries, professionals, builders and researchers to review the workflow. Publication does not grant an account, credential, membership, license, regulated status, transaction authority or right to act.
