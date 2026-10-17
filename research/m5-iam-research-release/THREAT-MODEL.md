# Threat Model

Scope: the free M5 IAM research release v0.2.0 running on one person's
computer. Out of scope: registration, credential issuance, anchoring, payment
and agent delegation, none of which this release performs.

## Assets

- The person's attestation and pod files (name, chosen state chain, optional contact).
- The integrity of the record: that what the person stated is what is stored.
- The person's privacy: nothing about them leaves the device.

## Trust boundaries

1. The person's operating-system account and disk.
2. The local app on `127.0.0.1` and the browser that talks to it.
3. The downloaded package, before it is opened.

## Threats and mitigations

| # | Threat | Mitigation in this release | Residual risk | NIST SP 800-53 |
| --- | --- | --- | --- | --- |
| T1 | Another website in the person's browser tries to create a pod or read state through the local app (CSRF, DNS rebinding) | App binds to 127.0.0.1; rejects any Host other than the loopback name; the form endpoint requires the app's own Origin and `application/json`; no route serves pod files | A process already running as the same user can still call the app | SC-7, AC-3 |
| T2 | Other user accounts on the computer read the pod | Files are created owner-only (0600, folders 0700) on POSIX | Administrators, and Windows (no POSIX permissions applied), are not covered; full-disk encryption is recommended | AC-3, AC-6, SC-28 |
| T3 | Someone edits the stored attestation | `verify` recomputes the hash chain and every recorded digest and reports any change | An attacker with write access can rewrite the whole chain consistently: the ledger detects change, it does not prevent it, and it is not a signature | SI-7 |
| T4 | One person creates many identities (Sybil) | None. The attestation is self-asserted by design | **Self-attestation provides no Sybil resistance.** Uniqueness and liveness require a separate verification step, which this release does not perform | IA-12 |
| T5 | Someone attests in another person's name | None beyond the statement's wording | The name is unverified and is labelled so everywhere it appears | IA-12 |
| T6 | The downloaded package is altered in transit or on a mirror | Published SHA-256 for the ZIP and per-file checksums; deterministic build lets anyone rebuild and compare | No code signing yet; a person who skips the checksum step is not protected | SI-7, CM-14 |
| T7 | Personal data leaks through the registry entry | Only a commitment hash is produced; it includes a random 122-bit identifier, so it cannot be matched by guessing; nothing is transmitted | If anchoring is added, the commitment design must be reviewed again | SC-28 |
| T8 | The app or engine makes unexpected network calls | Standard library only; tests assert the engine imports no network modules and the app binds to loopback; the page's Content Security Policy allows connections to itself only | Links to tool publishers open in the browser when the person clicks them | SC-7 |
| T10 | A sample certificate is mistaken for an issued one | Every certificate is stamped SAMPLE · NOT ISSUED · NOT ANCHORED; the IAM certificate file records `status: SAMPLE_NOT_ISSUED` and `issued_by: null` | A screenshot could be cropped to remove the stamp | SI-7 |
| T11 | The sample support panel is taken for a live payment, or a gift is routed to someone posing as the developer | No payment is possible in this release; the panel is labelled sample and no value moves. In the design, developer gifts go only to a payee whose Sigstore signing identity has been matched to a verified M5-CV payee | Matching a signing identity to a payee is a manual verification step that must exist before giving opens | IA-2, IA-5 |
| T12 | A provider is wrongly flagged as over-charging a ZIP, or a flag is read as an accusation | In this release all providers, rates and ZIPs are labelled samples. In the design, a flag states only published, comparable rate data from the M5Index and links to the provider's registry entry | Live listings need a documented method, a correction process and legal review before launch | AU-10, SI-7 |
| T13 | A selected right to refuse consent is taken as active, or ignored, before credentials are verified | The record says `SELECTED_NOT_ACTIVATED` and `activated: false` everywhere it appears; CYRUS acceptance and every change are ledgered and checked by `verify` | Nothing enforces the refusal on an IAM. Enforcement starts when credentials are verified, through the registered account and the agent runtime | AC-3, PT-4 |
| T9 | Optional contact (email or phone) is exposed | Stored only in the local pod; never transmitted | Stored unencrypted inside the pod; protection relies on T2 and disk encryption | SC-28 |

## Assumptions

- The person's operating system and browser are not already compromised.
- Python on the computer is genuine.

## Not claimed

No certification, audit or compliance is claimed. NIST identifiers show which
control each mitigation relates to.
