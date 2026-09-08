# Value Instrument and Jurisdiction Model

**Status: Draft design basis for public review**

A governance receipt must identify what form of value was used, how its amount
was denominated, and which external authorities and standards support any
legal or regulatory classification. These are separate facts.

## 1. Instrument identity

The receipt must identify the instrument type without converting an internal
label into a legal conclusion.

Supported categories should include:

- sovereign fiat currency;
- retail central bank digital currency;
- wholesale central bank digital currency;
- tokenized commercial-bank deposit;
- payment or fiat-referenced stablecoin;
- commodity-referenced stable-value token;
- crypto-collateralized stable-value token;
- algorithmic or other stable-value token;
- cryptoasset;
- tokenized security or financial instrument, when externally classified;
- tokenized real-world asset or claim;
- non-currency credit, point, or accounting unit.

The record should include, where applicable:

- issuer and issuer legal-entity reference;
- network and contract or native-asset identifier;
- Digital Token Identifier or another authoritative asset identifier;
- issue, version, and effective dates;
- reserve assets, reserve custodian, and attestation references;
- redemption right, redemption party, terms, and settlement period;
- transfer restrictions and eligible-holder rules;
- official classification and registration references.

The category records what the instrument purports or is determined to be. It
does not itself establish that the instrument is money, legal tender, a
security, a commodity, a deposit, or lawfully issued.

## 2. Value and denomination

The receipt must distinguish the settlement instrument from the unit used to
express value.

Examples:

- a stablecoin transferred on a blockchain but denominated in USD;
- a tokenized deposit denominated in EUR;
- a cryptoasset valued in USD for accounting without being USD or legal tender;
- a commodity-backed token valued by a quantity and unit of the commodity;
- a non-currency provider credit measured in service units.

An ISO 4217 currency code identifies a currency or fund denomination. Its use
does not establish that a referenced token is itself sovereign currency,
legal tender, insured money, or a central-bank liability.

The record should therefore include:

- `amount_type`;
- `amount`;
- `denomination_kind`;
- `denomination_code` and standards reference;
- `settlement_instrument_ref`;
- valuation source and timestamp when amount and settlement instrument differ;
- exchange-rate source and rate when conversion occurred.

## 3. Authority and jurisdiction basis

Any legal-status field must be supported by an external authority record, not
an M5 inference. Applicable authorities may include:

- sovereign or federal nation;
- state, province, canton, or equivalent subdivision;
- recognized Tribe, Tribal Nation, or Indigenous Nation;
- territory or possession;
- county, municipality, or local authority;
- central bank or monetary authority;
- financial, banking, securities, commodities, payments, tax, or sanctions
  regulator;
- court, legislature, official registry, or other competent authority;
- supranational or intergovernmental body within its actual mandate.

Jurisdictions must be represented as an applicable-authority graph rather than
an assumed hierarchy. Tribal, territorial, state, federal, local, and
supranational authority may be concurrent, independent, limited by subject
matter, or governed by treaties, compacts, statutes, regulations, and judicial
decisions.

Each authority assertion should record:

- authority type and canonical external identifier;
- jurisdiction and subject-matter scope;
- governing instrument, law, rule, order, charter, treaty, compact, or registry;
- the precise status asserted;
- effective and expiration dates;
- authoritative source URI or document reference;
- verification method and verification timestamp;
- status such as asserted, verified, registered, authorized, recognized,
  exempt, restricted, prohibited, disputed, expired, or unknown.

The word `approved` must not appear without identifying who approved what,
under which authority, for which jurisdiction, and for what period.

## 4. Standards references

Standards identifiers support interoperability; they do not grant legal status.
Relevant references may include:

- ISO 4217 for currency and funds codes;
- ISO 24165 for Digital Token Identifiers;
- ISO 10962 for Classification of Financial Instruments codes;
- ISO 17442 for Legal Entity Identifiers;
- ISO 20022 for financial-message definitions;
- ISO 3166 and UN M49 for country or area identification;
- UN/LOCODE for trade and transport locations;
- UN/CEFACT specifications for electronic trade data.

UN geographic, trade, or data standards do not constitute UN approval of a
currency, stablecoin, CBDC, cryptoasset, government, or sovereign claim. IMF,
BIS, UN, or other intergovernmental analysis or guidance must be labeled by its
actual function and must not be represented as authorization unless the body
has the legal mandate and has issued an authoritative decision.

## 5. Required legal-status safeguards

- A CBDC designation requires an authoritative central-bank or monetary-
  authority source.
- A legal-tender designation requires an authoritative source of law.
- A payment-stablecoin designation must identify the applicable statutory or
  regulatory definition and issuer status.
- A deposit or insured-deposit designation requires the responsible depository
  institution and authoritative legal or insurance basis.
- A security, commodity, or other regulated-instrument designation requires
  the applicable legal source or competent-authority determination.
- A value reference or price peg does not make a token the referenced currency.
- An M5 classification does not create recognition, approval, title,
  citizenship, governmental authority, monetary status, or transfer rights.
- Conflicting or incomplete authority records must produce an unresolved or
  disputed status and must not be silently converted into approval.
