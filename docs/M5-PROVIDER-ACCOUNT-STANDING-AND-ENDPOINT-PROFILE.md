# M5 Provider Account, Standing and Endpoint Profile

**Status: Draft for Public Comment**

A provider must be attributable to an accountable M5 account context rather
than to an API key, wallet, model, hostname, or plugin.

## Provider activation chain

```text
M5BOU / M5BOB / M5BOI / M5BOG
        ↓
account lifecycle ACTIVE
        ↓
accountable entity/institution verified
        ↓
required identity/entity evidence current
        ↓
GOOD_STANDING
        ↓
required capability credential current
        ↓
TitleChain Registry jurisdiction binding ACTIVE
        ↓
exact endpoint binding current
        ↓
M5Canon preflight
        ↓
AUTHORIZED SERVICE EVENT
```

## Standing states

```text
GOOD_STANDING
PENDING
SUSPENDED
REVOKED
EXPIRED
DISPUTED
UNKNOWN
```

Only `GOOD_STANDING` may satisfy a configured consequential provider gate.

## Endpoint rule

Endpoint records bind:

- M5 provider account;
- accountable entity;
- exact origin;
- protocol;
- credential/key/certificate evidence as applicable;
- redirect policy;
- data residency;
- permitted M5CAP function IDs;
- jurisdiction bindings;
- lifecycle and revocation state.

A valid endpoint cannot cure an invalid provider account, and a valid provider
account cannot authorize an unbound endpoint.

## Attempted denied events

Denied requests still produce privacy-safe telemetry:

```text
attempt event
→ usage attempt meter (billable=false)
→ Orbitalys vector when applicable
→ M5Canon DENY / UNRESOLVED
→ no provider execution
→ no paid settlement for the denied service
```

## Multi-namespace v2

Use independently evidenced namespace_bindings and external_identifiers from
[the namespace contract](M5-CONFORMANCE-AND-NAMESPACE-BOUNDARIES.md). The former
single-chain fields identify the aggregate registry record and do not establish
each jurisdiction. Friendly display values may live in presentation metadata.
