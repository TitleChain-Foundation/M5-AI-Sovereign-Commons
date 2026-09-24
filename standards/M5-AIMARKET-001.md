# M5-AIMARKET-001 — Sovereign Intelligence Baseline and Optional Compute

**Status: Draft for Public Comment · Version: 0.1.0 · September 23, 2026**

## 1. Scope and conformance

This proposed standard defines the baseline an M5 implementation MUST provide
when it represents an activated person's M5BOM context as conforming. M5BOM is
the public name for the existing `BOM` (Bank of Me) account context; it is not a
new provider account class. It does not imply a regulated bank account.

The sovereign local baseline is **$0 AI-service price, sovereign, and unmetered**.
It applies to compatible, lawfully usable local model artifacts on hardware
controlled by the person, without purchasing another operator's compute.
Conformance is vendor-neutral and covers local generative models and typed
decision models. Laya is a first featured candidate, not an exclusive supplier.

This is a proposed interoperability and economic standard, not enacted law,
an external license grant, a hardware subsidy, a deployed service, or a promise
that every model can run on every device. Implementations MUST disclose model
license, artifact revision/hash, supported hardware, storage and memory needs,
limitations, and available alternatives before claiming a working baseline.
An incompatible device MUST receive an honest readiness result, never a hidden
paid fallback or an invented claim that baseline inference is available.

## 2. Free Sovereign Intelligence

A person operating an approved local/open-weight model on hardware under that
person's control SHALL incur no model-access, inference, token, request,
subscription, telemetry, or compulsory network-service charge for the use of
that model. Local computation SHALL NOT be characterized as a metered AI
service merely because the device, electricity, storage, or connectivity used
to operate it has an underlying ownership or operating cost.

Here, approved means selected by the person from artifacts whose license,
integrity, and compatibility have been reviewed. It MUST NOT mean a recurring
vendor approval, a remote lease, or permission for an agent to take protected
actions. Account activation MUST NOT be presented as creating the person's
underlying right to possess or operate their own computing resources.

Where the individual supplies their own hardware, storage, energy, and
connectivity—including self-generated energy such as solar power—the resulting
local inference may be operated without any third-party AI-service payment.
Purchased energy may be zero without implying that the device, battery, solar
installation, or storage has no economic cost.

## 3. Compute classes

| Tier / compute class | AI-service price | Service metering | Control |
| --- | --- | --- | --- |
| I — M5 Sovereign Local | $0 | None | Human |
| II — Federated community/state compute | Disclosed, possibly subsidized | Transparent, if applicable | Accountable operator within agreed scope |
| II — Commercial pooled compute | Disclosed market price | Disclosed | Provider within agreed scope |
| III — Frontier hosted model | Disclosed market price | Disclosed token, workflow, or service units | Provider within agreed scope |

Tier II and III MUST be optional. Their limits or suspension MUST NOT disable
Tier I. A person MAY use Tier I without a payment method, subscription, hosted
API key, deposited balance, commerce receipt, or service usage counter.

## 4. Activation and continued local use

On activation, the implementation MUST give the person a readable baseline
statement and portable machine-readable profile identifying the principal,
account context, local artifact/license/hash, $0 service price, and controls.
Private identity and credentials MUST remain in the person's protected M5POD;
public examples MUST use synthetic references. A chat login alone does not
establish an activated M5 account or an authorized M5AGT.

After local artifact acquisition and installation, ordinary Tier I inference
MUST work offline. It MUST NOT require recurring account verification, a cloud
heartbeat, token replenishment, subscription renewal, or compulsory telemetry.
Account suspension, provider outage, or revocation of an M5-Eve delegation MUST
NOT disable the person's ordinary local model use or erase their local data.

Protected account functions, delegated actions, confidential third-party data,
external submissions, payment, and title/registry changes retain their own
current authorization requirements. Unresolved offline authority MUST block
the protected action, not unrelated local inference. A local model's output
never creates consent, title, standing, or legal authority.

## 5. Privacy, diagnostics, and portability

Tier I MUST have no service meter or usage cap. Diagnostic counters MAY be
enabled by the human for local troubleshooting; they MUST default OFF, remain
local, and be independently disableable without loss of inference. They MUST
NOT determine billing, quotas, access, or a provider's entitlement to data.
Training, analytics export, retention, and hosted processing require separate,
specific opt-in and MUST NOT be bundled into baseline activation.

The person MUST be able to export their profile and own records, select another
compatible local runtime, and delete optional diagnostics. Export MUST preserve
provenance and respect applicable third-party rights without becoming a vendor
lock-in mechanism. Consequential action receipts MAY remain required under
their own record policy; they are not AI consumption meters.

## 6. Optional paid escalation

Before Tier II/III use, disclose provider, capability, data leaving the device,
purpose, retention/region conditions, unit price, quote expiry, and maximum
spend. Obtain current, attributable human consent scoped to provider, purpose,
data and budget. No consent, expired quote, revoked consent, or insufficient
budget MUST produce a local choice, HOLD, or refusal—not automatic purchase.
Payment authorization does not replace M5Canon or accountable approvals.

The person MUST be able to cancel future escalation independently of Tier I.
Settled obligations for previously authorized external services are separate
from the continued $0 local baseline. OpenMeter and x402 are optional adapters.

## 7. Market comparison method

M5-AIMARKET MUST display **Sovereign Local Baseline = $0**. Show optional
infrastructure costs separately:

`device amortization + purchased electricity + storage + network`

Compare commercial alternatives by additional absolute service price for a
specified task, alongside capability, accuracy/quality, latency, capacity,
privacy, data movement, license and version. A percentage premium over zero is
undefined and MUST NOT be reported. Different capabilities MUST NOT be called
equivalent simply because both accept prompts. Unsupported local tasks must
be labeled unsupported, not assigned a fabricated local service price.

Reference service value is not revenue, a receivable, or a waived invoice.
Self-provided local inference MUST NOT be counted as billable demand or assigned
a commercial notional price. Voluntary research measurements, if any, must be
separately consented and clearly labeled, with no access consequence.

## 8. Conformance evidence

An implementation claiming this profile MUST demonstrate offline inference,
continued local use with account/network/commerce services unavailable, no
required payment or telemetry, no usage cap, export and runtime replacement,
and explicit opt-in before external spend. The public suite validates record
contracts and synthetic behavior only; it does not demonstrate a working
device deployment. Deployment evidence must name the tested device, artifact,
runtime and versions, method, results, date and limitations.

See the [baseline schema](../schemas/m5-bom-sovereign-baseline.schema.json),
[synthetic profile](../examples/m5-bom-sovereign-baseline.example.json),
[baseline tests](../tests/test_m5_bom_baseline.py), and
[activation framework](../docs/M5BOM-ACTIVATION-AND-SOVEREIGN-BASELINE.md).

The related [Sovereign Compute Access Act draft, sections 101–102](https://github.com/TitleChain-Foundation/icsn-standards/blob/main/legislation/sovereign-compute-access-act/OFFICIAL-TEXT.md)
is a legislative proposal. This standard does not assert enactment.
