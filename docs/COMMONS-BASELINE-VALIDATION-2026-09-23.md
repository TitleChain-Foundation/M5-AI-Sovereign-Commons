# Commons handoff and M5BOM baseline — validation evidence

**Date:** 2026-09-23 · **Maturity:** public draft / synthetic reference contracts.

Base: current main `9a127948964fe046536dd7785ec953d9b48e6ba5` fetched into a
fresh checkout. Branch: `feature/m5-event-plane-commerce-v4`. Open PRs #19
(homepage) and #20 (outreach) were inspected and preserved. This change does
not depend on the older reviewed outreach feature SHA.

## Source packages

Sept. 22 v3 supplied the base files. Sept. 23 Master Handoff supplied the
mandatory overlay. The member's subsequent Tier I clarification supersedes
old local-metering/default-billing language. Eve/Jev is the first featured
chat/hosted integration; M5-Eve remains open to other providers.

- `M5-FINAL-PR-PACKAGE-2026-09-22.zip`: `sha256:f3bf957c79564a6eb3e7c4599ee9a81f389d7fc5e44ad5d3a5c22ac8521c545a`
- `M5-MASTER-ENGINEERING-HANDOFF-2026-09-23 (1).zip`: `sha256:9b6abd8cb5b0ca53290a1e00579090767b2c5c42633e8e2534250dd54e4846e9`

## Acceptance results

Python 3.12; Numscript v0.0.25. Dependencies are declared in requirements-dev.txt
and the existing observatory requirements. No current assertion was weakened to
hide a failure. The exact-nine/twelve-dimension assertions were intentionally
replaced by explicit full inventory and thirteen-dimension checks.

```text
M5_REQUIRE_NUMSCRIPT=1 PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -m pytest -q -p no:cacheprovider tests reference-implementation/provider-neutral-governor/tests shadow-m5index/tests sec-public-input/observatory/tests
387 passed in 2.15s

.venv/bin/python shadow-m5index/scripts/validate_records.py
Validated 36 SHADOW asset records.

.venv/bin/python tools/check_public_release.py
PASS: repository JSON/schema, duplicate schema IDs, targeted secret/PII
patterns, generated junk, manifest coverage and checksums.

git diff --check
PASS: no output.
```

The complete run includes local Markdown-link validation, all current default
regressions, SHADOW seed tests and SEC observatory tests. Complete CI now runs
the same gate on every PR. Manifest regeneration occurs after final edits and
cleanup; the manifest excludes itself, as in the existing repository process.

## Requirement coverage

| Requirement | Evidence |
| --- | --- |
| Thirteen dimensions; explicit v1 migration; HOLD/REJECT and rollback | Migration guide, preserved v1 fixtures, handoff migration test |
| Multiple independently evidenced namespaces; distinct UN/NYC/NYS roles | Jurisdiction v2 schema and resolver tests |
| Technical control and external IDs cannot grant authority | Namespace basis constraints, issuer/source crosswalk tests |
| Free-public and local-only contradictions rejected | Event/commerce/request conditionals and negative tests |
| Provider delegation, standing, capabilities, credentials, approval | Provider schemas, action authorization and resolved evidence tests |
| Model confidence and successful payment cannot bypass policy | Replacement-provider and gate tests |
| CloudEvents attribute/source compatibility | Pinned 1.0.2 naming; URI-format dependency and test |
| Every metered catalog entry resolves; synthetic receipts generated | Entire catalog integration test, selector and valuation checks |
| Tier I excluded from service metering; local price zero | M5-AIMARKET-001, baseline schema, no-meter/no-receipt test |
| M5-Eve activation, expiry, suspension, live revocation | Activation schema and tests; resolver consulted each action |
| Existing function namespace respected | Public function-reference and M5CANON-as-capability rejection tests |
| Orbitalys cannot grant authority | authority_effect NONE constant and rejection test |
| Version pins and local artifact hash | Receipt schemas and latest rejection tests |
| M3/M4 links and titleholders retained | Transaction v2 schema and negative tests |
| Idempotency, conflicting replay, append-only correction resolution | Synthetic consumer and prior-event tests |
| Baseline survives account/provider loss; diagnostics optional | Baseline contract rejection tests; deployment evidence separately required |
| Optional paid escalation, scope, budget, expiry | Consent helper and tests; no real purchase or settlement |

## Public/private and maturity boundary

This patch contains public standards, schemas, synthetic examples and public
conformance fixtures. It does not deploy M5BOM accounts, run a device model,
issue credentials, verify production signatures, grant namespace authority,
connect a payment rail, or expose private M5Canon/M5POD material.

All real-name namespace examples remain UNRESOLVED. ESTABLISHED fixtures exist
only inside synthetic tests. Trusted resolver observations are test doubles,
not an implementation of authoritative source verification. Production needs
trust roots, authenticated evidence, current revocation, atomic execution,
durable deduplication, and device/runtime conformance evidence.

Laya/Jev/API/license pins remain deployment prerequisites. Synthetic version
strings must not be mistaken for reviewed production versions. External
references retain their native provenance and reference-only maturity where
not independently profiled. No provider partnership or certification is claimed.

The targeted secret/PII scanner covers specified token/private-key patterns,
SSN-shaped strings and assigned sensitive identifiers in repository text. It
is not a universal personal-data detector, git-history audit or binary OCR.
This patch adds/changes text artifacts, not private member records or binaries.
Existing public-source content is preserved. Scan tests exercise detection.

The ICSN research, crypto RFC, hardware follow-up, ECE launch and ecosystem audit
are separate jobs, not silently included or represented as completed here.
No automatic merge is authorized. Post-merge audit evidence must reference the
actual merged SHA and tests when a maintainer eventually merges this work.

## Changed-file inventory

- `.github/ISSUE_TEMPLATE/m5-openapi-early-access.yml`
- `.github/workflows/commons-conformance.yml`
- `LICENSE.md`
- `MANIFEST.sha256`
- `README.md`
- `docs/COMMONS-BASELINE-VALIDATION-2026-09-23.md`
- `docs/EXTERNAL-REFERENCE-REVIEW-2026-09-22.md`
- `docs/JEV-HOSTED-SYSTEM-ONE-PROFILE.md`
- `docs/LAYA-LOCAL-SYSTEM-ONE-PROFILE.md`
- `docs/M5-CANONICAL-CONTEXT-V1-V2-MIGRATION.md`
- `docs/M5-CONFORMANCE-AND-NAMESPACE-BOUNDARIES.md`
- `docs/M5-CREDENTIAL-TRUST-AND-JURISDICTION-BINDING.md`
- `docs/M5-EVE-CREDENTIALED-ACTIVATION-ARCHITECTURE.md`
- `docs/M5-INTELLIGENCE-ROUTER-AND-M5POD-RUNTIME.md`
- `docs/M5-OPENAPI-EARLY-ACCESS-AND-DEMAND-PILOT.md`
- `docs/M5-OPENAPI-METERING-X402-COMMERCE.md`
- `docs/M5-PROVIDER-ACCOUNT-STANDING-AND-ENDPOINT-PROFILE.md`
- `docs/M5-REFERENCE-PRICING-AND-DEMAND-MEASUREMENT.md`
- `docs/M5-TRANSACTION-FOOTPRINT-AND-ECONOMIC-CLASSIFICATION.md`
- `docs/M5BOM-ACTIVATION-AND-SOVEREIGN-BASELINE.md`
- `docs/OPEN-STANDARDS-EVIDENCE-REGISTRY.md`
- `docs/ORBITALYS-EVENT-THREAT-PLANE.md`
- `docs/README.md`
- `examples/README.md`
- `examples/m5-action-authorization.example.json`
- `examples/m5-bom-sovereign-baseline.example.json`
- `examples/m5-canonical-context-envelope.example.json`
- `examples/m5-commerce-receipt-laya-local.example.json`
- `examples/m5-credential-trust-record.example.json`
- `examples/m5-eve-activation.example.json`
- `examples/m5-event-envelope.example.json`
- `examples/m5-intelligence-request-laya-local.example.json`
- `examples/m5-intelligence-routing-receipt-laya.example.json`
- `examples/m5-jurisdiction-binding.example.json`
- `examples/m5-service-event-manifest.example.json`
- `examples/m5-sovereign-provider-endpoint.example.json`
- `examples/m5-transaction-footprint-property.example.json`
- `examples/orbitalys-threat-vector.example.json`
- `examples/provider-plugin-manifest.example.json`
- `m5-eve/README.md`
- `m5-openapi/README.md`
- `m5-openapi/metering/meters.example.yaml`
- `m5-openapi/pricing/catalog.example.json`
- `m5-openapi/pricing/reference-catalog-v1.example.json`
- `m5-openapi/providers/README.md`
- `m5-openapi/providers/provider-cost-catalog.example.json`
- `m5-pod/runtime/laya.profile.example.json`
- `reference-implementation/commons-contracts/README.md`
- `reference-implementation/commons-contracts/contracts.py`
- `requirements-dev.txt`
- `schemas/README.md`
- `schemas/m5-action-authorization.schema.json`
- `schemas/m5-bom-sovereign-baseline.schema.json`
- `schemas/m5-canonical-context-envelope.schema.json`
- `schemas/m5-commerce-receipt.schema.json`
- `schemas/m5-credential-trust-record.schema.json`
- `schemas/m5-eve-activation.schema.json`
- `schemas/m5-event-envelope.schema.json`
- `schemas/m5-intelligence-request.schema.json`
- `schemas/m5-intelligence-routing-receipt.schema.json`
- `schemas/m5-jurisdiction-binding.schema.json`
- `schemas/m5-service-event-manifest.schema.json`
- `schemas/m5-sovereign-provider-endpoint.schema.json`
- `schemas/m5-transaction-footprint.schema.json`
- `schemas/orbitalys-threat-vector.schema.json`
- `schemas/provider-plugin-manifest.schema.json`
- `standards/M5-AIGOV-001.md`
- `standards/M5-AIMARKET-001.md`
- `standards/M5-AIMOD-001.md`
- `standards/M5-AIPROV-001.md`
- `standards/M5-AISPACE-001.md`
- `standards/M5-EVENT-001.md`
- `standards/README.md`
- `tests/README.md`
- `tests/fixtures/canonical-context-v1.example.json`
- `tests/fixtures/canonical-context-v1.schema.json`
- `tests/test_commons_handoff.py`
- `tests/test_m5_bom_baseline.py`
- `tests/test_m5_commerce_schemas.py`
- `tests/test_m5_eve_activation.py`
- `tests/test_m5_event_plane_v3.py`
- `tests/test_public_release_scans.py`
- `tests/test_schemas.py`
- `tools/check_public_release.py`
