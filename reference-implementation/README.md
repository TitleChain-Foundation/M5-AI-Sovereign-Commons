# Reference Implementations

![Read the context before the implementation](../assets/section-review-path.svg)

This folder contains code that demonstrates bounded parts of the proposed
Commons architecture. Reference code is provided for inspection,
interoperability work, and testing. It is not a production service,
certification, security warranty, approved provider integration, or substitute
for an accountable implementation review.

## Explore this section

| Implementation | Purpose | Start here |
| --- | --- | --- |
| Provider-neutral governor | Demonstrates cost, context, budget, policy preflight, evidence-ledger handling, and replaceable provider adapters | [Implementation README](provider-neutral-governor/README.md) |

## Review path

Read the [governance standard](../standards/M5-AIGOV-001.md) before treating code
behavior as architectural intent. Then inspect the implementation, provider
adapters, and tests together. Dated provider pricing and context facts are
replaceable configuration snapshots, not M5 canonical truth.

Passing tests demonstrates only the cases exercised. It does not establish
production security, legal compliance, provider enrollment, or complete
conformance.
