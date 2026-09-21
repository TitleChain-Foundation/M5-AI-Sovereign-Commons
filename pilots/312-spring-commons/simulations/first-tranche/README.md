# Spring Commons first-tranche simulation

> **Synthetic developer demonstration only.** This package does not represent an offer, commitment, agency approval, legal opinion, tax determination, escrow instruction, settlement, draw authorization, or achieved impact. It performs no network or financial write.

This simulation turns the 23-document Spring Commons draft package into a reproducible stage-gate walkthrough for the illustrative **$25 million private-project tranche** described in the project overview. It demonstrates coverage and readiness; it does not prove that any participant or checkpoint has been approved.

## What developers can inspect

| Artifact | Purpose |
| --- | --- |
| [Stakeholder and checkpoint map](STAKEHOLDER-CHECKPOINT-MATRIX.md) | Human-readable lifecycle, authority, capital, community, worker, and impact coverage |
| [Synthetic tranche fixture](../../examples/PPT-EZ-CA-0001-first-tranche-simulation.json) | One blocked capital-design scenario using fictional participants and no real evidence |
| [Simulation schema](../../schemas/m5-first-tranche-simulation.schema.json) | Structural contract for fixtures |
| [`simulate_first_tranche.py`](simulate_first_tranche.py) | Offline deterministic evaluator that emits a non-authoritative receipt |
| [Example receipt](receipts/PPT-EZ-CA-0001-first-tranche-receipt.json) | Reproducible result showing why initial funding remains blocked |
| [Executable settlement architecture](EXECUTABLE-SETTLEMENT-ARCHITECTURE.md) | Numscript ledger postings, M5-x402 bindings, provider boundaries, and no-value token semantics |

The simulation reuses the capital-provenance concepts in [DOC-23](../../documents/public/DOC-23-Source-of-Funds-Entity-Provenance-Jurisdiction-Chain-and-Public-Transaction-Graph-Standard.md), but does not assert `SOURCE_CHAIN_ACTIVATED` or `DESTINATION_CHAIN_CONFIRMED`.

## Lifecycle

1. **Project intake** — establish asset identity and confirm the federal disposition path.
2. **Authority formation** — identify the eligible public grantee, operator, issuer, accountable humans, and exact authority sources.
3. **Diligence and structure** — complete title, condition, preservation, operating, risk, instrument, tax, and regulatory work.
4. **Conditional commitment** — collect a non-binding indication only after the provider, signatory, provenance, conflicts, and lane are classified.
5. **Definitive closing** — require executed controlling documents, public approvals, professional opinions, regulated providers, and conditions precedent.
6. **Escrow and source-chain confirmation** — reconcile authoritative bank/escrow evidence separately from source-chain evidence.
7. **Draw and development** — apply the DOC-06 order: evidence → authority → deterministic policy → professional certification → human/fiduciary approval → financial institution settlement → receipt.
8. **Community, worker, and impact reporting** — preserve participation rights, due process, privacy, and actual-versus-target measurement.

## Run locally

From the repository root:

```text
python pilots/312-spring-commons/simulations/first-tranche/simulate_first_tranche.py
python pilots/312-spring-commons/simulations/first-tranche/m5-x402/simulate_m5_x402.py
```

The evaluator reads local JSON only. By default it prints a receipt; `--output PATH` writes that receipt to a chosen local path. It never calls an agency, provider, bank, chain, model, or external API.

The M5-x402 runner validates the `PaymentRequired` → `PaymentPayload` retry and returns `402 HOLD` before any facilitator `verify` or `settle` call. The public payload is synthetic, unsigned, non-settleable, and lacks authoritative approvals by design.

The executable layer includes checksum-bound Numscript programs and synthetic
x402 v2 wire examples. The public examples are intentionally unsigned,
non-settleable, and bound to a custom local network identifier unsupported by
standard facilitators. See the [settlement architecture](EXECUTABLE-SETTLEMENT-ARCHITECTURE.md).

## Decision semantics

- `HOLD` — one or more required checkpoints lack acceptable authoritative evidence.
- `READY_FOR_AUTHORIZED_HUMAN_REVIEW` — fixture-level gates are complete enough to route to the humans and institutions named in controlling documents.
- `execution_authorized` is always `false`. This runner cannot approve a closing, activate a source chain, release escrow, authorize a draw, or move funds.
- `SIMULATED_PASS` can demonstrate a deterministic or documentation check, but cannot satisfy an external authority, regulated-provider, professional, or human/fiduciary gate.

## Extending safely

1. Copy the synthetic fixture; never overwrite it with private KYC, bank, identity, credential, or security-sensitive data.
2. Keep `synthetic: true`, `authority_effect: NONE`, `network_write: false`, and `financial_movement: false` in public examples.
3. Add a checkpoint with its controlling DOC references, stakeholder class, authority domain, and evidence class.
4. Add tests before changing pass rules. Fail closed on missing, stale, revoked, disputed, contradictory, or synthetic authority evidence.
5. Treat an evaluator result as routing evidence only. The authoritative agency, professional, fiduciary, bank, public owner, or signer still acts in its own system of record.

[Back to the Spring Commons overview](../../README.md)
