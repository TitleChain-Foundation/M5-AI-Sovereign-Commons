# M5POD Data Portability Profile

**Status:** Proposed Profile for Public Comment  
**Version:** 0.1  
**Reviewed:** September 7, 2026

## Purpose

This profile defines the minimum public-review requirements for portable data
across M5POD account contexts. It uses the Solid project as an important open
technical baseline without claiming that every M5POD is already a conforming
Solid Pod.

The profile applies to:

- BOM — an individual or human account context;
- BOU — a deliberately shared account context;
- BOB — a business account context;
- BOI — an institutional account context;
- BOG — a government or governance account context.

These are authority contexts. A storage protocol does not create the human,
entity, jurisdiction, ownership, agency, or lawful authority represented by an
account.

## Solid status

Solid provides open technical reports for decentralized data stores, identity,
authentication, authorization, notifications, and interoperability. The Solid
Protocol is a W3C Solid Community Group report, not a W3C Recommendation.

The Open Data Institute is a steward of the Solid project. ODI stewardship does
not make an M5 implementation conformant or establish a partnership.

## Portability requirements

A conforming M5POD portability implementation **MUST**:

1. export member-selected data in documented, non-proprietary formats;
2. preserve stable identifiers or provide an explicit remapping table;
3. export machine-readable provenance and modification timestamps;
4. distinguish authoritative records, member assertions, derived data, model
   inferences, simulations, and cached copies;
5. export access-policy intent separately from provider-specific enforcement;
6. identify schemas, vocabularies, media types, and versions;
7. preserve integrity digests and applicable signatures;
8. provide an inventory before transfer and a verification report afterward;
9. support partial, purpose-limited, and revocable transfers;
10. prevent silent inclusion of secrets, private keys, recovery material, or
    data outside the exporting principal's authority;
11. preserve legal holds, retention requirements, restrictions, and applicable
    jurisdictional metadata without claiming to determine the law;
12. record the accountable request, authorization decision, execution result,
    and errors.
13. preserve human refusal profiles, denial scope, lifecycle and revocation
   state, protocol version, integrity digests, and enforcement intent;
14. support selective disclosure of a refusal assertion without exporting
   private keys, exact location history, or unrelated personal data.

## Portable package layers

An export package should separate:

1. **Content** — selected records and media.
2. **Structure** — containers, relationships, schemas, and type indexes.
3. **Identity references** — identifiers and issuer references, not private
   authentication secrets.
4. **Policy intent** — grants, denials, purposes, expiry, and delegation
   references.
5. **Provenance** — origin, custody, transformation, attribution, and integrity.
6. **Restrictions** — consent, confidentiality, retention, legal hold, and
   jurisdictional constraints.
7. **Receipts** — export, transport, import, reconciliation, and deletion
   evidence.

For BOM accounts, restrictions include the portable
[M5HUM Refusal and Consent Profile](M5HUM-REFUSAL-CONSENT-PROFILE.md). A transfer
or storage provider cannot remove, weaken, or convert refusal into consent.

## Authorization boundary

```text
accountable human or lawful entity
        |
        v
current M5HUM/entity identity, role, credential, and delegation
        |
        v
selected records, purpose, recipient, jurisdiction, and restrictions
        |
        v
M5Canon deterministic ALLOW or DENY
        |
        v
portable package creation and integrity verification
        |
        v
recipient import, reconciliation, and receipt
```

Possession of a Pod URL, WebID, access token, encryption key, export archive, or
storage account does not establish authority to transfer every record.

## Solid compatibility work

Public reviewers should define which versions and profiles apply to:

- Solid Protocol;
- WebID Profile;
- Solid-OIDC;
- Web Access Control or Access Control Policy;
- notifications;
- type indexes and data-shape discovery;
- RDF serializations and non-RDF media;
- server, client, and authorization-agent behavior.

Where multiple Solid authorization approaches exist, the M5 profile **MUST**
name the selected approach and migration behavior. Provider-specific policy
must not be presented as portable merely because content is portable.

## Required conformance tests

The public conformance suite should include:

- export from one independent implementation and import into another;
- round-trip preservation of content, relationships, provenance, and
  restrictions;
- partial export and selective disclosure;
- revoked or expired grant rejection;
- cross-account-context isolation;
- identifier conflict and schema-version migration;
- denied secret and private-key export;
- interrupted transfer and safe retry;
- deletion-request and legal-hold conflict handling;
- receipt verification without exposing protected content;
- malicious archive, path traversal, active content, and oversized-media cases;
- accessibility and human-readable inventory review.

## AI and agent boundary

Models and agents may help classify, translate, index, or reconcile data only
within an authorized purpose. They **MUST NOT**:

- infer that all data is transferable;
- convert model inference into an authoritative member record;
- train on exported content without separate authorization;
- expand access while resolving schema conflicts;
- suppress failed or partial import results.

## Public review questions

1. Which Solid technical reports and versions should be mandatory?
2. Which data formats must every M5POD account support?
3. How should authorization intent survive migration between different policy
   engines?
4. How should shared, business, institutional, and governmental records handle
   joint authority and legal holds?
5. Which independent implementations should participate in interoperability
   testing?
6. What evidence is required before M5 may claim `CONFORMANT` rather than
   `PROFILED`?

