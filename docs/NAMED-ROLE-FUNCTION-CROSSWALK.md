# Named M5 Role and Function Crosswalk

**Status:** Draft for Public Comment  
**Scope:** Functional mapping only; not an activation, deployment, endorsement,
credential, or legal-status registry

## 1. Reading this crosswalk

This crosswalk gives memorable M5 role names a bounded, machine-readable
function. It does not establish that an implementation exists, is active, is
safe, has passed conformance, or is authorized for a particular person,
institution, instrument, or jurisdiction.

The authoritative fields for consequential operations are the canonical
function identifier, implementation identity, accountable operator, current
credentials, explicit delegation, applicable jurisdiction, deterministic
policy, required approvals, and evidence receipt.

No named role is a principal. No role may approve itself or expand its own
authority.

## 2. Accountable human origin

Human founders, members, operators, officers, and other accountable people are
not agents and must not be placed in an agent activation chain as software
components.

Public architecture should use the generic term **accountable M5HUM or lawful
entity**. Private histories may identify particular people only after privacy,
authority, provenance, and publication review.

## 3. Core named-role mapping

| Named role | Canonical bounded function | Plain-language purpose | Non-authority boundary |
| --- | --- | --- | --- |
| Satonaka | `M5CAP.PROVENANCE.SOURCE.ANALYZE.v1` | Examines source, repository, document, and authorship evidence | Cannot create authorship, ownership, or permission |
| Cyrus | `M5CAP.RIGHTS.CONSTRAINT.EVALUATE.v1` | Evaluates proposed actions against protected-rights constraints | Cannot create, remove, or waive rights |
| Savant | `M5CAP.PROVENANCE.CONTINUITY.VALIDATE.v1` | Validates origin, custody, transformation, attribution, continuity, and integrity across a provenance chain | Cannot grant approval or independently declare legal truth |
| Milner | `M5CAP.ACCOUNT.COGNITIVE_BOUNDARY.PROTECT.v1` | Protects the account's identity, knowledge, cognitive, policy, and operational boundary across BOM, BOU, BOB, BOI, and BOG | Cannot replace M5Canon or become the source of authority |
| Liberti | `M5CAP.ACCESS.RIGHTS_CHECK.v1` | Checks access and exit conditions against approved rights policy | Cannot create access rights or override lawful restrictions |
| Grace | `M5CAP.COMPUTE.PROFILE.VERIFY.v1` | Measures hardware, runtime, and sovereign-compute capabilities | Cannot certify hardware or authorize settlement without the required process |
| Louisa | `M5CAP.ENTITY.GOVERNANCE.ASSIST.v1` | Assists entity registration and governance workflows | Cannot form, register, or govern an entity without accountable legal action |
| Vionneta | `M5CAP.PROVENANCE.EVIDENCE.ATTEST.v1` | Records and anchors evidence origin, attribution, transformations, and integrity so the provenance chain can be inspected | Cannot independently establish title, authorship, or legal standing |
| Odea | `M5CAP.DATA.VAULT.PROTECT.v1` | Applies approved storage, retention, access, and recovery controls | Cannot take ownership of member data or change consent |
| 23andMine | `M5CAP.PERSONAL.HEALTH_WORKFLOW.ASSIST.v1` | Assists member-controlled health and genetic workflows | Cannot diagnose, consent, disclose, or authorize secondary use |
| Rosalind | `M5CAP.CONSENT.CONSTRAINT.ENFORCE.v1` | Enforces recorded consent and protected-data constraints | Cannot infer consent or expand a consent scope |
| Rowboat | `M5CAP.SYSTEM.NAVIGATION.ASSIST.v1` | Helps members navigate institutions and complex systems | Cannot act as the institution or make a binding decision |
| Martha | `M5CAP.COMMUNICATION.ALERT.ROUTE.v1` | Routes approved alerts and coordination messages | Cannot create emergency, governmental, or command authority |
| Lina | `M5CAP.RUNTIME.ORCHESTRATE.v1` | Coordinates approved services, models, networks, and workflows | Cannot authorize the work it orchestrates |
| Green | `M5CAP.ECONOMIC.ANALYZE.v1` | Analyzes economic conditions and possible consequences | Cannot issue, allocate, transfer, or move value |
| Borsetta | `M5CAP.CAPITAL.ACCESS.ANALYZE.v1` | Analyzes capital-access and community-finance options | Cannot promise funding, determine eligibility, or approve credit |
| Valoris | `M5CAP.VALUATION.ANALYZE.v1` | Produces bounded valuation analysis and evidence | Cannot set authoritative value or replace a qualified valuation |
| Nash | `M5CAP.INCENTIVE.OUTCOME.MODEL.v1` | Models incentives and possible equilibrium effects | Cannot determine rights, obligations, or binding contract terms |
| Lenore | `M5CAP.EXPERIENCE.ATTENTION.PROTECT.v1` | Applies approved attention and human-experience safeguards | Cannot infer consent or make medical or psychological determinations |
| Sophia | `M5CAP.CAPABILITY.LEARNING.MATCH.v1` | Matches declared skills, training, and role requirements | Cannot award credentials, employment, licensure, or authority |
| Mira | `M5CAP.ONBOARDING.NAVIGATE.v1` | Guides members through approved onboarding paths | Cannot approve identity, eligibility, or activation |
| Justitia | `M5CAP.DISPUTE.ANALYZE_AND_ROUTE.v1` | Organizes disputes, evidence, and available resolution paths | Is not a court, tribunal, or binding adjudicator |
| Dagny | `M5CAP.PUBLIC.WORKFLOW.ASSIST.v1` | Assists public communication, builder support, and approved workflows | Cannot bind a person or organization or make an official representation without delegation |
| Paine | `M5CAP.RECORD.PLAIN_LANGUAGE.EXPLAIN.v1` | Explains complex records in accessible language | The explanation is not the authoritative record or legal advice |
| DeepThought | `M5CAP.POLICY.COMPLEXITY.ANALYZE.v1` | Analyzes complex, multi-policy questions | Cannot resolve legal conflicts or issue binding interpretations |
| Satonaka-Repo | `M5CAP.REPOSITORY.INTEGRITY.VERIFY.v1` | Checks repository provenance, integrity, and release evidence | Cannot establish ownership or approve publication |
| Otonoma | `M5CAP.CYBERPHYSICAL.ACTION.ORCHESTRATE.v1` | Coordinates approved devices and cyber-physical workflows | Cannot cause physical action without explicit actuator authorization and safety controls |
| Sharprivin | `M5CAP.PORTFOLIO.STRATEGY.ANALYZE.v1` | Produces bounded portfolio and strategy analysis | Cannot trade, advise, allocate, or deploy capital without applicable authority |

## 4. Public data and index services

Public-facing services are not automatically agents.

| Reference service | Canonical function | Boundary |
| --- | --- | --- |
| Atlas | `M5CAP.INDEX.MULTISECTOR.AGGREGATE.v1` | Produces an attributable index calculation, not official economic truth |
| M5Node | `M5CAP.INDEX.MEMBER_COST.CALCULATE.v1` | Calculates a defined member cost measure, not an official government CPI |
| M5Scan | `M5CAP.ASSET.PUBLIC_RECORD.EXPLORE.v1` | Presents indexed public records, not authoritative title or legal status |

Each index must publish its methodology, sources, revision policy, uncertainty,
conflicts, and operator. The word "global," "public," or "sovereign" does not
make an index an official statistic of a government or intergovernmental body.

## 5. External implementations and provider-facing names

An external provider, product, standards body, agency, university, hospital, or
company must not be shown as an active M5 role merely because its service could
support a function.

Public materials may describe a potential function interface, but must record:

- provider or organization identity;
- relationship status;
- enrollment and verification status;
- authoritative evidence for any claimed relationship;
- scope and effective period;
- non-endorsement statement;
- suspension and revocation state.

Compatibility, API access, a commercial account, public documentation, or a
useful product does not establish participation or endorsement.

## 6. Required implementation states

Public registries should use evidence-based lifecycle states rather than one
ambiguous `active` label:

1. `CONCEPTUAL`
2. `SPECIFIED`
3. `IMPLEMENTED`
4. `TESTED`
5. `DEPLOYED`
6. `AUTHORIZED`
7. `SUSPENDED`
8. `REVOKED`
9. `RETIRED`

`DEPLOYED` does not mean `AUTHORIZED`. `TESTED` does not mean safe or legally
approved. `AUTHORIZED` must identify the accountable authority, scope,
jurisdiction, policy, evidence, and effective period.
