# Security Policy

## Draft status

This repository contains proposed standards and non-production reference code.
Do not use it as the sole control for consequential or regulated actions.

## Reporting

Do not disclose exploitable vulnerabilities, credentials, private evidence, or
production endpoint details in a public issue or Discussion.

Report a suspected vulnerability privately to
[security@titlechainfoundation.org](mailto:security@titlechainfoundation.org).
This dedicated address is the bootstrap confidential intake channel. After this
repository becomes public, GitHub Private Vulnerability Reporting should also be
enabled and used when available.

For general participation, documentation, or account-support questions, contact
[support@titlechainfoundation.org](mailto:support@titlechainfoundation.org).
The support address is not a vulnerability-reporting channel. Do not send
exploits, credentials, private evidence, production topology, or other sensitive
security material to it.

An initial vulnerability report should include only the information needed for
safe triage:

- affected public document, schema, code path, version, or commit, if known;
- vulnerability class and potential impact;
- whether exploitation has been observed;
- safe reproduction conditions without live credentials or personal data;
- preferred contact method and any disclosure constraints.

Do not attach active exploit code, secrets, personal data, or private M5POD
records unless the security team provides an approved transfer method. Inbound
files and links are untrusted and may be quarantined.

The security team should acknowledge the report, assign a case reference,
classify technical severity separately from disclosure sensitivity, and provide
instructions for any protected follow-up. Submission does not grant access to a
security compartment or establish that a vulnerability is confirmed.

Matrix/Element or another approved encrypted channel may be used for scoped
response coordination after triage. The authoritative case evidence remains in
the approved security record; a chat room, message-delivery indicator, or
transport encryption does not by itself prove identity, authority, receipt,
validation, or remediation.

Public disclosure must be coordinated after validation and remediation. The
project may retain a privacy-filtered record of receipt, decisions, corrections,
and disclosure status.

## Expected control properties

Implementations should:

- fail closed on missing, malformed, expired, revoked, or out-of-scope authority;
- keep personal, business, institutional, governmental, and sovereign contexts
  isolated;
- verify provider identity and endpoint binding before consequential calls;
- treat provider metadata and model output as untrusted input;
- constrain tools, sensors, actuators, and external side effects;
- preserve tamper-evident authorization and execution evidence;
- support revocation, recovery, rollback, and provider substitution;
- reject budget checks when required accounting evidence is unavailable or
  malformed.

The public threat model and bootstrap security and support contacts are included
in this candidate. External delivery to and acknowledgment from the security
address were confirmed on September 7, 2026.
