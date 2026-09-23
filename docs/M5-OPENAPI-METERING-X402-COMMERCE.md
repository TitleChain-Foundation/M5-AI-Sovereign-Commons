# M5 OpenAPI Metering, Pricing, x402, and Commerce

**Status: Draft reference architecture for public review**

> **OpenMeter measures. M5 prices. M5Canon authorizes. x402 settles. M5Bank accounts. Providers earn. TitleChain proves.**

## Keep the functions separate

```text
request
→ identity / account context
→ M5Canon authority
→ entitlement + budget
→ product + versioned quote
→ free / included / prepaid / contract / x402
→ execute
→ usage meter
→ commerce receipt
→ M5Bank accounting / provider payable
→ TitleChain evidence reference
```

Payment never creates authority.

## Commerce modes

```text
METER_ONLY
REFERENCE_PRICE_ONLY
PAYMENT_OPTIONAL
PAYMENT_ENFORCED
```

Default metered public-service demos to `METER_ONLY`. Tier I uses no service meter.

## Local sovereign Laya

A locally held Laya runtime on a principal-controlled M5POD is Tier I: free, sovereign, and unmetered.

```text
runtime = LAYA_LOCAL
service_metering = NONE
billable = false
model_access_price = 0
payment_required = false
diagnostics_default = OFF; optional local diagnostics only
```

Infrastructure costs can be tracked separately from model-access price.

## Hosted providers

Hosted Jev/frontier/provider calls may create provider cost.

Keep separate:

```text
provider_cost
M5 customer price
M5 platform/service fee
provider payable
settlement fee
```

## Versioned price catalog

Never hard-code commercial price in endpoint logic.

```text
product_id
price_version
billing_mode
meter
quantity
unit_price
currency
quoted_total
quoted_at
expires_at
```

Billing modes:

```text
LOCAL_SOVEREIGN
FREE
PLAN_INCLUDED
PREPAID_BALANCE
ENTERPRISE_CONTRACT
X402_PAY_PER_USE
INVOICE
```

## Agent budget controls

```text
per-call maximum
daily cap
monthly cap
provider cap
product allowlist
jurisdiction allowlist
human approval threshold
```

## Billable-event rule

Use idempotent sequencing:

```text
attempt
→ authenticate
→ authorize
→ quote
→ reserve entitlement / verify payment
→ execute
→ successful billable result
→ finalize usage
→ receipt
```

Validation errors, timeouts, provider failures, and retries must not silently double-charge.

## x402 settlement adapter

x402 is one settlement path behind an internal adapter. Do not hard-code one facilitator, chain, stablecoin, or wallet provider.

```text
request
→ authority
→ entitlement/budget
→ price quote
→ x402 payment required if applicable
→ verify
→ settle
→ execute/release result
→ meter
→ commerce receipt
→ accounting reconciliation
```

## M5Bank accounting adapter

Stablecoin receipt and USD settlement are separate events:

```text
PAYMENT_AUTHORIZED
PAYMENT_RECEIVED
ONCHAIN_FINAL
OFFRAMP_INITIATED
USD_SETTLED
PROVIDER_PAYABLE_RECORDED
PROVIDER_PAID
REFUNDED
RECONCILED
```

The public Commons repo contains interfaces and synthetic examples only. Production M5Bank keys, wallets, banking instructions, and customer records remain outside the public repository.

## Commerce receipt

A receipt should correlate:

```text
request
principal / agent
product / provider / runtime
M-Class tags
authority decision
entitlement
meter / quantity
price version
payment
usage event
execution result
provider cost
provider payable
M5 fee
transaction / asset
evidence digest
timestamps
```

## Tier I baseline and scope

[M5-AIMARKET-001](../standards/M5-AIMARKET-001.md) governs self-provided local
inference. It requires no service meter, usage cap, telemetry export, payment,
hosted routing or periodic account check. Diagnostics are OFF unless the human
opts into local diagnostics. Event/meter/commerce pipelines apply to metered
services, not every local inference. Protected action evidence remains separate.
Jev/Eve is the first featured hosted/chat integration; other providers remain
eligible under the same scoped controls. Laya is a first featured local candidate.
