# Spring Commons Capital-Provenance Schema

This folder contains the machine-readable JSON Schema for the Spring Commons
jurisdictional capital-provenance record. The schema defines the permitted shape
of a record; it is not intended to read like a narrative document.

## Read this first

The schema supports the workflow described in
[DOC-23](../documents/public/DOC-23-Source-of-Funds-Entity-Provenance-Jurisdiction-Chain-and-Public-Transaction-Graph-Standard.md):

1. resolve the entity and accountable authority;
2. document source-of-funds evidence and jurisdiction hops;
3. complete applicable regulatory routing;
4. record `SOURCE_CHAIN_ACTIVATED` only after the required evidence gates pass;
5. keep `DESTINATION_CHAIN_CONFIRMED` as a separate state; and
6. preserve corrections and supersessions instead of overwriting history.

## Choose a view

| View | Best for |
| --- | --- |
| [DOC-23 human-readable standard](../documents/public/DOC-23-Source-of-Funds-Entity-Provenance-Jurisdiction-Chain-and-Public-Transaction-Graph-Standard.md) | Understanding the policy, evidence states, and legal boundaries |
| [Synthetic example guide](../examples/README.md) | Seeing how one illustrative record uses the fields |
| [Raw JSON Schema](m5-jurisdictional-capital-provenance.schema.json) | Validators, implementers, and code generation |

Schema validation confirms structure only. It does not prove the truth of a
claim, establish legal authority, complete KYC/KYB or source-of-funds review, or
confirm settlement, title, lawful use of proceeds, or investment performance.

[Back to the Spring Commons overview](../README.md)
