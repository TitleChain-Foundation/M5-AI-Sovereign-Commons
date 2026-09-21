# Numscript + M5-x402 executable settlement simulation

> **Synthetic and write-disabled.** No bank, escrow, wallet, facilitator, chain, or financial account is connected. No funds move.

This package instantiates [M5-RICARDIAN-TRIPLE-LAYER-001](../../../../standards/M5-RICARDIAN-TRIPLE-LAYER-001.md):

1. the Spring Commons draft documents supply human terms;
2. the tranche fixture, pilot-scoped taxonomy, decision context, and M5Canon checkpoints supply machine policy and evidence; and
3. Numscript plus the M5-x402 profile supply bounded executable instructions.

## Division of responsibility

- **Numscript** models atomic double-entry postings inside a ledger boundary. Its output still requires an external system to concretize the transaction.
- **x402 v2** carries a payment requirement, signed payment payload, verification, and settlement response for a supported scheme/network.
- **M5-x402** is a proposed x402 extension that binds the payment to the Ricardian terms, policy, authority, approvals, Numscript plan, and evidence.
- **Provider adapters** connect to the actual regulated bank, escrow, custodian, issuer, or chain. They are absent from this public demo.

Every artifact binding resolves its declared URI and hashes those exact bytes. The human-terms binding identifies the canonical DOC-01–23 manifest; that schema-validated manifest independently identifies, versions, and hashes each PDF and records supersession history. The contract, human terms, policy, executable plan, and decision context share one contract identifier while retaining their own artifact identifiers and versions.

The decision context keeps internal M1–M5 class, external legal classification, jurisdiction graph, account type, human principal, credentials, delegation, mandate, institutional functions, and receipt access as separate dimensions. Every example state remains pending or unresolved. `M5-DTTC` is the internal member-pool identifier and cannot be substituted for external `DTCC`, `DTC`, `NSCC`, or `FICC` functions.

A bank ledger and a blockchain do not share one global atomic commit. Production execution therefore requires a conditional-settlement saga:

`REQUESTED → AUTHORITY_VERIFIED → POLICY_SATISFIED → SOURCE_RESERVED → DESTINATION_LOCKED → HUMAN_FIDUCIARY_APPROVED → SOURCE_COMMITTED → DESTINATION_RELEASED → RECONCILED → RECEIPTED`

Before an irreversible commit, failure releases reservations. After one leg becomes final, failure enters `EXCEPTION_HOLD` for the contractual correction, refund, recovery, insurance, or dispute process—never a fictional rollback.

## Simulation assets

| Asset | Meaning | Settlement use |
| --- | --- | --- |
| `USD/2` | Synthetic ledger denomination for the illustrative $25M tranche | Models escrow postings only; no external USD exists |
| `M5MARKER` | One project-state marker for the tranche | `NO_ASSIGNED_MONETARY_VALUE`; not accepted by x402; no title, security, redemption, or governance right |
| x402 `asset` | The explicit asset in a real payment requirement | Must be supported by the selected scheme, network, facilitator/provider, and controlling terms |

The marker's quantity is not a price. It exists so every Ricardian contract has an explicit digital representation even when that representation has no assigned monetary value.

## Included files

- [`numscript/reserve-tranche.num`](numscript/reserve-tranche.num) — models capital-provider funds entering segregated synthetic escrow.
- [`numscript/release-draw.num`](numscript/release-draw.num) — models a later approved draw from escrow to a permitted-use account.
- [`numscript/register-marker.num`](numscript/register-marker.num) — records one no-value tranche marker separately from money.
- [`m5-x402/payment-required.example.json`](m5-x402/payment-required.example.json) — synthetic x402 v2 `PaymentRequired` with the M5 Ricardian extension.
- [`m5-x402/payment-payload.example.json`](m5-x402/payment-payload.example.json) — visibly unsigned/non-settleable client echo for schema and binding tests.
- [`m5-x402/m5-x402-extension.schema.json`](m5-x402/m5-x402-extension.schema.json) — extension schema.
- [`m5-x402/simulate_m5_x402.py`](m5-x402/simulate_m5_x402.py) — validates the retry binding and demonstrates a pre-facilitator `402 HOLD`.

The normalized payment fingerprint is reconstructed from the actual server request method and normalized resource plus the x402 payment requirement and verified decision-context artifacts. It binds the x402 version, payment-identifier extension, accepted `extra` semantics, operation, scheme, network, asset, amount, recipient, maximum timeout, issuance time, absolute expiry, taxonomy, asset and legal classifications, jurisdiction graph, account authority, credential/delegation/mandate scope, institutional route, and receipt-access policy. The simulator rejects any mismatch before a provider call and accepts only explicitly untrusted fixture time.

The generated receipt validates against [`m5-first-tranche-receipt.schema.json`](../../schemas/m5-first-tranche-receipt.schema.json). It records all eight exact M5Canon function ID/URI pairs, policy and implementation versions, artifact and instruction digests, classification and authority state, institution-specific actions, deterministic timestamp and ordering anchor, prior/requested/resulting states, unresolved requirements, reconciliation status, access policy, and a genesis or previous-receipt linkage.

## Production boundary

A real implementation would need definitive agreements, selected regulated providers, a supported x402 scheme/network/asset, production adapters, custody and key management, sanctions/KYC routing, threat modeling, independent security review, monitored deployment, reconciliation, and incident recovery. Standard x402 facilitators settle supported on-chain mechanics; they do not validate M5 authority or off-chain bank finality.

[Back to the first-tranche simulation](README.md)
