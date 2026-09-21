# M5-RICARDIAN-TRIPLE-LAYER-001 — Ricardian Contract Binding and Execution

**Status:** Draft for Public Comment

## 1. Scope

This standard defines the three mandatory layers of an M5 Ricardian contract and the binding, authority, execution, settlement, and receipt rules between them. “MUST”, “MUST NOT”, “SHOULD”, and “MAY” are normative.

## 2. The three layers

Every conforming M5 Ricardian contract MUST contain or reference:

1. **Human controlling terms** — the human-readable agreement, identities and capacities of the parties, rights, duties, conditions, governing authority, signatures, amendment rules, dispute process, and legal source of truth.
2. **Machine policy and evidence** — a deterministic representation of the authorized terms, participants, credentials, delegations, restrictions, states, conditions precedent, approvals, evidence, privacy classes, and conflict rules.
3. **Executable instructions** — bounded code or declarative programs that can prepare and route permitted actions through named adapters and authoritative systems of record.

All three layers MUST share a contract identifier and MUST identify their own artifact identifier, version, content digest or digest manifest, URI, and explicit supersession history. A digest MUST cover the exact bytes resolved by its declared URI. A package binding MUST identify and hash a canonical manifest that, in turn, identifies and hashes every member. The executable layer MUST identify the exact human-terms and machine-policy versions it implements.

## 3. Authority and conflict rule

Executable code MUST NOT create legal authority, consent, title, standing, a license, a regulated status, a payment obligation, or a right not established by the controlling terms and authoritative sources.

Where layers conflict:

- authoritative law, official records, executed instruments, and authorized human or institutional acts control their legal domains;
- human controlling terms prevail over an inconsistent machine representation;
- machine policy MAY narrow execution but MUST NOT silently broaden human-granted authority;
- executable instructions MUST fail closed and route the conflict to authorized review; and
- correction MUST create a versioned, attributable record rather than overwrite history.

## 4. Mandatory execution gates

Before a consequential instruction, the executable layer MUST verify:

1. principal identity;
2. current standing or credential;
3. bounded delegation;
4. transaction and jurisdiction context;
5. deterministic policy decision;
6. required accountable human, professional, fiduciary, or institutional approval; and
7. instruction binding, idempotency, expiry, revocation, and evidence freshness.

A probabilistic model MAY classify, summarize, score, or route. It MUST NOT satisfy a deterministic authority or approval gate.

## 5. Settlement and adapters

Ledger programs such as Numscript MAY model deterministic, atomic movements inside their ledger boundary. Payment protocols such as x402 MAY negotiate, authorize, verify, and settle a supported network payment. Neither property establishes atomicity across an external bank ledger, blockchain, custodian, escrow, transfer agent, or public record.

Cross-system settlement MUST use bounded provider adapters and a recoverable state machine that distinguishes reservation, verification, approval, commit, finality, destination confirmation, reconciliation, correction, reversal, and exception hold. The authoritative bank, escrow, custody, chain, issuer, transfer-agent, or other provider record controls its own domain.

Adapters MUST declare provider identity, regulated role where applicable, environment, endpoint and asset allowlists, signer or credential scope, amount and fee ceilings, finality, timeout, replay and idempotency controls, cancellation semantics, reconciliation method, emergency pause, and evidence output.

## 6. M5-x402 profile

An M5-x402 profile MUST preserve the x402 core version, scheme, network, asset, amount, recipient, timeout, payload, verification, and settlement semantics. M5 terms MUST be carried as a versioned extension rather than silently changing core x402 fields.

The extension MUST bind:

- Ricardian contract ID, version, and human-terms digest;
- machine-policy ID, version, and digest;
- executable-plan ID, version, language, and digest;
- principal, role, credential, delegation, approval, and evidence references;
- the applicable versioned M1–M5 taxonomy and internal asset classification, separately from external legal classification;
- source and destination economic context and a versioned jurisdiction-authority graph;
- account context, human principal, credential, delegation, mandate, and revocation state;
- institution-specific routing functions and required actions without treating every institution as an approver;
- privacy/access policy and access-log requirements;
- payment identifier and normalized request fingerprint; and
- receipt, correction, supersession, and reconciliation references.

A standard x402 facilitator verifies and settles supported payment mechanics. It does not thereby verify M5 legal authority, professional judgment, off-chain bank finality, or the truth of extension claims. An M5-aware resource server MUST enforce those gates independently and MUST NOT present an unsupported custom network or asset as interoperable with a standard facilitator.

## 7. Token and representation rule

A conforming contract MUST identify every token, credential, digital twin, controllable electronic record, ledger asset, and settlement asset as a separate typed object.

A token MAY exist with:

- `valuation_status: NO_ASSIGNED_MONETARY_VALUE`;
- `transferability: NON_TRANSFERABLE`;
- `redeemability: NONE`;
- `fee_title_effect: NONE`;
- `security_or_investment_rights: NONE_UNLESS_SEPARATELY_CREATED`; and
- `settlement_eligibility: NOT_A_SETTLEMENT_ASSET`.

Issuing or recording a quantity of such a token MUST NOT be described as assigning a price, investment value, title interest, repayment right, governance right, or redemption value. Any later right or value requires a separately authorized instrument, policy version, classification review, and execution path.

A no-value project token MUST NOT be substituted for the payment asset in an x402 requirement. The x402 payment asset and amount remain explicit settlement terms.

## 8. Receipts and privacy

Every material transition MUST produce an attributable receipt containing the contract and policy versions, exact M5Canon function identifiers and matching canonical URIs, implementation version, instruction digest, actor and authority references, approvals, adapter/provider references and their distinct functions, prior and resulting states, timestamps and ordering anchor, exceptions, reconciliation status, field-level access policy and access-log references, and either a previous-receipt digest or an explicit genesis marker.

Receipts MUST distinguish simulation from production and observed facts from estimates or modeled outputs. Public receipts MUST NOT expose private keys, raw bank credentials, identity documents, unnecessary personal data, protected KYC/KYB evidence, or security-sensitive infrastructure details.

## 9. Simulation conformance

A public simulation MUST declare `synthetic: true`, `authority_effect: NONE`, `network_write: false`, and `financial_movement: false`. Mock signatures, provider proofs, ledger postings, x402 payloads, tokens, approvals, and receipts MUST be visibly synthetic and MUST NOT satisfy production gates.
