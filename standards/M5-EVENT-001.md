# M5-EVENT-001 — Event, Metering, Commerce and Threat Telemetry Profile

**Status: Draft for Public Comment**

## 1. Scope

This proposed standard defines a common event envelope for M5 providers,
services, assets, instruments, agents, intelligence runtimes, metering,
commerce, TitleChain evidence, and Orbitalys threat-vector processing.

It does not make the event bus, meter, threat score, wallet, payment protocol,
or model a source of legal authority.

## 2. CloudEvents-compatible envelope

M5 event records SHOULD use a CloudEvents 1.0-compatible envelope so the same
normalized event can be consumed by usage-metering and other subscribers
without inventing a second transport-specific record.

Minimum envelope fields:

```text
specversion
id
type
source
subject
time
datacontenttype
m5eventversion
data
```

`subject` SHOULD use an opaque M5/TitleChain reference rather than unnecessary
PII.

## 3. Event identity and delivery

Events MUST have stable immutable IDs. Consumers MUST be idempotent.

Use:

```text
idempotency_key
correlation_id
causation_id
trace_id
```

where applicable.

Corrections MUST be new append-only events using `corrects_event_id` or
`supersedes_event_id`; do not overwrite previously emitted history.

The reference architecture assumes at-least-once delivery with deterministic
de-duplication rather than promising exactly-once distributed delivery.

## 4. Time semantics

Where applicable preserve:

```text
observed_at
record_effective_at
recorded_at
processed_at
```

A retrieval timestamp is not the same thing as the legal/economic effective
time of the underlying source record.

## 5. Actor and provider separation

An event may identify:

- accountable principal;
- acting human/agent;
- selected M5 account context; and
- provider account where an external or organizational service is used.

A provider service account MUST be one of:

```text
M5BOU
M5BOB
M5BOI
M5BOG
```

and MUST carry the required current verification, standing, credential,
jurisdiction-chain, capability, and endpoint bindings before a consequential
service event may be authorized.

A BOM/M5HUM may originate or authorize an event but is not automatically a
commercial/institutional provider account.

## 6. Jurisdiction-chain requirement

Consequential events MUST reference the canonical TitleChain Registry
jurisdiction-chain binding, not only a free-text state/country code.

Human-readable jurisdiction codes MAY be included for display/search only.

The chain binding MUST retain external authority/evidence references. The
TitleChain namespace does not itself create governmental authority.

## 7. Event classification

Each event may contain:

```text
primary_m5_class
related_m5_classes[]
asset_refs[]
instrument_refs[]
entity_refs[]
```

M1 fee/payment events do not mutate the M2/M3 classification of the underlying
asset. M4 instruments do not erase M3 asset/title history.

## 8. Service-event taxonomy

Providers MAY publish a versioned service-event manifest.

Examples:

### Title

```text
title.search.started
title.record.located
title.owner.matched
title.exception.detected
title.transfer.recorded
```

### Mortgage / debt

```text
mortgage.originated
mortgage.assigned
mortgage.maturity.updated
mortgage.release.recorded
debt.claim.changed
```

### Fund / asset management

```text
instrument.created
asset.relationship.added
asset.relationship.removed
valuation.updated
distribution.recorded
collateral.changed
```

### Transfer agent

```text
holder.eligibility.checked
transfer.requested
transfer.authorized
transfer.denied
restriction.applied
restriction.released
```

### Audit / accounting

```text
evidence.requested
evidence.received
reconciliation.completed
exception.opened
exception.resolved
```

## 9. Usage and pricing

Metering, pricing, billing, payment, and accounting MUST remain distinct.

An event MAY reference:

```text
meter_id
quantity
product_id
price_version
actual_cost
reference_unit_price
notional_service_value
billed_amount
waived_amount
commerce_receipt_ref
```

Free-public events may have `billed_amount = 0` while still being metered and
reference-priced.

## 10. Intelligence runtime events

Local Laya, hosted Jev, local generative models, and hosted frontier providers
must remain separate runtime classes.

Local Tier I inference on principal-controlled hardware MUST be unmetered
with a $0 AI-service price. Optional local diagnostics cannot condition access.

## 11. Orbitalys threat vectors

Orbitalys MAY consume M5 Event Plane records to evaluate cross-plane threats,
including:

- identity/credential changes;
- provider standing changes;
- jurisdiction mismatch;
- endpoint substitution;
- titleholder conflict;
- duplicate/overlapping pledge relationships;
- debt/assignment-chain gaps;
- anomalous agent/model behavior;
- replay/duplicate payment;
- source/hash/freshness conflict; and
- license/redistribution-policy mismatch.

Orbitalys output is supporting evidence. It MUST NOT create, revoke, transfer,
or waive legal authority. Threat-vector records MUST state
`authority_effect: NONE`.

## 12. Privacy and data licensing

Events MUST minimize private data. Public/aggregate export requires both:

```text
privacy policy allows export
AND
data/source license allows export
```

Private per-customer economics, M5POD content, sensitive threat vectors, and
confidential provider terms SHOULD be represented by protected references rather
than copied into public event streams.

## 13. Optional modules

A service may implement the event profile without activating every M5 module.
A service manifest may declare:

```text
metering
orbitalys
titlechain_receipts
m5canon
commerce
x402
m5global_aggregate
```

No module flag creates authority or endorsement.

## Tier I baseline and scope

[M5-AIMARKET-001](../standards/M5-AIMARKET-001.md) governs self-provided local
inference. It requires no service meter, usage cap, telemetry export, payment,
hosted routing or periodic account check. Diagnostics are OFF unless the human
opts into local diagnostics. Event/meter/commerce pipelines apply to metered
services, not every local inference. Protected action evidence remains separate.
Jev/Eve is the first featured hosted/chat integration; other providers remain
eligible under the same scoped controls. Laya is a first featured local candidate.
