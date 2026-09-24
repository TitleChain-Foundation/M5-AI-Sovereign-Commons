# M5-AISPACE-001 — Spatial and Human-Experience Capabilities

**Status:** Draft for Public Comment

## 1. Scope

This standard governs spatial computing, simulation, sensors, actuators,
embodied systems, and human-experience boundaries. “MUST”, “MUST NOT”, “SHOULD”,
and “MAY” are normative.

## 2. Human and authority boundary

Models, agents, providers, spaces, devices, digital representations, and named
roles are bounded capabilities, never principals. They **MUST NOT** originate
consent, authority, legal status, or factual standing. Authority comes only from
accountable humans or lawful entities and applicable authoritative external
sources. M5Canon is deterministic and not AI.

Public labels do not confer legal status. “Level 5” and “Sovereign Nation”
terminology confers no governmental, diplomatic, legal, treaty, recognition, or
territorial status. A simulated place is not a jurisdiction, and a digital
representation is not the represented person or thing.

## 3. Capability manifest

A manifest **MUST** declare versioned `M5CAP.*` function IDs, inputs, outputs,
sensor classes, actuator classes, data handling, spatial bounds, prohibited
effects, accountable operator, emergency stop, and lifecycle state. Optional
named roles are explanatory labels and **MUST NOT** replace function IDs or
claim `M5CANON.*` control.

## 4. Human-experience boundary

Systems **MUST** record notice, consent or other lawful basis, accessibility,
age/guardianship constraints where applicable, human override, physical and
psychological safety limits, data minimization, retention, and recovery paths.
Silence, presence, biometric response, model inference, or continued use
**MUST NOT** be treated as consent unless an authoritative rule expressly makes
it valid in the recorded context.

Every M5HUM **MUST** be able to maintain a portable refusal profile in their
M5POD BOM account context. Participating systems **MUST** evaluate applicable
physical and digital refusal signals before persistent recording, retention,
identification, tracking, unrelated inference, training, sharing, or actuation.
Minimal transient sensor processing may be used only to detect, authenticate,
scope, and enforce a refusal; it must not be retained or repurposed. An active
or unresolved applicable refusal fails closed. Absence, withdrawal, or expiry
of a refusal profile does not grant consent. Implementations **MUST** provide an
accessible non-visual path and follow the
[M5HUM Refusal and Consent Profile](../docs/M5HUM-REFUSAL-CONSENT-PROFILE.md).

## 5. Authorization and safety

Consequential sensing or actuation **MUST** pass M5Canon’s Six Gates: principal,
standing, delegation, context, deterministic decision and accountable approval,
then receipt commit and bounded activation. Missing, revoked, expired,
disputed, or out-of-scope evidence fails closed. Emergency stop **MUST** remain
available independently of model output.

Suspected refusal-signal spoofing **MUST** pause and deny the covered operation,
create a security event, and route to an accountable human. It **MUST NOT**
silently resume capture. Any exception requires separately verified authority,
scope, necessity, proportionality, expiry, and an attributable receipt.

## 6. Separate dimensions and evidence

Economic class, account context, title state, representation, instrument state,
jurisdiction binding, authority state, USC, S-state, SR-state, external
classifications, credentials/standing, and provenance **MUST** remain thirteen
separate dimensions. Spatial proximity or representation **MUST NOT** establish
title, identity, jurisdiction, standing, or permission. Evidence and changes
**MUST** be attributable and append-only.

