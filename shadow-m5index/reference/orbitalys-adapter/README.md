# Orbitalys adapter boundary

This directory reserves the future public-safe adapter between SHADOW M5Index state/evidence events and Orbitalys threat analysis.

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
