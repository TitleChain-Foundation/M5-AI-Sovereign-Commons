# Validation Report

**Candidate:** M5 AI Sovereign Commons Release Candidate v0.7  
**Status:** Draft for Public Comment  
**Validation date:** September 10, 2026

## Completed checks

| Check | Result |
| --- | --- |
| Eight Draft 2020-12 JSON Schemas and paired synthetic examples | PASS |
| Schema validity, positive examples, required fields, unknown fields, and schema-specific negative cases | 30 tests passed |
| Provider-neutral governor, budget projection, malformed ledger, non-finite values, timestamps, and provider adapters | 49 tests passed |
| Clean-room publication-gate regression suite, including stale-manifest rejection | 10 tests passed |
| Combined public schema, governor, and publication-gate suite | 89 tests passed |
| Isolated deterministic instrument-authority gate plus collectible legacy M5Canon tests | 104 tests passed |
| Python/editor diagnostics for changed authority files | No errors |
| Editor diagnostics for the public pilot and SEC/RFI crosswalk | No errors |
| Relative Markdown links | PASS |
| GitHub standards-feedback issue-form YAML | PASS |
| Quarantined-source SHA-256 collision scan | No collisions |
| Public pilot privacy and regulatory-claim review | PASS; no blocking findings |
| Generated cache and bytecode removal | PASS |
| Exact public candidate and local allowlist inventory | 98 files each |
| Post-publication OpenAI fallback audit | Bearer authorization and SDK-error propagation regressions passed |
| Participation safeguards | Public Code of Conduct added and linked |
| GitHub security hardening | Secret scanning, push protection, vulnerability reporting, Dependabot alerts, and security updates enabled |
| Public navigation | Visual README landing pages cover all nine major public sections |
| Public activation links | Only `m5bank.app` for IAM setup and the root M5POD waitlist are presented as live starting actions |
| Public pilot pipeline | Pilot 001, replication, and national-scale framing added with fixed non-reversible redaction labels |
| Public Pilot Library visuals | Nine-part claims-safe visual sequence rebuilt from reviewed private concepts |

## Architecture decisions represented

- `M5CANON.*` identifies deterministic M5Canon controls.
- `M5CAP.*` identifies bounded supporting capabilities.
- Savant validates provenance and continuity of origin.
- Vionneta records and anchors provenance evidence and attribution.
- Milner protects account identity, knowledge, cognitive, policy, and operational
  boundaries across BOM, BOU, BOB, BOI, and BOG.
- Named roles do not create authority.
- Economic class, account context, Title Container, representation, wrapper,
  jurisdictional security state, USC, S-state, SR-state, external
  classifications, credentials/standing, and provenance remain independent.
- An M4 financial wrapper preserves its underlying M1, M2, or M3 class.
- Instrument lifecycle authorization fails closed.

## What these results do not prove

These checks do not establish:

- production readiness or security certification;
- legal or regulatory compliance;
- provider enrollment, endorsement, or participation;
- governmental, diplomatic, treaty, or sovereign recognition;
- correct operation of a future deployment;
- independent conformance of the new communications or M5POD portability
  profiles.

## Publication authorization

The owner-approved license structure, official license texts, patent boundary,
trademark boundary, final content/privacy review, and private security intake
are present. The accountable owner approved creation of the repository and the
exact first push on September 7, 2026.

`security@titlechainfoundation.org` is documented as the dedicated bootstrap
vulnerability-intake address, and `support@titlechainfoundation.org` is
documented for general help only. External delivery to and acknowledgment from
the security address were confirmed on September 7, 2026. GitHub Private
Vulnerability Reporting, secret scanning, push protection, Dependabot alerts,
and Dependabot security updates are enabled. Secret validity checks and
non-provider-pattern scanning are unavailable on the current repository plan
and remain disabled.

## New public-review profiles

The candidate now includes:

- an Open Standards Evidence Registry that separates formal standards,
  published specifications, guidance, implementations, ecosystems, services,
  M5-authored proposals, and candidate corridors;
- a Solid-aligned M5POD Data Portability Profile for BOM, BOU, BOB, BOI, and
  BOG account contexts;
- a transport-neutral Sovereign Communications Profile covering M5-native,
  federated, P2P/mesh, secure-messaging, collaboration, and standards-based
  media transports.
- a People's Trust Public Conformance Pilot that uses synthetic agricultural,
  food-and-water, and rights-reconstruction archetypes without naming or
  confirming a property, owner, seller, operator, valuation, or transaction;
- an informative Pilot and SEC Request-for-Input Crosswalk grounded in the
  official Federal Register record for Release No. 34-106246, File No.
  S7-2026-30.

These documents are `Draft for Public Comment`. They create requirements and
review questions, not claims of implementation, NIST compliance, Solid
conformance, certification, endorsement, or partnership.

The original 17-file pilot working package and its supporting research are
private review sources. Their files and archive are quarantined and hash
denylisted. They are not public candidate artifacts.

The final public pilot review confirmed that the synthetic scenario preserves
the permanent stewardship commons, isolated project layers, bounded accounts,
credential-before-capability rule, accountable transfer-agent boundary,
agricultural and food-and-water scenarios, historical rights reconstruction,
and reusable conformance controls without confirming a named target,
counterparty, transaction, acquisition, offering, or regulatory endorsement.

## Pre-existing M5Ecosystem test mismatch

The isolated `origin/main` worktree's older `test_m5canon_engine.py` cannot be
collected because it imports `ADJUDICATION_FEE_MAX_BPS` and other interfaces
that are not present in that branch's `core/m5canon_engine.py`. This mismatch
predates the new instrument-authority module. It was not hidden or converted
into a passing result.

The new authority suite and the collectible legacy-migration suite pass
together. The broader historical engine-test mismatch must be reconciled in the
private M5Ecosystem integration review before merging that separate branch.

## Manifest rule

`MANIFEST.sha256` contains the exact candidate file inventory and SHA-256 digest
for every public file except the manifest itself. The local clean-room allowlist
and quarantined-source denylist are intentionally not publication artifacts.
