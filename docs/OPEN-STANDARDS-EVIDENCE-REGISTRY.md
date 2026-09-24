# Open Standards Evidence Registry

**Status:** Draft for Public Comment  
**Version:** 0.1  
**Reviewed:** September 7, 2026

## Purpose

The M5 Sovereign Web Map identifies technologies, specifications,
organizations, projects, and candidate corridors that may contribute to an
interoperable sovereign internet. These references are not all the same kind of
artifact and do not have the same maturity.

This registry prevents a visual reference, logo, name, or hyperlink from being
misread as:

- implemented support;
- conformance or certification;
- partnership, endorsement, or enrollment;
- legal, regulatory, or governmental approval;
- an authoritative M5 dependency.

## Reference types

Every external reference **MUST** be assigned one type:

1. **Formal standard** — approved through a recognized standards process.
2. **Published specification** — an open technical specification that may not
   be a formal standard.
3. **Guidance or control framework** — requirements, outcomes, or controls that
   require an implementation-specific profile.
4. **Open-source implementation** — software that may implement one or more
   specifications.
5. **Stewardship or ecosystem organization** — a foundation, community, or
   consortium; the organization itself is not a technical standard.
6. **Commercial or permissioned network/service** — an optional integration
   target with independent governance and terms.
7. **M5-authored proposal** — a TitleChain Foundation draft submitted for
   review; it does not replace an external standard.
8. **Candidate corridor** — an area for investigation with no implementation or
   relationship claim.

## Evidence states

The public registry **MUST** use one of these states:

| State | Meaning |
| --- | --- |
| `REFERENCE_ONLY` | Relevant to research or discussion; no implementation claim |
| `EVALUATED` | Requirements and risks have been reviewed and recorded |
| `PROFILED` | M5 requirements and versioned external references are mapped |
| `IMPLEMENTED` | A named implementation exists with version and scope evidence |
| `TESTED` | Published tests and results cover the stated implementation scope |
| `CONFORMANT` | A defined conformance suite passes for a stated version and profile |
| `ATTESTED_OR_CERTIFIED` | A named authorized body has issued a current attestation or certification |
| `PARTNERED` | A current public record establishes a relationship and scope |

States do not imply one another except where the applicable profile expressly
requires prerequisite evidence. `PARTNERED` does not establish technical
conformance, and `CONFORMANT` does not establish partnership.

## Required evidence record

Each claim beyond `REFERENCE_ONLY` **MUST** identify:

- exact specification, implementation, or organization;
- reference type;
- version, revision, or dated retrieval;
- official source;
- M5 component and limited use;
- implemented requirement set;
- tests and results where applicable;
- known exclusions and risks;
- accountable reviewer;
- review and expiry dates;
- certification or partnership record when claimed.

## Current map classification

The following entries are classifications for review, not claims of
implementation or relationship:

| Map entry | Reference type | Initial evidence state | Public interpretation |
| --- | --- | --- | --- |
| TitleChain / M5-authored materials | M5-authored proposal | `PROFILED` only where a versioned public draft exists | Proposed architecture, not external law or certification |
| 23andMine | Candidate corridor | `REFERENCE_ONLY` | Human and genomic data-sovereignty research area |
| AMP PBC | Candidate corridor | `REFERENCE_ONLY` | Public-benefit compute concept unless a separate public record establishes more |
| Linux Foundation | Stewardship/ecosystem organization | `REFERENCE_ONLY` | Open-source ecosystem reference, not blanket Linux conformance |
| Agentic AI | Candidate corridor | `REFERENCE_ONLY` | Architecture area, not a standards body |
| OpenAPI Specification | Published specification | `EVALUATED` | Candidate service-interface format; implementation evidence is separate |
| Model Context Protocol | Published specification | `EVALUATED` | Candidate bounded tool/context interface; authorization remains with M5Canon |
| x402 / M5x402 | Published protocol plus M5-authored proposal | `REFERENCE_ONLY` | Optional payment-interface research; not legal authority or settlement |
| OpenInfra Foundation | Stewardship/ecosystem organization | `REFERENCE_ONLY` | Infrastructure ecosystem reference |
| Eclipse Foundation | Stewardship/ecosystem organization | `REFERENCE_ONLY` | IoT, edge, and tooling ecosystem reference |
| OpenHW Group | Stewardship/ecosystem organization | `REFERENCE_ONLY` | Open-hardware ecosystem reference; no device certification claim |
| Open Mainframe Project | Stewardship/ecosystem organization | `REFERENCE_ONLY` | Legacy-system migration ecosystem reference |
| Open Data Institute | Stewardship organization | `EVALUATED` | Stewardship and open-data governance reference |
| Solid technical reports | Published Community Group reports | `EVALUATED` | Candidate M5POD portability baseline; not a W3C Recommendation |
| Refuse Consent Protocol v1.1 | Published specification and open-source glyph generator | `PROFILED` | Candidate machine-readable refusal signal mapped by M5; no universal device compliance, legal override, patent, partnership, or endorsement claim |
| iMasons | Stewardship/ecosystem organization | `REFERENCE_ONLY` | Digital-infrastructure and sustainability reference |
| Canton | Commercial or permissioned network/service | `REFERENCE_ONLY` | Optional regulated-finance interoperability research |
| MEST | Candidate corridor | `REFERENCE_ONLY` | Workforce and security-training concept pending an authoritative public record |
| OpenFHE | Open-source implementation | `EVALUATED` | Candidate FHE implementation; it is not itself a NIST PQC standard |
| HomomorphicEncryption.org security standard | Published community standard | `EVALUATED` | Candidate FHE parameter and security reference |
| UN Foundation | Stewardship/ecosystem organization | `REFERENCE_ONLY` | Public-good reference; no UN approval or agency relationship claim |

## Standards and guidance profiles under review

### Cybersecurity and identity

- NIST Cybersecurity Framework 2.0
- NIST SP 800-53 Rev. 5, including current updates
- NIST SP 800-61 Rev. 3
- NIST SP 800-63 Rev. 4 and its identity, authentication, and federation volumes
- NIST SP 800-207 Zero Trust Architecture
- NIST SP 800-218 Secure Software Development Framework
- FIPS 203, 204, and 205 for applicable post-quantum cryptography

NIST publications require scoped control mappings and implementation evidence.
The phrase “NIST compliant” **MUST NOT** be used without identifying the exact
publication, revision, control or outcome scope, assessment method, system
boundary, and accountable assessor.

### Data portability

- Solid Protocol and related Solid technical reports
- RDF and Linked Data formats where selected by a portability profile
- HTTP and TLS requirements referenced by the selected Solid reports

The Solid Protocol is maintained through the W3C Solid Community Group process
and is not currently a W3C Recommendation. The Open Data Institute is a steward
of the Solid project. Neither fact establishes M5POD conformance.

### Communications

- Matrix open-federation APIs
- IETF RFC 9420 Messaging Layer Security where selected
- W3C/IETF WebRTC specifications for applicable real-time media
- optional peer-to-peer mesh protocols and external provider connectors

Transport encryption, federation, delivery, and platform authentication do not
create M5 identity, professional standing, consent, privilege, legal notice, or
authority.

### Identity and credentials

- W3C Verifiable Credentials Data Model 2.0
- W3C DID Core where an approved DID method is appropriate
- NIST SP 800-63 Rev. 4
- WebAuthn and approved authenticator profiles
- OAuth and OpenID specifications where selected

A credential format does not prove that an issuer is authoritative for the
claim or that the credential is current and in scope.

### Human refusal and spatial consent

- Refuse Consent Protocol v1.1 defensive publication and glyph artifacts
- M5HUM Refusal and Consent Profile
- M5-AISPACE pre-capture refusal evaluation

The external publication is attributed to Dominique Brack. Its publisher states
that the disclosed methods and systems are released into the public domain as a
defensive publication intended to establish prior art; the Silkproof repository
also carries an MIT License. M5 records independently verified SHA-256 and
SHA-512 digests but does not independently determine the legal effect of either
statement. The publication does not by itself establish universal device
support, legal effect, a patent right, or a relationship with M5.

## Public review questions

1. Are reference types and evidence states sufficiently distinct?
2. Which versioned specifications should become mandatory profiles?
3. What tests prove portability between independent M5POD implementations?
4. What NIST outcomes or controls apply to each deployment boundary?
5. Which claims require independent assessment rather than self-attestation?
6. How should corrections, expiry, supersession, and revocation be published?
7. Which map entries should remain candidate corridors rather than technical
   requirements?

## Official reference entry points

- NIST Cybersecurity Framework: <https://www.nist.gov/cyberframework>
- NIST publications: <https://csrc.nist.gov/publications>
- Solid technical reports: <https://solidproject.org/TR/>
- ODI Solid program: <https://theodi.org/what-we-do/solid/>
- Matrix specification: <https://spec.matrix.org/latest/>
- IETF RFC 9420: <https://www.rfc-editor.org/rfc/rfc9420.html>
- W3C standards and drafts: <https://www.w3.org/TR/>
- OpenFHE: <https://openfhe.org/>
- HomomorphicEncryption.org: <https://homomorphicencryption.org/>
- Refuse Consent Protocol: <https://github.com/Silkproof/refuse-consent-protocol>


## September 23 contract profile additions

| Reference | Type | State / pin | Limited role |
| --- | --- | --- | --- |
| CloudEvents | Published specification | PROFILED: 1.0.2, reviewed 2026-09-23 | Event envelope; wire specversion 1.0 |
| W3C VC Data Model | Formal W3C Recommendation | PROFILED: 2.0 | Credential shape; not issuer trust |
| W3C VC 2.1 | Draft reference in Sept. 22 handoff | REFERENCE_ONLY; not adopted by this profile | No production baseline claim |
| OpenMeter | Metering implementation/service | REFERENCE_ONLY; integration version pending | Replaceable usage adapter for metered services |
| x402 V2 | Published payment protocol reference | REFERENCE_ONLY; adapter version pending | Optional settlement, not authorization |
| GLEIF LEI/vLEI | Organizational identity ecosystem | REFERENCE_ONLY; deployment profile pending | Preserve native credential/source framework |
| OpenCorporates | Corporate-data service | REFERENCE_ONLY | Entity discovery/provenance; not universal standing |
| Laya | External local-model candidate | REFERENCE_ONLY; exact artifact/license/runtime pin required | First featured local typed-decision candidate |
| Jev/Eve | External hosted/chat candidate | REFERENCE_ONLY; exact API/license pin required | First featured hosted/chat integration; replaceable |
| Sumsub / ID.me | Identity-verification service candidates | REFERENCE_ONLY; exact evidence profile pending | Native evidence only; no blanket W3C VC claim |

The maintainer-supplied Sept. 22 source review is historical source material,
not independent implementation verification. This patch profiles CloudEvents
1.0.2 and W3C VC 2.0; provider-specific behavior, prices, licenses and API versions
must be verified before deployment. Public synthetic pins do not fulfill that
requirement. No partnership, enrollment, or endorsement is asserted.

Sources: [CloudEvents 1.0.2](https://github.com/cloudevents/spec/blob/v1.0.2/cloudevents/spec.md),
[W3C VC 2.0](https://www.w3.org/TR/vc-data-model-2.0/),
[historical source list](EXTERNAL-REFERENCE-REVIEW-2026-09-22.md).
