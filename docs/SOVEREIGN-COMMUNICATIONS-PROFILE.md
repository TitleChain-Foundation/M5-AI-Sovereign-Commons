# Sovereign Communications Profile

**Status:** Proposed Profile for Public Comment  
**Version:** 0.1  
**Reviewed:** September 7, 2026

## Purpose

This profile defines a transport-neutral, credential-bound communication
architecture for M5POD members. It is intended to support migration from
provider-controlled communication silos toward an interoperable sovereign
internet.

The M5POD secure inbox is the default sovereign endpoint and authoritative
record. No external transport is required to exercise an M5 right.

## Transport classes

| Class | Examples | Role |
| --- | --- | --- |
| M5-native | M5POD secure inbox and compartments | Authoritative member-controlled endpoint |
| Open federation | Matrix/Element deployments | Federated rooms and real-time event exchange |
| P2P or mesh | BitChat-style BLE mesh; future reviewed protocols | Hyperlocal, offline, delayed, and disruption-tolerant transport |
| Secure messaging service | Signal and WhatsApp services | Optional external transport subject to current provider behavior |
| Meeting/collaboration service | Zoom, Roam, Teams, Slack, and similar services | Optional calls, meetings, collaboration, and notifications |
| Standards-based media | WebRTC profiles; IETF MLS where selected | Candidate interoperable media and group-security components |

Matrix is an open federated protocol. BitChat is an informative peer-to-peer
mesh example. Signal, WhatsApp, Zoom, Roam, Teams, and Slack are external
services and are not federated M5 infrastructure merely because a connector is
available.

## Participation

Protected channel participation **MUST** require:

1. an active, verified M5HUM identity credential for a human participant, or an
   applicable verified entity identity and accountable human operator;
2. current account context and standing;
3. explicit channel purpose, security level, jurisdiction, and membership
   policy;
4. required role or professional credentials;
5. explicit delegation, engagement, or representation where applicable;
6. endpoint and device assurance appropriate to the channel;
7. a current M5Canon authorization decision.

Public outreach and emergency vulnerability intake **MUST** provide a safe
bootstrap path for people who do not yet hold an M5 credential. Unverified
submissions enter quarantine and do not receive protected-channel access.

## Professional channels

Additional credentials refine access; they do not replace identity or create
general authority.

A legal channel may require:

- authoritative credential issuer;
- current license or professional status;
- jurisdiction and practice scope;
- client identity and engagement;
- matter-specific delegation and need-to-know;
- confidentiality, privilege, recording, and retention policy.

A professional title or credential does not automatically create an
attorney-client, clinician-patient, fiduciary, agency, or other protected
relationship. The same scoped approach applies to medical, accounting,
engineering, security-response, governmental, and institutional channels.

## Security levels

Technical severity and disclosure sensitivity are independent.

| Sensitivity | Default transport boundary |
| --- | --- |
| S1 Public | Approved public and member channels |
| S2 Member-restricted | Credential-bound private channels |
| S3 Security-team restricted | M5POD compartment or specifically approved encrypted room |
| S4 Compartmented | M5POD compartment by default; exceptional controlled federation |
| S5 Critical infrastructure restricted | Dedicated M5POD compartment unless an accountable authority approves another system |

M5 sensitivity labels do not create governmental classification. Government
classified information **MUST NOT** enter an M5 channel unless a separately
authorized system and lawful handling process permit it.

## Messages and media

The profile may support text, files, images, voice, video, screen recordings,
calls, and meetings. Inbound content **MUST** be treated as untrusted and
handled according to policy, including:

- quarantine before automatic opening or execution;
- content-type, size, active-content, malware, and metadata controls;
- cryptographic digest and available transport metadata;
- provenance validation and evidence anchoring;
- admission only to the authorized compartment;
- separate authorization for transcription, translation, summarization,
  recording, biometric analysis, or model processing;
- no model training without separate explicit authority.

## Mesh and delayed delivery

A P2P mesh can re-form routes as peers appear and disappear. This property
should be described as opportunistic and self-reforming, not as a guarantee of
delivery, identity, availability, confidentiality, or recovery.

Mesh profiles **MUST** define:

- device-to-M5HUM binding with privacy preservation;
- message expiry, replay protection, deduplication, and hop limits;
- delayed credential-status and revocation handling;
- store-and-forward confidentiality and metadata exposure;
- lost, captured, or malicious relay behavior;
- reconciliation when authoritative connectivity returns;
- emergency shutdown and compromised-device recovery.

## Bridges and connectors

Every bridge or connector changes the security boundary. It **MUST** be:

- visible to participants;
- separately identified and versioned;
- purpose-, direction-, data-, and channel-scoped;
- subject to endpoint and provider verification;
- time-limited and revocable;
- disabled by default for S4 and S5 content;
- represented in privacy-filtered receipts;
- tested for retention, logs, backups, bots, transcription, and notification
  leakage.

## NIST-oriented control mapping

This profile is designed for mappings to:

- NIST Cybersecurity Framework 2.0 outcomes;
- NIST SP 800-53 Rev. 5 control selections;
- NIST SP 800-61 Rev. 3 incident response;
- NIST SP 800-63 Rev. 4 identity, authentication, and federation assurance;
- NIST SP 800-207 zero-trust principles;
- NIST SP 800-218 secure software development;
- applicable FIPS cryptographic requirements.

The profile does not claim blanket NIST compliance. Each deployment **MUST**
publish its system boundary, selected outcomes or controls, implementation
evidence, assessment method, residual risks, and assessor.

## Required public conformance work

The public review should produce:

1. transport and bridge capability manifests;
2. credential and professional-role profiles;
3. channel security-level policy;
4. privacy-filtered communication receipt schema;
5. cross-transport identity-binding tests;
6. revocation and compromised-device tests;
7. mesh partition, replay, delay, and reconciliation tests;
8. media quarantine and transformation-consent tests;
9. accessibility and emergency-communication tests;
10. NIST outcome and control mappings with explicit non-applicable findings.

## Public review questions

1. Which communication functions must work without the legacy web or a central
   provider?
2. Which Matrix, MLS, WebRTC, and mesh versions should become profile
   requirements?
3. How can a peer prove current M5HUM authorization without broadcasting the
   member's identity?
4. How should revocation work during partitions and extended outages?
5. Which transports and bridges are permissible at each sensitivity level?
6. What proves delivery, receipt, acknowledgment, consent, or legal notice?
7. How should professional credentials and matter-specific relationships be
   represented without exposing private records?
8. Which organizations and independent implementers should test this profile?
