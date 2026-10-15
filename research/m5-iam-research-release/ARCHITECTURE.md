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
    consent/consent.json     two separate choices, both REFUSED unless approved
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
`network_write: false` and `financial_movement: false`. The machine record
reserves signature slots for the holder and for an approved agency that later
verifies the IAM through M5-x401 (`RESERVED_NOT_SIGNED`; nothing is signed in
this release). `verify` recomputes the
ledger chain and every recorded digest and fails closed on any difference.

## Consent

Activation records two separate choices in `consent/consent.json`, each
`APPROVED` or `REFUSED`, and both default to `REFUSED`:

- **Record sharing:** whether the IAM record may be shared beyond the device.
- **Agent access (CYRUS Protocol):** whether agents the holder chooses may read
  the pod and assist. Approval never lets an agent act, pay, sign or
  authorize: an IAM-only pod has `can_authorize: []`.

The human terms state that refusal is the default. The holder can change
either choice at any time, in the app or with `m5_iam.py consent`. Each change
is appended to the file's history and to the ledger (`CONSENT_RECORDED`,
`CONSENT_CHANGED`), so `verify` detects any edit made outside the tool.

## Registry entry (simulated)

`registry/registry-receipt.json` carries a real SHA-256 commitment over the
contract identifier and the three parts, a reference derived from it, and a
sample block number. It is marked `SIMULATED_NOT_ANCHORED`. The contract
identifier contains a random 122-bit local identifier, so the commitment cannot
be confirmed by guessing a name and state chain. At launch, only this
commitment would be anchored.

## Sample certificates

After activation the app shows three kinds of sample Certificate of Title, in
the M5Ledger certificate design, each stamped **SAMPLE · NOT ISSUED · NOT
ANCHORED**:

| Certificate | Subject | Where it comes from |
| --- | --- | --- |
| IAM origin | The person's IAM account | `registry/certificate-iam-origin.json`, written to the pod and recorded in the ledger; carries the registry commitment |
| Software license | Any free tool in the catalog | Generated on screen from the catalog entry; records the tool's SPDX license and states that the license is granted by its makers, not by the certificate |
| Licensed service | A paid service (sample: Element plan) | Generated on screen; shows both paths: an existing customer shows proof of the plan, a new customer pays the provider directly through M5-OpenAPI |

Under each software certificate, an **optional support** panel (sample, no
value moves) lets the person set an amount and a schedule (one time, per hour,
day, week, month or year) for two separate gifts:

- **The developers,** paid directly once their Sigstore release signature is
  matched to a verified payee: their own wallet, or the M5 entity account they
  contribute through.
- **Pay it forward to TitleChain Foundation,** directed to the TitleChain
  Sovereign Purpose Trust for its mission. Off unless chosen.

Gifts are never part of a fee split and the software stays free either way.
Terms, payment rails and protection rules are in the separately published fine
print.

### Previews of what opens later (samples)

- **Purchase protection** under the paid-service certificate: optional, from
  credentialed providers only, sorted by price, with each provider's fee, its
  rate in the member's ZIP and the commons median for that ZIP.
- **Reputation:** none at IAM. A person's reputation is their M5Nash Score,
  which starts with Bank of Me and grows with giving, paying it forward,
  completed classes and time and talents given to the community; entity
  accounts build their own scores.

No certificate is issued by this release. A Certificate of Title is issued by
the TitleChain Registry only after launch.

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
