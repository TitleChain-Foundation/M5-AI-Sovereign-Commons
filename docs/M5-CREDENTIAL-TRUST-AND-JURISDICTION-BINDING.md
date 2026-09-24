# M5 Credential Trust and Jurisdiction-Chain Binding

**Status: Draft for Public Comment**

## 1. Purpose

M5 separates identity proofing, legal-entity identity, organizational role,
professional/regulatory standing, jurisdiction, and action authority. A single
source or credential must not silently establish all of them.

## 2. Evidence stack

A provider or accountable entity may be supported by multiple sources:

```text
human identity evidence
+
legal entity evidence
+
organizational role / delegation
+
professional or regulatory standing
+
jurisdiction evidence
+
capability scope
+
endpoint binding
```

M5Canon evaluates the required links for the exact action.

## 3. Legal-entity evidence

Permitted evidence categories may include:

- authoritative company/business registry records;
- OpenCorporates records with source/provenance references;
- LEI records;
- vLEI credentials and role credentials;
- official government/institution records; and
- other approved, versioned entity evidence.

OpenCorporates is useful for normalized company data and provenance, but it must
not be treated as universal proof of current good standing. Where current legal
standing matters, use the applicable authoritative registry or another source
accepted by policy.

## 4. Credential formats

M5 is credential-format neutral.

Profiles may accept, where appropriate:

- `W3C_VC_2_0`;
- `VLEI` / the applicable GLEIF vLEI credential profile;
- `OIDC_ASSERTION`;
- `SAML_ASSERTION`;
- `API_ATTESTATION`;
- `REGISTRY_RECORD`; or
- another explicitly profiled format.

Do not convert an external credential into a different format merely for
branding. If M5 issues a derived W3C VC based on external evidence, the derived
credential must preserve the original evidence references, issuer, timestamps,
assurance/profile, and limitations.

## 5. W3C VC baseline

Use W3C Verifiable Credentials Data Model 2.0 as the stable W3C baseline for
this release profile. Newer working drafts must not be represented as the
production baseline until separately reviewed and adopted.

A cryptographically valid VC is not automatically trusted for every claim.
Verifier policy must still decide:

```text
is the issuer accepted for this claim type?
is the credential current?
is the subject correct?
is the assurance/profile sufficient?
is the jurisdiction/scope correct?
has the credential been revoked/suspended?
is the requested use permitted?
```

## 6. Identity-proofing providers

Services such as Sumsub, ID.me, and other approved identity-proofing providers
may supply identity evidence, reusable verified attributes, or credential
status through their supported interfaces.

Do not publicly claim that a named provider issues W3C VC 2.0 credentials unless
the exact integration and official provider documentation establish that fact.
When the provider supplies another attestation/API result, retain that format
and provenance or derive an M5 credential only through an approved issuer path.

## 7. Issuer Trust Registry

M5 deployments should maintain a versioned issuer/evidence trust registry.

Each entry identifies:

```text
issuer / source identity
credential or evidence format
claim types accepted
assurance/profile accepted
jurisdictions/scopes
policy version
status
reviewed_at
effective_at
expires_at
revocation/suspension reference
official evidence references
```

Recommended trust-profile states:

```text
REFERENCE_ONLY
EVALUATED
APPROVED_FOR_PROFILE
SUSPENDED
REVOKED
EXPIRED
```

`APPROVED_FOR_PROFILE` means accepted by the named M5 deployment policy for a
specific purpose. It does not imply endorsement by TitleChain Foundation,
government, regulator, or standards body.

## 8. Provider account contexts

Provider-capable M5 account contexts are:

```text
M5BOU
M5BOB
M5BOI
M5BOG
```

A BOM/M5HUM may be the accountable human principal but is not represented as a
commercial/institutional service provider account.

### M5BOU

A BOU may be an operating/project unit rather than a separate legal entity. If
it is not independently incorporated, it must bind to:

```text
verified parent M5 account
+
verified parent entity/institution
+
explicit current delegation
+
capability scope
+
jurisdiction scope
+
effective period / revocation
```

Parent association alone never transfers authority.

### M5BOB / M5BOI / M5BOG

These contexts must identify the accountable legal entity, institution, or
public authority. If a BOI context represents an instrument rather than an
institution, it is not provider-eligible until an accountable institution is
resolved separately.

## 9. TitleChain Registry jurisdiction binding

Consequential M5 actions do not authorize against a free-text jurisdiction
string.

Resolve:

```text
external authoritative jurisdiction evidence
        ↓
credential / role / standing evidence
        ↓
TitleChain Registry VC Namespace
        ↓
canonical chain_ref
        ↓
M5CANON.JURISDICTION.RESOLVE.v1
```

A jurisdiction binding should contain:

```text
binding_id
titlechain_registry_ref
vc_namespace_ref
chain_ref
display_code
display_name
external_authority_refs
credential_refs
status
verified_at
effective_at
expires_at
```

`display_code` and `display_name` are not the authority source.

## 10. Fail-closed conditions

Consequential provider execution must fail closed or require accountable human
review when any required link is:

- missing;
- expired;
- revoked;
- suspended;
- disputed;
- mismatched;
- outside jurisdiction;
- outside capability scope;
- outside delegation scope; or
- bound to a different endpoint/provider identity.

## Multi-namespace v2

Use independently evidenced namespace_bindings and external_identifiers from
[the namespace contract](M5-CONFORMANCE-AND-NAMESPACE-BOUNDARIES.md). The former
single-chain fields identify the aggregate registry record and do not establish
each jurisdiction. Friendly display values may live in presentation metadata.
