# Authority + Participant Registry Template — PPT-EZ-CA-0001

Use one row per role/capability. `TBD` means the role is anticipated but no legally effective participant has been selected or verified.

| Status | Plane | Institution / Entity | Office / Role | Human Principal / Signer | Authority Source | Jurisdiction | Scope | Credential / Registration | Effective / Expiry | Revocation / Good Standing Source | Required Co-Approvals | System of Record | M5 Account Context | Agent Delegation | Evidence Receipt |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| VERIFY | Federal disposition | U.S. GSA | TBD | TBD | Federal disposition authority / project-specific delegation | Federal | 312 Spring disposition | TBD | TBD | TBD | As required | GSA official record | M5BOG evidence context if used | None unless approved | TBD |
| VERIFY | Historic program | National Park Service | Historic Surplus / preservation role TBD | TBD | Program authority / project decision | Federal | Historic use / preservation / lease review as applicable | TBD | TBD | TBD | As required | NPS official record | M5BOG evidence context if used | None unless approved | TBD |
| SELECT | Public grantee | Eligible public entity | Governing body / authorized signer TBD | TBD | Charter/statute/resolution/conveyance documents | State/local | Fee-title receipt and public restrictions | TBD | TBD | TBD | Governing-body approvals | Official public records | M5BOG evidence context if used | None unless approved | TBD |
| CONDITIONAL | California | Governor's Office | TBD | TBD | Only if law/pathway assigns actual function | California | TBD | TBD | TBD | TBD | TBD | Official state record | M5BOG if used | None unless approved | TBD |
| CONDITIONAL | California | Attorney General | TBD | TBD | Only if law/entity/trust/pathway assigns actual oversight/function | California | TBD | TBD | TBD | TBD | TBD | Official state record | M5BOG if used | None unless approved | TBD |
| CONDITIONAL | Los Angeles | Mayor's Office | TBD | TBD | Only if charter/delegation/project approval assigns function | Los Angeles | TBD | TBD | TBD | TBD | TBD | Official city record | M5BOG if used | None unless approved | TBD |
| CONDITIONAL | Los Angeles | City Council / County Board | TBD | TBD | Resolution / ordinance / charter / applicable law | Los Angeles | Public-grantee/lease/financing actions as applicable | TBD | TBD | TBD | As required | Official legislative record | M5BOG if used | None unless approved | TBD |
| SELECT | Capital | Issuer / borrower / project vehicle | Authorized signer | TBD | Governing docs / board consent / financing instrument | Applicable | Instrument-specific | Entity + signer verification | TBD | TBD | Counsel / governing approvals | Corporate / financing records | M5BOB/M5BOI | Bounded agents only | TBD |
| CONDITIONAL | Securities | Registered transfer agent | TA role | TBD | Registration + engagement | Federal / transaction | Security issue | Current registration | TBD | SEC / regulator source | Issuer / counsel as applicable | TA official books | M5BOB/M5BOI | Bounded agent if permitted | TBD |
| CONDITIONAL | Market | Broker-dealer / placement / ATS | TBD | TBD | Registration + engagement | Applicable | Offering/distribution/secondary market | Current registration | TBD | FINRA/SEC/other authoritative source | Instrument-specific | Regulated firm's books | M5BOB/M5BOI | Bounded agents only | TBD |
| CONDITIONAL | Settlement/custody | DTC/DTCC participant or custodian | TBD | TBD | Participation/custody agreement | Applicable | Only if chosen structure uses it | Current status | TBD | Authoritative participant/custody source | As required | Official system | M5BOB/M5BOI | Bounded agents only | TBD |
| SELECT | Funds | Bank / escrow | Account / escrow authority | TBD | Account/escrow agreement | Applicable | Receipt / hold / release / reconciliation | Regulated status | TBD | Authoritative banking source | Draw approvals | Bank/escrow ledger | M5BOB/M5BOI | Bounded automation if permitted | TBD |
| SELECT | Assurance | CPA / auditor | Engagement partner / authorized professional | TBD | License + engagement | Applicable | Audit/attestation/tax scope | Current license/good standing | TBD | State board / firm source | Engagement-specific | Professional workpapers/report | M5BOB/M5BOI | Bounded agents only | TBD |
| CONDITIONAL | Fiduciary | Trustee / fiduciary / trust agent | TBD | TBD | Trust/appointment instrument + law | Applicable | Defined fiduciary duties | As required | TBD | Governing source | As required | Trust/appointment records | M5BOI/M5BOB | Bounded agents only | TBD |

## Status vocabulary

- `VERIFY` — institution is expected in the working pathway; exact office, person and authority evidence not yet resolved.
- `SELECT` — a functional role is expected but provider/participant is not yet selected.
- `CONDITIONAL` — role is activated only if the final legal/financial/project path requires it.
- `ACTIVE` — participant selected; authoritative role/credential evidence current; scope approved.
- `SUSPENDED` — authority temporarily unavailable or under review.
- `REVOKED` — authority terminated/revoked; execution must fail closed.
- `EXPIRED` — time-bounded authority ended; execution must fail closed.
