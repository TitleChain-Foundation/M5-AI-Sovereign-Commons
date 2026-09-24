# Laya — M5POD Local System 1 Profile

**Status: Draft integration profile for public review**

Laya is proposed as the resident local System 1 decision engine inside M5POD.

Laya is a bounded decision runtime, not a human/legal authority and not a replacement for M5Canon.

## Role

Use Laya when the task can be expressed as a bounded typed decision rather than free-form generation.

Typical outputs:

- choice;
- boolean probability;
- score;
- classification;
- routing decision;
- anomaly flag;
- confidence;
- escalation decision.

```text
M5HUM / lawful entity
        ↓
M5POD
        ↓
Laya local runtime
        ↓
typed probabilistic decision
        ↓
M5Canon
        ↓
ALLOW / DENY / HUMAN REVIEW
```

## Local-first economics

For a locally held model on user-controlled hardware:

```text
model_access_cost = 0
x402_required = false
billable = false
diagnostics_default = OFF; optional local diagnostics only
```

Track separately:

```text
compute_cost
energy_cost
storage_cost
network_cost
```

Metering does not automatically mean billing.

## Reliability boundary

Preferred wording:

> Laya avoids free-form text generation for typed decision tasks. Its outputs remain bounded and structured, but classifications and probabilities can still be wrong and remain subject to thresholds, testing, deterministic policy, and human review.

## Authority boundary

Laya may inform a decision. It may not independently:

- transfer title;
- move money;
- create a lien or pledge;
- sign a legal instrument;
- issue a credential;
- create eligibility;
- create authority;
- override an authoritative registry;
- override M5Canon; or
- override required human/institutional approval.

## Escalation

Escalation may go to:

- larger local generative model;
- Jev/other qualified hosted System 1 provider;
- approved frontier provider;
- human review.

Escalation never bypasses M5Canon.

## Tier I baseline and scope

[M5-AIMARKET-001](../standards/M5-AIMARKET-001.md) governs self-provided local
inference. It requires no service meter, usage cap, telemetry export, payment,
hosted routing or periodic account check. Diagnostics are OFF unless the human
opts into local diagnostics. Event/meter/commerce pipelines apply to metered
services, not every local inference. Protected action evidence remains separate.
Jev/Eve is the first featured hosted/chat integration; other providers remain
eligible under the same scoped controls. Laya is a first featured local candidate.
