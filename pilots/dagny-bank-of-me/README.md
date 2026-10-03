# Dagny Bank of Me M5-VX simulation

> **Synthetic and write-disabled.** This demo does not move money, cash,
> property, services, credentials, or authority. It does not call Base44,
> Brale, Stripe, a wallet, a facilitator, M5POD, or TitleChain.

This package demonstrates how one Dagny storefront purchase can be represented
through the four initial M5-VX settlement/resource modalities:

- `DIGITAL` — M5Pay with an x402 v2 request and the proposed M5-x402 binding;
- `CASH` — evidence of physical cash delivery, never tokenized cash;
- `ASSET` — a party-valued trade-in or property transfer; and
- `SERVICE` — party-valued work applied as consideration.

The fixture models a synthetic USD 100 purchase composed of USD 40 DIGITAL,
USD 20 CASH, USD 25 ASSET, and USD 15 SERVICE. This composition is for
demonstration only. A production contract decides whether modalities may be
combined and which legal, tax, payment, custody, and consumer-protection rules
apply.

## Tool boundaries

| Function | Tool or boundary |
| --- | --- |
| Payment wrapper | x402 v2 |
| M5 payment binding | proposed M5-x402 |
| DIGITAL adapter | M5Pay |
| Candidate stablecoin provider | Brale/private-label stablecoin; not connected |
| Usage measurement | OpenMeter; not called by this fixture |
| Ledger instruction language | Formance Numscript; represented by a reference only |
| CASH evidence capture | provider-neutral camera/OCR interface; scanner not selected |
| Receipt storage | private M5POD target reference; no write |
| Provenance | optional TitleChain target reference; no write |

PocketBase, if evaluated later, would be local application infrastructure. It
is not a cash scanner, settlement provider, key store, M5POD replacement, or
canonical dependency.

## Cash privacy rules

- A banknote remains physical cash.
- A serial number is not required.
- Images and OCR text are optional and minimized.
- Evidence is private by default and access controlled.
- The public receipt carries references and hashes, not private attachments.
- Bilateral acknowledgement is required before a real exchange can reach
  `SETTLED`.

## Run

From the repository root:

```text
python pilots/dagny-bank-of-me/simulate_m5_vx.py
```

The command validates the fixture, checks that all four legs add to the agreed
purchase value, emits four deterministic synthetic M5 Value Receipts, and
validates the receipt bundle. Use `--output PATH` to write the bundle.

`consideration_reconciled` means only that the four consideration legs equal
the agreed purchase price. The bundle separately identifies the purchased
resource; it is not a double-entry ledger or proof of real delivery.

The public synthetic fixture uses SHA-256 digests instead of publishing private
locator strings. A plain digest does not protect a low-entropy locator from
guessing. Production evidence commitments require a holder-controlled random
blinding nonce or keyed HMAC, with the disclosure method defined by an approved
privacy profile.

Receipt and bundle hashes use UTF-8 JSON with keys sorted, no insignificant
whitespace, `ensure_ascii=false`, and SHA-256. A receipt hash excludes the
`receipt_hash` field; the bundle hash excludes the `bundle_hash` field.

Verify a generated bundle independently:

```text
python pilots/dagny-bank-of-me/simulate_m5_vx.py \
  --verify pilots/dagny-bank-of-me/receipts/dagny-mixed-value-exchange.receipt.json
```

## Dagny UI contract

The live Base44 storefront can consume the fixture and receipt shapes as a
write-disabled demonstration:

1. show `DIGITAL`, `CASH`, `ASSET`, and `SERVICE` as payment choices;
2. show the DIGITAL asset, FX quote, spread, and BPS allocations before
   acknowledgement;
3. collect only optional CASH evidence and require both acknowledgements;
4. label ASSET and SERVICE values as party-agreed, not M5 appraisals;
5. display `SIMULATION — NO VALUE MOVED` on every screen and receipt; and
6. never invoke a provider from the public demo.

Production enablement requires separately approved schemas, authority and
privacy review, provider contracts, key custody, adapters, reconciliation,
incident handling, and deployment controls.
