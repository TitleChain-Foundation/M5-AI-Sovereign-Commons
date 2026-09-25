# Exhibit B - Repository and Contract Architecture Crosswalk

> **© 2026 TitleChain Foundation.** Part of the Foundation's written submission
> to the SEC on File No. S7-2026-30 (emailed September 23, 2026; pending SEC
> posting). Licensed under CC-BY-4.0 with required attribution. TitleChain
> Foundation, M5 and related marks are not licensed, and no patent rights are
> granted. See [NOTICE](../NOTICE.md). *This notice is added by the repository and
> is not part of the submitted text.*

**Pinned baselines:**\
- M5-AI-Sovereign-Commons: `3a7b4b79b23399e9c362a124ca87f433a36321a3`\
- icsn-standards: `a0a7341213dbf4abad5fa0aeb46b43e7b95c6660`

| Layer / artifact | Purpose in SEC demonstration | Authority boundary |
|---|---|---|
| `pilots/312-spring-commons/README.md` | Full public-asset reference transaction, capital provenance, title/right separation | Draft; external legal records control |
| `pilots/312-spring-commons/INITIATIVE-FIT-GAP-REVIEW.md` | Evidence gates; simulated pass vs pending external | Code success is not approval |
| `docs/PILOT-SEC-RFI-CROSSWALK.md` | Maps public pilot to SEC recordkeeping questions | Research crosswalk, not SEC position |
| `docs/M5CANON-FUNCTION-NAMESPACE.md` | Deterministic function/authority namespace | M5Canon enforces supplied authority; does not create it |
| `docs/M5AGT-AUTHORITY-AND-ACTIVATION.md` | Agent activation/delegation constraints | Agent cannot exceed principal |
| `docs/M5-CREDENTIAL-TRUST-AND-JURISDICTION-BINDING.md` | Entity/role/credential/jurisdiction evidence stack | Credentials are evidence, not licenses |
| `docs/M5-CONFORMANCE-AND-NAMESPACE-BOUNDARIES.md` | Namespace and conformance boundaries | Friendly namespace is not governmental authority |
| `docs/PEOPLES-TRUST-PUBLIC-PILOT.md` | Repeatable farmland conformance simulation | Synthetic/proposed until external evidence |
| `shadow-m5index/README.md` | Public asset/debt/ownership research layer | Research state separate from canonical authority |
| `shadow-m5index/reports/SHADOW-CAMEL-REPORT-Q3-2026.md` | Published public-data systemic-risk research | Not official CAMELS/regulator finding |
| `docs/SHADOW-M5INDEX-PUBLIC-INGESTION-AND-QR.md` | Public contribution, evidence, QR/asset indexing | Submission cannot self-promote to canonical |
| ICSN `docs/M5MST-ASSET-MINTING-AND-TITLECHAIN-REGISTRATION.md` | Origination/title-registration event model | Mint/origination authority != transfer authority |
| ICSN `docs/TRANSFER-AGENT-DIGITAL-ASSET-REFERENCE-ARCHITECTURE.md` | Known entity -> human -> bounded agent -> recordkeeping | Regulated TA remains accountable |
| ICSN `docs/SWIFTBRIDGE-INTEROPERABILITY.md` | Maps legacy identifiers/rails without discarding originals | Not SWIFT/BIS endorsement or replacement |
| ICSN `docs/M5-GLOBAL-INDEX-AND-EXCHANGE.md` | Provenance-aware public economic intelligence | Not a securities exchange/ATS/trading venue |
| ICSN `architecture/M5-L0-L8-ZK-REFERENCE-ARCHITECTURE.md` | Layered proof/credential/reference architecture | Proof system does not create authority |
| ICSN Article 12 CER mapping | Keeps CER control distinct from title/authority | Control != title != authority |

## Review rule

Repository presence proves that an artifact exists at the pinned commit. It does not prove an external fact, agency approval, production deployment, legal conclusion, or independent replication.
