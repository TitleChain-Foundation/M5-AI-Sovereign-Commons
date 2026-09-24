# Conformance, namespace resolution and authority

**Draft for Public Comment.** VALID JSON ≠ VERIFIED EVIDENCE ≠ AUTHORIZED ACTION.
MODEL RESULT ≠ POLICY RESULT ≠ AUTHORITY RESULT.

## Independent namespace bindings

Each transaction may carry multiple bindings with separate scope, role,
controller, canonical entity, authority evidence, registration provenance,
hashes, validation record/time, standing, validity, dispute, revocation and
supersession state. Namespace classes include nation, state, province,
territory, tribal nation, municipality, county, agency, regulator, court,
international organization, treaty body and special authority.

The public example distinguishes unitednationschain.eth (institutional),
newyorkcitychain.eth (municipal), and newyorkchain.eth (state). All three are
UNRESOLVED synthetic assertions. Their inclusion makes no claim about actual
registration, controller, endorsement or governmental/institutional authority.
Geographic containment creates no authority inheritance.

ENS/DNS/DID control, a wallet, address, chain ID, or ISO code alone cannot
establish authority. JNR/index records validate and index existing evidence;
they do not manufacture it. An ESTABLISHED declaration must be corroborated by
independently resolved current authority, registration and validation records,
matching namespace, controller, entity, role, scope, and hashes.

SWIFT/BIC, ISO 20022, LEI/vLEI, ISIN, CUSIP, MIC, registry, tax and routing IDs
remain external crosswalk metadata. Preserve issuer, source, version and object
relationship. No identifier grants title, jurisdiction, standing or transfer
authority. Never publish real private tax or account identifiers as examples.

## Enforcement responsibilities

| Layer | Responsibility |
| --- | --- |
| JSON Schema | Required fields, types, versions and internal contradictions |
| Trusted evidence resolver | Authenticate issuer/source, integrity, scope, freshness, revocation and disputes |
| Deterministic authorization | Apply current policy, credentials, delegation, namespaces, provider standing/capability/endpoint and required approvals |
| Executor | Recheck immediately before protected execution; bind action to evaluated request and prevent replay |
| Evidence receipt | Preserve separate model result, policy result, approval, authority result and executed action |

The [public reference module](../reference-implementation/commons-contracts/contracts.py)
uses injected resolver observations and synthetic fixtures. It is not private
M5Canon, a production verifier, or a signature service. Production deployments
must authenticate resolver responses and specify trust roots, freshness bounds,
revocation availability, atomic authorization/execution and durable replay
protection. Missing or unreachable evidence fails closed for protected actions.

Payment success and model confidence cannot override a failed gate. Required
approvals cannot be self-issued by the agent. Tier I ordinary local inference
remains separate from these protected-function controls.

## Event and pricing profile

CloudEvents is pinned to specification 1.0.2 (wire specversion 1.0). Its
extension name is m5eventversion; underscores are not permitted in context
attribute names. The source is a URI-reference. See the
[pinned source](https://github.com/cloudevents/spec/blob/v1.0.2/cloudevents/spec.md).

The reference meter registry is an internal JSON-compatible YAML fixture, not
production OpenMeter configuration. Every metered catalog entry resolves to a
defined meter whose selector addresses data.units. Local products have meter
null. The synthetic consumer covers FREE_PUBLIC reference pricing only; it
never executes a payment. Denied attempts may be counted but are not billed.
Event IDs and idempotency keys must be durable in production; conflicting
replays are rejected. Corrections point to an existing prior event and require
separate reconciliation rather than additional billable consumption.

Receipts pin applicable model/runtime/API/adapter/policy/event/meter/catalog/
activation/settlement versions. NOT_APPLICABLE denotes an absent component;
it is not permission to omit a relevant version. Local model artifacts require
a digest. Floating latest is invalid. Synthetic pins are not verified vendor
versions and must never be deployed as if they were.

## Function namespace scope

Existing M5CAP/M5CANON functions are reused and checked against the public
namespace. Orbitalys remains a threat schema/profile with authority_effect NONE.
A new named threat capability identifier is deferred to separate namespace
review; no additional M5CAP function is silently registered by this patch.
