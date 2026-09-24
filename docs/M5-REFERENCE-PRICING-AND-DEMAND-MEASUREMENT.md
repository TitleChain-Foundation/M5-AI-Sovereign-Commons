# M5 Reference Pricing and Demand Measurement

**Status: Internal-calibration design published for review; illustrative values are not a production offer.**

## Principle

> **Free does not mean unmeasured. Measured does not mean charged.**

Metered third-party service events may carry a product/meter reference
before the paywall is activated.

Keep these values separate:

```text
actual_cost_usd
reference_unit_price_usd
notional_service_value_usd
billed_amount_usd
waived_amount_usd
provider_cost_usd
provider_payable_usd
platform_fee_usd
```

`notional_service_value_usd` is internal product analytics, not recognized
revenue or a receivable.

## Commerce enforcement modes

Use these system modes instead of coupling business logic to x402:

```text
METER_ONLY
REFERENCE_PRICE_ONLY
PAYMENT_OPTIONAL
PAYMENT_ENFORCED
```

Settlement method is separate:

```text
LOCAL_SOVEREIGN
FREE_PUBLIC
PLAN_INCLUDED
PREPAID
CONTRACT
INVOICE
X402
```

## Free contributor phase

Public contributors may upload or nominate public-safe evidence without charge.
The system still records event volume, processing cost, and reference value.

Example:

```text
evidence submitted        billed $0
source retrieved          billed $0
evidence verified         billed $0
asset state recalculated  billed $0
```

Each may still have a reference price and cost measurement.

## Initial internal calibration catalog

The following values are deliberately **illustrative calibration seeds**, not
public prices or commitments:

| Product/event | Meter | Reference unit price |
| --- | --- | ---: |
| Public evidence submission | `evidence_submitted` | $0.01 |
| Source ingest/retrieval | `source_ingest` | $0.02 |
| Source verification | `evidence_verified` | $0.05 |
| Corroboration event | `evidence_corrob` | $0.10 |
| Basic asset-state query | `asset_query` | $0.02 |
| Evidence bundle | `evidence_bundle` | $0.10 |
| Debt/encumbrance research | `debt_query` | $0.10 |
| Title/ownership-state research | `title_query` | $0.10 |
| SHADOW derived analysis | `shadow_analysis` | $0.25 |
| Change event/webhook | `change_event` | $0.01 |
| M5Canon evaluation | `m5canon_eval` | $0.05 |
| Local Laya decision | None — unmetered | $0 AI-service price |

Hosted Jev/frontier/provider cost must be pulled from a versioned provider-cost
catalog. Do not hard-code volatile vendor pricing into product logic.

## First paid project

The first paid design partner should use a project/contract entitlement while
its contracted service events remain metered underneath. Do not require microbilling to prove
willingness to pay.

The paywall can then activate selected premium resources while free contribution
remains open.

## Demand proof

Track the progression:

```text
documentation read
→ early access request
→ test credential
→ first call
→ repeat call
→ paid project
→ recurring paid usage
→ enterprise contract
```

Stronger demand metrics include:

- paid projects;
- recurring revenue;
- repeated API usage;
- reference/notional service value;
- actual service cost;
- gross margin;
- M2/M3 value touched where disclosure permits;
- M4 instrument value touched where disclosure permits; and
- human-review burden.

## Sovereign baseline exclusion

Sovereign Local Baseline = $0. Tier I has no service meter, billable demand or
commercial notional value. Optional infrastructure estimates are separate.
The Event→Meter→Catalog→Receipt fixture covers metered services only. Commercial
comparisons use additional absolute price and task/capability evidence, never a
percentage markup over zero. See [M5-AIMARKET-001](../standards/M5-AIMARKET-001.md).
