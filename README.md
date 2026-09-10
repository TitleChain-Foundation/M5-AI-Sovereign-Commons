# M5 AI Sovereign Commons

**Status: Release Candidate v0.7 — Draft for Public Comment**

![M5 AI Sovereign Commons: human authority, open standards, public pilots, and evidence](assets/commons-overview.svg)

This repository is a proposed public standards commons for governing AI models,
agents, providers, plugins, connectors, MCP servers, local runtimes, sensors,
and embodied systems without treating any of them as an independent source of
human or legal authority.

It is not a Stable production release, a certification program, or evidence
that any external provider has joined, endorsed, or been credentialed by M5.

> **Humans and accountable institutions authorize. AI agents and automated
> systems act only within explicit, verifiable, and revocable limits.**

## Start here

| I want to understand | Visual landing page |
| --- | --- |
| What the Commons contains and how the documents fit together | [Documentation map](docs/README.md) |
| What the four normative proposals cover | [Proposed standards](standards/README.md) |
| How the public waitlist, demo, M5-CV, Commons, and project pathways connect | [Activation pathway](docs/activation/README.md) |
| How the machine-readable records and samples fit together | [Schemas](schemas/README.md) and [synthetic examples](examples/README.md) |
| How the proposed People's Trust pilot tests the standards | [People's Trust Public Pilot Library](pilots/peoples-trust/README.md) |
| What public SEC input says and how it becomes actionable review | [SEC Public Input Summary](sec-public-input/README.md) |
| What the reference code demonstrates | [Reference implementations](reference-implementation/README.md) |
| What the current tests do and do not prove | [Tests and validation](tests/README.md) |
| Which visuals are approved for public orientation | [Visual assets](assets/README.md) |
| What is safe to publish or how to report a vulnerability | [Public-review boundaries](#public-review-boundaries) and [Security](SECURITY.md) |

**Public review path:** visual orientation -> maintained source text -> scoped
Discussion or Issue -> evidence and review -> proposed change -> attributable
decision.

## Proposed standards

| Standard | Scope |
| --- | --- |
| [M5-AIGOV-001](standards/M5-AIGOV-001.md) | Provider, plugin, tool, budget, privacy, authorization, and evidence governance |
| [M5-AIMOD-001](standards/M5-AIMOD-001.md) | Resident and open-weight model artifacts, hardware profiles, and portability |
| [M5-AISPACE-001](standards/M5-AISPACE-001.md) | Spatial, embodied, experiential, sensor, simulation, and actuator governance |
| [M5-AIPROV-001](standards/M5-AIPROV-001.md) | Provider identity, credential status, and verified endpoint binding |

The standards are proposed for public criticism and independent implementation.
They do not replace law, regulation, contracts, official records, qualified
professional judgment, or the accountability of a regulated entity.

## Authority boundary

The reference architecture follows this relationship:

```text
accountable human or legal entity
→ current role, credential, jurisdiction, and policy
→ explicit delegation
→ deterministic M5Canon evaluation
→ bounded M5AGT or automated action
→ tamper-evident evidence receipt
```

- M5Canon is a deterministic authority-control layer, not an AI agent.
- M5AGT cannot create authority or exceed its principal's current authority.
- A wallet, token, API key, login, credential, model, or smart contract is not
  independent proof of legal authority.
- Account context, asset classification, and external legal status remain
  separate questions.
- Missing, expired, revoked, altered, or out-of-scope authority must fail closed.

## Public-review boundaries

Public participation does not require private M5POD evidence, credentials,
personal data, internal keys, production endpoints, or confidential M5Canon
materials. Do not submit them to issues or pull requests.

Participation is governed by the
[Public Participation Code of Conduct](CODE_OF_CONDUCT.md), the
[contribution requirements](CONTRIBUTING.md), and the private reporting process
in [SECURITY.md](SECURITY.md).

Useful review includes:

- authority and delegation failure modes;
- provider and plugin substitution;
- privacy, retention, and data residency;
- model and artifact provenance;
- hardware and runtime measurements;
- endpoint-binding and redirect controls;
- prompt, tool, model, and sensor threat vectors;
- accessibility, human oversight, and recovery;
- conformance tests and interoperable schemas.

## Release state

The normative text, schemas, examples, and reference code remain under review.
See [RELEASE-STATUS.md](RELEASE-STATUS.md) before relying on any artifact.

The proposed separation between value instruments, denominations, governing
jurisdictions, and standards references is documented in
[Value Instrument and Jurisdiction Model](docs/VALUE-INSTRUMENT-AND-JURISDICTION.md).

Supporting public-review materials:

- [Visual documentation map](docs/README.md)
- [M5Canon Function Namespace](docs/M5CANON-FUNCTION-NAMESPACE.md)
- [M5AGT Authority and Activation](docs/M5AGT-AUTHORITY-AND-ACTIVATION.md)
- [Named Role and Function Crosswalk](docs/NAMED-ROLE-FUNCTION-CROSSWALK.md)
- [Open Standards Evidence Registry](docs/OPEN-STANDARDS-EVIDENCE-REGISTRY.md)
- [M5POD Data Portability Profile](docs/M5POD-DATA-PORTABILITY-PROFILE.md)
- [Activation Pathway](docs/activation/README.md)
- [Sovereign Communications Profile](docs/SOVEREIGN-COMMUNICATIONS-PROFILE.md)
- [People's Trust Public Conformance Pilot](docs/PEOPLES-TRUST-PUBLIC-PILOT.md)
- [Pilot and SEC Request-for-Input Crosswalk](docs/PILOT-SEC-RFI-CROSSWALK.md)
- [People's Trust Public Pilot Library](pilots/peoples-trust/README.md)
- [SEC Public Input Summary](sec-public-input/README.md)
- [Threat Model](THREAT-MODEL.md)
- [Draft JSON Schemas](schemas/README.md) and [synthetic examples](examples/README.md)
- [Tests and validation](tests/README.md)

Run the focused schema suite with:

```text
python -m pytest tests/test_schemas.py
```

The approved repository license mapping and official license texts are recorded
in [LICENSE.md](LICENSE.md) and [LEGAL-NOTICES.md](LEGAL-NOTICES.md).

## No production claim

Passing the included tests demonstrates only the cases those tests exercise.
It does not establish production security, legal compliance, provider
enrollment, hardware certification, or full standards conformance.
