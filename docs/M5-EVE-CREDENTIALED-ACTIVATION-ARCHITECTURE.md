# M5-Eve — Credentialed Activation Architecture

**Status: Draft for Public Comment**

## Canonical naming

`M5-Eve` is the credentialed M5 workspace and conversational agent.

The name **Eve** is used by the Jev experience for its chat-agent interface.
Within M5, the implementation is explicitly named **M5-Eve** because it operates
inside the M5 identity, account, credential, delegation, jurisdiction, evidence,
and M5Canon control architecture.

Eve is the Jev chat experience selected as the first featured integration.
M5-Eve is its M5 account-bound integration, open to other providers.

Jev is an intelligence provider/runtime that M5-Eve may use. M5-Eve can also
use Laya, local generative models, hosted frontier models, deterministic code,
and bounded tools according to M5 routing and policy.

## Cognitive architecture

The working M5 cognitive map is:

```text
                    M5-EVE
          credentialed activated interface
                       │
          ┌────────────┴────────────┐
          ↓                         ↓
       MILNER                    LENORE
  cognitive boundary        deliberative thought
  memory / context          reflection / synthesis
  knowledge partition       conscious reasoning
          │                         │
          └────────────┬────────────┘
                       ↓
             M5 INTELLIGENCE ROUTER
                       │
      ┌────────────────┼────────────────┐
      ↓                ↓                ↓
 Laya local         Jev hosted      generative models
 System 1           System 1        local / hosted
      │                │                │
      └────────────────┼────────────────┘
                       ↓
                    M5Canon
         deterministic authority/control
                       ↓
            bounded authorized action
```

## Milner

Milner is the reference cognitive-boundary function for the M5 account.

Milner protects and partitions:

- identity context;
- account knowledge;
- memory;
- private and public evidence boundaries;
- operating context;
- policy context;
- project context; and
- cross-context access.

Milner is not a legal principal and does not create authority.

The existing public M5 function namespace should continue to map Milner to:

`M5CAP.ACCOUNT.COGNITIVE_BOUNDARY.PROTECT.v1`

## Lenore

Lenore is the deliberative-thinking function.

Today, Lenore represents the reasoning layer that can:

- compare evidence;
- reconcile conflicts;
- synthesize;
- reflect;
- explain;
- formulate questions;
- surface uncertainty and blind spots;
- determine when deeper analysis is needed; and
- route unresolved matters toward additional intelligence or human review.

Lenore is also the future research home for CTM-inspired cognitive architecture,
including candidate "brainish" internal representations, competing specialist
processes, attention/broadcast mechanisms, self-checks, counterfactual review,
and blind-spot discovery.

This is an architecture/research description, not a claim that Lenore or any
model is literally conscious or sentient. Any future CTM-inspired implementation
must remain bounded by M5 identity, evidence, privacy, delegation, and M5Canon
authority controls.

## Laya

Laya is the preferred local System 1 decision runtime inside the M5POD for
bounded typed decisions where local policy, capability, privacy, and confidence
permit.

Examples include:

- classification;
- routing;
- boolean probability;
- scoring;
- triage;
- anomaly flags; and
- escalation decisions.

Local Laya under Tier I remains free and unmetered on principal-controlled
hardware. Diagnostics are optional and cannot become access conditions.

## Jev

Jev is an optional hosted System 1 intelligence runtime and also the technology
associated with the Eve chat-agent experience from TypeSafe.

Inside M5, Jev/Eve is the first featured hosted/chat integration. Other providers may
implement the same bounded M5-Eve interface; no provider supplies authority.

Use Jev when hosted System 1 capacity, task fit, scale, latency, or an approved
deployment policy makes it appropriate.

## M5-Eve credential

M5-Eve is a credentialed `M5AGT`, never the principal.

A conforming activation record should be capable of identifying:

```text
agent_id
agent_class = M5AGT
principal_ref
active_account_context
credential_ref
delegation_ref
capability_refs
jurisdiction_binding_refs
effective_at
expires_at
revocation_ref
lifecycle_state
```

M5-Eve authority is always bounded by:

```text
principal
+ account context
+ credential
+ delegation
+ capability
+ purpose
+ scope
+ jurisdiction
+ effective period
+ required approvals
+ revocation state
```

M5-Eve must never infer authority from possession of a chat session, API token,
wallet, model, memory, or account association.

## M5-Eve operating purpose

M5-Eve is intended to become the active internal workspace for:

```text
ASK
INGEST
RECONCILE
ROUTE
ACT
```

The chat transcript is not the system state.

The underlying state should resolve through attributable records:

```text
source
→ document / record
→ claim
→ entity / asset / instrument
→ jurisdiction
→ evidence state
→ event
→ current state
```

This permits M5-Eve to ingest large quantities of data without turning the
workspace into a prompt or chat-history archive.

## Category manifests

M5-Eve should organize operational knowledge through **category manifests**
rather than large prompt packs or one-off chat summaries.

The initial category vocabulary is:

```text
GSA
CRE
FARM
SHADOW
AGENCIES
```

A category manifest describes the durable operating domain. Individual projects,
assets, agencies, documents, and events reference one or more categories.

Examples:

```text
312 Spring Commons
categories: [GSA, CRE]

farmland project / pipeline
categories: [FARM]

SHADOW M5Index research
categories: [SHADOW]

SEC or other public-agency work
categories: [AGENCIES]
```

The manifest should carry machine-readable routing metadata such as:

```text
manifest_id
category
purpose
canonical_source_refs
allowed_data_classes
restricted_data_classes
default_evidence_policy
default_jurisdiction_scope
relevant_capability_refs
current_state_refs
open_question_refs
review_queue_refs
event_stream_refs
```

Projects should not duplicate the category definition. A project points to the
category manifest and carries its own project-specific identifiers, assets,
jurisdiction bindings, evidence, events, and current state.

This keeps M5-Eve's knowledge organization stable as projects grow:

```text
CATEGORY MANIFEST
      ↓
PROJECT / ASSET / AGENCY INSTANCE
      ↓
SOURCE / CLAIM / EVIDENCE / EVENT
      ↓
CURRENT STATE
```

A record may belong to multiple categories when appropriate. Category membership
is routing/context metadata only; it does not create legal authority, ownership,
jurisdiction, or access rights.

## Authority boundary

Regardless of which intelligence runtime M5-Eve uses:

```text
model output
≠ authority

M5-Eve credential
≠ principal authority

successful payment
≠ authority

threat score
≠ authority
```

Consequential execution remains subject to deterministic M5Canon evaluation and
the required accountable human or institutional approvals.

## Canonical shorthand

> **Milner is the cognitive boundary. Lenore is the deliberative-thinking
> function and future CTM-inspired research layer for blind-spot discovery.
> M5-Eve is the credentialed activated interface. Laya is local System 1.
> Jev is optional hosted System 1. Category manifests organize GSA, CRE, FARM,
> SHADOW, and AGENCIES. M5Canon authorizes consequential action.**

## Machine-readable activation

Use [activation schema](../schemas/m5-eve-activation.schema.json) and its
[synthetic example](../examples/m5-eve-activation.example.json). Protected
execution must re-resolve current activation and evidence; snapshots cannot
override expiry or revocation. Model, policy, approval, authority and execution
are separate in the [action contract](../schemas/m5-action-authorization.schema.json).
Ordinary Tier I inference follows the [M5BOM baseline](M5BOM-ACTIVATION-AND-SOVEREIGN-BASELINE.md).
Category manifests are proposed metadata, not implemented runtime routing.
