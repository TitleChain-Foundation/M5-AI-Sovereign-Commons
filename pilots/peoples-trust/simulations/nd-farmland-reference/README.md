# AG-PILOT-001 — North Dakota Farmland Repurchase & Stewardship Simulation

**Simulation ID:** `ND-FARM-SIM-001`\
**Development lane:** `FARMLAND / REDEVELOPMENT`\
**State:** `SAMPLE-DATA SIMULATION`\
**Jurisdiction:** North Dakota, United States\
**Asset class:** Agricultural land / operating farm\
**Public-data class:** Anonymized and normalized reference scenario

> **PUBLIC-SAFE SIMULATION ONLY.** This scenario is derived from prior public
> research into a real North Dakota farmland transaction, but the public
> simulation intentionally does not identify the seller trust, beneficial owner,
> trustee, exact parcel, county, operator, address, exact acreage, exact purchase
> price, or any claimed current transaction counterparty. It is not evidence
> that the asset is available, offered for sale, under contract, financed, or
> participating in the People's Trust.

## Why this simulation exists

The Farmland / Redevelopment lane needs a complete end-to-end process, not just
a project vision. The simulation tests how a researched farm asset could move
through title, authority, classification, financing, escrow, conveyance,
stewardship, operating rights, any separately created financial instrument,
recordkeeping, correction and succession.

The governing rule is:

> **Classify the underlying asset, right, instrument, intent, actor and
> transaction before choosing the regulatory or fiduciary path.**

A digital record, token, credential or M5 classification does not decide legal
classification by itself.

## Normalized reference profile

| Field | Public simulation value |
| --- | --- |
| State | North Dakota |
| Scale | Approximately 2,000 acres |
| Farm type | Large operating row-crop / specialty-crop farm |
| Illustrative acquisition range | Approximately $12M–$15M |
| Seller | `REFERENCE-SELLER-TRUST-A` |
| Beneficial owner | Not published |
| Trustee / signatory | Not published; authority must be independently verified |
| Existing operator | `LOCAL-FARM-OPERATOR-A` |
| Operator strategy | Preserve qualified local operating continuity where lawful and commercially appropriate |
| Stewardship entity | Proposed People's Trust project steward, subject to lawful formation and agricultural-ownership eligibility |
| Financial-instrument layer | Optional; classified before activation |
| Records | Synthetic/sample records only |

---

# 1. Authority + Jurisdiction + Capital Provenance Matrix

Every consequential project action must resolve the matrix before execution.

| Matrix field | Example for this simulation | Required result |
| --- | --- | --- |
| Underlying asset | North Dakota farmland | Real-property / agricultural-land law identified |
| Underlying right | Fee title, lease, crop right, operator right, debt claim, revenue share, security interest, commodity contract, etc. | Rights kept separate |
| Instrument | Deed, note, membership/equity interest, revenue-share contract, commodity forward/future/swap, security, tokenized security, grant, PRI, loan | Classified from actual terms |
| Intent | Purchase land, finance acquisition, hedge crop price, share profits, lend, donate, operate, steward | Intent documented |
| Issuer / obligor | Project vehicle / borrower / other lawful party | Legal identity and authority verified |
| Holder / participant | Buyer, lender, investor, member, operator, hedger, grantor | Eligibility and role verified |
| State jurisdiction | North Dakota plus other relevant state(s) | State property, securities, trust/entity and agricultural-law review |
| Federal securities lane | SEC / federal securities law if instrument is a security or offering falls within federal regime | Counsel/classification required |
| Commodity/derivatives lane | CFTC / CEA if futures, swaps, commodity interests or commodity-pool activity is used | Derivatives classification required |
| Joint/overlapping lane | State + SEC; SEC + CFTC; state + federal; banking + securities, etc. | Multiple lanes may apply |
| Banking / escrow lane | Regulated bank, trust company, licensed/authorized escrow or closing provider as applicable | Money movement bounded |
| Transfer-agent lane | Registered/authorized transfer agent where applicable to a security/instrument | Official holder record identified |
| Trustee / fiduciary lane | Trustee, fiduciary, collateral agent, indenture trustee, escrow agent or other appointed fiduciary where applicable | Appointment and duties documented |
| Title / recorder lane | County/state authoritative title/recording system | Official land title remains controlling |
| Tax / accounting lane | CPA/tax advisers and official tax records | Separate professional/official record |
| M5 / TitleChain role | Policy, evidence, provenance, permissioning, receipts, reconciliation | Never silently becomes legal authority |

The matrix is resolved per instrument. There is no assumption that one regulator
or one intermediary controls the entire project.

---

# 2. Financial Instrument Classification Matrix

This matrix is a **routing aid, not a legal conclusion**. Actual classification
depends on the instrument's terms, rights, transaction structure, participants,
jurisdictions and intended use.

| Illustrative arrangement | Underlying economic/right basis | Possible primary regulatory lane(s) | Possible accountable recordkeeper / fiduciary |
| --- | --- | --- | --- |
| Cash purchase of farmland | Fee title | State real-property, agricultural-ownership, tax and recording law | Title/closing provider, recorder, buyer/seller counsel |
| Farm lease / operating agreement | Contractual use/operating right | State contract, property, agricultural and licensing law | Parties / property records where applicable |
| Secured acquisition loan | Debt + lien/security interest | State lending/UCC; federal/state banking as applicable; securities law may apply depending on instrument/offering | Bank/lender, collateral agent, title/UCC record |
| Privately placed note | Debt instrument offered to investors | State securities + federal securities, subject to exemptions/preemption and actual facts | Issuer + transfer agent/registrar or trustee if used |
| LLC/LP membership interest financing farm acquisition | Equity/economic interest | State entity/securities + federal securities depending offering | Issuer/member ledger; transfer agent if used/required |
| Revenue/profit-share instrument | Contractual right to revenue/profits | May be a security depending facts/structure; state and federal securities review | Issuer + qualified recordkeeper/transfer agent if applicable |
| Tokenized share/note/security | Same underlying security represented digitally | Securities law still follows the security; tokenization does not erase issuer/holder/transfer restrictions | Registered/authorized transfer agent or other lawful authoritative record |
| Direct spot sale of crops | Physical agricultural commodity sale | Commercial/agricultural law; CFTC derivatives rules generally not triggered merely by ordinary spot commerce | Buyer/seller commercial records |
| Commercial forward for physical crop delivery | Agricultural commodity delivery contract | CEA/CFTC analysis depends on structure and statutory exclusions; commercial contract law also applies | Contract parties / commodity intermediaries as applicable |
| Exchange-traded crop future or option | Commodity future/option | CFTC / CEA | Registered exchange, FCM, clearinghouse and related records |
| Commodity swap / hedge | Commodity price/risk derivative | CFTC / CEA; swap rules and eligible participant requirements as applicable | Swap counterparties / registered intermediaries / SDR where applicable |
| Commodity pool investing/trading in commodity interests | Pooled vehicle trading futures/swaps/options | CFTC/CPO/CTA regime; securities law may also apply to interests in the pool | CPO/CTA/FCM/custodian/administrator as applicable |
| Security future | Future on a single security or narrow-based security index | Joint SEC + CFTC | Jointly regulated market/intermediary infrastructure |
| Grant / philanthropy | Restricted or unrestricted contribution | State charitable/trust/tax rules; not automatically a security | Grantor/grantee/fiduciary/accounting records |
| PRI / mission investment | Debt/equity/other mission investment | Classification follows actual instrument; may implicate securities, tax and fiduciary rules | Foundation/investor + issuer + applicable intermediary |
| Cooperative patronage/member right | Cooperative/member relationship | State cooperative/entity law; securities treatment depends on actual rights and offering | Cooperative/member records; other recordkeeper if applicable |

### Classification principle

The **underlying asset alone does not determine the regulator**.

Farmland can sit underneath:

- an ordinary deed;
- a secured loan;
- an equity or membership interest;
- a revenue-sharing instrument;
- a security;
- a tokenized security;
- a crop sale;
- a futures or swap hedge;
- a commodity pool; or
- combinations of these.

The applicable lane therefore follows the **actual legal/economic instrument and
transaction**, not the word “farm,” “token,” “community,” or “trust.”

---

# 3. Bounded Escrow, Treasury and Fiduciary Functions

The project must not use “escrow,” “treasury,” “trust,” “custody,” and
“operating account” as interchangeable labels.

## 3.1 Acquisition / Title Closing Escrow

**Purpose:** hold purchase funds and closing documents pending satisfaction of
the land-purchase closing conditions.

**May receive:**
- authorized acquisition funds;
- lender proceeds;
- buyer funds;
- permitted closing documents/instructions.

**May release only when:**
- authorized purchase agreement is effective;
- title conditions are satisfied or properly waived;
- required approvals are present;
- deed and closing documents are executed;
- lender/funding conditions are satisfied;
- closing instructions authorize release.

**Authoritative result:** regulated/authorized escrow or bank closing record +
official deed recording.

**Cannot:**
- decide investor eligibility;
- create land title by itself;
- change the purchase price without authorized instruction;
- act as transfer agent merely because it holds money;
- release funds on an AI-only instruction.

State:
`ACQUISITION_ESCROW_FUNDED`
→ `CLOSING_CONDITIONS_SATISFIED`
→ `AUTHORIZED_RELEASE`
→ `TITLE_RECORDING_CONFIRMED`

## 3.2 Securities Subscription / Impoundment Escrow, if applicable

Use only when the selected securities path requires or uses an escrow/
impoundment arrangement.

**Purpose:** hold investor subscription funds until the conditions of the
offering/exemption are satisfied.

**May release only under the governing offering documents, applicable state/
federal requirements and authorized escrow instructions.**

North Dakota, for example, has state securities exemptions that can require
offering proceeds to be placed in escrow before release.

**Cannot:**
- determine that an instrument is exempt;
- accept investors outside the approved offering conditions;
- substitute for issuer, broker-dealer or transfer-agent duties.

State:
`SUBSCRIPTION_RECEIVED`
→ `INVESTOR_ELIGIBILITY_CONFIRMED`
→ `OFFERING_CONDITION_MET`
→ `AUTHORIZED_RELEASE_TO_ISSUER`
or
→ `REFUND_REQUIRED`

## 3.3 Capital Improvement / Project Draw Account

**Purpose:** control funded improvements, infrastructure or rehabilitation after
acquisition.

This may be an escrow, controlled account, lender-controlled draw account or
other lawful structure depending on the actual financing.

Each draw references:

- funding source;
- approved budget/use code;
- requesting authorized human;
- approving authority;
- invoice/vendor;
- milestone/evidence;
- lien/insurance/inspection requirements if applicable;
- bank/escrow authoritative transaction;
- TitleChain reconciliation receipt.

AI may prepare a draw request but does not self-approve release.

## 3.4 Farm Operating Account

**Purpose:** ordinary farm operations under the operator agreement.

Not automatically an escrow.

Bounded to:

- payroll/labor;
- seed/input purchases;
- equipment/service expenses;
- utilities;
- insurance;
- ordinary operating expenses;
- authorized revenue receipts.

Operator permissions remain budget-, role- and scope-bounded.

## 3.5 Stewardship Reserve

**Purpose:** long-term reserve for stewardship, maintenance, conservation,
resilience or specified project obligations.

It must have:

- permitted-use policy;
- withdrawal authority;
- approval threshold;
- investment/cash policy if applicable;
- reporting;
- prohibited-use rules;
- successor-control process.

It is not a general operating slush fund.

## 3.6 Distribution / Waterfall Account, if applicable

If an economic instrument lawfully provides distributions, the payment account
executes only the adopted waterfall.

It does not decide who the holder is.

Holder eligibility and authoritative ownership come from the issuer/transfer
agent/other legally controlling record.

## 3.7 Tax / Insurance / Debt-Service Reserves

Separate reserves may be used for property tax, insurance, debt service or other
contractually required obligations.

Each reserve has a defined source, use, withdrawal authority and reconciliation
record.

---

# 4. Function-Based Intermediary Matrix

Select regulated and fiduciary participants by **function**, not by brand.

| Function | Candidate role | Core responsibility | Must not be confused with |
| --- | --- | --- | --- |
| Land conveyance | Title/closing/recording professionals | Diligence, closing, deed/recording workflow | Transfer agent |
| Money movement | Bank / escrow provider | Hold/release funds according to lawful instructions | Securities holder record |
| Securities ownership record | Transfer agent / issuer recordkeeper as legally applicable | Maintain holder/transfer records, restrictions, corrections | Land recorder |
| Debt administration | Trustee / paying agent / collateral agent / loan servicer | Administer instrument-specific duties | Farm operator |
| Project fiduciary | Trustee / steward fiduciary / appointed fiduciary | Duties defined by governing instrument/law | Bank merely because it holds an account |
| Offering/distribution | Broker-dealer / placement agent if required/used | Securities distribution/activity within scope | Transfer agent |
| Custody | Qualified/authorized custodian where applicable | Safeguard assets within scope | Title owner |
| Commodity derivatives | FCM / DCM / swap intermediary / CPO/CTA as applicable | Futures/swaps/pool functions | Farm spot-crop buyer |
| Farm operations | Qualified local operator | Grow/manage/operate under agreement | Trustee, transfer agent or title owner unless separately authorized |
| Public evidence | TitleChain/M5 | Evidence, provenance, policy, permission, reconciliation | Any authoritative regulated/government record |

A participant may perform more than one lawful role only when the applicable
law, registration, appointment and conflict controls permit it.

---

# 5. End-to-End Process

## Gate 0 — Research
`RESEARCH_REFERENCE_ONLY`

## Gate 1 — Asset record
`ASSET_REFERENCE_CREATED`

## Gate 2 — Title / agricultural-jurisdiction diligence
Resolve official title, parcels, liens, leases, severable rights, agricultural
ownership restrictions, tax and applicable North Dakota requirements.

North Dakota agricultural ownership/entity eligibility must be independently
reviewed before selecting a project steward.

`TITLE_DILIGENCE_COMPLETE`

## Gate 3 — Seller/entity/signatory authority
`SELLER_AUTHORITY_VERIFIED`

## Gate 4 — Steward/acquisition entity eligibility
`STEWARD_ENTITY_ELIGIBLE`

## Gate 5 — Rights matrix
Separate title, operator, member/steward, debt, security interest, economic
instrument, commodity contract and evidence rights.

`RIGHTS_SEPARATION_CONFIRMED`

## Gate 6 — Instrument classification
For each funding or economic instrument:

1. identify underlying right;
2. identify instrument form;
3. identify intent/use;
4. identify issuer/obligor;
5. identify holder/participant;
6. determine state-law lane;
7. determine federal securities lane;
8. determine CFTC/CEA lane;
9. determine banking/escrow lane;
10. determine transfer-agent/trustee/fiduciary role;
11. identify authoritative system of record;
12. record counsel/compliance determination and unresolved questions.

`INSTRUMENT_CLASSIFICATION_COMPLETE`

No offering, transfer, hedge or regulated capability activates before this gate.

## Gate 7 — Operator continuity
`OPERATOR_PATH_APPROVED`

## Gate 8 — Capital provenance
For each dollar/instrument preserve:

`source → provider → vehicle → jurisdiction → instrument → escrow/bank rail → destination → use → resulting right`

`SOURCE_CHAIN_ACTIVATED`

This does not prove destination receipt.

## Gate 9 — Escrow/account architecture
Create only the accounts needed by the chosen structure:

- acquisition/title closing escrow;
- subscription/impoundment escrow if applicable;
- capital-improvement draw account if applicable;
- farm operating account;
- stewardship reserve;
- tax/insurance/debt-service reserve if applicable;
- distribution/waterfall account if applicable.

`ESCROW_AND_ACCOUNT_BOUNDARIES_CONFIRMED`

## Gate 10 — Conditional purchase agreement
`AUTHORIZED_OFFER_READY`

## Gate 11 — Funding and subscription gates
All applicable investor, lender, donor, grant, derivatives, banking and state/
federal conditions must pass before money is released.

`FUNDING_CONDITIONS_SATISFIED`

## Gate 12 — Closing
`CONVEYANCE_RECONCILED`

## Gate 13 — Steward/operator activation
`FARM_STEWARDSHIP_ACTIVE`

## Gate 14 — Economic instrument activation, if any
`ECONOMIC_RIGHT_ACTIVE`
or
`NO_SEPARATE_ECONOMIC_INSTRUMENT`

## Gate 15 — Operating lifecycle
`OPERATING`

## Gate 16 — Correction / succession / transfer
`CORRECTED`, `SUPERSEDED`, `SUCCESSOR_ACTIVE`, or lawful transfer state.

---

# 6. Example Decision Matrix

Before an agent exposes a capability, evaluate:

| Question | Example answer | Result |
| --- | --- | --- |
| Is this a land-title action? | Yes | Route to title/recording authority; do not use securities ledger as deed |
| Is money being held pending closing? | Yes | Acquisition escrow controls |
| Are investor funds held pending offering conditions? | Maybe | Separate securities subscription/impoundment escrow if required |
| Is the participant buying a profit/equity interest? | Yes | Securities classification review required |
| Is the instrument represented digitally? | Yes | Digital format does not eliminate securities classification |
| Is the project hedging potato/crop price with a futures/swap product? | Yes | CFTC/CEA derivatives analysis and authorized intermediaries required |
| Is the project selling physical crops spot/ordinary commercial delivery? | Yes | Commercial/agricultural path; do not automatically label it a derivatives transaction |
| Is a security future used? | Yes | Joint SEC/CFTC lane |
| Does state securities law apply? | Potentially | State registration/exemption/notice analysis remains explicit |
| Does a transfer agent hold the farm deed? | No, unless separately a lawful title owner in another role | Transfer-agent record is not land title |
| Can trustee/fiduciary act outside governing instrument? | No | Fail closed |
| Can TitleChain reconcile all records? | Yes | Evidence/reconciliation only; authoritative source stays external |

---

# 7. SEC Public-Input Connection

The simulation should now feed the SEC review with concrete tests for:

- one authoritative record per legal object;
- transfer-agent/issuer/holder-record continuity;
- machine-readable restrictions with authoritative source;
- correction and supersession;
- successor portability;
- human/entity authority before automation;
- bank/escrow versus securities-record separation;
- state/federal jurisdiction matrix;
- underlying-right preservation across digital wrappers;
- fiduciary/trustee/transfer-agent role separation.

The SEC's current transfer-agent proposal is still a proposal. The simulation is
a Foundation public-review implementation test and not an SEC-approved sandbox.

---

# 8. Public Privacy Rule

Public files must not contain the source trust, beneficial owner, trustee,
operator/company identity, exact county/parcel combination, exact acreage,
exact historical purchase price, source addresses, identifying coordinates or
metadata/filenames that reveal the source asset.

The point is to test **the process, classification and controls**, not publish a
target list.
