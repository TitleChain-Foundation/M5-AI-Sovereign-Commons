# Threat Model

**Status:** Draft for Public Comment  
**Scope:** M5 AI Sovereign Commons specifications and non-production reference
implementations

## 1. Security objective

The system must prevent a model, agent, provider, plugin, credential, wallet,
namespace, endpoint, sensor, or automation from becoming the source of its own
authority.

Consequential actions must fail closed unless M5Canon can verify the accountable
principal, current credentials and standing, applicable jurisdiction, explicit
delegation, deterministic policy, required accountable approvals, and evidence
receipt.

## 2. Protected interests

- human safety, dignity, autonomy, and consent;
- identity, credentials, affiliations, and private M5POD records;
- legal-entity, governmental, Tribal, territorial, and institutional boundaries;
- title, ownership, beneficial-interest, and provenance records;
- money, value instruments, assets, securities, and settlement instructions;
- source artifacts, model artifacts, provider identities, and endpoints;
- budgets, usage records, audit evidence, and governance receipts;
- sensor, spatial, biometric, health, neural, and experiential data;
- physical actuators, robots, vehicles, devices, and infrastructure.

## 3. Trust boundaries

The following must remain separate:

- accountable principal versus delegated actor;
- personal, shared, business, institutional, governmental, and sovereign account
  contexts;
- M5Canon deterministic controls versus M5AGT supporting capabilities;
- private M5POD evidence versus public review material;
- provider identity versus model or endpoint identity;
- model memory or weights versus member evidence and records;
- observation versus derived feature, inference, reconstruction, simulation,
  human assertion, and authoritative record;
- internal M1-M5 classification versus external legal classification;
- instrument identity versus denomination, valuation, and settlement method.

## 4. Threats and required mitigations

| Threat | Required mitigation |
| --- | --- |
| Prompt, tool, document, or retrieval injection | Treat all content as untrusted; allowlist tools; isolate instructions from evidence; require policy checks at the side-effect boundary |
| Agent self-authorization | Reject agent-supplied authority; require a current principal, delegation, and accountable approval |
| Principal or account-context confusion | Bind every action to one explicit principal and account context; prevent BOM, BOU, BOB, BOI, and BOG privilege bleed |
| Credential theft, staleness, suspension, or revocation | Verify issuer, proof, scope, status, time, jurisdiction, and revocation at decision time |
| Delegation expansion | Match exact purpose, action, instrument, data, system, jurisdiction, amount, duration, and prohibited uses |
| Canonical context-envelope tampering | Sign or integrity-protect the envelope; verify schema, issuer, version, digest, freshness, and replay constraints |
| Classification used as permission | Keep classification independent; require the Six-Gate authority decision |
| Malicious or substituted provider | Verify provider identity, enrollment state, endpoint binding, TLS and redirect policy, artifact digest, and revocation status |
| Model or dependency poisoning | Pin and verify artifact revisions, digests, provenance, licenses, software bills of materials, and evaluation evidence |
| Budget or ledger bypass | Check projected spend; reject malformed, missing-required, negative, non-finite, or temporally ambiguous records |
| Data exfiltration or cross-context leakage | Minimize data; apply purpose and residency controls; separate tenants and contexts; redact public evidence |
| Cross-border or jurisdictional leakage | Resolve the applicable-authority graph; enforce transfer, residency, and disclosure policy before data movement |
| Sensor or experiential overreach | Require informed, specific, revocable consent; minimize collection; distinguish observation from inference |
| Simulation or synthetic output presented as fact | Label provenance class; prohibit promotion to authoritative record without accountable verification |
| Unsafe physical action | Require actuator-specific authorization, safety interlocks, limits, human stop controls, and post-action evidence |
| Governance-log privacy leakage | Store minimal references and digests; restrict sensitive evidence; separate public proof from private content |
| Receipt replay or equivocation | Use unique request IDs, timestamps, nonces where applicable, policy versions, chained integrity evidence, and append-only correction records |
| Denial or suppression of correction | Preserve historical truth, correction authority, reason, time, and superseding state without destructive overwrite |
| Misleading provider, agency, or standards-body claim | Require authoritative relationship evidence and explicit non-endorsement status |

## 5. High-risk action classes

Stronger credentials, approvals, and segregation of duties are required for:

- money or value issuance;
- stablecoin, CBDC, or tokenized-deposit operations;
- securities and financial wrappers;
- title or beneficial-interest changes;
- transfer, redemption, burn, freeze, or administrative control;
- identity, credential, consent, or rights-state changes;
- health, biometric, genetic, neural, or experiential-data use;
- physical or cyber-physical action;
- governmental, Tribal, territorial, institutional, or regulated workflows.

## 6. Failure behavior

Missing, malformed, expired, revoked, altered, contradictory, disputed, or
out-of-scope evidence must produce denial or an explicit unresolved state.

Implementations must not:

- guess missing authority;
- convert an unresolved status into approval;
- accept a model's confidence as evidence;
- continue on a stale cached decision where re-evaluation is required;
- silently skip malformed ledger or audit records;
- return a success-shaped result after an enforcement failure.

## 7. Reporting and public review

Public issues must not contain credentials, secrets, private M5POD evidence,
regulated personal data, production endpoints, or unpatched exploit details.

A verified private security-reporting destination must exist before the
repository is made public. Receipt and incident examples used in public review
must be synthetic.

## 8. Residual risk

Schemas and reference tests can demonstrate structural conformance only. They do
not prove legal compliance, secure deployment, accurate external authority,
correct model behavior, hardware safety, provider enrollment, or production
readiness.
