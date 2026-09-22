# Orbitalys adapter boundary

This directory reserves the future public-safe adapter between SHADOW M5Index state/evidence events and Orbitalys threat analysis.

Orbitalys is accessed through the M5 API under a separate private license. The
private service, API endpoints, credentials, proprietary models, and proprietary
outputs are not included in this repository and are not licensed under its
`Apache-2.0` or `CC-BY-4.0` terms. Any repository-authored adapter code may be
used under the repository license, but it does not grant access to or rights in
the private integration.

The adapter may:

- accept versioned, public-safe asset-state and provenance events;
- return identified threat vectors, affected nodes/edges, evidence references, severity, confidence, and mitigation suggestions; and
- append findings without rewriting authoritative state.

The adapter must not:

- grant authority, approve a transaction, or create a delegation;
- mutate source evidence or promote an evidence state;
- infer closing, title, ownership, debt, environmental clearance, or eligibility from a score;
- expose private M5POD or credential material; or
- convert a People’s Trust nomination into a right or commitment.

No executable adapter is included in v0.1.

[Back to methodology](../../methodology/README.md)
