# Release Status

## Current designation

**Release Candidate v0.7 — Draft for Public Comment**

This designation means the proposed standards and supporting reference
materials are sufficiently assembled for structured review. It does not mean
the implementation is Stable, production-hardened, certified, or complete.

## What may be reviewed

- seven proposed M5 standards (AI governance, models, spatial capabilities,
  providers, Ricardian contracts, the sovereign intelligence baseline, and the
  event plane);
- machine-readable schemas and non-authoritative examples;
- a provider-neutral reference governor;
- provider adapters with dated, replaceable configuration facts;
- conformance and regression tests;
- governance, contribution, security, and legal boundaries.

## What this designation does not establish

- production readiness or security certification;
- legal or regulatory compliance;
- complete threat-model coverage;
- external provider enrollment, endorsement, or credential status;
- authoritative classification by an AI model;
- approval of a particular model, provider, device, or deployment;
- completion of independent implementation or conformance testing.

## Conditions before the first public push

- [x] Each proposed public file has completed content and privacy review.
- [x] All eight synthetic examples validate against their Draft 2020-12 JSON
      Schemas, including schema-specific negative tests.
- [x] Governor budget and malformed-ledger regression tests pass.
- [x] The documented local schema, governor, and publication-gate tests pass.
- [x] Provider facts have a dated source and are marked non-canonical.
- [x] Owner approval of the dual-license structure is recorded.
- [x] Patent and trademark boundary notices are included.
- [x] Automated checks find no archives, credentials, private paths, generated
      caches, quarantined-source hash collisions, or stale release artifacts.
- [x] The candidate manifest is regenerated from the final reviewed public
      tree and passes exact path and digest verification.
- [x] The documented `security@titlechainfoundation.org` private intake passed
      an external delivery and acknowledgment test on September 7, 2026.
- [x] The accountable owner approved creation of the repository and exact first
      push on September 7, 2026.

## Conditions before a Stable release

Stable status requires a separately reviewed release decision based on
implementation maturity, security review, conformance coverage, operational
evidence, governance approval, and documented residual risks. Publication of a
Draft does not satisfy those conditions.

## Included public-comment artifacts

- `standards/`: four Draft-for-Public-Comment standards.
- `schemas/`: exactly eight Draft 2020-12 schemas.
- `examples/`: one synthetic example paired with each schema.
- `tests/test_schemas.py`: positive, required-field, unknown-field, and
  schema-specific negative validation.
- `docs/OPEN-STANDARDS-EVIDENCE-REGISTRY.md`: evidence types and claim states.
- `docs/M5POD-DATA-PORTABILITY-PROFILE.md`: Solid-aligned portability
  requirements for every M5POD account context.
- `docs/SOVEREIGN-COMMUNICATIONS-PROFILE.md`: credential-bound federation,
  P2P/mesh, external connectors, media, and NIST-oriented mappings.
- `docs/PEOPLES-TRUST-PUBLIC-PILOT.md`: synthetic, evidence-gated
  agricultural and food-and-water conformance scenarios with non-reversible
  public redaction labels.
- `docs/PILOT-SEC-RFI-CROSSWALK.md`: informative public-review questions
  grounded in the current official SEC/Federal Register proposal record.

These artifacts remain drafts. Their inclusion and successful format validation
do not finalize licensing or establish legal status, endorsement, enrollment,
certification, production readiness, or external recognition.
