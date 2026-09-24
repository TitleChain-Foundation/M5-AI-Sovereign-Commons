# M5-AIPROV-001 — Provider Enrollment, Account Standing, Jurisdiction and Endpoint Binding

**Status: Draft for Public Comment**

## 1. Scope

This standard defines provider, plugin, service, endpoint, identity-evidence,
standing, jurisdiction-chain, credential, and lifecycle records.

## 2. Provider account requirement

A provider used for an organizational, institutional, or public service
**MUST** resolve to one current M5 provider-capable context:

```text
M5BOU | M5BOB | M5BOI | M5BOG
```

A wallet, API key, model, agent, plugin, domain, endpoint, token, or credential
alone **MUST NOT** be treated as the accountable provider principal.

A BOM/M5HUM may be the accountable human principal but is not automatically the
service-provider account.

## 3. Provider trust stack

Provider records **MUST** separately preserve:

- M5 account identity and account type;
- accountable entity/institution/public authority;
- parent account and delegation where applicable;
- enrollment status;
- entity/account verification state;
- current standing;
- identity/entity evidence stack;
- capability credentials;
- jurisdiction-chain bindings;
- endpoint bindings;
- lifecycle/effective period; and
- append-only provenance.

A status in one dimension does not imply another.

## 4. Entity and identity evidence

M5 MAY profile official registries, OpenCorporates, LEI, vLEI, W3C Verifiable
Credentials, identity-proofing providers, regulatory/professional registries,
and other approved evidence sources.

The original source, credential format, issuer, timestamps, limitations, and
status MUST remain attributable.

A credential format does not make an issuer authoritative for every claim.

OpenCorporates or another aggregator MAY support discovery/provenance but MUST
NOT be treated as universal proof of current legal good standing where the
underlying authoritative register does not establish that state.

## 5. Issuer/evidence trust profiles

A deployment SHOULD maintain a versioned trust registry stating which issuers
or sources are accepted for which claim types, assurance profiles,
jurisdictions, and purposes.

A valid signature from an unaccepted issuer does not satisfy the corresponding
M5Canon credential gate.

## 6. M5BOU rule

If an M5BOU is not independently incorporated, it MUST resolve to:

```text
verified parent M5 account
+ accountable parent entity/institution
+ current explicit delegation
+ capability/purpose/scope
+ jurisdiction
+ effective period
+ revocation state
```

A hierarchy edge alone grants no authority.

## 7. Jurisdiction-chain binding

Consequential provider actions **MUST** bind to the canonical TitleChain
Registry jurisdiction chain for the requested capability and action.

Human-readable values such as `CA`, `WA`, `US-CA`, or country names MAY be
stored for display/search but MUST NOT substitute for the canonical chain
binding.

The binding MUST retain the external authority/evidence sources that justify the
jurisdiction and capability claim. The TitleChain namespace itself does not
create jurisdiction or governmental authority.

## 8. Endpoint controls

Endpoint records **MUST** bind:

- provider M5 account;
- accountable entity;
- exact origin/protocol;
- credential/key/certificate evidence where applicable;
- redirect policy;
- data residency;
- supported `M5CAP.*` functions;
- jurisdiction bindings; and
- lifecycle/revocation state.

Identity, endpoint, redirect, key, operator, credential, jurisdiction,
standing, policy, or capability changes require reevaluation.

## 9. Machine-readable states

Provider records must separately state enrollment, verification, account
lifecycle, standing, endpoint lifecycle, credential lifecycle, and
jurisdiction-binding lifecycle.

Missing, expired, revoked, suspended, disputed, or mismatched required bindings
fail closed for consequential execution.

## 10. Endorsement boundary

Enrollment, verification, compatibility, marketplace presence, a valid
credential, or an active endpoint does not imply TitleChain Foundation,
government, regulator, or third-party endorsement.

## Preserved activation and status controls

Provider activation MUST pass the Six Gates and commit an attributable,
tamper-evident receipt before bounded execution. Enrollment MUST NOT imply
verification, activation or endorsement; public provider records retain
endorsed=false. “Level 5” and “Sovereign Nation” confer no official status.
An instrument-only BOI is not a provider until an accountable institution and
its authority are independently resolved. The public schemas conservatively
require parent and delegation references for every M5BOU.

Multi-namespace bindings and external identifiers follow the
[conformance boundary](../docs/M5-CONFORMANCE-AND-NAMESPACE-BOUNDARIES.md).
Provider registrations must not be required for ordinary self-provided Tier I
inference. An account context does not make the human a commercial provider.
