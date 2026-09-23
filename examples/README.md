# Synthetic Examples

![Read the context before the examples](../assets/section-review-path.svg)

This folder provides one synthetic, non-production example for each published
JSON Schema. The examples make record structure easier to inspect and test.
They are not credentials, approvals, authoritative records, live provider
registrations, production endpoints, or evidence about a real person, asset,
organization, model deployment, or transaction.

## Explore this section

| Example | Validates against |
| --- | --- |
| [Governance receipt](governance-receipt.example.json) | [Governance receipt schema](../schemas/governance-receipt.schema.json) |
| [Canonical context envelope](m5-canonical-context-envelope.example.json) | [Canonical context schema](../schemas/m5-canonical-context-envelope.schema.json) |
| [Provider plugin manifest](provider-plugin-manifest.example.json) | [Provider plugin schema](../schemas/provider-plugin-manifest.schema.json) |
| [Sovereign provider endpoint](m5-sovereign-provider-endpoint.example.json) | [Provider endpoint schema](../schemas/m5-sovereign-provider-endpoint.schema.json) |
| [Model artifact](m5-aimod-model-artifact.example.json) | [Model artifact schema](../schemas/m5-aimod-model-artifact.schema.json) |
| [Hardware profile](m5-aimod-hardware-profile.example.json) | [Hardware profile schema](../schemas/m5-aimod-hardware-profile.schema.json) |
| [Capability manifest](m5-aispace-capability-manifest.example.json) | [Capability manifest schema](../schemas/m5-aispace-capability-manifest.schema.json) |
| [Human-experience boundary](m5-human-experience-boundary.example.json) | [Human-experience boundary schema](../schemas/m5-human-experience-boundary.schema.json) |
| [Human refusal profile](m5-human-refusal-profile.example.json) | [Human refusal profile schema](../schemas/m5-human-refusal-profile.schema.json) |

## How to use these examples

1. Read the applicable [proposed standard](../standards/README.md).
2. Inspect the controlling [schema](../schemas/README.md).
3. Compare this synthetic instance with the required and prohibited states.
4. Run the [validation tests](../tests/README.md).

Do not copy sample identifiers or values into a production system without an
independent authority, privacy, security, and implementation review.

## Sanitized member-supplied illustration

The [Sovereign Self refusal projection](member-supplied/README.md) illustrates
how a Refuse Consent Genesis Mark may appear in an M5POD Bank of Me account. It
is deliberately separate from the synthetic conformance fixtures above. It
contains no Ownership Key, recovery card, wallet secret, legal name, or private
M5POD identifier, and it does not prove ownership, authority, consent, patent
rights, legal effect, or device compliance.

- [m5-jurisdiction-binding](m5-jurisdiction-binding.example.json) — [schema](../schemas/m5-jurisdiction-binding.schema.json).

- [m5-credential-trust-record](m5-credential-trust-record.example.json) — [schema](../schemas/m5-credential-trust-record.schema.json).

- [m5-event-envelope](m5-event-envelope.example.json) — [schema](../schemas/m5-event-envelope.schema.json).

- [orbitalys-threat-vector](orbitalys-threat-vector.example.json) — [schema](../schemas/orbitalys-threat-vector.schema.json).

- [m5-service-event-manifest](m5-service-event-manifest.example.json) — [schema](../schemas/m5-service-event-manifest.schema.json).

- [m5-intelligence-request](m5-intelligence-request-laya-local.example.json) — [schema](../schemas/m5-intelligence-request.schema.json).

- [m5-intelligence-routing-receipt](m5-intelligence-routing-receipt-laya.example.json) — [schema](../schemas/m5-intelligence-routing-receipt.schema.json).

- [m5-transaction-footprint](m5-transaction-footprint-property.example.json) — [schema](../schemas/m5-transaction-footprint.schema.json).

- [m5-commerce-receipt](m5-commerce-receipt-laya-local.example.json) — [schema](../schemas/m5-commerce-receipt.schema.json).

- [m5-action-authorization](m5-action-authorization.example.json) — [schema](../schemas/m5-action-authorization.schema.json).

- [m5-bom-sovereign-baseline](m5-bom-sovereign-baseline.example.json) — [schema](../schemas/m5-bom-sovereign-baseline.schema.json).

- [m5-eve-activation](m5-eve-activation.example.json) — [schema](../schemas/m5-eve-activation.schema.json).
