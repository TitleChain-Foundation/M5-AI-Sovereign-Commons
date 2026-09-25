# Exhibit C - M5 Classification to Regulatory Authority Routing

> **© 2026 TitleChain Foundation.** Part of the Foundation's written submission
> to the SEC on File No. S7-2026-30 (emailed September 23, 2026; pending SEC
> posting). Licensed under CC-BY-4.0 with required attribution. TitleChain
> Foundation, M5 and related marks are not licensed, and no patent rights are
> granted. See [NOTICE](../NOTICE.md). *This notice is added by the repository and
> is not part of the submitted text.*

## Purpose

M5 classification is a machine-readable routing aid. It does not make a governmental jurisdictional determination.

```text
ASSET / RIGHT
-> M5 CLASSIFICATION
-> TRANSACTION / EVENT
-> ACTOR + CAPACITY
-> JURISDICTION
-> EXTERNAL LEGAL CHARACTERISTICS
-> POTENTIALLY APPLICABLE AUTHORITIES
-> REGULATED FUNCTION
-> REQUIRED LICENSE / APPROVAL / RECORD / EVIDENCE
-> AUTHORIZED HUMAN / BOUNDED AGENT
-> HOLD / ALLOW / REJECT
-> EXECUTION
-> AUTHORITATIVE RECORD
-> RECEIPT
```

## Routing matrix

| Event / characteristic | Potential pathway to evaluate | Authoritative determination remains with | Fail-closed evidence |
|---|---|---|---|
| Security issuance/transfer/holder record | Federal/state securities + transfer-agent requirements | SEC, applicable state law, courts, authorized regulated entities | instrument analysis, issuer authority, TA status where required, restrictions |
| Commodity/derivatives activity | Commodity/derivatives requirements | CFTC and applicable law/market authorities | product/activity analysis, registration/venue status where required |
| Bank/payment/settlement event | Banking/payment/settlement requirements | applicable federal/state banking/payment authorities | account owner, authorized signer, rail, settlement record |
| AML/BSA-relevant regulated activity | AML/BSA controls | FinCEN plus applicable functional regulator(s) | covered entity/activity, policy, screening/KYC evidence as required |
| Real-property conveyance | State/local property/title/recording | applicable state/local law, recorder/clerk/court | deed/instrument, authorized signers, recording evidence |
| Government asset disposition | Public-property/disposition rules | owning agency and applicable statutory authorities | disposition authority, approvals, restrictions, executed instrument |
| Tax event | Federal/state/local tax | IRS and applicable state/local tax authorities | transaction facts, classification, filing/payment evidence |
| Professional act | Licensing/professional rules | applicable licensing authority | current license/appointment/scope |
| Ambiguous or mixed event | Multi-agency/legal review | relevant authorities/counsel | `REGULATORY_HOLD` until resolved |

## Required machine states

- `ROUTE_IDENTIFIED`
- `ROUTE_MULTI_AUTHORITY`
- `EXTERNAL_CLASSIFICATION_REQUIRED`
- `REGULATORY_HOLD`
- `LEGAL_REVIEW_REQUIRED`
- `AUTHORITY_EVIDENCE_VERIFIED`
- `ROUTE_SUPERSEDED`

No internal classification may self-promote to `GOVERNMENT_APPROVED`.
