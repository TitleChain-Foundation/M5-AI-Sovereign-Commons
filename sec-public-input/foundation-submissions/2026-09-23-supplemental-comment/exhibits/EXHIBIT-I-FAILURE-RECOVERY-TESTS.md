# Exhibit I - Failure, Recovery and Successor-State Tests

> **© 2026 TitleChain Foundation.** Part of the Foundation's written submission
> to the SEC on File No. S7-2026-30 (emailed September 23, 2026; pending SEC
> posting). Licensed under CC-BY-4.0 with required attribution. TitleChain
> Foundation, M5 and related marks are not licensed, and no patent rights are
> granted. See [NOTICE](../NOTICE.md). *This notice is added by the repository and
> is not part of the submitted text.*

| Test | Expected behavior |
|---|---|
| Valid key + revoked authority | HOLD/REJECT; no inference from cryptographic validity |
| Missing agency approval | HOLD; simulation cannot create approval |
| Expired credential | HOLD and revalidation |
| Jurisdiction mismatch | HOLD/REJECT and authoritative resolution |
| False/friendly namespace | no governmental authority inferred |
| Wallet/TA record conflict | HOLD; reconcile to authoritative record |
| Transfer journal/MSF inconsistency | record difference; investigate/reconcile |
| Stale/disputed attestation | no authority inference; review |
| Unauthorized freeze/seize | REJECT; preserve attempted action evidence |
| Provider/chain failure | successor-state migration without changing rights/authority |
| Key compromise | revoke/replace key; preserve authoritative history |
| Cryptographic deprecation | migration receipt; no silent state change |
| TA succession | portable records, authority, reconciliation, exceptions |
| AI agent exceeds delegation | DENY; preserve evidence receipt |
| Bank rail says paid, chain says pending | no title/holder change until authoritative conditions reconcile |

## Cryptographic resilience invariant

**Technical control does not manufacture authority, and the authoritative record must survive the technology used to represent it.**
