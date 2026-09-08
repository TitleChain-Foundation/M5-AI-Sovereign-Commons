# M5-AIPROV-001 — Provider Enrollment and Endpoint Binding

**Status:** Draft for Public Comment

## 1. Scope

This standard defines provider, plugin, and endpoint identity, enrollment,
verification, and lifecycle records. “MUST”, “MUST NOT”, “SHOULD”, and “MAY”
are normative.

## 2. Status and authority boundary

A provider, model, agent, plugin, credential, endpoint, or named role is a
bounded capability, never a principal. Enrollment or verification records
**MUST** identify the accountable human or lawful entity from which authority
derives and the authoritative external sources used.

M5Canon **MUST** evaluate policy deterministically and is not AI. Public labels,
compatibility, connectivity, marketplace presence, enrollment, or verification
do not confer legal status, endorsement, certification, or authority. “Level 5”
and “Sovereign Nation” terminology confers no governmental, diplomatic, legal,
treaty, recognition, or sovereign status.

## 3. Machine-readable status

Provider records **MUST** separately state enrollment status (`not_enrolled`,
`pending`, `enrolled`, `suspended`, `revoked`, or `expired`), verification
status (`unverified`, `pending`, `verified`, `failed`, `disputed`, or `expired`),
effective period, verifier, evidence references, and `endorsed: false`.
Enrollment **MUST NOT** imply verification, and verification **MUST NOT** imply
endorsement, activation, legal standing, or external participation.

## 4. Endpoint and plugin controls

Endpoint records **MUST** bind provider identity, protocol, exact origin,
credential method, certificate or key evidence where applicable, data
residency, redirect policy, supported `M5CAP.*` function IDs, and lifecycle
state. Named roles may explain an implementation but **MUST NOT** substitute for
function IDs or own an `M5CANON.*` decision.

Activation **MUST** follow the M5Canon Six Gates: principal, standing,
delegation, context, deterministic decision/approval, and receipt commit before
bounded use. Identity, endpoint, redirect, key, operator, credential,
jurisdiction, policy, or capability changes require reevaluation. Missing,
expired, revoked, altered, disputed, or mismatched bindings fail closed.

## 5. Context and provenance

Economic class, account context, Title Container, representation, wrapper,
jurisdictional security state, USC, S-state, SR-state, external
classifications, credentials/standing, and provenance **MUST** remain twelve
independent dimensions. Provider status in any one dimension **MUST NOT** imply
another. Enrollment, verification, suspension, revocation, and endpoint-change
events **MUST** be append-only, attributable, ordered, and tamper-evident.

