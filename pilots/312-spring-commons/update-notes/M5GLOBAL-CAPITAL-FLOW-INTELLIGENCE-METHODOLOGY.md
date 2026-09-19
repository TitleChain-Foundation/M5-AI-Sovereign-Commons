# M5Global Capital-Flow Intelligence — Working Methodology v0.6

**Status:** Draft research methodology / public review  
**Project anchor:** PPT-EZ-CA-0001 / 312 Spring Commons  
**Related:** DOC-23 / M5-CAPGRAPH-001  
**Date:** September 19, 2026

## Purpose

Define how privacy-protected TitleChain/M5 transaction evidence and external reference data may be transformed into reproducible public economic intelligence without turning the registry into a surveillance database, credit rating, investment recommendation, government-statistics substitute, or unregistered exchange.

The research layer is intended to answer questions such as: **Where is verified capital originating, through which lawful structures is it moving, where is it being deployed, what kinds of productive assets or public projects are receiving it, and where are verified opportunity gaps emerging?**

## Working outputs

- **M5 Global Capital Flow Index (M5-GCFI)** — research indicators for capital source/destination, instrument mix, deal-stage movement, productive-asset activation, and transaction friction.
- **M5 Opportunity Registry** — structured project/opportunity status metadata, not an offering venue.
- **Jurisdiction flow maps** — canonical JNR source-to-destination paths with distinct jurisdiction roles.
- **Entity + place graph views** — canonical M5 entities cross-referenced to official identifiers and optional BrightQuery, OpenCorporates, OpenData.org, Overture/GERS, and other reference IDs.
- **Sector / productive-infrastructure indicators** — energy, water, food, compute, housing/space, workforce, preservation, public infrastructure, and other project categories.
- **Process indicators** — time, cost, reconciliation, credential reuse, correction, and regulatory-routing metrics.

## Evidence hierarchy

Analytics must distinguish four classes:

1. **Authoritative evidence** — legally controlling government records, executed agreements, regulated books/records, bank/escrow records, licenses, court orders, or other records with controlling legal effect in their domain.
2. **Reference evidence** — BrightQuery, OpenCorporates, OpenData.org, Overture/GERS, directories, public datasets, and other sources useful for entity or place resolution but not inherently authoritative for legal authority.
3. **Derived analytics** — values calculated from evidence under a published methodology.
4. **Model inference** — statistical or AI-generated estimates, classifications, scenarios, or forecasts that are not observations.

No reference source, model output, wallet, domain name, or chain alias may silently be promoted into legal authority.

## Open entity + spatial grounding

A material participant may be represented by one canonical M5/TitleChain identifier while maintaining a versioned crosswalk to other identifiers where available, including:

- official company/registration number and jurisdiction;
- EIN, LEI, CIK, or professional/regulatory identifiers where applicable;
- BrightQuery identifier;
- OpenCorporates jurisdiction/company-number reference;
- OpenData.org reference identifier;
- Overture/GERS place/location identifier;
- JNR jurisdiction identifier;
- technical aliases such as `.eth` names.

Each crosswalk should preserve provider/source, dataset release or retrieval timestamp, match method, match confidence, reviewer state, correction history, valid-from/valid-to state, and successor/supersession links.

OpenData.org coverage figures or other provider counts are **dated external-source metadata**, not conformance requirements and not permanent facts inside M5.

## Source-chain activation

`SOURCE_CHAIN_ACTIVATED` is a controlled evidence state, not a claim that a financial transfer has settled or that a destination has received funds.

Minimum preconditions should include, as applicable:

- legal capital-provider entity resolved;
- accountable signer/governing authority verified;
- relevant M5 role/credential state current;
- source-of-funds evidence verified and source-of-wealth review completed where required;
- material fund/SPV/trust/holding-company path resolved;
- jurisdiction role for each material hop resolved;
- instrument and restrictions identified;
- material affiliate/vendor/related-party relationships reviewed;
- material side-arrangement existence/effect represented in the graph;
- required regulatory/professional routing completed or explicitly pending;
- applicable privacy/disclosure class assigned;
- versioned evidence receipt produced.

If a required element is stale, disputed, contradictory, or unresolved, the state should route to `HOLD` or `REVIEW_REQUIRED` rather than `SOURCE_CHAIN_ACTIVATED`.

`DESTINATION_CHAIN_CONFIRMED` is separate and requires destination-side authoritative evidence that the funds were legally received or deployed as represented. Settlement finality, title change, investment performance, and use-of-proceeds reconciliation are still separate states.

## Capital-origin dimensions

Do not publish a single ambiguous “country of funds” field. Distinguish:

1. ultimate source jurisdiction where required and lawfully determinable;
2. provider entity domicile;
3. fund/trust/SPV domicile;
4. control/beneficial jurisdiction where required and lawful;
5. remitting account/institution jurisdiction;
6. settlement/custody jurisdiction;
7. currency and settlement rail;
8. instrument governing-law jurisdiction;
9. project destination jurisdiction;
10. public-authority jurisdiction;
11. economic-risk jurisdiction where determinable and material.

A single transaction may legitimately touch several jurisdictions. Public analytics should preserve these roles rather than collapsing them into a nationality label.

## Canonical jurisdiction model

- Use canonical country/state/province/territory/tribal/local identifiers.
- Resolve through ICSN JNR or another documented canonical mapping.
- ENS-style names are optional technical aliases/adapters.
- Alias status must be explicit.
- Default `.eth` aliases are **not government-verified** and do not imply affiliation, delegated authority, sovereignty, or control of an official government domain.
- Historical jurisdiction mappings and corrections should be versioned rather than overwritten.

## Public-sector capital provenance

Public or intergovernmental funding requires its own authority lineage, including when applicable:

- appropriating/awarding authority;
- program or statutory basis;
- fiscal period and award/resolution identifier;
- permissible-use restrictions;
- matching or co-funding conditions;
- procurement rules;
- reporting/audit/clawback conditions;
- accountable public official or governing body;
- destination and expenditure evidence.

A state or national jurisdiction label does not itself prove that a government supplied or approved funds.

## Publication rules

Every public indicator should publish or link to:

- methodology version;
- data coverage dates;
- dataset/provider snapshots and access dates;
- update cadence;
- source-lineage classes;
- evidence eligibility rules;
- verification/confidence state;
- revision/correction history;
- privacy threshold/suppression rule;
- conflict-of-interest policy;
- treatment of missing/stale/disputed/corrected data;
- aggregation or banding method;
- known limitations.

## Observation vs inference

Every analytic output should carry one of these labels:

- `OBSERVED`
- `ESTIMATED`
- `MODELED`
- `SCENARIO`
- `FORECAST`

A geographic or network correlation must not be presented as proof of motive, control, creditworthiness, project quality, government policy, investment merit, or suitability without separate evidence and an appropriate methodology.

## Privacy and anti-reidentification

- Aggregate, band, delay, or suppress values where exact publication could identify protected participants or expose confidential negotiations.
- Establish minimum cohort thresholds before publishing small-sample jurisdiction, sector, or participant statistics.
- Delay publication when real-time disclosure could create security, privacy, market-integrity, procurement, or negotiation risk.
- Do not publish raw KYC/KYB files, account credentials, protected beneficial-owner personal data, private keys, suspicious-activity information, precise security-sensitive locations, or confidential architecture.
- Preserve regulator/qualified-assurance access to underlying evidence where legally appropriate.
- Public dashboards should expose the minimum facts necessary to support reproducibility and accountability.

## External dataset governance

For each external dataset or connector used, preserve:

- provider/publisher;
- license and attribution requirements;
- release/snapshot and access date;
- original source lineage when available;
- transformations, filters, joins, conflation, and deduplication;
- match-confidence method/threshold;
- known coverage gaps/staleness;
- correction/challenge process;
- redistribution/privacy constraints;
- whether each field is authoritative, reference, derived, or inferred.

This permits BrightQuery, OpenCorporates, OpenData.org, Overture/GERS, and future connectors to remain replaceable rather than becoming proprietary authority roots.

## Quality / provenance states

Suggested states include:

- `DISCOVERED`
- `ENTITY_RESOLVED`
- `AUTHORITY_VERIFIED`
- `SOURCE_EVIDENCE_PENDING`
- `SOURCE_EVIDENCE_VERIFIED`
- `JURISDICTION_PATH_RESOLVED`
- `REGULATORY_ROUTING_COMPLETE`
- `SOURCE_CHAIN_ACTIVATED`
- `INSTRUMENT_EXECUTED`
- `FUNDS_COMMITTED`
- `ESCROW_RECEIVED`
- `CONDITIONS_PRECEDENT_SATISFIED`
- `DRAW_AUTHORIZED`
- `FUNDS_DISBURSED`
- `DESTINATION_CHAIN_CONFIRMED`
- `USE_RECONCILED`
- `ASSET_MILESTONE_EVIDENCED`
- `REPORTING_CURRENT`
- `HOLD`
- `REVIEW_REQUIRED`
- `REJECTED`
- `REVOKED`
- `CORRECTED`
- `REVERSED`
- `DISPUTED`
- `FROZEN`
- `MIGRATED`

A public indicator may be computed only from states permitted by the methodology version.

## Opportunity Registry boundary

Opportunity metadata may describe project stage, location, asset class, public-benefit category, procurement/service needs, research needs, or capital-formation status. Suggested status vocabulary:

- `PUBLIC_INFORMATION_ONLY`
- `PARTICIPANTS_SOUGHT`
- `CAPITAL_DESIGN`
- `QUALIFICATION_OPEN`
- `OFFERING_OR_TRANSACTION_ACTIVE` — only when actual lawful documents and authorized participants support that status
- `FUNDED`
- `ACTIVATING`
- `OPERATING`
- `CLOSED`
- `ARCHIVED`

The registry does not itself constitute an offer, recommendation, suitability decision, market listing, or guarantee that a participant is eligible to transact.

## “Index and Exchange” boundary

The term **M5 Global Index and Exchange** may describe the long-term architecture, but implementation should proceed in stages:

1. registry and verified evidence;
2. public/private economic intelligence;
3. opportunity discovery and qualified routing;
4. regulated transaction functions **only through legally authorized operators and venues**.

The current research/index layer does not perform regulated exchange, ATS, broker-dealer, transfer-agent, custody, clearing, banking, money-transmission, settlement, or investment-advisory functions. Any future regulated function requires the actual registrations, licenses, approvals, exemptions, supervision, and authorized operator required for the specific activity.

## Spring Commons initial metrics

- percent of material capital with complete JCP paths;
- percent of funding events reaching `SOURCE_CHAIN_ACTIVATED` without manual exception;
- percent separately reaching `DESTINATION_CHAIN_CONFIRMED`;
- committed/funded amounts by source/destination jurisdiction, subject to privacy thresholds;
- instrument mix;
- public/private/philanthropic/tax-credit capital mix;
- time from entity resolution to capital eligibility;
- time from commitment to escrow/draw;
- number of repeated entity-data requests avoided through reusable current credentials;
- external-ID crosswalk coverage and match-review rate;
- related-party/vendor concentration;
- capital-to-productive-asset mapping completeness;
- reconciliation/correction/dispute rate;
- public evidence coverage;
- privacy-suppression rate;
- dataset/version lineage completeness.

## Interpretation rule

The intelligence layer should help users ask **where verified capital is moving, what it is funding, through which lawful structures, and where opportunity or infrastructure gaps appear**. It should not tell a person what to buy, assign a political conclusion, infer motive from geography, or state that a project is safe or suitable merely because its data are visible.
