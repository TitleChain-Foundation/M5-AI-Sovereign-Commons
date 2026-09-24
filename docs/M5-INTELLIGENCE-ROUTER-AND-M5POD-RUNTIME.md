# M5 Intelligence Router and M5POD Runtime

**Status: Draft architecture for public review**

M5 does not treat AI as one interchangeable hosted chatbot.

> **Code when code is enough. Laya when a decision is enough. Jev when hosted System 1 scale or fit is needed. Generative AI when reasoning or generation is needed. Humans and accountable institutions authorize all of it.**

## Runtime classes

```text
L0 — deterministic code
L1 — Laya local System 1
L2 — resident local generative model
L3 — Jev / other hosted System 1 provider
L4 — approved hosted frontier / specialist generative provider
```

This is not a mandatory escalation ladder. A task should terminate at the lowest qualified layer.

## Routing order

```text
1. authority
2. privacy
3. task shape
4. local capability
5. confidence / quality
6. cost
7. latency
8. availability
9. escalation
```

Cost never overrides privacy or authority.

## Request contract

```text
principal_ref
agent_ref
task_type
output_type
privacy_mode
local_required
external_allowed
provider_allowlist
provider_denylist
max_external_cost_usd
latency_target_ms
confidence_floor
human_review_below
jurisdiction_constraints
data_residency_constraints
```

## Example routes

### Local typed decision

```text
task_type = classify_asset_evidence
output_type = CHOICE
local_required = true
max_external_cost_usd = 0
        ↓
Laya
```

### Large public batch

```text
task_type = index_batch_classification
output_type = TYPED_DECISION
privacy_mode = PUBLIC
external_allowed = true
        ↓
Laya batch or Jev/other approved System 1
selected by current benchmark + policy
```

### Long-form reasoning

```text
task_type = analyze_financing_package
output_type = GENERATIVE_LONG_FORM
        ↓
local generative model
or approved hosted frontier provider
```

## Fail closed

- `local_required=true` and no qualified local runtime → no external route.
- private data forbidden from external disclosure → local only.
- provider absent from allowlist → no route.
- budget exceeded → no paid route.
- confidence below threshold → human review or permitted escalation.
- consequential action without M5Canon authorization → deny execution.

## Metering versus billing

```text
Local Laya:
service_metering = NONE
billable = false
external_model_access_cost = 0

Hosted provider:
metered = true
provider_cost = versioned
billable = entitlement/price-policy dependent
```

## Receipt chain

```text
intelligence request
→ routing receipt
→ runtime/provider result
→ M5Canon decision
→ bounded action if authorized
→ usage event
→ commerce receipt when priced/billable
→ TitleChain evidence reference when applicable
```

## Tier I baseline and scope

[M5-AIMARKET-001](../standards/M5-AIMARKET-001.md) governs self-provided local
inference. It requires no service meter, usage cap, telemetry export, payment,
hosted routing or periodic account check. Diagnostics are OFF unless the human
opts into local diagnostics. Event/meter/commerce pipelines apply to metered
services, not every local inference. Protected action evidence remains separate.
Jev/Eve is the first featured hosted/chat integration; other providers remain
eligible under the same scoped controls. Laya is a first featured local candidate.
