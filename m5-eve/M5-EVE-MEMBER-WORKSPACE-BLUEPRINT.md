# M5 Eve Member Workspace Blueprint

**Status:** Informative Draft for Public Comment

**Implementation state:** `SPECIFIED` with a tested local policy adapter; not `DEPLOYED` or `AUTHORIZED`

**Initial project:** `PPT-EZ-CA-0001 / 312 Spring Commons`

## 1. Objective

Create a reusable conversational workspace that helps an accountable member navigate public evidence, private approved records, project contexts, decisions, and bounded tools without confusing authentication, account possession, model output, or agent execution with legal authority.

M5 Eve is an interface and delegated workflow assistant. M5Canon remains the deterministic authority-control layer. Official agency, land, court, bank, regulated-provider, governance, and executed-instrument records remain controlling.

## 2. Trust planes

```text
presentation plane
  Next.js chat, accessible UI, session UX

application identity plane
  password preview or per-user OAuth session

M5 identity and context plane
  principal, standing, selected BOM/BOU/BOB/BOI/BOG context

authority plane
  current credential, delegation, jurisdiction, policy, co-approvals

execution plane
  bounded tools; read, draft, submit, sign, move value, or actuate are distinct

evidence plane
  request, decision, source links, output digest, reviewer, receipt, correction
```

No lower plane may infer a higher plane. In particular:

- application login $\ne$ M5 identity;
- M5 identity $\ne$ membership or role;
- membership $\ne$ project access;
- project access $\ne$ delegated authority;
- draft approval $\ne$ legal signature;
- simulated pass $\ne$ external approval;
- wallet/account access $\ne$ payment authority; and
- a model recommendation $\ne$ an attributable institutional decision.

## 3. Account hierarchy

A workspace session has one authenticated application subject and zero or more available M5 contexts. Selection changes the active data/policy boundary; it does not expand authority.

| Context | Intended scope | Activation evidence |
| --- | --- | --- |
| `BOM` | Member-controlled personal workspace | Verified principal, accepted terms/consents, active membership or service state where applicable |
| `BOU` | Project/operating unit such as Spring Commons | Project role appointment, context grant, purpose, scope, term, revocation source |
| `BOB` | Business or organization | Entity identity, current signer/role evidence, governing authority, jurisdiction |
| `BOI` | Institution or instrument | Institution/instrument identity, regulated or contractual role, issue-specific scope |
| `BOG` | Government/public authority | Official institution/office identity and project-specific statutory, delegated, or decision authority |

A context edge records navigation or association only. Action authority requires a separate delegation bound to:

`principal + context + capability + purpose + scope + jurisdiction + effective period + required approvals + revocation state`

## 4. Capability classes

Capabilities are independently enabled. A deployment must never use one general “agent active” switch.

| Class | Examples | Default |
| --- | --- | --- |
| Public read | Read repository, public docket metadata, public project status | Optional allow after source controls |
| Private read | Read approved member/project records | Deny until identity, context, consent, and data policy pass |
| Analyze | Compare evidence, identify gaps, create candidate findings | Deny until bounded sources and output labels are configured |
| Draft | Prepare non-binding summaries, checklists, correspondence | Deny until reviewer and destination controls exist |
| External submit | Send an application, filing, email, or form | Deny; requires explicit transaction-specific approval |
| Legal signature | Execute an agreement or certification | Deny; human/institution-controlled |
| Financial action | Commit, escrow, draw, transfer, subscribe, or settle value | Deny; regulated systems and explicit approvals control |
| Physical action | Site access, procurement award, construction, actuator command | Deny; applicable owner/AHJ/safety authority controls |
| Evidence publish | Publish source metadata, approved report, or receipt | Deny until review, privacy, attribution, and correction controls pass |

## 5. Deterministic preflight

Every consequential request must produce one of:

- `ALLOW` — all configured requirements passed for the exact action;
- `HOLD` — required evidence, approval, context, or capability is incomplete;
- `DENY` — policy prohibits the action or authority is invalid; or
- `ESCALATE` — a named accountable human/institution must decide.

Minimum checks:

1. application session authenticated;
2. principal and selected context verified;
3. context lifecycle is `AUTHORIZED` for the deployment;
4. hierarchy/context grant is current;
5. requested capability exists and is enabled;
6. explicit delegation matches principal, context, capability, purpose, scope, and jurisdiction;
7. delegation is current and not suspended, revoked, expired, or superseded;
8. required approvals are present and current;
9. data access and destination are permitted;
10. output is labeled by evidence/review state; and
11. an attributable receipt is emitted.

Missing information returns `HOLD`; invalid or prohibited authority returns `DENY`. The model cannot alter the decision.

## 6. Eve template mapping

The upstream Vercel template provides UI, chat streaming, session cursors, optional memory, database persistence, rate limiting, OAuth, and optional connectors. Map it as follows:

| Eve surface | M5 use | Required control |
| --- | --- | --- |
| Password starter | Private operator prototype | One trusted operator only; no member rollout |
| Better Auth subject | Application identity | Bind separately to verified M5 principal/context grants |
| Browser/Neon history | Conversation record | Retention, access, correction, export, and deletion policy |
| Blob memory | Convenience profile | Consent, minimization, context partitioning, review/reset; never authority |
| Agent instructions | Behavioral constraints | Versioned and reviewed, but subordinate to deterministic policy |
| Tools/connectors | Bounded capability adapters | Capability-specific delegation, scopes, HITL, receipt, revocation |
| Slack/Notion/Linear/Sentry | Optional external systems | Provider authorization and data classification; no implicit trust |

## 7. Deployment profiles

### Operator preview

Use `EVE_CHAT_PASSWORD` only. It is shared-secret access for one trusted operator; everyone knowing it shares one Eve principal and connection grants. Do not invite independent BOM members.

### Member beta

Require complete production mode:

- Neon database;
- Upstash Redis;
- Better Auth secret;
- Sign in with Vercel client ID/secret and `openid email profile` scopes;
- per-user private Blob memory only if approved; and
- an M5 context/delegation adapter.

Vercel authentication may be replaced later by another approved identity provider, but provider login still remains distinct from M5 standing and authority.

### Institutional/project operation

Add authoritative-source adapters, M5Canon policy, role/credential refresh, approval routing, immutable receipt storage, privacy/security operations, incident response, manual fallback, provider exit, and independent assurance.

## 8. Spring Commons profile

Initial permitted goals:

- monitor the SEC docket and GSA/NPS public sources;
- compare source snapshots and flag candidate changes;
- navigate the fit-gap review and transaction matrix;
- draft non-binding reports, checklists, and questions;
- route unresolved items to accountable reviewers; and
- publish only human-approved public-safe updates.

Initial prohibited effects:

- applicant selection or eligibility determination;
- official submission or certification;
- capital solicitation or commitment;
- proof-of-funds assertion;
- escrow, draw, payment, or settlement;
- deed/title or transfer-agent record mutation;
- procurement, site entry, construction, or physical control; and
- promotion of `SUBMITTED`, `SOURCE_VERIFIED`, or generated text to authoritative truth.

The machine-readable [default deployment profile](deployment-profile.example.json) encodes these defaults.

## 9. Multi-tenant data boundary

Partition data by principal and context. Queries must not rely only on a user-supplied context ID. Resolve access server-side from current grants.

At minimum:

- database rows carry tenant/context ownership;
- every query enforces the authorized context set;
- memory is per principal and, for sensitive workflows, per context;
- connectors use least-privilege grants and context-specific destinations;
- logs redact secrets and protected data;
- public sources are separated from private evidence;
- export/deletion/correction paths preserve required legal holds; and
- cross-context retrieval is denied unless an explicit, reviewable policy permits it.

## 10. Receipts and review state

Each assistant output used in a project workflow should record:

- request and output digests;
- principal and active context identifiers;
- capability and delegation identifiers;
- policy/version and decision;
- model/provider identifier where permitted;
- source identifiers and retrieval dates;
- evidence and human-review state;
- required/received approvals;
- timestamps and effective period; and
- correction/supersession links.

A receipt proves what the system evaluated and produced. It does not prove the underlying claim or confer legal effect.

## 11. Delivery milestones

1. **PR-1 — architecture:** this blueprint, profile, reference preflight, tests, CI, and public navigation.
2. **PR-2 — template fork:** separate application repository based on the Apache-2.0 Eve template, with upstream notices and M5 branding.
3. **PR-3 — identity/context:** production authentication, verified M5 principal binding, context switcher, server-side tenancy.
4. **PR-4 — authority:** delegation registry, M5Canon adapter, approvals, revocation, and receipts.
5. **PR-5 — Spring Commons read/draft pilot:** public-source connectors, evidence bundle, review queue, no external writes.
6. **PR-6 — controlled connectors:** approved project systems with least privilege and human confirmation.
7. **PR-7 — independently reviewed beta:** privacy/security/accessibility testing and bounded member enrollment.

## 12. Launch gates

Do not call the service an authorized member workspace until:

- the operator and data controller are identified;
- terms, privacy, retention, correction, export, and deletion policies are adopted;
- identity proofing and context-grant processes are approved;
- every capability has an owner, policy, scope, and revocation path;
- tenancy and cross-context isolation tests pass;
- human approval cannot be bypassed by prompt, tool, connector, or model output;
- incidents, provider loss, and manual operation are tested;
- accessibility review passes; and
- independent security/privacy review findings are resolved or accepted.
