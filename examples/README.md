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

## How to use these examples

1. Read the applicable [proposed standard](../standards/README.md).
2. Inspect the controlling [schema](../schemas/README.md).
3. Compare this synthetic instance with the required and prohibited states.
4. Run the [validation tests](../tests/README.md).

Do not copy sample identifiers or values into a production system without an
independent authority, privacy, security, and implementation review.
