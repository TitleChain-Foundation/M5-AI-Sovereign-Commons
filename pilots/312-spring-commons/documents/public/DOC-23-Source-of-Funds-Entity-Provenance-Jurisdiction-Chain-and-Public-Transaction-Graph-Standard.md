# DOC-23 — Source of Funds, Entity Provenance, Jurisdiction Chain & Public Transaction Graph Standard

Project: PPT-EZ-CA-0001 / 312 Spring Commons  
Document code: DOC-23 / M5-CAPGRAPH-001  
Version: v0.6 — September 19, 2026  
Status: Working draft / public review / counsel review / technical review  
Public-commons objective: Demonstrate a machine-readable, regulator-auditable, privacy-preserving transaction graph for the full economic pathway surrounding a public asset.

> **Draft / demonstration only.** This document does not create an investment, authorize a transfer, approve a participant, establish a government relationship, replace KYC/KYB/AML or other legal review, or create a regulated market. Official deeds, government records, bank/escrow records, transfer-agent books, executed contracts, licenses, professional records, court orders, and other legally authoritative records remain controlling in their respective domains.

## 1. Purpose

DOC-23 establishes the proposed transparency, provenance, jurisdiction, participant, and capital-lineage rules for the Spring Commons pilot and future People’s Public Trust / M5 commons implementations.

The objective is simple:

> **No material dollar, entity, authority, economic right, control right, conflict, restriction, or project obligation should become operative while remaining outside the transaction’s disclosed authority and evidence graph.**

That does **not** mean publishing protected personal data, bank account details, private keys, confidential security architecture, privileged legal advice, or other information that law or sound security practice requires to remain protected. It means that the existence, legal source, accountable parties, material economic effect, authority state, and evidence reference for a material transaction relationship must be discoverable by the parties and regulators entitled to inspect it, and publicly disclosed at the appropriate level when the information is properly public.

This standard is intended to reduce two forms of friction at the same time:

1.  **Opacity friction** — repeated diligence, hidden affiliates, uncertain authority, conflicting terms, stale credentials, side arrangements, shell-company chains, unverifiable source-of-funds claims, and vendor-specific records.
2.  **Compliance friction** — repeated collection of the same entity information, paper-heavy onboarding, fragmented good-standing checks, repeated professional-license verification, duplicated KYC/KYB, manual jurisdiction analysis, and disconnected audit evidence.

The intended result is **verified once, monitored continuously, reused only within the scope of current authority and current law**.

## 2. Core principles

### 2.1 Human and legal-entity accountability first

Every material action must resolve to an accountable human or legally accountable entity. A wallet, domain name, API credential, blockchain address, AI model, smart contract, login, or token does not create legal authority by itself.

### 2.2 Entity provenance before permission

Before an entity receives an M5BOB, M5BOI, M5BOG, regulated-service, fiduciary, vendor, investor, issuer, or other consequential project role, the system should resolve the legal entity against authoritative or independently verifiable sources and identify the current human authority required for the proposed action.

### 2.3 Source of funds is a graph, not a label

A capital contribution should not be labeled simply “Singapore money,” “UK money,” “Texas money,” or similar shorthand. The system should preserve the distinct jurisdictions associated with the capital path: ultimate economic source where required and lawfully determinable, fund or vehicle domicile, capital-provider domicile, beneficial/control relationships where required, remitting account and bank jurisdiction, currency, settlement rail, project destination, and governing legal pathway.

### 2.4 A shell or SPV is a node, not an opacity wall

Lawful SPVs, funds, holding companies, trusts, and special-purpose vehicles may be appropriate. Their existence does not end provenance analysis. The transaction graph should follow the relevant ownership, control, funding, contractual, and economic relationships to the degree required by law, risk policy, and the transaction.

### 2.5 No undisclosed material side economics

No material side letter, rebate, referral payment, affiliated procurement commitment, exclusivity, data right, veto, conversion right, option, warrant, priority, guarantee, revenue share, minimum purchase, hardware commitment, cloud commitment, off-take obligation, most-favored-nation term, or other material economic/control arrangement may silently alter the project economics or governance outside the authoritative transaction graph.

### 2.6 Privacy is part of transparency

Transparency means publishing and sharing the **right evidence with the right audience**, not placing all data on a public ledger. Personal and security-sensitive information should remain encrypted, permissioned, selectively disclosed, or represented by verifiable status proofs where appropriate.

### 2.7 Official records remain authoritative

TitleChain and M5 may index, reconcile, attest, route, and preserve evidence. They do not autonomously replace the legal effect of authoritative public records, regulated books and records, executed instruments, or legally responsible professional decisions.

### 2.8 Technical jurisdiction aliases do not create sovereign authority

ICSN Jurisdiction Naming & Resolution Registry (JNR) identifiers and optional ENS-style aliases are technical resolution aids. They do not establish governmental affiliation, delegated authority, sovereign recognition, or control of an official government domain.

## 3. The transaction graph

The Spring Commons transaction graph should represent at least the following node classes and relationships.

### 3.1 Principal node classes

| **Node class**                 | **Examples**                                                                     | **Minimum relationship evidence**                                                      |
|--------------------------------|----------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|
| Human principal                | Investor signer, agency official, CPA, contractor principal, fiduciary           | Identity, role, authority source, status, expiry/revocation where applicable           |
| Legal entity                   | Fund, LLC, bank, public agency, foundation, vendor, issuer                       | Legal name, jurisdiction, registration identifier, status, parent/affiliate links      |
| Government/public body         | GSA, NPS, public grantee, municipal office, permitting body                      | Statutory/charter/delegation source, office, signer/approver authority                 |
| Professional/regulated actor   | Transfer agent, broker-dealer, CPA, attorney, trustee, custodian                 | Registration/license/engagement, scope, good standing/current status                   |
| Capital source                 | Grant, PRI, debt, equity, tax-credit investment, public appropriation            | Provider, instrument, source evidence, restrictions, jurisdiction path                 |
| Investment/contract instrument | Note, preferred interest, subscription, grant, lease, vendor contract            | Controlling terms, parties, version, restrictions, approval state                      |
| Asset                          | Building, equipment, PV module, server, battery, receivable, contract right      | Provenance, title/stewardship, financing restrictions, lifecycle state                 |
| Account/rail                   | Bank account, escrow, custody account, settlement rail                           | Authorized institution, account class, jurisdiction, role; sensitive details protected |
| Jurisdiction                   | Country, state/province, territory, tribal/local jurisdiction                    | Canonical code, JNR record, authority source, alias state                              |
| Event                          | Commitment, approval, draw, transfer, payment, correction, revocation            | Instruction, authority, timestamp, result, authoritative record, receipt               |
| Policy/restriction             | Eligibility, use-of-proceeds, transfer restriction, approval condition           | Legal source, version, placement/removal authority, effective state                    |
| Evidence                       | Filing, registry record, license, bank receipt, signed agreement, audit evidence | Source URI/identifier, issuer/custodian, timestamp, digest, access class               |

### 3.2 Required material relationships

The graph should support explicit edges such as:

- `HUMAN_CONTROLS_OR_REPRESENTS_ENTITY`
- `ENTITY_OWNS_OR_CONTROLS_ENTITY`
- `ENTITY_PROVIDES_CAPITAL`
- `CAPITAL_FUNDS_INSTRUMENT`
- `INSTRUMENT_FUNDS_PROJECT`
- `PROJECT_ACQUIRES_OR_ACTIVATES_ASSET`
- `PARTY_HAS_AUTHORITY_TO_SIGN`
- `PARTY_HAS_AUTHORITY_TO_APPROVE`
- `PARTY_HAS_FIDUCIARY_DUTY`
- `PARTY_HAS_REGULATED_ROLE`
- `PARTY_IS_AFFILIATE_OF_VENDOR`
- `CONTRACT_CREATES_ECONOMIC_RIGHT`
- `CONTRACT_CREATES_RESTRICTION`
- `PAYMENT_SATISFIES_OR_ADVANCES_OBLIGATION`
- `EVENT_CHANGES_STATE`
- `EVIDENCE_SUPPORTS_EVENT`
- `JURISDICTION_GOVERNS_ENTITY`
- `JURISDICTION_GOVERNS_EVENT`
- `FUNDS_REMITTED_FROM_JURISDICTION`
- `FUNDS_DESTINED_FOR_JURISDICTION`
- `ALIAS_RESOLVES_TO_JURISDICTION`

The graph must distinguish **evidence of a relationship** from **the legal instrument that creates the relationship**.

## 4. Three information planes

A public commons should be inspectable without turning private participants into a surveillance product. DOC-23 therefore requires a three-plane disclosure architecture.

### 4.1 Public transparency plane

Public by default when legally and contractually appropriate:

- project identity and current stage;
- participating legal entities and their project roles;
- public registration identifiers and public good-standing/state information;
- instrument category and high-level material economics;
- material public restrictions and public-benefit obligations;
- material related-party relationships and conflicts;
- material vendor/capital-provider affiliations;
- public approvals, resolutions, permits, and official notices;
- aggregate capital origin/destination indicators;
- transaction state, without exposing protected financial credentials;
- public asset provenance and lifecycle fields;
- methodology, revisions, confidence, and source lineage for public indicators.

### 4.2 Regulator / qualified assurance plane

Available to the entitled regulator, bank, transfer agent, auditor, counsel, fiduciary, tax professional, or other authorized reviewer as applicable:

- complete KYB/KYC evidence;
- beneficial-ownership/control evidence where required;
- source-of-funds and source-of-wealth evidence where required;
- bank/escrow statements and transaction confirmations;
- subscription and investor-qualification evidence;
- sanctions, watch-list, licensing, registration, and professional-status results where required;
- tax and accounting workpapers where applicable;
- confidential side letters and related-party contracts;
- regulator examination/export packages;
- incident, correction, exception, and investigation records.

### 4.3 Private protected plane

Not intended for an immutable public ledger:

- bank account and routing numbers;
- tax identifiers not lawfully public;
- identity-document images;
- private residential addresses where protected;
- passwords, API secrets, private keys, recovery phrases;
- sensitive wallet-security details;
- private communications and privileged legal material;
- health, biometric, and unrelated personal information;
- security-sensitive infrastructure topology;
- private compute workloads or customer content;
- information restricted by law, contract, court order, regulator rule, or safety policy.

A public record may state that protected evidence exists, who is authorized to inspect it, its evidence identifier/digest, and which requirement it satisfies without publishing the protected content itself.

## 5. Entity resolution and M5 credential onboarding

### 5.1 M5 account sequence

The proposed onboarding sequence for Spring Commons is:

`M5BOM verified human root`  
`→ role / entity relationship`  
`→ legal entity resolution`  
`→ current credential / registration / good-standing evidence`  
`→ jurisdiction + scope`  
`→ M5BOB / M5BOI / M5BOG or other role account`  
`→ M5-CV status record`  
`→ project-specific eligibility`  
`→ bounded action permission`

An M5 credential records or references verified evidence. It does not itself create a government license, securities registration, professional license, fiduciary appointment, or statutory authority.

### 5.2 BrightQuery as a reference entity-intelligence connector

Spring Commons proposes to evaluate **BrightQuery or equivalent** as a reference entity-resolution/KYB intelligence connector. BrightQuery publicly describes a data architecture organized around Organizations, Legal Entities, Locations, Addresses, and People, with company identity, ownership, legal status, financial, executive/contact, and compliance-related attributes derived substantially from government filings and official sources.

BrightQuery should be treated as an **evidence and resolution input**, not as the final source of legal authority. A project decision may require direct confirmation from a Secretary of State, SEC/IAPD/FINRA or other regulator, licensing board, tax authority, government agency, bank, court, professional body, or the actual executed instrument.

### 5.3 OpenCorporates interoperability

OpenCorporates may provide an additional official-source legal-entity reference layer. OpenCorporates has publicly documented BrightQuery’s incorporation of OpenCorporates data alongside other official sources. Where OpenCorporates is used, the record should preserve the underlying jurisdiction/company-number key and the source registry provenance when available.

### 5.4 OpenData.org — Open Global Entity Graph

OpenData.org is proposed as an additional open reference layer for entity grounding and public reproducibility. As of September 2026, OpenData.org describes itself as a nonprofit, open-source global entity directory covering approximately 324 million organizations, 1.2 billion people, 512 million places, and 222 countries, with 162 reference identifiers and records tracing to official public sources. It states that the data is freely downloadable and identifies BrightQuery as an initiating member and seed-data provider.

These counts are provider-reported and may change. DOC-23 therefore treats coverage counts as dated source metadata, not as a conformance requirement. The project should record the dataset release/version, access date, license/terms, source lineage, transformation history, and match result used for a specific entity-resolution decision.

OpenData.org may be useful for public reproducibility because a regulator, researcher, project participant, or member of the public can inspect an open reference graph without depending on a single proprietary terminal. It remains a reference-resolution layer; legal existence, authority, beneficial ownership, licensure, regulatory status, and transaction permission still require the applicable authoritative evidence.

### 5.5 Overture Maps / GERS spatial grounding

Location and address identity should be grounded separately from legal-entity identity. Overture Maps Foundation provides open geospatial data and a Global Entity Reference System (GERS) for stable, resolvable IDs across real-world places and other mapped features. BrightQuery joined Overture Maps Foundation as a General Member in February 2026 and has contributed entity/location data to Overture’s Places work.

For M5, an Overture/GERS identifier may help resolve where a business, public asset, branch, project site, or operating location exists in the physical world and may help reconcile duplicate place records across datasets. A GERS or other spatial identifier does not prove legal ownership, entity authority, regulatory status, title, beneficial ownership, or permission to transact.

### 5.6 Canonical identifier crosswalk

The M5 graph should maintain a versioned crosswalk rather than treating any single vendor identifier as universal. A resolved entity or location may carry multiple identifiers, each with its own source, scope, freshness, and confidence state.

- M5 canonical entity / participant identifier;

- jurisdiction + official company/registration number;

- EIN or other tax identifier where lawfully used and appropriately protected;

- LEI, CIK, NPI, license/registration number, or other regulated identifier where applicable;

- BrightQuery bq_id or equivalent provider key;

- OpenCorporates identifier / jurisdiction-company-number mapping;

- OpenData.org reference / ODC identifier where present;

- Overture GERS identifier for the relevant place/location where present;

- source registry identifier, record version, last-verified timestamp, match method, confidence state, and dispute/correction state.

A canonical crosswalk should support one-to-many and many-to-one relationships, entity mergers/splits, name changes, jurisdiction migrations, successor entities, branch/location changes, and conflicting source records. Identity resolution should fail to REVIEW_REQUIRED when material source conflicts cannot be reconciled.

### 5.7 Data-provider independence

The standard must not hard-code BrightQuery, OpenCorporates, or any single commercial vendor as mandatory infrastructure. A connector is conformant if it can provide the required entity-resolution, source-lineage, freshness, and evidence attributes and can be replaced without breaking the canonical M5/TitleChain record.

### 5.8 Good standing is not sufficient by itself

A company shown as active or in good standing is not automatically approved for a project role. Depending on the role, additional evidence may be required for:

- beneficial/control relationships;
- authority to sign;
- professional or regulatory registration;
- insurance/bonding;
- litigation/bankruptcy/tax status where lawfully relevant;
- sanctions/restrictions;
- project-specific eligibility;
- procurement conflict review;
- investor or financial-instrument qualification;
- fiduciary appointment;
- jurisdiction-specific conditions.

## 6. Source of funds, source of wealth, and capital provenance

### 6.1 Separate concepts

DOC-23 distinguishes:

- **Source of funds (SoF):** the immediate origin of the money used for the specific transaction.
- **Source of wealth (SoW):** how the relevant person/entity accumulated the broader wealth from which funds derive, when such review is required.
- **Capital-provider domicile:** where the investing/lending/grant entity is legally organized.
- **Fund/vehicle domicile:** where an intermediate fund, trust, SPV, or vehicle is organized.
- **Remittance jurisdiction:** jurisdiction of the account/institution from which the funds are transmitted.
- **Beneficial/control jurisdiction:** relevant jurisdictional attributes of controlling/beneficial persons or entities, maintained only to the extent lawful and necessary.
- **Settlement jurisdiction/rail:** jurisdiction and infrastructure governing the payment/settlement leg.
- **Project destination:** jurisdiction where project capital is deployed.
- **Economic-risk jurisdiction:** jurisdiction in which a party ultimately bears economic exposure, where determinable and material.

These attributes should not be collapsed into one “country of funds” field.

### 6.2 Capital provenance path — M5-JCP-001

Each material funding event should produce a **Jurisdictional Capital Provenance Path (JCP)**.

Example — illustrative only:

`Ultimate capital source: SG`  
`→ Fund vehicle: SG`  
`→ Investing entity: US-DE`  
`→ Remitting bank/account jurisdiction: GB`  
`→ Settlement currency/rail: USD / regulated bank rail`  
`→ Project destination: US-CA / Los Angeles`  
`→ Instrument: project debt / preferred / grant / other lawful instrument`  
`→ Use: approved Spring Commons budget category`  
`→ Evidence: source + bank/escrow + instrument + authorization receipts`

The point is not to label the capital “Singaporean,” “British,” or “American” based on a single hop. The point is to make the **lineage reconstructable**.

### 6.3 Minimum capital provenance fields

- capital event ID;
- provider entity ID;
- accountable human/signatory ID;
- entity domicile;
- immediate source-of-funds category;
- fund/SPV/trust nodes, if any;
- relevant parent/control nodes;
- ultimate source evidence status where required;
- remitting institution and jurisdiction;
- receiving bank/escrow and jurisdiction;
- currency and settlement rail;
- amount or public disclosure band;
- instrument and tranche;
- project destination jurisdiction;
- permitted use-of-proceeds category;
- restrictions/conditions;
- required approvals;
- verification status and date;
- public/regulator/private disclosure class;
- authoritative financial record reference;
- TitleChain/M5 evidence receipt;
- correction/reversal/supersession link, if any.

## 7. Jurisdiction Chain and naming

### 7.1 Canonical jurisdiction first

The canonical jurisdiction record should be based on stable jurisdiction identifiers and authoritative jurisdiction metadata. Examples include country codes, state/province codes, territory/tribal/local identifiers, and verified government references.

### 7.2 ICSN JNR

The **ICSN Jurisdiction Naming & Resolution Registry (JNR)** provides the resolution layer between canonical jurisdiction records, project identifiers, TitleChain identifiers, verified government references, and optional external naming adapters.

### 7.3 ENS-style aliases

Aliases such as the following may be used illustratively if actually registered and correctly mapped:

- `singaporechain.eth`
- `japanchain.eth`
- `canadachain.eth`
- `unitedkingdomchain.eth`
- `unitedstateschain.eth`
- `texaschain.unitedstateschain.eth`
- `newyorkchain.unitedstateschain.eth`
- `washingtonchain.unitedstateschain.eth`
- `californiachain.unitedstateschain.eth`

The alias should resolve to the canonical JNR jurisdiction record. **The alias is not evidence of governmental sponsorship or sovereign authority.**

### 7.4 Alias verification states

Every alias should carry a status such as:

- `PROJECT_ALIAS` — project-controlled technical alias;
- `COMMUNITY_ALIAS` — community-maintained reference alias;
- `VERIFIED_EXTERNAL_REFERENCE` — mapped to authoritative external data;
- `GOVERNMENT_VERIFIED` — only when an authorized government body has actually verified/controlled the relationship;
- `REVOKED_OR_STALE` — no longer relied upon.

The default for an ordinary `.eth` project name is **not** `GOVERNMENT_VERIFIED`.

### 7.5 Multi-jurisdiction path

A transaction may traverse multiple jurisdiction nodes without changing the legal identity of the underlying asset or instrument. M5 should preserve the path rather than rewrite the asset according to the payment rail.

## 8. No undisclosed material terms

### 8.1 General rule

No project participant may receive or impose a material economic or control right that is absent from the authoritative transaction graph.

### 8.2 Material terms include, when applicable

- pricing, yield, interest, discount, preferred return, fees, carried interests;
- warrants, options, conversion rights, redemption rights;
- liquidation or payment priority;
- guarantees, puts, calls, floors, caps;
- collateral/security rights;
- veto, consent, governance, observer, appointment, or removal rights;
- revenue shares, royalties, rebates, referral/success fees;
- side payments or in-kind consideration;
- exclusive procurement, preferred-vendor, cloud, data, hardware, software, energy, off-take, or licensing commitments;
- rights of first refusal/offer/negotiation;
- most-favored-nation rights;
- data-use, IP, model-training, commercialization, or exclusivity rights;
- affiliate transactions;
- termination payments;
- contingent benefits tied to future projects or future commons.

### 8.3 Confidential side letters

Side letters are not categorically prohibited. A legitimate confidential side letter may exist for tax, legal, regulatory, commercial, privacy, or institutional reasons. However:

- its existence must be recorded;
- accountable parties must be identified;
- its material economic/control effects must be classified;
- any effect on other participants, priority, project assets, public-benefit obligations, procurement, or governance must be disclosed at the legally appropriate level;
- the authoritative document should have an evidence identifier/digest and access policy;
- it may not be used to silently contradict public deal terms or evade a required approval.

### 8.4 Anti-evasion rule

A material relationship should not become non-material merely because it is split across affiliates, invoices, consulting contracts, rebates, multiple SPVs, token wrappers, or separate project phases. Related events may be aggregated for conflict, concentration, and disclosure analysis.

## 9. Related-party, vendor, and strategic-dependency transparency

Capital providers and beneficial/control affiliates may also sell goods or services to the project. That relationship is not automatically prohibited, but it must be visible and reviewable.

A related-party or strategic-dependency record should capture:

- capital provider / vendor relationship;
- common owners/controllers/board relationships;
- contract value and duration;
- pricing/procurement method;
- competing bids or independent benchmark where applicable;
- exclusivity or minimum-purchase commitments;
- hardware/software/cloud/data/IP dependency;
- financing condition tied to vendor selection;
- conflict review;
- approving authority;
- termination/migration rights;
- concentration and continuity risk.

This protects Spring Commons from accepting capital that quietly obligates the project to purchase affiliated hardware, cloud capacity, software, data, professional services, or other inputs merely to support another participant’s revenue or balance sheet.

## 10. Regulated and fiduciary participant graph

Where the transaction requires regulated or fiduciary actors, the graph should identify the actual selected participant and the scope of its responsibility. Candidate role classes include:

- registered transfer agent;
- broker-dealer / placement agent;
- ATS or exchange, if lawfully applicable;
- bank / escrow / custody provider;
- DTC/DTCC or participant infrastructure if the selected instrument and market pathway actually uses it;
- trustee / fiduciary / trust company;
- CPA / independent auditor;
- tax professional;
- securities and transaction counsel;
- valuation/appraisal professional;
- title/recording professional;
- insurance / surety provider;
- public agency and authorized public official;
- licensed architect/engineer/contractor;
- other regulated specialists required by the asset or instrument.

The record should include registration/license or appointment source, role, scope, good-standing/current status, expiry/renewal, responsible human, conflict status, and system of record.

## 11. Capital-flow state machine

A funding event should progress through explicit states rather than one undifferentiated “paid” flag.

`DISCOVERED`  
`→ ENTITY_RESOLVED`  
`→ AUTHORITY_VERIFIED`  
`→ SOURCE_EVIDENCE_PENDING`  
`→ SOURCE_EVIDENCE_VERIFIED`  
`→ REGULATORY_ROUTING_COMPLETE`  
`→ INSTRUMENT_EXECUTED`  
`→ FUNDS_COMMITTED`  
`→ ESCROW_RECEIVED`  
`→ CONDITIONS_PRECEDENT_SATISFIED`  
`→ DRAW_AUTHORIZED`  
`→ FUNDS_DISBURSED`  
`→ USE_RECONCILED`  
`→ ASSET/MILESTONE_EVIDENCED`  
`→ REPORTING_CURRENT`

Exception states should include:

`HOLD` · `REVIEW_REQUIRED` · `REJECTED` · `REVOKED` · `CORRECTED` · `REVERSED` · `DISPUTED` · `FROZEN` · `MIGRATED`

Every transition should record the authority and evidence that permitted it.

## 12. Regulatory-routing matrix

DOC-23 does not hard-code one universal compliance checklist. Requirements are determined by the actual participant, asset, instrument, jurisdiction, amount, transaction purpose, and regulated function.

The project rule engine may route for additional review when facts trigger areas such as:

- securities offering / transfer restrictions;
- registered transfer-agent functions;
- broker-dealer/placement/ATS/exchange/custody requirements;
- banking, escrow, payment, money-transmission, or custody boundaries;
- KYC/KYB/AML and sanctions controls;
- beneficial-ownership/control review;
- foreign-investment review where legally applicable;
- tax withholding/reporting;
- public procurement/conflict-of-interest rules;
- grant/PRI/tax-credit restrictions;
- historic-preservation/public-conveyance restrictions;
- professional licensing;
- privacy/data-transfer requirements;
- environmental/building/fire/health and other project approvals.

The graph should store the **routing result, responsible reviewer, authoritative source, and current status**, not simply a generic “compliant” label.

## 13. M5Global jurisdictional capital intelligence

### 13.1 Purpose

Once project records are normalized, privacy-protected, and source-linked, they can support a public economic-intelligence layer showing where lawful capital is originating, how it is structured, where it is being deployed, which project categories are attracting capital, and where financing gaps remain.

### 13.2 M5 Global Capital Flow Index — research layer

Working name: **M5 Global Capital Flow Index (M5-GCFI)**.

The M5-GCFI is proposed as a research and economic-intelligence product derived from authorized M5Global / TitleChain evidence. It is **not** a credit rating, investment recommendation, government statistic, securities price index, or regulated trading venue merely because it aggregates data.

Potential public indicators include:

- capital committed / funded by source jurisdiction;
- capital destination by country/state/local project geography;
- public / philanthropic / debt / equity / tax-credit / operating-capital mix;
- sector and productive-infrastructure category;
- instrument class and maturity bands where publishable;
- average time from qualification to funding;
- deal-stage conversion rates;
- transaction-friction metrics;
- local vs. cross-border capital share;
- concentration by provider/affiliate/vendor;
- source-to-destination network paths;
- project pipeline and capital-gap indicators;
- settlement rail and currency aggregates;
- resilience/energy/water/food/compute/public-benefit project categories;
- verified opportunity status by jurisdiction.

### 13.3 Opportunity registry

A public **M5 Opportunity Registry** may expose non-confidential project opportunities using structured status labels such as:

- `RESEARCH`
- `DILIGENCE`
- `PUBLIC_AUTHORITY_PENDING`
- `CAPITAL_FORMATION_DESIGN`
- `QUALIFIED_PARTICIPANTS_SOUGHT`
- `INSTRUMENT_NOT_YET_OFFERED`
- `OFFERING_ACTIVE_ONLY_IF_LAWFULLY_AUTHORIZED`
- `FUNDED`
- `ACTIVATION`
- `OPERATING`
- `CLOSED / ARCHIVED`

Listing an opportunity does not itself constitute an offer of a security or guarantee eligibility to participate.

### 13.4 “Exchange” boundary

The M5 economic architecture may use the term **M5 Global Index and Exchange** as a future concept. DOC-23 requires a strict naming and legal boundary:

- the current **index/intelligence layer** may organize and display public/project data and opportunity metadata;
- it must not be represented as a registered securities exchange, ATS, broker-dealer, transfer agent, custodian, clearing agency, bank, or other regulated venue unless and until the relevant operator has the legally required status and the specific activity is authorized;
- any future order matching, trading, clearing, custody, settlement, or regulated transfer functionality must be separately governed and connected through appropriately authorized participants.

### 13.5 Methodology requirements

Any derived public indicator must carry:

- published methodology;
- source lineage;
- data coverage period;
- update frequency;
- confidence/verification state;
- revision history;
- privacy threshold;
- conflict controls;
- known limitations;
- treatment of missing/stale data;
- methodology version.

### 13.6 Open entity + spatial grounding layer

M5Global should be able to join project and capital-flow records to open reference graphs without making those graphs authoritative for the transaction. OpenData.org can provide open entity-reference joins; OpenCorporates and BrightQuery or equivalent sources can provide additional legal-entity and corporate-family evidence; Overture/GERS can provide stable spatial/place references. The resulting M5 record should preserve which source supported which attribute.

The public value is interoperability: a capital-flow record can be connected to a verified legal entity, its relevant jurisdiction, its physical operating location, its project destination, and its instrument/evidence history using stable reference keys rather than name matching alone. The legal value remains in the authoritative underlying records and the authorized professionals/institutions responsible for the transaction.

### 13.7 Data-license, version, and transformation lineage

Every external dataset used in public analytics or entity resolution should preserve its license/terms, dataset release or snapshot, retrieval date, source lineage, transformations, joins, confidence/match state, and correction history. Open data should not be silently mixed with restricted or proprietary data in a way that makes the resulting public dataset legally unusable or impossible to reproduce.

Where a provider reports changing coverage counts, DOC-23 favors dated dataset metadata over static marketing numbers. Public dashboards should state the applicable snapshot and should not imply that every provider record has been independently verified by M5 or TitleChain.

## 14. Public analytics without misleading origin claims

Capital-origin analytics should support multiple dimensions at once. For example, a project dashboard may show:

- **Provider domicile:** Singapore
- **Fund domicile:** Singapore
- **Investing SPV:** Delaware, United States
- **Remitting institution:** United Kingdom
- **Currency:** USD
- **Destination:** California, United States
- **Project:** Spring Commons LA

A simplified visualization may label this as `SG → US-DE → GB → US-CA`, but the underlying data must explain what each hop means.

The same method applies to domestic paths, such as:

`US-NY capital provider → US-DE vehicle → US-TX project`

or public capital:

`US federal appropriation / grant authority → agency program → US-CA public grantee → Spring Commons eligible use`

This makes trends analyzable without pretending every jurisdiction hop means the same thing.

## 15. Privacy, aggregation, and anti-reidentification controls

Public capital intelligence must not expose protected individuals merely because the graph can resolve them internally.

Controls should include:

- aggregation thresholds for small cohorts;
- amount bands or delayed publication where exact amounts could identify a protected participant;
- separation of public entity identifiers from private personal identifiers;
- role-based access;
- selective disclosure / verifiable status proofs;
- suppression of security-sensitive bank/custody details;
- purpose limitation;
- retention rules;
- correction/challenge/export procedures where applicable;
- audit of who accessed restricted evidence;
- independent privacy/security review.

The public should be able to understand **who the material institutional participants are and how the economics work** without obtaining unrelated personal dossiers.

## 16. Continuous monitoring and credential revocation

Onboarding is not a one-time event. Material changes should trigger re-evaluation.

Monitorable changes may include:

- entity dissolution, merger, conversion, bankruptcy, or loss of good standing;
- ownership/control change;
- authorized signer change;
- professional license/registration lapse or revocation;
- sanctions/restrictions change;
- material litigation or enforcement status when lawfully relevant;
- address/jurisdiction change;
- regulator registration change;
- bank/escrow/custodian relationship change;
- change to side terms, conflicts, or affiliate relationships;
- instrument amendment;
- policy/restriction change;
- material vendor dependency change.

A stale credential must not silently remain executable. M5Canon should fail closed for actions that require current evidence.

## 17. Regulator-ready evidence package

For any material capital event, an authorized reviewer should be able to reconstruct:

1.  **Who** acted — human and entity.
2.  **In what capacity** — M5 account/role and legal authority source.
3.  **For which jurisdiction** — applicable legal and project jurisdictions.
4.  **What capital** — source-of-funds path, instrument, amount/band, restrictions.
5.  **What terms** — controlling instrument and any material side arrangements.
6.  **What approvals** — public, corporate, fiduciary, lender, transfer-agent, counsel, or professional approvals.
7.  **What system executed** — bank/escrow/custody/settlement/transaction system.
8.  **What authoritative record changed** — bank record, project ledger, transfer-agent record, deed/record, contract state, etc.
9.  **What TitleChain/M5 evidence was produced** — state receipt, digest, provenance link, policy version.
10. **What exceptions/corrections occurred** — holds, reversals, corrections, disputes, migrations.
11. **What remains private** — access classification and lawful reason.

A regulator should not need to operate the project’s wallet, node, AI model, private cloud account, or vendor dashboard to understand the transaction history.

## 18. Spring Commons implementation

### 18.1 First-use case

Spring Commons will use DOC-23 to test whether a public asset transaction can expose a complete and reusable economic graph from federal/public authority through capital formation and productive asset activation.

Illustrative lifecycle:

`GSA / federal disposition authority`  
`→ qualifying public grantee and public title`  
`→ approved Public Trust / operator / lease or stewardship structure`  
`→ M5 participant onboarding`  
`→ project/investment instrument`  
`→ regulated/professional participants`  
`→ source-of-funds provenance`  
`→ escrow and milestone draw`  
`→ rehabilitation / productive infrastructure`  
`→ TitleChain asset passports`  
`→ operating revenue / public-benefit metrics`  
`→ investor / public / regulator reporting`

### 18.2 Public capital graph dashboard — proposed

A future public dashboard may show, subject to legal/privacy review:

- committed/funded capital by source jurisdiction;
- project destination;
- instrument category;
- current stage;
- verified participant entities;
- material conflicts/affiliate relationships;
- uses of proceeds;
- funded asset categories;
- transaction timing/friction metrics;
- economic/resilience outputs;
- correction/reconciliation status.

### 18.3 No claim of completed deployment

DOC-23 is an architecture and implementation requirement. It does not represent that BrightQuery, OpenCorporates, any bank, transfer agent, government agency, investor, or named jurisdiction has agreed to participate in Spring Commons.

## 19. SEC S7-2026-30 alignment

DOC-23 is designed as an implementation companion to the TitleChain Foundation’s public-comment architecture concerning the SEC’s proposed Transfer Agent Rules, File No. S7-2026-30 / Release No. 34-106246.

It operationalizes the following concepts from that work:

| **SEC/public-standards concept**               | **DOC-23 implementation**                                                                                     |
|------------------------------------------------|---------------------------------------------------------------------------------------------------------------|
| Human/entity authority root                    | Entity resolution + accountable signer + current authority source                                             |
| Classification before execution                | Actor, asset, instrument, jurisdiction, restriction, regulatory-routing state                                 |
| Credential-bound authority                     | M5-CV references current role/license/registration/appointment evidence                                       |
| Federated technical systems                    | BrightQuery/OpenCorporates/registries/banks/transfer agents remain replaceable systems of record/input        |
| One accountable regulated actor where required | Official transfer-agent/bank/custody/professional responsibilities remain with selected authorized party      |
| Machine-readable restrictions                  | Material deal/transfer/use restrictions linked to legal source and removal authority                          |
| Regulator-ready evidence                       | Exportable authority + capital + terms + event + authoritative-record package                                 |
| Semantic dependency map                        | Affiliates, vendors, banks, agents, jurisdictions, policies, rails, evidence and conflicts become graph edges |
| Privacy-preserving intelligence                | Public jurisdiction/sector/capital indicators without routine disclosure of private human data                |
| Pilot / conformance environment                | Spring Commons provides a public implementation test without claiming regulatory approval                     |

The SEC proposal remains a **proposed rule** unless and until the Commission adopts final rules. This pilot does not claim SEC approval or safe-harbor status.

## 20. Conformance requirements

An implementation claiming DOC-23 conformance should demonstrate:

1.  Every material participant has a canonical entity/person identifier and evidence source.
2.  Every consequential action resolves to current authority and scope.
3.  Every material capital event carries a JCP path.
4.  Material affiliate and related-party relationships are represented.
5.  Material side arrangements cannot silently change project economics/control.
6.  Public, regulator, and protected data planes are enforced.
7.  Alias/jurisdiction records distinguish technical naming from legal authority.
8.  Authoritative external records can be reconciled to TitleChain/M5 evidence.
9.  Corrections/reversals/supersessions are preserved rather than overwritten.
10. Public analytics publish methodology, lineage, revision history, privacy thresholds, and limitations.
11. Vendor/provider substitution is possible without losing canonical provenance/history.
12. Regulator-ready evidence can be exported in documented human- and machine-readable formats.

## 21. Risk factors and limitations

DOC-23 cannot eliminate risk. Relevant risks include:

- inaccurate or stale source data;
- incomplete beneficial/control information;
- legal restrictions on data publication or cross-border transfer;
- false positives/negatives in entity matching;
- mistaken jurisdiction attribution;
- nominee/intermediary opacity;
- forged or compromised credentials;
- shell-company layering designed to evade review;
- conflicted procurement or related-party pricing;
- undisclosed side agreements;
- incomplete regulator integration;
- inconsistent public records;
- change in law or regulatory interpretation;
- privacy leakage through overly granular analytics;
- data-provider outage or licensing change;
- concentration in one identity/entity-data provider;
- misuse of an ENS-style alias as if it were official governmental authority;
- public misunderstanding of an index as a recommendation, rating, or regulated exchange;
- divergence between TitleChain state and authoritative external records.

Where authoritative sources conflict, execution should halt or route to reconciliation according to the project’s M5Canon rules.

## 22. Implementation sequence

### Phase 1 — schema and governance

- adopt DOC-23 fields and edge vocabulary;
- establish JNR canonical jurisdiction records;
- define public/regulator/private data classes;
- define materiality and conflict thresholds;
- define evidence-retention and correction rules.

### Phase 2 — Spring Commons participant graph

- resolve project legal/public entities;
- resolve candidate regulated/professional participant classes;
- onboard authorized humans and current authority evidence;
- create vendor/affiliate/conflict graph;
- establish BrightQuery/OpenCorporates/registry connectors as available.

### Phase 3 — capital graph

- define each capital lane and instrument class;
- capture JCP source/destination path;
- connect escrow/draw events;
- record use of proceeds and funded assets;
- reconcile bank/escrow records to TitleChain evidence.

### Phase 4 — public dashboard / M5Global research

- publish privacy-safe project/capital metadata;
- publish source-to-destination jurisdiction flows;
- publish methodology and limitations;
- measure friction reduction and data quality;
- expose opportunity status without creating an unregistered offering venue.

### Phase 5 — replication

- reuse current credentials and entity graph where legally permitted;
- refresh/reverify stale evidence;
- add new jurisdiction nodes and project chains;
- compare capital movement and opportunity gaps across commons;
- support public/private-sector discovery of lawful projects and service opportunities.

## 23. Machine-readable record profile

A conforming capital-provenance record should be representable as JSON/JSON-LD or an equivalent open format and should include the project, participant, authority, capital, jurisdiction, instrument, restrictions, evidence, privacy class, and event state.

See companion schema:

`schemas/m5-jurisdictional-capital-provenance.schema.json`

and example:

`examples/PPT-EZ-CA-0001-jurisdictional-capital-provenance-example.json`

## 24. Source-chain activation protocol

### 24.1 Activation trigger

A jurisdiction source-chain becomes active for a capital event only after the applicable entity, authority, and source-of-funds evidence has reached the project’s verified state. The chain record is therefore an evidence-backed transaction path, not a marketing tag inferred from a wallet address, domain name, IP address, currency, bank brand, or participant nationality.

For a material funding event, the proposed activation sequence is:

ENTITY_RESOLVED

AUTHORITY_VERIFIED

SOURCE_EVIDENCE_VERIFIED

JURISDICTION_PATH_RESOLVED

REGULATORY_ROUTING_COMPLETE

SOURCE_CHAIN_ACTIVATED

INSTRUMENT_EXECUTED

ESCROW / SETTLEMENT EVENT

DESTINATION_CHAIN_CONFIRMED

USE-OF-PROCEEDS RECONCILED

The SOURCE_CHAIN_ACTIVATED state means the project can publish or expose the permitted jurisdiction-path metadata for that event. It does not mean that a government endorsed the transaction, that a chain alias is an official government record, or that a regulated financial transfer has completed.

Activation should occur independently for each material capital event. A single provider may therefore create multiple source-chain records over time if the source vehicle, remitting institution, instrument, beneficial/control structure, governing law, or destination changes. Historical paths remain versioned rather than being overwritten.

The system should distinguish SOURCE_CHAIN_ACTIVATED from DESTINATION_CHAIN_CONFIRMED. The first means the verified source/jurisdiction path is ready to be represented in the transaction graph; the second means the destination-side authoritative evidence confirms where the funds were legally received or deployed.

### 24.2 Jurisdiction roles within a source chain

Each jurisdiction node must carry a role so users can distinguish why that jurisdiction appears in the path. Recommended roles include:

ULTIMATE_SOURCE_JURISDICTION — where the ultimate economic source is located or organized, when review is required and lawfully determinable.

CAPITAL_PROVIDER_DOMICILE — legal domicile of the investing, lending, granting, or contributing entity.

FUND_OR_VEHICLE_DOMICILE — domicile of a fund, trust, SPV, holding company, or other intermediary.

CONTROL_JURISDICTION — relevant controlling/beneficial ownership jurisdiction where legally required.

REMITTANCE_JURISDICTION — jurisdiction of the sending institution/account.

SETTLEMENT_JURISDICTION — jurisdiction associated with the legally relevant settlement provider or rail.

INSTRUMENT_GOVERNING_JURISDICTION — governing law/jurisdiction of the financing instrument.

PROJECT_DESTINATION_JURISDICTION — jurisdiction in which project capital is deployed.

PUBLIC_AUTHORITY_JURISDICTION — jurisdiction of a public grant, appropriation, conveyance, tax-credit, or other public authority source.

ECONOMIC_RISK_JURISDICTION — jurisdiction in which material economic exposure ultimately resides, where determinable.

A single transaction may therefore activate several jurisdiction nodes. Public analytics should never collapse those roles into a single “country of money” field.

### 24.3 Chain-link event record

Every source-chain hop should preserve at least: canonical jurisdiction ID; jurisdiction role; JNR identifier; optional alias; alias verification state; source entity; destination entity; instrument or payment leg; event time; evidence references; verification/confidence state; public/regulator/private classification; and correction/supersession links.

Illustrative machine path:

SG\[provider\] → US-DE\[vehicle\] → GB\[remittance\] → US-CA\[destination\] → PPT-EZ-CA-0001\[project\]

An alias view may display `singaporechain.eth → unitedstateschain.eth / delaware → unitedkingdomchain.eth → californiachain.unitedstateschain.eth`, but the canonical record remains the JNR/evidence record and each alias must be separately mapped and status-tagged.

## 25. Public-sector and intergovernmental funding provenance

Public money requires a different provenance profile from private capital. A public-source event should preserve the actual legal authority for the funds rather than merely naming the government that transmitted them.

Public-capital fields should include, where applicable:

appropriation, budget, bond, grant, tax-credit, subsidy, public-bank, procurement, or other statutory/program authority;

authorizing legislature, agency, board, authority, or governing body;

program name and fiscal period;

award/resolution/agreement identifier;

eligible recipient and subrecipient chain;

purpose/use restrictions;

matching or cost-share conditions;

draw/reimbursement conditions;

reporting, audit, recapture, clawback, or reversion terms;

responsible public officials and delegated authority;

public payment/treasury/escrow system of record;

destination project and funded asset/milestone.

This allows federal, state, county, municipal, tribal, territorial, and other public capital to appear in the same economic graph as private and philanthropic capital without erasing the different legal authorities that govern public funds.

Illustrative domestic path:

US-FED\[program authority\] → US-CA\[eligible public grantee\] → PPT-EZ-CA-0001\[approved use\] → asset/milestone receipt

Illustrative state path:

US-NY\[public authority or capital source\] → project vehicle / authorized recipient → destination project jurisdiction

## 26. Cross-border capital and jurisdiction review

Cross-border source chains should trigger rule-based review rather than a blanket assumption that foreign capital is permitted or prohibited. The actual legal requirements depend on the participant, asset, instrument, activity, source, destination, regulated function, and current law.

Potential review domains include, where actually applicable:

KYC/KYB, beneficial ownership, source-of-funds/source-of-wealth, AML and sanctions requirements;

securities offering, solicitation, resale, transfer, broker-dealer, transfer-agent, ATS/exchange, custody, and investor-eligibility rules;

banking, payment, foreign-exchange, escrow, custody, money-transmission, and settlement requirements;

tax residence, withholding, information reporting, treaty, FATCA/CRS or analogous obligations where applicable;

foreign-investment/national-security review where the actual asset, rights, parties, or transaction trigger such review;

public-procurement, grant, tax-credit, public-benefit-conveyance, historic-preservation, or government-funding restrictions;

data-localization, privacy, cross-border data-transfer, records-retention, and regulator-access requirements;

anti-bribery, conflicts, political-exposure, fiduciary, and public-integrity controls where applicable.

DOC-23 does not predetermine which of these regimes applies. It requires the system to record the routing question, authoritative source, responsible reviewer, determination, effective date, and evidence state before a regulated or restricted action proceeds.

## 27. M5 capital intelligence and forecasting governance

### 27.1 Observation before prediction

The first M5Global capital-intelligence layer should prioritize verified observed facts: where capital was sourced, through what structures and rails it moved, where it was deployed, how long qualification and closing took, what restrictions applied, what assets or services were activated, and what corrections occurred.

Only after the observed dataset is sufficiently complete may the system publish derived trend, gap, scenario, or forecast products. Derived analysis must never be displayed as if it were an authoritative transaction fact.

### 27.2 Public/private-sector analytical uses

Subject to lawful access, privacy controls, methodology, and data quality, possible analytical products include:

inbound and outbound capital flow by jurisdiction and project category;

cross-border and interstate capital corridors;

capital-source mix by grants, PRI, debt, equity, tax credits, public funds, operating capital, and other lawful classes;

verified project pipeline and capital-gap indicators;

time-to-qualification, time-to-close, and transaction-friction measures;

capital concentration, related-party concentration, and service-provider concentration;

renewal/replication rates for verified participants across projects;

sector demand for energy, water, food, compute, housing, preservation, infrastructure, education, or other project classes;

local procurement and workforce participation;

currency, settlement-rail, and conversion aggregates;

public-private/philanthropic co-investment patterns;

regional opportunity discovery for lawful capital providers and service providers.

### 27.3 Forecast and inference labels

Every non-observed analytical output should carry a label such as OBSERVED, ESTIMATED, MODELED, SCENARIO, or FORECAST. It should include methodology/version, source period, confidence/uncertainty, known exclusions, revision history, and a statement that the output is not an investment recommendation, valuation, credit rating, government forecast, or guarantee.

Predictive outputs should not infer protected traits about individuals or expose restricted beneficial-owner, bank, wallet, or identity information.

### 27.4 Index methodology governance

The M5-GCFI and related indices should be independently reproducible from documented inputs where practicable. Methodology changes should be versioned, dated, explained, and applied prospectively or with clearly labeled historical restatement. Conflicts of interest should be disclosed where an index operator, data provider, project sponsor, capital provider, or service provider could benefit from the resulting indicator.

Public users may infer trends from published observations, but the system should never present correlation as proof of motive, beneficial control, creditworthiness, investment quality, or government policy. Model-generated forecasts should be separated from observed transaction evidence and should identify the input period, assumptions, methodology version, and uncertainty.

Where a jurisdiction or participant has too few events for safe publication, the public layer should aggregate, delay, band, or suppress the data to reduce re-identification, confidentiality, market-manipulation, and misleading-small-sample risk.

## 28. Public opportunity discovery and capital routing boundary

The M5 Opportunity Registry may help the public and private sector discover verified projects, open procurement needs, capital requirements, service opportunities, and current project status. Search and discovery may be organized by jurisdiction, sector, project class, capital need, stage, credential requirement, and public-benefit category.

A discovery layer should distinguish at minimum:

PUBLIC_INFORMATION_ONLY — public research / no transaction invitation;

PARTICIPANTS_SOUGHT — builders, vendors, reviewers, or service providers sought;

CAPITAL_DESIGN — capital structure under development / no offer;

QUALIFICATION_OPEN — participant credentialing or diligence open, subject to applicable law;

OFFERING_OR_TRANSACTION_ACTIVE — only when a lawful instrument and authorized parties actually support that status;

FUNDED / ACTIVATING / OPERATING — capital or operations in progress;

CLOSED / ARCHIVED — no current participation pathway.

The present “M5 Global Index and Exchange” concept should therefore be implemented in stages: registry and intelligence first; opportunity discovery second; regulated transaction functions only through operators and intermediaries that possess the registrations, licenses, approvals, exemptions, and supervisory controls required for the specific activity.

The system may route a qualified participant to an authorized bank, broker-dealer, registered transfer agent, ATS/exchange, custodian, escrow provider, public procurement portal, grant process, or other lawful execution venue. M5/TitleChain should preserve the permission and evidence state without falsely representing the public intelligence layer itself as the regulated venue.

## 29. Reference sources and project relationships

### Public sources

- U.S. Securities and Exchange Commission — Transfer Agent Rules, Release No. 34-106246, File No. S7-2026-30: `https://www.sec.gov/rules-regulations/2026/09/s7-2026-30`
- BrightQuery public data architecture / coverage / KYB materials: `https://brightquery.com/` and `https://docs.brightquery.com/`
- OpenCorporates article documenting BrightQuery’s use of OpenCorporates data and official-source provenance: `https://blog.opencorporates.com/2021/12/06/understanding-small-businesses-why-you-need-data-from-official-sources/`
- OpenCorporates legal-entity data documentation: `https://knowledge.opencorporates.com/`

- OpenData.org — Open Global Entity Graph / Open Directory of Entities: https://opendata.org/ (coverage and partner statements accessed September 19, 2026).

- Overture Maps Foundation — BrightQuery membership/contribution announcement (February 25, 2026): https://overturemaps.org/announcements/2026/brightquery-joins-overture-maps-foundation-to-expand-open-places-data-coverage/

- Overture Maps Foundation — GERS / open spatial data documentation: https://overturemaps.org/ and https://docs.overturemaps.org/

### Related Spring Commons documents

- DOC-01 — Master Deal Term Sheet
- DOC-05 — Investor Executive Brief
- DOC-06 — Capital Escrow and Draw Agreement
- DOC-10 — TitleChain Evidence and Digital Records Schedule
- DOC-11 — Private Offering / PPM Framework
- DOC-12 — Subscription Agreement and Investor Questionnaire
- DOC-15 — Master Risk Factors and Disclosure Schedule
- DOC-16 — M5Canon Master Ricardian and Machine Policy Standard
- DOC-17 — Authority, Jurisdiction and Source-of-Truth Matrix
- DOC-19 — Federated Registry / Governance Agreement
- DOC-20 — M5-CV Credential, Privacy and Zero-Knowledge Manifest
- DOC-21 — Project Benchmark and Performance Methodology
- DOC-22 — State-to-Entity Due Process Channel Standard

## 30. One-sentence public rule

> Know the human. Resolve and ground the entity. Verify the authority. Trace the capital. Activate the evidence-backed jurisdiction path. Disclose the material terms. Protect private data. Record the authoritative result. Then make the public economic graph useful without turning transparency into surveillance or an unregulated market.

**TitleChain / M5Canon \| U.S. Patent Nos. 11,720,888 & 12,518,273 \| Public Commons: TitleChain Foundation / ICSN \| github.com/TitleChain-Foundation \| titlechainfoundation.org**

## 31. Appendix A — Minimum public capital-flow dashboard fields

A conforming public dashboard should expose only fields that are lawful and appropriate for public disclosure, and should make clear which values are observed, inferred, delayed, aggregated, or withheld.

project ID, project name, project jurisdiction, and current project stage;

capital event count and aggregated amount/band by source-jurisdiction role;

provider/fund/remittance/destination jurisdiction path at the permitted aggregation level;

instrument class and capital-source class;

public/private/philanthropic/tax-credit/operating-capital mix;

current verification state and last refresh date;

material public related-party or strategic-dependency flags;

use-of-proceeds category and funded asset category;

transaction timing and friction metrics;

public-benefit/productive-infrastructure category;

correction, reversal, dispute, or stale-data flag;

methodology version, source coverage, confidence label, and revision date.

The dashboard should provide drill-through to public evidence references where lawful, while regulator-only and private evidence remains protected.

## 32. Appendix B — Example jurisdiction aliases and canonical roles

The following names are illustrative technical aliases only. They are not representations of government control, sponsorship, or official status:

`singaporechain.eth` → canonical JNR record for Singapore, alias status PROJECT_ALIAS unless separately verified;

`japanchain.eth` → canonical JNR record for Japan;

`canadachain.eth` → canonical JNR record for Canada;

`unitedkingdomchain.eth` → canonical JNR record for the United Kingdom;

`unitedstateschain.eth` → canonical JNR record for the United States;

`texaschain.unitedstateschain.eth` → canonical JNR record for Texas;

`newyorkchain.unitedstateschain.eth` → canonical JNR record for New York;

`washingtonchain.unitedstateschain.eth` → canonical JNR record for Washington;

`californiachain.unitedstateschain.eth` → canonical JNR record for California.

If an alias is unavailable, unregistered, disputed, stale, or controlled by an unrelated party, the system must continue to operate from the canonical JNR record and verified government references. Alias availability must never determine legal authority.

## 33. Appendix C — Capital-source taxonomy

For analytics, capital should be classified independently from jurisdiction. Suggested classes include:

PUBLIC_GRANT / APPROPRIATION

PHILANTHROPIC_GRANT

PROGRAM_RELATED_INVESTMENT

HISTORIC_TAX_CREDIT_CAPITAL

NMTC_OR_OTHER_TAX_CREDIT_CAPITAL

COMMERCIAL_DEBT

MISSION_ALIGNED_DEBT

PROJECT_EQUITY_OR_PREFERRED_CAPITAL

TENANT_OR_OPERATOR_CAPITAL

VENDOR_FINANCING

PUBLIC_BANK_OR_DEVELOPMENT_FINANCE

INSURANCE_OR_SURETY_SUPPORTED_CAPITAL

COMMUNITY_OR_MEMBER CAPITAL — only where lawfully structured;

OPERATING_REVENUE_REINVESTMENT

OTHER_LAWFUL_CAPITAL — with explicit classification and evidence.

The taxonomy should not determine legal characterization. Securities, tax, accounting, banking, public-finance, and other legal classifications remain controlled by applicable law and qualified professional determinations.

## 34. Appendix D — Entity-reference crosswalk fields

For each material entity or location used in the graph, the project should preserve a source-aware identifier crosswalk. Suggested fields include:

- M5 canonical entity/location ID;

- canonical legal name and known historical/DBA names;

- jurisdiction and official registration/company number;

- public regulatory identifiers where applicable (for example LEI or CIK);

- BrightQuery bq_id or equivalent provider key;

- OpenCorporates identifier / registry mapping;

- OpenData.org reference / ODC identifier where available;

- Overture GERS ID for physical place/location where available;

- source record URI or source-system key;

- dataset release/version and retrieval timestamp;

- match method: exact identifier / authoritative crosswalk / deterministic composite / probabilistic candidate;

- match confidence and reviewer state;

- valid-from / valid-to / superseded-by fields;

- dispute, correction, merge, split, relocation, or successor-entity state.

## 35. Appendix E — Source-chain activation evidence gate

A source chain should not move to SOURCE_CHAIN_ACTIVATED until the project can answer, at the level required for the transaction:

- Which legal entity is providing the capital?

- Which accountable human or governing body has authority to commit it?

- What is the source-of-funds evidence and, where required, source-of-wealth evidence?

- What fund/SPV/trust/holding-company path sits between ultimate source and project?

- Which jurisdiction role applies to each hop?

- Which bank/escrow/custody/settlement record is authoritative for the financial leg?

- Which instrument and material restrictions govern the capital?

- Are any capital provider, affiliate, vendor, equipment, cloud, data, procurement, or revenue relationships related parties or strategic dependencies?

- Are side arrangements present, and if so is their material effect represented in the graph?

- What regulatory routing is required before the next action?

- What information may be public, regulator/assurance only, or private/protected?

- What evidence receipt and version establish that this activation state is current?

If any required answer is unresolved, stale, disputed, or contradicted by an authoritative source, the state should route to HOLD or REVIEW_REQUIRED rather than SOURCE_CHAIN_ACTIVATED.

## 36. Appendix F — Open-reference data governance

Open entity and location data improves reproducibility but does not remove the need for source governance. For every external open dataset used in M5Global or Spring Commons analytics, preserve:

- dataset/provider name and responsible publisher;

- license and attribution obligations;

- release/snapshot identifier and access date;

- original source lineage when published;

- transformations, filters, joins, conflation, and deduplication performed by the project;

- match-confidence method and threshold;

- known coverage gaps and stale-data risks;

- correction/challenge process;

- privacy and redistribution limits;

- whether the field is authoritative evidence, reference evidence, derived analytics, or model inference.

OpenData.org, OpenCorporates, BrightQuery, Overture/GERS, and future connectors should therefore plug into M5 as interchangeable evidence/reference sources under common provenance rules, rather than becoming the authority root themselves.
