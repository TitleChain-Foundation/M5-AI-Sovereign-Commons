# M5HUM Refusal and Consent Profile

**Status:** Proposed Profile for Public Comment
**Version:** 0.1
**Reviewed:** September 20, 2026

## Purpose

This profile gives every human represented as an M5HUM a portable, human-controlled way to express refusal before sensors, models, agents, robots, marketplace APIs, or value workflows capture or use data about them. The full record belongs in the person's M5POD Bank of Me (BOM) account context. Only the minimum assertion needed for a particular interaction should be disclosed.

The profile references and supports the Refuse Consent Protocol v1.1 glyph and cryptographic-spatial pattern as an external published specification. It does not claim that an arbitrary camera, robot, platform, or authority will recognize or obey the signal. It does not convert a visual marker, wallet, credential, or M5 account into governmental sovereignty or a universal legal veto.

## Human-first rule

The human is the principal. A guardian, fiduciary, or other lawful representative may act only under separately verified authority. An M5AGT, registrar, device, model, or named role **MUST NOT** create, widen, withdraw, supersede, or waive a person's refusal.

Every M5HUM implementation **MUST** make a refusal profile available without requiring the person to buy an agent, subscribe to surveillance, disclose unnecessary identity data, or grant recording consent. Absence of a profile, inability to display a glyph, silence, presence, biometric response, or continued use **MUST NOT** be interpreted as consent.

“Human sovereignty” in this profile means agency and control over the person's M5 account and delegated capabilities. It does not assert statehood, diplomatic status, immunity, jurisdiction, or recognition.

## Portable BOM record

A conforming record **MUST** include:

1. a stable profile and subject reference;
2. human control and lifecycle state;
3. exact protocol version, source locations, and integrity digests;
4. supported signal channels, including the glyph or a signed digital assertion;
5. refused sensor and operation classes;
6. spatial and temporal scope without unnecessary location disclosure;
7. issuer, proof, revocation-status, and optional offline-ledger references;
8. deterministic pre-capture enforcement actions;
9. explicit exception references, if any; and
10. privacy-preserving decision, enforcement, and incident receipts.

The portable record **MUST** preserve refusals, denials, expiry, supersession, revocation information, signatures, provenance, and integrity digests during M5POD export and import. Private keys, precise location history, and unrelated personal data **MUST NOT** be included merely to prove refusal.

A BOM record **MAY** reference a member-supplied Genesis Mark or similar public
display artifact. The public projection **MUST NOT** contain an ownership key,
recovery card, wallet secret, private account identifier, or other
authentication material. A displayed serial number and image digest record what
the member supplied; they do not prove possession, ownership, identity,
transferability controls, protocol authority, consent status, or legal effect.

## Detection and enforcement

A participating sensor or autonomous system **MUST** evaluate applicable physical and digital refusal signals before persistent recording, retention, identification, tracking, unrelated inference, training, sharing, or actuation. Minimal transient acquisition and processing **MAY** occur only to detect, authenticate, scope, and enforce a refusal signal. That transient data **MUST NOT** be retained or reused for another purpose and **MUST** be discarded when refusal applies. A verified active refusal produces an M5Canon denial for the covered operation and triggers the declared action, such as dropping a frame, muting a payload, disabling a sensor, redacting the subject, halting processing, or rerouting.

In this profile, **pre-capture** means before persistent capture or downstream use, not before the minimum ephemeral sensor operation technically required to detect a physical signal.

An unresolved or malformed signal **MUST** pause and deny the covered operation pending deterministic resolution. Suspected spoofing **MUST** pause, deny, generate a security event, and route to an accountable human; it **MUST NOT** silently resume capture. This is an M5 fail-closed strengthening of the external v1.1 example, which describes ignoring an invalid optical command after geospatial comparison.

Offline implementations **MAY** verify a current signed ledger or equivalent locally cached status set. They **MUST** define freshness, rollback, revocation, clock, GNSS, key-compromise, and recovery controls. Connectivity failure cannot silently convert an unresolved refusal into permission.

## Consent remains separate

Refusal and consent are separate records. Withdrawing or expiring a refusal profile does not grant consent. A consent record **MUST** still identify the purpose, recipient, data and operation scope, effective period, revocation path, and applicable authority or lawful basis.

The phrase “consent to not record” in an external example is treated by M5 as a refusal or denial, not affirmative consent. M5 implementations **MUST NOT** use double negatives or dark patterns to obtain permission.

## Exceptions and competing authority

There are no implied emergency, law-enforcement, contractual, property, platform, employer, or public-interest exceptions. An exception may be applied only when a separately identified authoritative source and competent accountable decision-maker establish its scope. The decision **MUST** be necessary, proportionate, time-bounded, attributable, reviewable, and recorded without exposing more personal data than required.

M5Canon records and evaluates supplied authority evidence; it does not determine law or manufacture legal authority. Where applicable law requires collection despite refusal, the system must preserve the refusal, identify the authority relied upon, minimize collection, constrain downstream use, and issue a receipt or delayed notice where legally permitted.

## M5 integration points

- **M5POD/BOM:** stores the private source record and exports selective assertions.
- **M5-AISPACE-001:** requires pre-capture evaluation by sensor and embodied capabilities.
- **Human-experience boundary:** records the applicable refusal profile and decision.
- **M5AGT activation:** evaluates refusal before rights constraints and bounded activation.
- **Rosalind:** may implement consent-constraint enforcement but is never the source of refusal or authority.
- **Odea:** may protect the private profile and disclosure boundary.
- **M5Canon:** returns deterministic deny, allow, or unresolved according to current evidence and policy.

## External source evidence

The source publication is Dominique Brack, *The Refuse Consent Protocol*, v1.1, dated August 18, 2026. The publisher states that the disclosed information, methods, and systems are released into the public domain as a defensive publication intended to establish prior art. The Silkproof repository also distributes its code and artifacts with an MIT License. This profile records those publisher statements; it does not independently determine their legal effect.

- PDF SHA-256: `2f6db7b61e964e4b36af44ba1255666b1de3830b05ac8d35f057f00d033f2237`
- PDF SHA-512: `bb79784df46a40990f4357e3eb28c1966fc812c4d0b1dcbd4e23214ae481edbcf6e331ddcae3506492afbd516b9a8e75029b66d38c8a883ad7a538d878345127`
- SVG SHA-256: `e3a599737982f4ef22117bae49e42336d3dad03b2fb8776405392c3875021b06`
- Public PDF: <https://refuseconsent.com/downloads/Defensive_Publication_The_Refuse_Consent_Protocol_v1.1_18.Aug.2026_D._BRACK.pdf>
- Official repository: <https://github.com/Silkproof/refuse-consent-protocol>

The public PDF and repository PDF are byte-identical. The repository's 128-character publication hash matches the SHA-512 value above. M5 independently records SHA-256 to avoid algorithm ambiguity. The defensive publication, stated public-domain/prior-art intent, and MIT license are verifiable publication facts. Any patent, patent-application, ownership, priority, enforceability, or legal-coverage claim **MUST** be recorded separately with an authoritative identifier and qualified review; this profile makes no such claim.

## Minimum conformance cases

A conformance suite **MUST** demonstrate:

- active refusal denial before capture or storage;
- no consent inferred when a profile is absent, withdrawn, expired, or unreadable;
- fail-closed handling of malformed, stale, revoked, spoof-suspected, or unreachable evidence;
- offline signature, freshness, rollback, and revocation checks;
- scope isolation across sensors, operations, places, and time;
- selective disclosure and round-trip M5POD portability;
- explicit, attributable, expiring exception handling;
- privacy-preserving receipts and incident escalation; and
- accessibility through non-visual signal and control paths.

Passing schema tests proves only record shape. Device behavior, identity, legal effect, interoperability, security, and universal adoption require separate evidence.

## Illustrative member account projection

The [sanitized Sovereign Self example](../examples/member-supplied/m5pod-sovereign-self-refusal.json)
shows how a member-supplied Refuse Consent Genesis Mark may be referenced from a
private M5POD BOM refusal profile while exposing only a public social image,
public mark number, and integrity digest. It is illustrative and unverified; it
is not a credential, ownership record, or export of private M5POD evidence.
