# M5-AIMOD-001 — Model Artifacts and Hardware Profiles

**Status:** Draft for Public Comment

## 1. Scope

This standard defines portable records for model artifacts and measured
hardware/runtime profiles. “MUST”, “MUST NOT”, “SHOULD”, and “MAY” are normative.

## 2. Non-principal model boundary

A model, inference runtime, agent, benchmark, provider, or hardware device is a
bounded capability, never a principal. It **MUST NOT** create authority,
delegate to itself, approve itself, or turn an output into authoritative fact.
All authority derives from accountable humans or lawful entities and verified
external authoritative sources.

M5Canon **MUST** make authorization decisions deterministically and is not AI.
“Level 5”, “Sovereign Nation”, model names, public labels, registrations, and
profile results confer no governmental, diplomatic, legal, treaty,
sovereign-recognition, professional, certification, or endorsement status.

## 3. Artifact manifest

An artifact manifest **MUST** identify its digest algorithm and digest, format,
version, provenance events, accountable operator, intended capability function
IDs, runtime constraints, and lifecycle status. It **MUST** distinguish
`M5CAP.*` function IDs from optional named roles. Named roles are labels for
implementations; they are not authority and cannot own `M5CANON.*` controls.

License identifiers and use constraints, when supplied, are assertions pending
their authoritative source and legal review. This Draft does not finalize
licensing.

## 4. Hardware profile

A hardware profile **MUST** identify the measured system, measurement method,
time, workload, resources, result units, and provenance. Measurements **MUST
NOT** be presented as certification, endorsement, universal performance, or
authorization. Unknown values remain unknown and **MUST NOT** be synthesized.

## 5. Activation and change control

Before use, the M5Canon Six-Gate sequence **MUST** resolve principal, standing,
delegation, context, deterministic decision/required approval, and receipt
commit before activation. A digest, model, runtime, operator, endpoint,
credential, jurisdiction, policy, or material hardware change **MUST** cause
reevaluation. Missing or invalid evidence fails closed.

## 6. Context separation

Implementations **MUST** keep economic class, account context, Title Container,
representation, wrapper, jurisdictional security state, USC, S-state, SR-state,
external classifications, credentials/standing, and provenance as twelve
independent dimensions. Model output **MUST NOT** collapse or infer one from
another. Artifact and profile history **MUST** be append-only and attributable.

