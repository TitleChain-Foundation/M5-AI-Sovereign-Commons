# America's People's Trust Farmland — Project Control Index

**Status:** Project adapter to the [M5 Commons Project Control Pack](../../docs/project-control-pack/M5-COMMONS-PROJECT-CONTROL-PACK-STANDARD.md)\
**Project:** AG-PILOT-001 / ND-FARM-SIM-001 / FARMLAND / REDEVELOPMENT\
**Date:** September 24, 2026

This index maps the eight common controls to the Farmland public materials.
`AG-PILOT-001 / ND-FARM-SIM-001` is the first full project-control example. It
is an anonymized sample-data simulation: it identifies no nonpublic property,
owner, trustee, operator, county, parcel or transaction.

## Control map

| Control | Where it is answered | Current state |
| --- | --- | --- |
| Asset/right/source-of-truth | [ND-FARM-SIM-001 simulation](simulations/nd-farmland-reference/README.md) · [sample record](simulations/nd-farmland-reference/ND-FARM-SIM-001.sample.json) · [Pilot in one view](README.md#the-pilot-in-one-view) | DRAFT |
| Authority/jurisdiction/capital provenance | [ND-FARM-SIM-001 simulation](simulations/nd-farmland-reference/README.md) · [Activation Bridge](ACTIVATION-BRIDGE.md) · [Capital and Operating Partner Brief](CAPITAL-AND-OPERATING-PARTNER-BRIEF.md) | DRAFT |
| Instrument/regulatory routing | [Financial Instrument, Escrow & Fiduciary Matrix](simulations/nd-farmland-reference/FINANCIAL-INSTRUMENT-ESCROW-FIDUCIARY-MATRIX.md) · [Financial classification and escrow update](FARMLAND-FINANCIAL-CLASSIFICATION-AND-ESCROW-UPDATE.md) · [Pilot/SEC crosswalk](../../docs/PILOT-SEC-RFI-CROSSWALK.md) | DRAFT |
| Participant eligibility/credentials | [Activation Bridge](ACTIVATION-BRIDGE.md) · [Participation Passport standard](../../docs/project-control-pack/M5-PROJECT-PARTICIPATION-PASSPORT-AND-ELIGIBILITY-MATRIX.md) · [Participant matrix below](#participant-matrix) | ADDED — REVIEW |
| Escrow/treasury/fiduciary | [Financial Instrument, Escrow & Fiduciary Matrix](simulations/nd-farmland-reference/FINANCIAL-INSTRUMENT-ESCROW-FIDUCIARY-MATRIX.md) · [Financial classification and escrow update](FARMLAND-FINANCIAL-CLASSIFICATION-AND-ESCROW-UPDATE.md) | DRAFT |
| Transfer/restriction/correction/succession | [ND-FARM-SIM-001 simulation](simulations/nd-farmland-reference/README.md) · [Pilot Project Pipeline](README.md#pilot-project-pipeline) | DRAFT |
| Risk/disclosure/privacy | [Public pipeline without private targets](README.md#public-pipeline-without-private-targets) · [ND-FARM-SIM-001 privacy boundary](simulations/nd-farmland-reference/README.md) | DRAFT |
| State machine/tests | [ND-FARM-SIM-001 simulation](simulations/nd-farmland-reference/README.md) · [Conformance review sequence](README.md#conformance-review-sequence) · [`tests/test_farmland_reference_simulation.py`](../../tests/test_farmland_reference_simulation.py) | DRAFT |

No control is `VERIFIED`. The exact underlying research stays outside the
public simulation.

## Participant matrix

Not every participant is an owner. Title ownership, member/steward
governance, economic or investment rights and operating authority remain
separate. M5-CV holds reusable evidence; project-specific permission is issued
only through a Farmland
[Project Participation Passport](../../docs/project-control-pack/M5-PROJECT-PARTICIPATION-PASSPORT-AND-ELIGIBILITY-MATRIX.md).

| Role | Pathway | Gate before action | Does not create |
| --- | --- | --- | --- |
| Public supporter / reviewer | SUPPORT / review | None; review is free | Any title, economic, voting or operating right |
| Member / steward | Governance | Lawful structure providing the role; admission and consent | Title ownership or economic rights |
| Local farm operator | WORK | Operator agreement; scoped, revocable operating authority | Title, trustee or transfer-agent authority |
| Worker / vendor | WORK | Selection, engagement and required licences | Ownership or governance rights |
| Donor / grantor | SUPPORT | Donation or grant terms accepted by the project | Ownership, investment, voting or profit rights |
| Lender | FINANCIAL PARTICIPATION | Instrument classification; lender eligibility; source-of-funds review | Title or operating authority |
| Investor / economic-right participant | FINANCIAL PARTICIPATION | Instrument-specific classification, disclosure, eligibility and admission | Title ownership or steward governance |
| Commodity / hedging participant, if applicable | FINANCIAL PARTICIPATION | CFTC/commodity-derivatives routing and registered intermediary where required | Securities or title rights |
| Trustee / fiduciary | Regulated / fiduciary | Documented appointment and duties | Farm operating authority |
| Transfer agent, if applicable | Regulated / fiduciary | Registered transfer agent appointed where required | Title or custody authority |
| Bank / escrow provider | Regulated / fiduciary | Regulated institution appointed; bounded account function | Fiduciary status merely because it holds an account |
| Authorized signatory / draw approver | Authority | Current, scoped, revocable release authority per account | Authority outside the governing instrument |

Opportunities are matched against M5-CV using the
[Work, Opportunity and Support Matching](../../docs/project-control-pack/M5-CV-WORK-OPPORTUNITY-AND-SUPPORT-MATCHING.md)
model. The project remains the decision-maker for hiring, contracting,
admission and financial participation.
