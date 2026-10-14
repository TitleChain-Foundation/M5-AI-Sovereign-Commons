# Evidence Record

Prepared by TitleChain Foundation on 2026-10-13 for the M5 IAM research
release. Every entry states whose work it is. Where an item is under review,
pending or not public, it says so.

## 1. This release

| Evidence | Status | How to check |
| --- | --- | --- |
| Source, tests and documentation for M5 IAM Free v0.2.0 | Submitted for review in this repository | [`reference-implementation/m5-iam-free/`](../../reference-implementation/m5-iam-free/) |
| Automated tests for the IAM release | Passing at publication | `python3 -m pytest tests/test_m5_iam_free.py -q` |
| Repository-wide test suite and public-release scan | Passing at publication | `python3 -m pytest -q`; `python3 tools/check_public_release.py` |
| Reproducible demonstration with published digests | Matches on the build machine | `python3 reference-implementation/m5-iam-free/demo/reproduce.py` |
| Deterministic package build | Byte-identical across builds (tested) | `python3 tools/build_iam_package.py --output-dir dist` |
| Pre-publication privacy check | Completed; see [PRIVACY-CHECK.md](PRIVACY-CHECK.md) | — |

## 2. LF Decentralized Trust: Proof-of-Control working group

**Relationship:** TitleChain Foundation is a working group participant and
contributor. The Proof-of-Control standard is the working group's work; the
items below are the Foundation's contributions to it. None has been adopted
into the standard at the date of this record.

| Contribution | Authored by | Date | Status |
| --- | --- | --- | --- |
| [Pull request #105](https://github.com/LFDT-ProofOfControl/ov-poc-standard/pull/105): use case and proposal, legal-entity agents under an accountable human | TitleChain Foundation | 2026-10-08 | Open, under review |
| [Issue #106](https://github.com/LFDT-ProofOfControl/ov-poc-standard/issues/106): 5.1.1, resolve actions to the legal entity and the accountable human | TitleChain Foundation | 2026-10-08 | Open |
| [Issue #107](https://github.com/LFDT-ProofOfControl/ov-poc-standard/issues/107): pseudonymity with principal-held linkage and declared disclosure conditions | TitleChain Foundation | 2026-10-08 | Open |
| [Issue #108](https://github.com/LFDT-ProofOfControl/ov-poc-standard/issues/108): principal-exportable verification bundle across provider moves | TitleChain Foundation | 2026-10-08 | Open |
| [Issue #109](https://github.com/LFDT-ProofOfControl/ov-poc-standard/issues/109): publish the rules behind computed values; stamp time-triggered events at their deadline | TitleChain Foundation | 2026-10-08 | Open |

The issues were filed as public comments on Proof-of-Control v0.1. The
commenter disclosed a commercial interest in the M5 implementation and the
related patents in the comment record.

## 3. Membership

TitleChain Foundation has applied for membership of the Linux Foundation and
of LF Decentralized Trust. Both applications are pending at the date of this
record. The Foundation is not yet a member of either.

## 4. Standards used but not contributed to

The release uses or maps to these standards. No membership, contribution,
certification or endorsement is claimed.

| Body | Standard | Use |
| --- | --- | --- |
| Agentic AI Foundation (Linux Foundation) | Model Context Protocol, AGENTS.md | Agent tooling conventions in the wider M5 framework; not exercised by the IAM release |
| x402 Foundation (Linux Foundation) | x402 | Payment conditions in the wider framework; not exercised (the IAM is free) |
| x401 specification (draft) | x401 | Proof requests in the wider framework; not exercised by the IAM release |
| W3C | DIDs, Verifiable Credentials | Target for registered identity; not issued by this release |
| Open Data Institute | Solid | Pod and container layout |
| NIST | SP 800-53 Rev. 5, CSF 2.0 | Control references in the threat model |
| Linux Foundation | SPDX | License identifiers in the tool catalog |

## 5. The Foundation's own public standards work

These are TitleChain Foundation repositories. They are the Foundation's own
publications, not standards adopted by an external body.

| Item | Repository | Status |
| --- | --- | --- |
| [RFC 0002](https://github.com/TitleChain-Foundation/icsn-standards/pull/82): Proof-of-Control profile for legal-entity agents under an accountable human | icsn-standards | Merged 2026-10-08 |
| [M5Canon Six-Gate machine-readable reference package](https://github.com/TitleChain-Foundation/icsn-standards/pull/81) | icsn-standards | Merged 2026-10-08 |
| [Article 12 CER control mapping](https://github.com/TitleChain-Foundation/icsn-standards/pull/78) | icsn-standards | Merged 2026-09-22 |
| [TitleChain Patent Pledge 1.0 and IP policy](https://github.com/TitleChain-Foundation/icsn-standards/pull/85) | icsn-standards | Open |
| [Downloadable M5POD starter package (Norton Ranch Blueprint)](https://github.com/TitleChain-Foundation/M5-AI-Sovereign-Commons/pull/31) | M5-AI-Sovereign-Commons | Merged 2026-10-08 |
| M5-RICARDIAN-TRIPLE-LAYER-001 three-part contract standard | M5-AI-Sovereign-Commons, `standards/` | Published, draft |

## 6. Private repositories

The M5 implementation is developed in private repositories, which are not part
of this public release: the M5Ecosystem source and audit repository, the M5
member application, and the Bank of Me member site. Technical evidence from
them (architecture, audit records, test results) is available to reviewers on
request.
