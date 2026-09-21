# Machine-Readable Schemas

![Read the context before the schemas](../assets/section-review-path.svg)

This folder contains nine JSON Schema Draft 2020-12 definitions for
inspectable governance, provider, model, hardware, context, capability, and
human-experience records. Schema validity means only that a document has the
required machine-readable shape. It does not prove that a claim is true, an
authority is current, a provider is approved, or an action is lawful.

## Explore this section

| Schema | Record represented | Paired sample |
| --- | --- | --- |
| [Governance receipt](governance-receipt.schema.json) | Deterministic decision, approvals, evidence, and bounded execution | [Example](../examples/governance-receipt.example.json) |
| [Canonical context envelope](m5-canonical-context-envelope.schema.json) | Twelve independent context and classification dimensions | [Example](../examples/m5-canonical-context-envelope.example.json) |
| [Provider plugin manifest](provider-plugin-manifest.schema.json) | Plugin identity, capabilities, constraints, and provider facts | [Example](../examples/provider-plugin-manifest.example.json) |
| [Sovereign provider endpoint](m5-sovereign-provider-endpoint.schema.json) | Provider identity and endpoint binding | [Example](../examples/m5-sovereign-provider-endpoint.example.json) |
| [Model artifact](m5-aimod-model-artifact.schema.json) | Model provenance, format, integrity, and portability facts | [Example](../examples/m5-aimod-model-artifact.example.json) |
| [Hardware profile](m5-aimod-hardware-profile.schema.json) | Runtime hardware and resource requirements | [Example](../examples/m5-aimod-hardware-profile.example.json) |
| [Capability manifest](m5-aispace-capability-manifest.schema.json) | Bounded spatial or embodied capabilities | [Example](../examples/m5-aispace-capability-manifest.example.json) |
| [Human-experience boundary](m5-human-experience-boundary.schema.json) | Consent, safety, accessibility, sensor, and actuator limits | [Example](../examples/m5-human-experience-boundary.example.json) |
| [Human refusal profile](m5-human-refusal-profile.schema.json) | Portable M5HUM/M5POD refusal scope, verification, enforcement, and lifecycle | [Example](../examples/m5-human-refusal-profile.example.json) |

## Validation path

Review the [synthetic examples](../examples/README.md), then the
[schema test landing page](../tests/README.md). The focused schema suite checks
all nine pairs, required fields, unknown fields, and selected fail-closed
conditions.
