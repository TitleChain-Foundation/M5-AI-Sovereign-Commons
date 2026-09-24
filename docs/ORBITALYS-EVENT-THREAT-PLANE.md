# Orbitalys Event Threat Plane

**Status: Draft for Public Comment**

Orbitalys is the cross-plane threat-vector graph for M5 events. It consumes
normalized event/evidence state and produces bounded threat observations for
M5Canon and accountable reviewers.

## Planes observed

```text
identity / entity
credentials / delegation
jurisdiction
asset / title / rights
debt / liens / claims
M4 instruments / collateral relationships
provider / endpoint
agent / model / runtime
payment / settlement
source / provenance / licensing
```

## Example vector families

```text
PROVIDER_STANDING_CHANGED
CREDENTIAL_EXPIRED
JURISDICTION_SCOPE_MISMATCH
ENDPOINT_PROVIDER_MISMATCH
TITLEHOLDER_CONFLICT
DUPLICATE_PLEDGE_VECTOR
ASSIGNMENT_CHAIN_GAP
SOURCE_HASH_CHANGED
EVIDENCE_STALE
AGENT_SCOPE_ANOMALY
BUDGET_ANOMALY
PAYMENT_REPLAY
LICENSE_RESTRICTION_CONFLICT
```

## Output boundary

Orbitalys may output:

```text
severity
confidence
affected_refs
evidence_refs
recommended_control
```

Possible recommended controls:

```text
MONITOR
REVERIFY
STEP_UP_AUTHENTICATION
REQUIRE_ADDITIONAL_EVIDENCE
REQUIRE_HUMAN_REVIEW
PAUSE_PENDING_REVIEW
```

The vector itself must state:

```text
authority_effect = NONE
```

M5Canon or an accountable human/institution determines the legally or
operationally relevant response.
