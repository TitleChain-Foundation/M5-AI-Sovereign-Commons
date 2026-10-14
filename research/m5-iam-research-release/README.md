# M5 IAM Free — Research Release v0.2.0

**Publisher:** TitleChain Foundation · **Status:** research release, draft for public review · **Date:** 2026-10-13

This is the citable landing page for the free M5 IAM research release. It
collects the source code, license, installation instructions, architecture,
threat model, automated tests, a reproducible demonstration, the
pre-publication privacy check, and the evidence record of the Foundation's
related standards work.

## What the release does

A person downloads one ZIP, opens a local app, and attests to their humanity in
one short form. The app creates an IAM starting pod on their own computer: the
attestation in three matching parts (human-readable terms, machine-readable
record, executable check), a hash-chained ledger, a simulated TitleChain
Registry entry that holds only a commitment hash, and a sample Certificate of
Title for the IAM origin. It then shows what the person
has, free and open tools they can use, and the registered accounts they could
open later. Nothing is sent over the network.

The research question it supports: can a human-rooted identity origin be
created, held and checked entirely on a device the person controls, with only
a non-identifying commitment ever leaving that device?

## Contents

| Item | Where |
| --- | --- |
| Source code | [`reference-implementation/m5-iam-free/`](../../reference-implementation/m5-iam-free/) |
| License | [`LICENSE.md`](../../LICENSE.md): Apache-2.0 for code and tests, CC-BY-4.0 for documentation |
| Installation | [`INSTALL.md`](INSTALL.md) |
| Architecture | [`ARCHITECTURE.md`](ARCHITECTURE.md) |
| Threat model | [`THREAT-MODEL.md`](THREAT-MODEL.md) |
| Automated tests | [`tests/test_m5_iam_free.py`](../../tests/test_m5_iam_free.py) |
| Reproducible demonstration | [`reference-implementation/m5-iam-free/demo/`](../../reference-implementation/m5-iam-free/demo/) |
| Pre-publication privacy check | [`PRIVACY-CHECK.md`](PRIVACY-CHECK.md) |
| Evidence of related work | [`EVIDENCE.md`](EVIDENCE.md) |
| How to cite | [`CITATION.cff`](CITATION.cff) |
| Member guide | [`m5-pod/iam-free/M5IAM-FREE-PACKAGE.md`](../../m5-pod/iam-free/M5IAM-FREE-PACKAGE.md) |
| Package manifest | [`m5-pod/iam-free/m5iam-package.manifest.json`](../../m5-pod/iam-free/m5iam-package.manifest.json) |

## Reproduce it in three commands

```bash
python3 -m pytest tests/test_m5_iam_free.py -q                     # automated tests
python3 reference-implementation/m5-iam-free/demo/reproduce.py      # same digests on any machine
python3 tools/build_iam_package.py --output-dir dist                # byte-identical ZIP
```

Requirements: Python 3.9 or later, and `pytest` for the tests. The code itself
uses only the Python standard library.

## Launch gate

Counsel approval is required before public launch. The fine print for giving,
payments, purchase protection and the Trust reserve is published separately.

## What this release is not

It does not issue a TCID, verify identity, create an account or a licensed
M5POD, anchor anything to a ledger, move value, or give any authority to act.
The attestation is the person's own statement. The registry entry is a
simulation. Self-attestation alone provides no Sybil resistance; see the threat
model.
