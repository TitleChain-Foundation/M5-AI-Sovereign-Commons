# M5-AIGOV-001 — AI Governance and Deterministic Authorization

**Status: Draft for Public Comment**

## 1. Scope and normative language

This standard defines governance records for models, agents, providers, plugins,
tools, value-related actions, and event-driven execution. “MUST”, “MUST NOT”,
“SHOULD”, and “MAY” are normative.

## 2. Authority boundary

M5Canon **MUST** be deterministic and is not AI. Models, agents, providers,
plugins, named roles, event buses, meters, threat scores, wallets, payment
protocols, and endpoints are bounded capabilities or evidence surfaces and
**MUST NOT** be treated as independent principals.

All authority derives from accountable humans or lawful entities plus the
applicable authoritative external sources.

## 3. Six-Gate control

Every consequential action **MUST** pass:

1. **Principal** — resolve the accountable human or lawful entity.
2. **Role/credential/standing** — verify current identity, entity, role,
   credential, standing, scope, and delegation.
3. **Jurisdiction** — resolve the canonical TitleChain Registry jurisdiction
   binding and the external applicable-authority graph supporting it.
4. **Deterministic policy** — evaluate current entity, asset, instrument,
   restrictions, budgets, policy, threat inputs, and limits without model
   discretion.
5. **Accountable approval** — verify every required approval.
6. **Evidence/receipt** — commit an attributable receipt before bounded
   consequential execution.

Missing, malformed, expired, revoked, suspended, disputed, mismatched, or
out-of-scope inputs **MUST** fail closed as `deny` or `unresolved`.

## 4. Function and named-role boundary

Machine policy uses `M5CANON.*` control identifiers and `M5CAP.*` capability
identifiers. Named roles are human-readable implementation labels only.

Orbitalys threat-vector output, Laya/Jev/model output, OpenMeter usage, and x402
payment evidence are inputs/evidence and cannot own the final M5Canon decision.

## 5. Independent dimensions

Records **MUST** preserve these independent dimensions without inference or
collapse:

1. economic class;
2. account context;
3. TitleChain asset/title state;
4. representation;
5. M4 instrument state;
6. jurisdiction-chain binding;
7. authority/policy state;
8. USC transaction/settlement context;
9. S-state;
10. SR-state;
11. external classifications;
12. credentials/standing; and
13. provenance.

The older canonical `wrapper` dimension is superseded by explicit M4 instrument
state. An M4 instrument must preserve its links to underlying M2/M3 assets or
rights where applicable.

## 6. Provider execution

A provider action may be authorized only when the applicable provider account
resolves to a verified `M5BOU`, `M5BOB`, `M5BOI`, or `M5BOG` context in current
required standing with current capability, jurisdiction-chain, and endpoint
bindings.

An M5BOU without independent legal identity must additionally have a verified
parent account/entity and current explicit delegation. Parent association alone
never grants authority.

## 7. Jurisdiction binding

Human-readable jurisdiction labels are display/search values only.
Consequential authorization **MUST** resolve the canonical TitleChain Registry
jurisdiction-chain binding and supporting external authority sources.

The TitleChain namespace does not itself create governmental authority,
recognition, title, license, or legal status.

## 8. Threat inputs

Orbitalys may identify threat vectors and recommend controls. Threat scores do
not automatically create or revoke legal authority. M5Canon applies the
versioned deterministic policy that determines whether a vector requires
reverification, hold, denial, step-up authentication, or human review.

## 9. Commerce inputs

Metering, reference pricing, billing, settlement, and accounting are separate
from authority. Successful payment does not satisfy an authority gate.

Tier I sovereign local inference is unmetered and has a $0 AI-service price.
Optional local diagnostics are human-controlled and cannot condition access.
See [M5-AIMARKET-001](M5-AIMARKET-001.md).

## 10. Receipts

Receipts **MUST** be attributable, versioned, ordered where required,
tamper-evident, append-only, and retain exact function/policy versions and
correction/supersession links. Schema validity proves only shape, not legal
validity, endorsement, enrollment, title, authority, or regulatory status.

## Preserved governance controls

“Level 5” and “Sovereign Nation” confer no governmental, diplomatic, treaty,
recognition or legal status. A change in principal, delegation, artifact,
endpoint, jurisdiction, policy, credential or risk MUST trigger reevaluation.
Machine policies MUST use versioned M5CANON/M5CAP identifiers. Named roles and
their signed results cannot replace authorization. Savant validates provenance
continuity; Vionneta records evidence; Milner protects the cognitive/account
boundary. These remain distinct functions.

Value-instrument identity, denomination, valuation, authority graph, standards,
approvals and lifecycle MUST remain distinct. No currency is assumed. Issue,
transfer, redemption, suspension, expiry, revocation and destruction MUST verify
current authority; unsupported legal classifications remain unknown/disputed.
The generic reference metering fixture uses USD explicitly, not as a universal
denomination. Protected action controls do not revoke ordinary Tier I inference.
