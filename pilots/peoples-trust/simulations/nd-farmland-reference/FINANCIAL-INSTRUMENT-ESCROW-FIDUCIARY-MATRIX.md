# ND-FARM-SIM-001 — Financial Instrument, Escrow & Fiduciary Matrix

**Status:** SAMPLE-DATA / PUBLIC-REVIEW MATRIX\
**Purpose:** Convert the farmland simulation from a generic capital plan into a
function-by-function classification and execution matrix.

## Rule

No financial instrument or money-movement capability is activated until the
project resolves:

`underlying asset → underlying right → instrument → intent → issuer/obligor → holder/participant → jurisdiction(s) → regulator(s) → regulated/fiduciary function → authoritative record → escrow/release conditions → evidence/reconciliation`

## Instrument routing

| Instrument / transaction | State | SEC | CFTC | Bank / escrow | Transfer agent / fiduciary |
| --- | --- | --- | --- | --- | --- |
| Farmland deed purchase | Primary property/agricultural lane | Normally not securities merely because land is purchased | Not ordinarily a derivatives transaction | Closing escrow/bank | Title/closing fiduciary roles as applicable |
| Secured farm loan | Lending/UCC/property | May implicate securities law depending note/offering facts | Usually no unless derivative added | Loan funding/escrow | Collateral agent/trustee/servicer if structured |
| Equity/LLC/LP interest | Entity + state securities | Federal securities review | No, unless derivative overlay | Subscription escrow if used/required | Issuer/transfer agent/administrator as applicable |
| Revenue/profit share | Contract + state securities review | May be security depending facts | No, unless commodity derivative features | Subscription/payment account | Issuer/TA/trustee if applicable |
| Tokenized security | State securities still relevant | Security remains subject to securities framework | Only if product also falls within CFTC lane | Funding/custody as applicable | Transfer agent/official holder record |
| Spot crop sale | Commercial/agriculture | Not ordinarily security | Not ordinarily futures/swap | Operating bank | Commercial counterparties |
| Crop future / option | State commercial matters may coexist | Only if security-related product | Primary CFTC lane | FCM/customer funds infrastructure | FCM/DCM/clearing roles |
| Commodity swap | Contract + state law may coexist | Security-based swap rules only if the product is security-based | CFTC swap lane for commodity swap | Swap/payment infrastructure | Swap intermediaries/fiduciaries as applicable |
| Commodity pool interest | State securities may apply to pool interest | Pool interests may also be securities | CFTC CPO/CTA/commodity-interest lane | Custody/FCM | CPO/CTA/administrator/custodian |
| Security future | State securities may coexist | Joint SEC lane | Joint CFTC lane | Registered market infrastructure | Jointly regulated intermediaries |
| Grant/PRI | State charity/trust/tax | Follows actual investment instrument if any | Follows commodity derivative use if any | Grant/payment account | Foundation fiduciary/trustee as applicable |

## Escrow / controlled-account routing

| Account/function | Trigger | Release authority | Authoritative money record | Prohibited shortcut |
| --- | --- | --- | --- | --- |
| Acquisition closing escrow | Executed land purchase agreement | Closing instructions + required signers/conditions | Escrow/bank | AI-only release |
| Securities subscription/impoundment escrow | Offering structure requires/uses it | Offering conditions + eligibility + authorized release | Escrow/bank | Treating receipt of funds as issuance |
| Improvement/draw controlled account | Funded improvement plan | Budget + milestone + approvals | Bank/escrow | Operator self-approval outside delegated limit |
| Farm operating account | Stewardship active + operator agreement | Operator within approved budget/scope | Bank | Treating operating cash as investor escrow |
| Stewardship reserve | Reserve policy active | Defined fiduciary/governance approval | Bank/trust account | General-purpose withdrawal |
| Distribution/waterfall account | Lawful economic instrument activated | Holder record + adopted waterfall | Bank/paying agent | Using wallet possession as holder proof |
| Debt-service/tax/insurance reserve | Financing or project covenant | Contract-defined | Bank/trust | Unapproved reallocation |

## Required actor matrix

| Function | Accountable role | Evidence before activation |
| --- | --- | --- |
| Sell land | Actual owner/trust + authorized signer | Title + governing authority |
| Buy land | Eligible acquisition/steward entity | Formation + agricultural ownership eligibility + signer authority |
| Hold closing funds | Authorized escrow/bank | Engagement/account + instructions |
| Issue security | Issuer + authorized signer | Governing docs + securities classification/path |
| Maintain holder record | Transfer agent/issuer recordkeeper as legally applicable | Appointment/registration/status |
| Act as trustee/fiduciary | Trustee/fiduciary | Appointment + governing instrument + scope |
| Place/distribute securities | Broker-dealer/placement agent if required/used | Registration + engagement + scope |
| Trade commodity interests | FCM/DCM/CPO/CTA/swap parties as applicable | Registration/exemption/status + mandate |
| Operate farm | Local farm operator | Executed operating agreement |
| Approve draw | Designated human/fiduciary/committee | Current authority + budget/milestone |
| Reconcile evidence | TitleChain/M5 | Source references + receipts; never substitutes for source authority |

## Fail-closed examples

- `UNKNOWN_INSTRUMENT_CLASSIFICATION` → no offering capability
- `STATE_SECURITIES_PATH_UNRESOLVED` → no in-state sale
- `FEDERAL_SECURITIES_PATH_UNRESOLVED` → no securities sale
- `CFTC_CLASSIFICATION_UNRESOLVED` → no futures/swap/pool capability
- `ESCROW_RELEASE_AUTHORITY_MISSING` → no release
- `TRANSFER_AGENT_REQUIRED_NOT_ACTIVE` → no regulated transfer
- `FIDUCIARY_APPOINTMENT_STALE` → no fiduciary action
- `TITLE_AUTHORITY_UNVERIFIED` → no deed execution
- `OPERATOR_AUTHORITY_REVOKED` → no operating draw
- `SOURCE_CHAIN_NOT_ACTIVATED` → no capital deployment
- `DESTINATION_CHAIN_NOT_CONFIRMED` → do not mark funds deployed
