# M5 OpenAPI Early Access and Demand Pilot

**Status: Proposed public demand test — no production paid API is claimed by this repository**

The fastest way to prove demand is to measure real interest and real usage
before overbuilding a marketplace.

The TitleChain Foundation Commons can publish the open interface, schemas,
evidence rules, and test fixtures. A commercial M5Bank or other accountable
operator may separately offer paid access under its own terms, pricing,
licensing, compliance, billing, settlement, and support obligations.

## Initial demand products

The first products should be narrow and easy to explain:

1. **Asset State** — normalized public-safe asset identity, title-state,
   ownership-state, disposition-state, and provenance references.
2. **Evidence Bundle** — source references and evidence-state metadata for a
   specific asset claim.
3. **Debt / Encumbrance Research** — public-safe debt, lien, assignment,
   maturity, and evidence state where lawfully available.
4. **Change Events** — machine-readable updates when a verified public record or
   research state changes.
5. **SHADOW Derived Research** — published or separately licensed derived
   indicators with clear methodology and confidence boundaries.
6. **M5Canon Evaluation** — separately priced deterministic policy/authority
   evaluation by an authorized commercial deployment; never represented as a
   legal opinion.

## Demand signal to collect

For each prospective user, capture only public/business-safe information:

- organization / role;
- use case;
- asset sector;
- geography;
- endpoint requested;
- expected monthly calls;
- latency requirement;
- historical/bulk-data need;
- webhook need;
- desired evidence state;
- willingness to join a paid pilot;
- preferred billing mode;
- requested start date.

Do not collect private keys, nonpublic transaction evidence, personal financial
records, or confidential counterparty data in a public GitHub issue.

## What counts as demand

Track progressively stronger evidence:

```text
page view
→ documentation read
→ GitHub issue / form submission
→ API key request
→ test call
→ repeated call
→ paid pilot
→ recurring paid usage
→ enterprise commitment
```

The primary proof should be **paid or contracted usage**, not social engagement.

## Pilot operating modes

1. `METER_ONLY` — free test users; measure behavior and cost.
2. `REFERENCE_PRICE_ONLY` — show or internally compute a hypothetical price.
3. `PAID_DESIGN_PARTNER` — small number of customers billed manually or through
   an approved payment rail while product fit is validated.
4. `X402_TEST` — machine payment on synthetic/test endpoints.
5. `X402_LIVE` — selected production endpoints only after reconciliation,
   refund, licensing, security, and accounting controls are operating.

## Commercial boundary

Do not sell public-source documents merely because they are publicly
accessible. Confirm the source terms and any redistribution limits.

The commercial value should come from lawful normalization, provenance,
freshness, state tracking, derived analysis, workflow integration, support,
service levels, and authorized machine access.

## Metrics for a first 30-day demand report

Publish aggregate, privacy-safe metrics such as:

- number of API access requests;
- unique organizations;
- sectors represented;
- requested monthly call volume;
- most requested data products;
- test calls;
- repeat users;
- paid pilots;
- recurring revenue;
- aggregate M1 API/data revenue;
- aggregate M2/M3 asset value touched by those workflows where disclosure is
  permitted;
- aggregate M4 instrument value touched where disclosure is permitted;
- average data/compute cost per successful response; and
- gross margin before human review.

## Call to action

Use the public Early Access issue form for non-confidential product interest.
Commercial terms, private deployment facts, production credentials, and
confidential data must move to an appropriate private channel.
