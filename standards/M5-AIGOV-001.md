# M5-AIGOV-001 — AI Governance and Deterministic Authorization

**Status:** Draft for Public Comment

## 1. Scope and normative language

This standard defines governance records for models, agents, providers, plugins,
tools, and value-related actions. “MUST”, “MUST NOT”, “SHOULD”, and “MAY” are
normative.

## 2. Authority boundary

M5Canon **MUST** be implemented as a deterministic policy and authority-control
system; it is not AI. Models, agents, providers, plugins, and named roles are
bounded capabilities and **MUST NOT** be treated as principals. All authority
comes from accountable humans or lawful entities and authoritative external
sources. Public labels, registration, schema validity, and conformance claims do
not confer legal status.

“Level 5” and “Sovereign Nation” are descriptive M5 terminology only. They
**MUST NOT** be represented as conferring governmental, diplomatic, legal,
treaty, sovereign-recognition, or other official status.

## 3. Six-Gate control

Every consequential action **MUST** pass, in order:

1. **Principal:** resolve an accountable human or lawful entity.
2. **Role and credential:** verify current identity, credentials, role,
   standing, scope, and explicit, bounded, revocable delegation.
3. **Jurisdiction:** resolve the applicable-authority graph and authoritative
   external sources.
4. **Deterministic policy:** evaluate the current instrument, entity,
   restrictions, limits, and versioned policy without model discretion.
5. **Accountable approval:** verify every approval required by policy, law,
   contract, governance, or risk classification.
6. **Evidence and audit anchor:** commit an attributable, tamper-evident receipt
   before bounded execution.

A missing, malformed, expired, revoked, altered, disputed, or out-of-scope input
**MUST** yield `deny` or `unresolved`, never implicit approval. A change in
principal, delegation, artifact, endpoint, jurisdiction, policy, credential, or
risk state **MUST** trigger reevaluation.

## 4. Function identifiers and roles

Machine policy **MUST** use versioned `M5CANON.*` control identifiers and
`M5CAP.*` capability identifiers. Named roles such as Cyrus or Savant are
human-readable implementation labels only. Their signed results are supporting
evidence, not authorization. A display name **MUST NOT** substitute for a
function identifier, and a capability **MUST NOT** implement or claim ownership
of the final M5Canon decision.

Savant is the reference named role for
`M5CAP.PROVENANCE.CONTINUITY.VALIDATE.v1`: it validates origin, custody,
transformation, attribution, continuity, and integrity across a provenance
chain. Vionneta records and anchors the provenance evidence that makes that
chain inspectable. Milner performs
`M5CAP.ACCOUNT.COGNITIVE_BOUNDARY.PROTECT.v1`, protecting the identity,
knowledge, cognitive, policy, and operational boundary of BOM, BOU, BOB, BOI,
and BOG account contexts. These functions are distinct and none grants
authority.

## 5. Twelve independent dimensions

Records **MUST** preserve, without inference or collapse, these dimensions:

1. economic class;
2. account context;
3. Title Container;
4. representation;
5. wrapper;
6. jurisdictional security state;
7. USC;
8. S-state;
9. SR-state;
10. external classifications;
11. credentials and standing; and
12. provenance.

An entry in one dimension **MUST NOT** establish another. Unknown or conflicting
dimensions remain explicit and fail closed where material.

## 6. Instrument lifecycle and receipts

Value instrument identity, denomination, valuation, jurisdiction-authority
graph, standard references, approvals, named-role results, deterministic
M5Canon decision, and append-only provenance **MUST** be separately recorded.
No currency, including USD, may be assumed. Issue, transfer, redemption,
suspension, expiry, revocation, and destruction controls **MUST** verify current
authority and lifecycle state. Unsupported legal classifications **MUST** remain
`unknown` or `disputed`.

Receipts **MUST** be attributable, ordered, tamper-evident, append-only, and
retain the exact function and policy versions. Schema validation demonstrates
format only, not legality, approval, enrollment, endorsement, or authority.
