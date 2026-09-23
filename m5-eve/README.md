# M5 Eve Member Workspace

**Status: PR-1 architecture and fail-closed reference controls. No hosted member service is deployed by this repository.**

M5 Eve is the proposed member-facing conversational workspace for navigating M5 account contexts, public evidence, bounded project workflows, and approved tools. It is designed to begin with an accountable M5HUM or lawful entity and extend through independently authorized BOM, BOU, BOB, BOI, and BOG contexts.

> A chat login authenticates access to a workspace. It does not establish identity, membership, eligibility, legal capacity, role, delegation, funding, approval, title, or transaction authority.

## Start here

| Artifact | Purpose |
| --- | --- |
| [Architecture and activation blueprint](M5-EVE-MEMBER-WORKSPACE-BLUEPRINT.md) | Account hierarchy, trust boundaries, deployment modes, phased delivery, and Spring Commons mapping |
| [Default-deny deployment profile](deployment-profile.example.json) | Machine-readable example with all consequential capabilities disabled |
| [Eve template deployment guide](templates/eve-chat/README.md) | Safe upstream clone path, environment variables, licensing, and production upgrade boundary |
| [Reference authority adapter](reference/adapter.py) | Deterministic preflight policy for context, delegation, scope, approvals, and capability flags |
| [Reference tests](../tests/test_m5_eve_adapter.py) | Fail-closed cases and the bounded Spring Commons review path |

## Account model

```text
accountable principal
→ verified identity and standing
→ selected M5 account context
→ current lifecycle state
→ explicit delegation and policy
→ required co-approvals
→ deterministic preflight decision
→ bounded assistant action
→ evidence receipt
```

The workspace treats these contexts as distinct:

- **BOM** — member/person context;
- **BOU** — independently bounded project or operating-unit context;
- **BOB** — business/organization context;
- **BOI** — institution/instrument context; and
- **BOG** — government/public-authority context.

A parent/child navigation relationship is not inherited authority. A BOM member may see a BOU only when an accountable institution has granted that access. The member may act only under a separate current delegation for the requested capability, scope, jurisdiction, and effective period.

## Deployment choices

The upstream [Vercel eve Chat Template](https://github.com/vercel/eve/tree/main/apps/templates/eve-chat-template) is Apache-2.0 software and provides a useful interface/runtime starting point. This repository does not vendor or silently fork it.

- **Starter/password mode:** one trusted operator, shared principal, browser-local history. Suitable only for private evaluation—not member rollout.
- **Production identity mode:** per-user Sign in with Vercel, Neon history, Upstash rate limiting, and optional private Blob memory. This improves application authentication and persistence but still does not establish M5 authority.
- **M5-integrated mode:** production identity plus verified M5 context, current authorization/delegation, M5Canon preflight, capability registry, receipts, revocation, human approval, and source-of-truth reconciliation.

Anyone may clone the upstream template, but an installation must not display itself as an authorized M5 member workspace unless the implementation, operator, authority, jurisdiction, policies, and evidence have reached an attributable `AUTHORIZED` lifecycle state.

## Spring Commons initial use

For `PPT-EZ-CA-0001`, M5 Eve may initially support public-source research, SEC-comment comparison, GSA/NPS checklist navigation, draft preparation, unresolved-evidence routing, and readiness reporting.

The default profile disables funding, signature, submission, procurement, construction, title, bank, settlement, and production-record actions. Spring Commons remains `HOLD`, with external requirements `PENDING_EXTERNAL` and authority effect `NONE`.

## Naming recommendation

Use **M5 Eve Member Workspace** for the capability and **M5 Eve** for the interface. Avoid “M5-evechat” as the primary name: “workspace” reflects governed records, projects, approvals, and tools rather than implying that a chat session itself is the authority plane.

## Public contribution boundary

Cloners may inspect, adapt, and test the architecture. They must:

- preserve upstream license and attribution requirements for any copied Eve code;
- identify modifications and the accountable operator;
- keep secrets and private M5POD material out of repositories and public chat;
- publish capability and authority states accurately;
- fail closed when context, delegation, evidence, approval, or provider state is missing; and
- avoid implying TitleChain Foundation, Vercel, a provider, agency, or regulator authorizes or endorses their deployment.

## Featured provider and sovereign baseline

Eve is the Jev chat experience selected for the first featured integration.
M5-Eve remains open to other providers; model/chat choice never changes the
principal or grants authority. The Vercel template above retains its separate
source attribution and does not prove vendor identity or API compatibility.
See the [M5BOM baseline](../docs/M5BOM-ACTIVATION-AND-SOVEREIGN-BASELINE.md) and
[activation schema](../schemas/m5-eve-activation.schema.json).
