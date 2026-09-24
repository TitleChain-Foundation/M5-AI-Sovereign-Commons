# Jev — Hosted System 1 Provider Profile

**Status: Draft informative provider profile for public review**

Jev is an optional hosted System 1 provider in the M5 intelligence architecture.

It is not the default local intelligence layer and is not an authority source.

## Role

Use Jev or another qualified hosted System 1 provider for typed-decision workloads when policy permits and hosted capacity is the better fit.

Examples may include:

- large public-data batch classification;
- SHADOW/index processing;
- high-volume structured decision workloads;
- workloads exceeding local M5POD capacity;
- workloads where benchmark policy selects the hosted provider;
- enterprise deployments intentionally choosing hosted service.

```text
authorized public/permitted state
        ↓
M5 Intelligence Router
        ↓
hosted System 1 provider
        ↓
typed decision + confidence
        ↓
M5Canon
        ↓
ALLOW / DENY / HUMAN REVIEW
```

## Provider-neutral rule

Do not encode `Jev is smarter than Laya` as an architectural assumption.

Selection depends on privacy, task shape, benchmark evidence, capability, confidence, cost, latency, availability, data residency, commercial terms, and policy.

Provider prices/model IDs/limits are volatile and must remain in a versioned provider-cost catalog, not routing code.

## Metering

Reference usage fields:

```text
provider = JEV
request_count
input_units
decision_count
latency_ms
retry_count
provider_cost
human_escalation
```

Provider cost is not automatically the M5 customer price.

## Authority boundary

Payment or successful inference never establishes title, collateral availability, legal capacity, signer authority, transfer authority, regulatory eligibility, or M5Canon authorization.
