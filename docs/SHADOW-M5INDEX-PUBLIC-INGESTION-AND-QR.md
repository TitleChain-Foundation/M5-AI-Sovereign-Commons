# SHADOW M5Index — Public Ingestion, Asset Steward & QR Architecture

**Status:** Engineering implementation specification
**Repository:** `TitleChain-Foundation/M5-AI-Sovereign-Commons`
**Suggested path:** `docs/SHADOW-M5INDEX-PUBLIC-INGESTION-AND-QR.md`

---

# 1. Objective

Build a public contribution system for SHADOW M5Index that allows people to:

1. discover an asset;
2. choose a research sector;
3. nominate a new asset;
4. add evidence to an existing asset;
5. upload or link public records;
6. help resolve title, ownership, debt, rights, environmental, and disposition questions;
7. receive a permanent evidence receipt;
8. track review status;
9. maintain a local asset record over time.

Initial priority sectors:

- **Government Buildings & Land**
- **Commercial Real Estate**
- **Farmland**

The public website should be the simple front door.

The GitHub repository should be the open technical source of truth.

---

# 2. Public front door

Create a SHADOW landing page with three primary cards:

```text
SHADOW M5Index

[ GOVERNMENT BUILDINGS & LAND ]
Public buildings, federal land, surplus property,
public-benefit conveyances, dispositions and auctions.

[ COMMERCIAL REAL ESTATE ]
Office, retail, industrial, multifamily and other CRE,
including debt, maturity, servicing and distress.

[ FARMLAND ]
Agricultural land, operators, leases, mortgages,
water/mineral rights, conservation and title state.
```

Each card opens a filtered index.

Suggested routes:

```text
https://titlechainfoundation.org/shadow/government
https://titlechainfoundation.org/shadow/cre
https://titlechainfoundation.org/shadow/farmland
```

Generic index:

```text
https://titlechainfoundation.org/shadow
```

---

# 3. Report links

The SHADOW CAMEL Report should contain three clickable sector buttons:

```text
EXPLORE GOVERNMENT BUILDINGS & LAND
EXPLORE COMMERCIAL REAL ESTATE
EXPLORE FARMLAND
```

Each button should open the appropriate public index filter.

Do not send ordinary readers directly to raw GitHub data.

The website is the public interface.

The repo is the audit/evidence layer.

---

# 4. Permanent Asset ID

Every asset receives one stable canonical identifier:

```text
SHD-000001
SHD-000002
SHD-000003
...
```

Existing `SHD-001` identifiers can remain valid.

Do not encode meaning into the identifier.

Category, state, jurisdiction, owner and status can change.

The Asset_ID must not.

---

# 5. Permanent asset URL

Each Asset_ID receives a permanent public URL:

```text
https://titlechainfoundation.org/shadow/assets/SHD-029
```

Optional readable slug:

```text
https://titlechainfoundation.org/shadow/assets/SHD-029/spring-street-courthouse
```

The Asset_ID is authoritative.

The slug is decorative and may change.

If the asset name changes, the QR code still works.

---

# 6. QR code rule

Generate one QR code for every canonical asset.

The QR must encode only the permanent public Asset URL.

Example:

```text
QR-SHD-029
→ https://titlechainfoundation.org/shadow/assets/SHD-029
```

Do not encode:

- ownership data;
- personal data;
- deed text;
- wallet addresses;
- scores;
- temporary report URLs.

Those data may change.

The QR should point to the permanent record.

---

# 7. QR file layout

Create:

```text
shadow-m5index/
└── qr/
    ├── SHD-001.svg
    ├── SHD-001.png
    ├── SHD-002.svg
    ├── SHD-002.png
    └── ...
```

Create a registry:

```text
shadow-m5index/registry/qr-registry.json
```

Example:

```json
{
  "asset_id": "SHD-029",
  "canonical_url": "https://titlechainfoundation.org/shadow/assets/SHD-029",
  "qr_svg": "qr/SHD-029.svg",
  "qr_png": "qr/SHD-029.png",
  "created_at": "2026-09-22",
  "status": "active"
}
```

QR generation should be deterministic.

Rebuilding the QR directory should produce the same URL for the same Asset_ID.

---

# 8. Core repository structure

Create:

```text
shadow-m5index/
├── README.md
│
├── registry/
│   ├── assets.jsonl
│   ├── asset-index.csv
│   ├── asset-index.json
│   └── qr-registry.json
│
├── data/
│   ├── canonical/
│   │   ├── government/
│   │   ├── cre/
│   │   └── farmland/
│   │
│   ├── submissions/
│   │   ├── new-assets/
│   │   └── evidence/
│   │
│   └── archived/
│
├── evidence/
│   ├── metadata/
│   └── manifests/
│
├── schemas/
│   ├── asset.schema.json
│   ├── government-asset.schema.json
│   ├── cre-asset.schema.json
│   ├── farmland-asset.schema.json
│   ├── evidence-submission.schema.json
│   ├── title-state.schema.json
│   ├── debt-state.schema.json
│   ├── rights.schema.json
│   ├── environmental-state.schema.json
│   └── contributor-receipt.schema.json
│
├── methodology/
│
├── qr/
│
├── scripts/
│   ├── validate_records.py
│   ├── build_index.py
│   ├── generate_qr.py
│   ├── build_completeness.py
│   └── promote_submission.py
│
├── public/
│   ├── government/
│   ├── cre/
│   └── farmland/
│
└── tests/
```

---

# 9. Asset classification

Add a required field:

```json
"sector": "government"
```

Allowed initial values:

```text
government
cre
farmland
```

Allow future sectors without changing Asset_ID.

Examples:

```json
{
  "asset_id": "SHD-029",
  "sector": "government",
  "asset_type": "courthouse"
}
```

```json
{
  "asset_id": "SHD-101",
  "sector": "cre",
  "asset_type": "office"
}
```

```json
{
  "asset_id": "SHD-205",
  "sector": "farmland",
  "asset_type": "agricultural_land"
}
```

---

# 10. Common asset schema

Every sector inherits a common base record.

Required or recommended fields:

```text
Asset_ID
Sector
Asset_Name
Asset_Type
Address
City
County
State
Postal_Code
Country
Latitude
Longitude

Parcel_ID
Legal_Description
Jurisdiction

Current_Owner
Recorded_Grantee
Ownership_Resolution_State
Sponsor
Ultimate_Capital

Disposition_State
Transaction_Proof_State

Title_Verification_State
Title_Source
Title_Instrument_ID

Rights_State
Encumbrance_State
Claims_State
Obligations_State
Environmental_State

Debt_State
Current_Lender
Servicer
Maturity_Date

M5MST_State

TSI
DSI
ASI
DPI
OOI
CCI
PVMI
PBOI

Evidence_State
Last_Verified
Completeness_Pct
Open_Questions
```

---

# 11. Government Buildings & Land extension

Government records should support:

```text
Government_Level
Originating_Agency
Current_Agency
GSA_Location_Code
GSA_Control_Number
Case_Number
Sale_Number

Federal_Property_Status
Excess_Status
Surplus_Status

Public_Benefit_Eligibility
Public_Benefit_Window_Open
Public_Benefit_Window_Close

Disposition_Authority
Disposition_Method
Auction_Open_Date
Auction_Close_Date
Award_Date
Closing_Date

Historic_Status
Public_Use_Restrictions
Reversionary_Interest
Preservation_Covenant

Annual_Operating_Cost
Deferred_Maintenance
Avoided_Capital_Cost
Vacancy
Occupancy
```

Public page actions:

```text
ADD FEDERAL / PUBLIC ASSET
ADD DISPOSITION RECORD
ADD DEED
ADD PUBLIC-BENEFIT PROGRAM
ADD RESTRICTION / COVENANT
ADD ENVIRONMENTAL RECORD
NOMINATE FOR PEOPLE'S TRUST REVIEW
```

---

# 12. Commercial Real Estate extension

CRE records should support:

```text
Property_Type
Building_Count
Year_Built
Rentable_SF
Gross_SF
Vacant_SF
Occupancy_Pct

NOI
Appraised_Value
Observed_Value

Borrower
Original_Lender
Current_Lender
Loan_Balance
Interest_Rate
Maturity_Date
LTV
DSCR

CMBS_Trust
Master_Servicer
Special_Servicer

Modification_State
Extension_State
Default_State
Foreclosure_State
Receivership_State
REO_State

Note_Buyer
Current_Owner
```

Public page actions:

```text
ADD CRE ASSET
ADD LOAN
ADD ASSIGNMENT
ADD SERVICER
ADD MATURITY
ADD MODIFICATION
ADD FORECLOSURE
ADD NEW OWNER
ADD VALUATION / APPRAISAL SOURCE
```

---

# 13. Farmland extension

Farmland records should support:

```text
Total_Acres
Tillable_Acres
Irrigated_Acres
Pasture_Acres

Current_Operator
Owner_Operator_Relationship
Lease_State

Crop_Type
Agricultural_Use

Soil_Classification
Water_Rights
Irrigation_Rights
Mineral_Rights
Pipeline_Rights
Utility_Easements

Conservation_Easements
Government_Program_Restrictions

Mortgage
Lender
Maturity_Date

Environmental_State
Drainage_State
Flood_State

Corporate_Farming_Restrictions
Foreign_Ownership_Restrictions
State_Agricultural_Restrictions

Operator_Continuity
Public_Benefit_Opportunity
```

Public page actions:

```text
ADD FARM / LAND
ADD OPERATOR
ADD LEASE
ADD WATER RIGHT
ADD MINERAL RIGHT
ADD PIPELINE / EASEMENT
ADD MORTGAGE
ADD CONSERVATION RECORD
ADD AGRICULTURAL RESTRICTION
```

---

# 14. Public asset page

Every Asset_ID page should use the same layout.

Example:

```text
SHD-029
SPRING STREET COURTHOUSE
Los Angeles, California

[ GOVERNMENT ]

STATUS
Federal disposition watch

RESEARCH COMPLETION
43%

TITLE STATE
SOURCE LOCATED

OWNERSHIP
Federal / GSA

DEBT
Not yet resolved

RIGHTS / OBLIGATIONS
Partial

ENVIRONMENT
Review required

PEOPLE'S TRUST
Under review
```

Then:

```text
[ ADD EVIDENCE ]
[ TAKE A RESEARCH TASK ]
[ NOMINATE / COMMENT ]
[ DOWNLOAD RECORD ]
```

And QR code:

```text
[ QR ]
Scan to open this permanent asset record
```

---

# 15. Research checklist

Each asset page should show a completion checklist.

Example:

```text
ASSET IDENTITY
✅ Address
✅ Agency
✅ Asset type

TITLE
🟡 Parcel ID
🟡 Current deed
⬜ Prior deed
⬜ Restrictions

OWNERSHIP
✅ Recorded owner
⬜ Sponsor
⬜ Ultimate capital

DEBT
⬜ Mortgage
⬜ Current lender
⬜ Maturity
⬜ Release / satisfaction

RIGHTS
⬜ Easements
⬜ Mineral rights
⬜ Water rights
⬜ Pipeline rights

ENVIRONMENT
⬜ EPA check
⬜ State environmental check
⬜ Remediation obligations

DISPOSITION
✅ Listed
✅ Sale method
⬜ Award
⬜ Closing
⬜ Recorded transfer
```

A contributor chooses one missing item.

---

# 16. Do not make people edit GitHub

The ordinary public contributor should never need to understand Git, JSON, or pull requests.

Public flow:

```text
WEBSITE
↓
SELECT SECTOR
↓
SELECT ASSET
or
ADD NEW ASSET
↓
SELECT EVIDENCE TYPE
↓
UPLOAD / LINK
↓
SUBMIT
```

Engineering flow:

```text
FORM SUBMISSION
↓
submission JSON
↓
schema validation
↓
submission ID
↓
evidence receipt
↓
review queue
↓
agent extraction
↓
human/source verification
↓
PR to canonical data
↓
merge
↓
index rebuild
↓
asset page update
```

---

# 17. Public contribution forms

Create four main form actions:

## A. Add a new asset

Fields:

```text
Sector
Asset name
Address / location
Why it belongs in SHADOW
Government agency / owner if known
Parcel ID if known
Source URL
Upload
Contributor notes
```

## B. Add evidence to an existing asset

Required:

```text
Asset_ID
Evidence_Type
Source_Agency
Source_URL
Document_Date
Recorded_Date
Instrument_Number
Upload_or_Link
Claim_Supported
Contributor_Notes
```

## C. Correct an existing record

Required:

```text
Asset_ID
Field_Being_Challenged
Current_Value
Proposed_Correction
Supporting_Source
Evidence
```

## D. Nominate for People's Trust review

Required:

```text
Asset_ID
Community
Proposed_Public_Benefit
Why_Review_Is_Warranted
Known_Local_Partners
Public_Source
```

Nomination does not create an ownership, financing or investment right.

---

# 18. GitHub Issue Forms for immediate V0.1

Before a full web application exists, use GitHub Issue Forms.

Create:

```text
.github/ISSUE_TEMPLATE/
├── shadow-new-asset.yml
├── shadow-add-evidence.yml
├── shadow-correction.yml
└── shadow-peoples-trust-nomination.yml
```

This allows ingestion to begin immediately.

The public website can link to those forms.

Later, replace the GitHub-facing UX with a native web form while keeping the same schemas.

---

# 19. Submission identifiers

Every submission receives:

```text
SUB-2026-000001
SUB-2026-000002
...
```

Every evidence item receives:

```text
EVD-2026-000001
EVD-2026-000002
...
```

Example:

```json
{
  "submission_id": "SUB-2026-000245",
  "asset_id": "SHD-029",
  "evidence_id": "EVD-2026-000883",
  "status": "SUBMITTED"
}
```

---

# 20. Evidence files

Do not place large binary files directly into the normal Git history when avoidable.

The canonical repo should store:

```text
evidence metadata
document hash
source URL
official instrument number
recording office
retrieval date
file location / public archive reference
```

Example:

```json
{
  "evidence_id": "EVD-2026-000883",
  "asset_id": "SHD-029",
  "type": "deed",
  "source_office": "Los Angeles County Recorder",
  "instrument_number": "XXXXXXXX",
  "recorded_at": "YYYY-MM-DD",
  "source_url": "...",
  "sha256": "...",
  "evidence_state": "SOURCE_VERIFIED"
}
```

Small public documents may be preserved where licensing allows.

Large documents should use approved object/file storage while the repo retains the manifest and hash.

---

# 21. Evidence workflow

Canonical states:

```text
SUBMITTED
↓
SOURCE_VERIFIED
↓
CORROBORATED
↓
CANONICAL
```

Also support:

```text
UNRESOLVED
DISPUTED
REJECTED
CORRECTED
SUPERSEDED
```

No public form directly writes `CANONICAL`.

---

# 22. Research steward roles

Allow contributors to adopt a research role.

Possible roles:

```text
LOCAL STEWARD
TITLE STEWARD
DEBT STEWARD
ENVIRONMENTAL STEWARD
RIGHTS STEWARD
CAPITAL STEWARD
FARMLAND STEWARD
HISTORIC STEWARD
```

A steward maintains the evidence record.

A steward does not acquire ownership or decision authority over the asset.

---

# 23. Adopt an Asset Record

Public CTA:

# ADOPT AN ASSET RECORD

Meaning:

> Help maintain the public research record for one asset.

Not:

> Adopt or acquire the actual property.

Display on asset page:

```text
CURRENT RESEARCH STEWARDS

Local:
open

Title:
open

Debt:
open

Environmental:
Jane D.

Rights:
open
```

---

# 24. QR use cases

Each Asset_ID QR can be used in:

- SHADOW reports;
- social cards;
- printed field sheets;
- community meetings;
- university research projects;
- county-record research packets;
- property site visits;
- presentations;
- People's Trust feasibility documents.

A scan should always open the current canonical public record.

---

# 25. QR plus task parameter

The permanent QR points only to the asset.

For campaigns, optional URLs may add a non-authoritative query parameter.

Example:

```text
https://titlechainfoundation.org/shadow/assets/SHD-029?action=add-evidence
```

or:

```text
?action=title
?action=environment
?action=debt
```

The underlying Asset_ID remains the same.

---

# 26. Category-specific report QR codes

The SHADOW report can also contain three sector QR codes:

```text
QR-GOV
→ /shadow/government

QR-CRE
→ /shadow/cre

QR-FARM
→ /shadow/farmland
```

Then each featured property receives its own Asset_ID QR.

That produces two layers:

```text
SECTOR QR
→ discover assets

PROPERTY QR
→ maintain one asset
```

---

# 27. Data ingestion pipeline

V0.1:

```text
GitHub Issue Form
↓
manual / agent triage
↓
submission JSON
↓
validation
↓
PR
↓
human review
↓
merge
↓
build index
```

V0.2:

```text
TitleChain Foundation web form
↓
submission API
↓
object storage for files
↓
submission JSON
↓
GitHub PR / review queue
↓
canonical merge
```

V1:

```text
Automated public feeds
+
citizen evidence
+
professional review
↓
SHADOW graph
```

---

# 28. Automated feed connectors

Build connectors after manual ingestion is stable.

Priority:

## Government

```text
GSA accelerated disposition
RealEstateSales.gov
GSA press releases
FRPP / IOLP
HUD Title V
NPS / federal public-benefit programs
```

## CRE

```text
County recorder
County assessor
SEC EDGAR ABS-EE
FFIEC
FDIC BankFind
planning / zoning feeds
foreclosure notices
```

## Farmland

```text
County recorder
County assessor / GIS
USDA
state agriculture departments
state water databases
state mineral records
conservation easement registries
planning / zoning
```

Every automated import remains evidence-linked.

---

# 29. Do not auto-promote scraped data

Automated ingestion may create:

```text
SOURCE_LOCATED
```

or:

```text
SUBMITTED
```

It must not create:

```text
CANONICAL
```

without the required verification policy.

---

# 30. Completeness score

Every asset page should calculate:

```text
Research Completion
```

Example:

```text
Asset identity       100%
Title                 50%
Ownership             70%
Debt                   0%
Rights                20%
Environment           40%
Disposition          100%
Evidence              62%
```

Overall:

```text
RESEARCH COMPLETION: 55%
```

This is not TSI.

It is simply dataset completeness.

---

# 31. Priority queues

Create public queues:

```text
MOST INCOMPLETE
NEWLY LISTED
PUBLIC-BENEFIT WINDOW
BUYER UNKNOWN
LENDER UNKNOWN
TITLE RECORD NEEDED
ENVIRONMENTAL REVIEW
RIGHTS UNRESOLVED
FARMLAND WATER RIGHTS
CRE MATURITY WATCH
```

That tells volunteers exactly where effort is needed.

---

# 32. Public-benefit alert

For government assets, create a distinct status:

```text
PUBLIC_BENEFIT_WINDOW:
OPEN
```

Display prominently:

```text
PUBLIC-BENEFIT REVIEW WINDOW OPEN

Help document:
- eligible uses
- local public entities
- nonprofit partners
- title restrictions
- community need
```

Do not state that a People's Trust is automatically eligible.

Eligibility must be resolved under the applicable disposition program.

---

# 33. M5 / TitleChain integration

A public submission does not directly alter TitleChain Asset State.

Flow:

```text
PUBLIC SUBMISSION
↓
SHADOW EVIDENCE RECORD
↓
verification
↓
canonical claim
↓
TitleChain Asset State event
↓
M5Index update
```

Example:

```text
EVD-2026-000883
DEED FOUND

↓ verified

TITLE_EVENT:
CURRENT_DEED_SOURCE_VERIFIED

↓ recompute

TSI updated
SHADOW page updated
```

---

# 34. M5 Global integration

Public-safe aggregate events may later feed M5 Global Index and Exchange.

Examples:

```text
government assets entering disposition
acreage entering sale
CRE debt nearing maturity
farmland ownership changes
water-right changes
liens released
environmental obligations identified
assets entering public-benefit review
```

Do not publish private M5POD records.

---

# 35. GitHub Actions

Create:

```text
.github/workflows/shadow-validate.yml
```

Run on every SHADOW PR.

Tests:

```text
schema validation
Asset_ID uniqueness
submission ID uniqueness
evidence ID uniqueness
required source fields
no private fields
valid state enums
valid evidence states
valid cross-record Asset_ID references
QR registry completeness
no canonical claim without evidence
```

Also create:

```text
.github/workflows/shadow-build-index.yml
```

On merge:

```text
build CSV
build JSON
build JSONL
recalculate completeness
generate QR codes
build public index manifests
```

---

# 36. V0.1 public launch

Do not wait for the full application.

Launch with:

1. SHADOW README;
2. 36 seed properties;
3. Government / CRE / Farmland category pages;
4. GitHub Issue Forms;
5. Add Evidence button;
6. stable Asset_ID URLs;
7. QR codes;
8. contributor queue;
9. completeness checklist;
10. weekly promoted canonical updates.

This is sufficient to begin public ingestion.

---

# 37. Suggested first QR set

Generate property QRs immediately for the seed records.

Priority:

```text
SHD-029 Spring Street Courthouse
SHD-030 Fort Worth Federal Center
SHD-031 Fritz G. Lanham Federal Building
SHD-033 Celebrezze Federal Building
SHD-034 Goodfellow Federal Facility
SHD-035 Federal Center South
SHD-036 Bozeman Federal Building
SHD-021 Hawkinsville AFSSS
SHD-009 Big Spring mineral rights
SHD-018 Racine SSA
```

Then generate the remaining canonical asset QRs automatically.

---

# 38. Public instructions

Keep the public language simple:

## FIND THE ASSET.

Choose Government, CRE, or Farmland.

## FIND ONE RECORD.

Deed. Mortgage. Easement. Environmental record. Assignment. Sale notice. Public-benefit document.

## ADD THE EVIDENCE.

Upload it or link the authoritative source.

## WE VERIFY IT.

Submissions do not overwrite the public record.

## THE INDEX IMPROVES.

Every verified record updates the public knowledge graph.

---

# 39. Public CTA

# Find the asset. Find the record. Add the evidence.

SHADOW M5Index gives communities a shared place to assemble public records, understand what an asset actually is, trace the debt and ownership behind it, identify rights and obligations that travel with it, and evaluate lawful public-benefit pathways before an opportunity disappears.

---

# 40. Engineering build order

## PR 1
Create directory structure and schemas.

## PR 2
Import 36 seed assets into canonical JSON/JSONL.

## PR 3
Build three sector indexes:
Government / CRE / Farmland.

## PR 4
Implement evidence submission schema and GitHub Issue Forms.

## PR 5
Implement asset detail Markdown/JSON generation.

## PR 6
Implement stable canonical URLs and QR registry.

## PR 7
Generate QR images for all seed assets.

## PR 8
Implement completeness calculation and contributor task queues.

## PR 9
Implement validation GitHub Action.

## PR 10
Wire TitleChain Foundation website to index pages and contribution forms.

## PR 11
Add automated source connectors.

---

# 41. Definition of done

V0.1 is ready when a member of the public can:

1. click Government, CRE or Farmland;
2. browse assets;
3. open one property;
4. see what is known and unknown;
5. scan or share its QR;
6. choose one missing research task;
7. upload/link an authoritative record;
8. receive a submission/evidence ID;
9. see the contribution enter review;
10. later see verified evidence incorporated without losing provenance.

---

# 42. Canonical principle

> **The public does not edit the truth. The public contributes evidence to the record.**

SHADOW verifies, versions, and preserves the evidence chain.

**Find the asset. Find the record. Add the evidence.**
