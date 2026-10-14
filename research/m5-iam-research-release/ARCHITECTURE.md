# Architecture

## Components

| Component | File | Role |
| --- | --- | --- |
| Pod engine | `m5_iam.py` | Creates the pod, writes the three-part attestation, the identifiers, the registry entry and the ledger; verifies and exports. Standard library only, no network calls |
| Local app | `m5_iam_app.py` + `app.html` | Serves one page on `127.0.0.1`, reads the pod state, and accepts the attestation form from its own page only |
| Catalog | `iam-catalog.json` | State chains, free tools (discovery links with licenses) and the registered accounts a person could open later |
| Launchers | `Start M5 IAM.command`, `Start M5 IAM.bat` | Double-click start on macOS and Windows |
| Demonstration | `demo/reproduce.py` | Fixed inputs, published expected digests |
| Package builder | `tools/build_iam_package.py` | Deterministic ZIP with per-file checksums |

## Flow

```text
person ── form (name, state chain, "I am attesting to my humanity") ──▶ local app (127.0.0.1)
                                                                          │ Host, Origin and Content-Type checks
                                                                          ▼
                                                                     pod engine
                                      ┌───────────────────────────────────┼────────────────────────────┐
                                      ▼                                   ▼                            ▼
                         attestation/ (three parts)              registry/ (simulated)          ledger/events.jsonl
                         human-terms.md   (words)                commitment = SHA-256 over      hash-chained record of
                         human-attestation.json (data)           contract id + the three        every file written
                         executable-check.json  (check)          parts; no personal data
```

## Pod layout

```text
M5POD-IAM/
  m5readme.md, m5agent/, m5-iam.html
  M0-M5IAM-000/
    iam.json                 IAM ONLY · self-attested, not verified · free
    attestation/             human terms, machine record, executable check
    identifiers/             local identifier; TCID and others empty until registration
    registry/                simulated TitleChain Registry entry
    receive/                 reserved
    ledger/events.jsonl      append-only, hash-chained
```

Every folder starts with `m5readme.md` and agent tooling lives in `m5agent/`,
so the pod is not tied to a single agent or vendor.

## Three-part record

The attestation follows M5-RICARDIAN-TRIPLE-LAYER-001 (in `standards/`): the
human terms control; the machine record binds the digest of the terms and of
the executable check; the executable check declares `authority_effect: NONE`,
`network_write: false` and `financial_movement: false`. `verify` recomputes the
ledger chain and every recorded digest and fails closed on any difference.

## Registry entry (simulated)

`registry/registry-receipt.json` carries a real SHA-256 commitment over the
contract identifier and the three parts, a reference derived from it, and a
sample block number. It is marked `SIMULATED_NOT_ANCHORED`. The contract
identifier contains a random 122-bit local identifier, so the commitment cannot
be confirmed by guessing a name and state chain. At launch, only this
commitment would be anchored.

## Standards used

| Standard | How it is used here |
| --- | --- |
| Solid (Open Data Institute) | Pod and container layout |
| M5-RICARDIAN-TRIPLE-LAYER-001 | Three-part attestation record |
| x401 (draft) | Not exercised in this release: no proof is requested from a third party |
| x402 | Not exercised: the IAM is free and no payment occurs |
| LF Decentralized Trust Proof-of-Control | Informs the human-at-the-root design; agent delegation is out of scope for IAM |
| W3C DID / Verifiable Credentials | Not issued: the local identifier is not a DID and no credential is issued |
| NIST SP 800-53 Rev. 5 / CSF 2.0 | Threat model controls are referenced by identifier |
| SPDX | License identifiers in the tool catalog |
