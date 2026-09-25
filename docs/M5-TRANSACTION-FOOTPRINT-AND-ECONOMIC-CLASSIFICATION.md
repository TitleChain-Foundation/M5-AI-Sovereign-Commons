# M5 Transaction Footprint and Economic Classification

**Status: Draft design basis for public review**

Every economic event receives its own classification and footprint. A fee, payment, security/investment instrument, or authority state never overwrites the identity, title evidence, or history of the underlying asset.

## Working classes

```text
M1 — Money / Payment / Access / Utility / Fee Events
M2 — Commodity
M3 — Title / Ownership Asset
M4 — Security / Investment Instrument
M5 — Jurisdiction / Sovereign Authority State
```

These are M5 internal classes. External legal/regulatory classifications remain separate, versioned records supported by authoritative sources.

The account ladder uses the same numbers for a different purpose: **M0** is a
sovereign human with a self-asserted `000-IAM` identifier who is not yet
credentialed; credentialing activates **M1-BOM** (Bank of Me), then M2-BOU,
M3-BOB, M4-BOI and M5-BOG as separately authorized contexts. Account tiers are
written with their suffix (`M3-BOB`) so they are never confused with these
asset classes (`M3`). See the [Glossary](../GLOSSARY.md).

## M3 — actual titled/ownership asset

Each M3 record preserves the independently identifiable asset:

```text
asset_id
asset_type
authoritative_title_source
recorded_titleholder
jurisdiction
valuation + source + timestamp
rights
liens
mortgages
claims
leases
licenses
easements
pledges
restrictions
transfer / pledge authority
provenance
correction / supersession history
```

## M4 — actual security/investment instrument

M4 is the security or investment instrument itself. M4 is **not** canonical shorthand for an opaque financial wrapper.

If an M4 instrument depends on M3 assets or rights, enumerate those links individually.

```text
M4 PROJECT NOTE
issuer = ProjectCo
principal = $25M

  ├─ M3 ASSET A
  │  titleholder = Entity A
  │  relationship = revenue right
  │  allocated value = ...
  │  pledge / lien = ...
  │  priority = ...
  │
  └─ M3 ASSET B
     titleholder = Entity B
     relationship = collateral
     ...
```

An SPV/entity record never silently converts its holdings into one unidentified basket.

## Anti-rehypothecation

Before an M3 asset/right is attached to an M4 instrument:

```text
identify asset
→ resolve titleholder
→ verify pledge/assignment authority
→ inspect existing liens/pledges
→ inspect priority
→ inspect restrictions
→ inspect valuation evidence
→ determine unresolved/conflicting state
→ M5Canon
```

Public machine states may include:

```text
AVAILABLE_FOR_REVIEW
PARTIALLY_ENCUMBERED
FULLY_ENCUMBERED
CONFLICTING_CLAIM
TITLE_OR_AUTHORITY_UNRESOLVED
DENY
HUMAN_REVIEW_REQUIRED
```

No machine state substitutes for authoritative title/lien records, applicable law, or qualified professional review.

## M1 fee/event taxonomy

Each charge is a separate M1 event.

```text
UTILITY
COMPUTE
DATA
MODEL
PROFESSIONAL_SERVICE
REGULATED_SERVICE
NETWORK
SETTLEMENT
STATUTORY_FEE
TAX
INSURANCE
FINANCING
ADMINISTRATIVE
OTHER
```

This prevents title insurance, taxes, professional fees, or financing costs from being mislabeled as utility charges merely because they are M1 events.

## Transaction Footprint

The footprint distinguishes:

```text
underlying asset value      → M2 / M3
instrument value            → M4
transaction/service costs   → M1
authority/jurisdiction      → M5
```

It may also reference:

```text
OpenMeter usage
Laya local compute
Jev / provider usage
frontier-model usage
M5Canon evaluation
x402 settlement
M5Bank accounting
TitleChain evidence
```

## Aggregate index output

Where disclosure and licensing permit, public-safe aggregates can support future M5 Global Index and Exchange indicators such as:

- transfer cost / asset value;
- data and compute cost;
- transaction time;
- human-review ratio;
- financing friction;
- jurisdictional cost;
- machine-commerce activity;
- M2/M3 underlying value associated with M4 instruments;
- provider economics.

Private M5POD records and confidential customer data do not become public index inputs merely because they are metered.
