# Glossary

Plain-language definitions of the names used across the M5 AI Sovereign
Commons. Canonical specifications live in
[ICSN Standards](https://github.com/TitleChain-Foundation/icsn-standards); this
page is a reading aid, and the linked source text controls.

## Organizations and front doors

| Name | What it is |
| --- | --- |
| **TitleChain Foundation** | The public-interest foundation that stewards these open standards and the public commons. [titlechainfoundation.org](https://titlechainfoundation.org) |
| **ICSN Standards** | The Foundation's standards program: specifications, namespaces, classifications and bridge mappings. [Repository](https://github.com/TitleChain-Foundation/icsn-standards) |
| **M5 AI Sovereign Commons** | This repository: the standards applied to real projects, SEC public review and public research |
| **M5 / M5Bank** | The M5 implementation and member entry point, separate from the Foundation's standards work. Whitepapers, including *Pax Economica*, and the FAQ are at [m5bank.app](https://m5bank.app) |
| **Pax Economica** | The Foundation's research into peaceful economic coordination. It is not a fund, financial product or investment right |
| **TitleChain / TitleChain Registry** | The record of asset identity, title evidence, provenance and asset-state changes. It links to authoritative records and never replaces them |

## The authority chain

| Name | What it is |
| --- | --- |
| **M5IAM** | Identity and access: the free, self-asserted starting identifier (`000-IAM`). It does not by itself verify legal identity |
| **TCID** | The TitleChain identifier for a human root |
| **M5HUM** | Human Principal: a credentialed human who answers for every agent acting on their behalf. See the [refusal and consent profile](docs/M5HUM-REFUSAL-CONSENT-PROFILE.md) |
| **M5Canon** | The deterministic rules engine that allows or denies each consequential action. It is not an AI. See the [function namespace](docs/M5CANON-FUNCTION-NAMESPACE.md) |
| **M5AGT** | An AI agent acting under bounded, revocable authority from a human principal. It cannot exceed that authority. See [M5AGT](docs/M5AGT-AUTHORITY-AND-ACTIVATION.md) |
| **M5CAP** | A bounded supporting capability that M5Canon may invoke |
| **Six-Gate control** | The checks every consequential action passes in [M5-AIGOV-001](standards/M5-AIGOV-001.md): principal, credential and standing, jurisdiction, policy, and more |
| **Fail closed** | If any required authority is missing, stale, revoked or out of scope, the action holds or is refused |

## People, data and participation

| Name | What it is |
| --- | --- |
| **M5POD** | The private, member-controlled environment for credentials, records, storage and selective proof. See [data portability](docs/M5POD-DATA-PORTABILITY-PROFILE.md) |
| **M5-CV** | Reusable, holder-controlled evidence of skills, standing and contributions. It is never blanket permission |
| **Participation Passport** | The project-specific permission issued after eligibility checks. See the [passport standard](docs/project-control-pack/M5-PROJECT-PARTICIPATION-PASSPORT-AND-ELIGIBILITY-MATRIX.md) |
| **WORK / SUPPORT / FINANCIAL PARTICIPATION** | Three separate ways to take part in a project. Support never creates ownership, investment, voting or profit rights. See [matching](docs/project-control-pack/M5-CV-WORK-OPPORTUNITY-AND-SUPPORT-MATCHING.md) |
| **M5 Eve** | The proposed member-facing assistant workspace. See [M5 Eve](m5-eve/README.md) |
| **DUNA** | A decentralized unincorporated nonprofit association, the membership structure referenced for commons governance |

## Two numbered ladders: accounts and asset classes

The M-numbers are used for **two separate things**. Account tiers are written
with their suffix (`M3-BOB`) so they are never confused with asset classes
(`M3`).

**Account ladder: who is acting**

| Tier | Context | Meaning |
| --- | --- | --- |
| **M0** | `000-IAM` | A sovereign human with a self-asserted identifier who is not yet credentialed |
| **M1-BOM** | Bank of Me | The first credentialed account type: the individual. [M5-AIMARKET-001](standards/M5-AIMARKET-001.md) gives it a $0 local intelligence baseline |
| **M2-BOU** | Bank of Us | A bounded project, collective or operating unit |
| **M3-BOB** | Bank of Business | A business or organization |
| **M4-BOI** | Bank of Institutions | An institution or regulated operator |
| **M5-BOG** | Bank of Government / Governance | A government or public authority |

Each context is separately authorized. Seeing a context never means acting in it.

**Asset classes: what is being exchanged**

| Class | Meaning |
| --- | --- |
| **M1** | Money / Payment / Access / Utility / Fee Events |
| **M2** | Commodity |
| **M3** | Title / Ownership Asset |
| **M4** | Security / Investment Instrument |
| **M5** | Jurisdiction / Sovereign Authority State |

These are internal classes that route a transaction to the right authorities.
They never decide its legal status. See the
[classification model](docs/M5-TRANSACTION-FOOTPRINT-AND-ECONOMIC-CLASSIFICATION.md).

## Contracts, value and routing

| Name | What it is |
| --- | --- |
| **Ricardian contract** | One agreement in three bound layers: human-readable terms, machine-readable policy, and bounded executable settlement. See [M5-RICARDIAN-TRIPLE-LAYER-001](standards/M5-RICARDIAN-TRIPLE-LAYER-001.md) |
| **M5-x402** | The payment-protocol binding used for metered machine commerce |
| **Value instrument model** | How a receipt records the instrument (fiat, CBDC, stablecoin, token, security) separately from its denomination and legal status. See [the model](docs/VALUE-INSTRUMENT-AND-JURISDICTION.md) |
| **JNR** | The ICSN Jurisdiction Naming & Resolution Registry, the canonical jurisdiction layer. Chain aliases such as `unitedstateschain.eth` are technical adapters only |
| **Jurisdiction profile slot** | A reserved place for a jurisdiction's records. Only that jurisdiction's own lawful authority can activate it |
| **Event Plane** | The common event envelope for providers, metering, commerce and threat telemetry. See [M5-EVENT-001](standards/M5-EVENT-001.md) |
| **Orbitalys** | The cross-plane threat-vector graph for M5 events. It maps threats without deciding authority |

## Projects

| Name | What it is |
| --- | --- |
| **Project Control Pack** | The same eight control questions asked of every project. See [the standard](docs/project-control-pack/M5-COMMONS-PROJECT-CONTROL-PACK-STANDARD.md) |
| **312 Spring Commons** | The GSA / CRE project: a historic federal building in Los Angeles. Its designation is **PPT-EZ-CA-0001** (People's Public Trust Economic Zone 0001 — California), a project benchmark, not an official state zone |
| **People's Public Trust** | The public-trust framework under which the projects are designed and reviewed |
| **Public Trust of America** | The proposed entity referenced in Spring Commons. Its relationship to the other parties is still conceptual |
| **America's People's Trust Farmland** | The FARMLAND project, also called **People's Trust**. Its first sample-data pilot is **AG-PILOT-001 / ND-FARM-SIM-001** |
| **Global UN Commons (UN-NY-0001)** | The GLOBAL project: independent concept research, with no UN affiliation or endorsement |
| **Open World Convention** | A proposed public framework for digital records, human authority and peaceful economic coordination. Not a treaty |
| **Public Bank of California** | A concept-only public-capital layer in Spring Commons. Not a chartered bank or agency |

## Public research

| Name | What it is |
| --- | --- |
| **SHADOW M5Index** | Systemic Holdings, Assets, Debt & Ownership Watch: public research on real-world asset state. See [SHADOW](shadow-m5index/README.md) |
| **SHADOW CAMEL** | A proposed public-data methodology. Not an official CAMELS bank rating |
| **TSI · ASI · DPI · OOI** | Title State Integrity · Asset Stress Index · Debt Pressure Index · Ownership Opacity Index |
| **CCI · PVMI · PBOI** | Capital Concentration Index · Public Value Migration Index · Public Benefit Opportunity Index |
| **SEC observatory** | The hourly monitor of SEC File No. S7-2026-30, with human-reviewed summaries. See [SEC public input](sec-public-input/README.md) |
| **Open Commons Review** | A dated implementation review of the SEC work. It is not an SEC filing |
