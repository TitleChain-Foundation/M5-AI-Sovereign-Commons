# Biological Stewardship Registry — From Land Registry to Living Systems

**Status:** Draft public-review extension to America's People's Trust Farmland
**Project context:** AG-PILOT-001 / ND-FARM-SIM-001
**Reference implementation 001:** [Sovereign Herd](../norton-ranch-blueprint/sovereign-herd/README.md)

## Caretaking covenant

The registry begins from the view that human beings are **caretakers and stewards** of the places and living systems entrusted to us.

A parcel, herd, crop, hive, forest edge, lake, wetland or trail may sit inside a legal or operational boundary, but the registry should never imply that law, title or technology gives human beings unlimited moral authority over the life within that boundary.

The purpose of these records is to make care more durable: to preserve knowledge, document responsibility, protect continuity, support restoration, improve animal and ecological welfare, and help the next steward understand what came before.

The same principle extends beyond farms. Over time, this framework can describe stewardship relationships involving soils, forests, oceans, rivers, lakes, wetlands, watersheds, habitat, public trails and other shared natural systems where humans have a duty of care even when no private ownership claim exists.

A working farm does not end at the parcel boundary.

The farmland registry establishes the property, authoritative source-of-truth references, lawful stewardship and operating authority. The Biological Stewardship Registry extends that architecture to the living systems being raised, grown, managed or cared for on the land.

It is an evidence and stewardship layer. It does not claim that every living organism is legally titled property, that every biological relationship is ownership, or that an M5 record replaces government, veterinary, agricultural, food-safety, livestock-identification or other authoritative records.

## Reference relationship

```text
AUTHORITATIVE LAND / PROPERTY RECORD
        ↓
LAWFUL OWNER / STEWARD / OPERATOR
        ↓
FARM BUSINESS ENTITY
        ↓
FARM / PARCEL / FIELD / OPERATING AREA
        ↓
BIOLOGICAL STEWARDSHIP REGISTRY
        │
        ├── LIVESTOCK
        │    ├── individual animal
        │    ├── herd / flock
        │    └── breeding / production group
        │
        ├── CROPS
        │    ├── field / crop cycle
        │    ├── seed or planting lot
        │    └── harvest / storage lot
        │
        ├── ORCHARD / VINEYARD
        │    ├── block
        │    └── individual plant where useful
        │
        ├── APIARY
        │    └── hive / colony
        │
        └── OTHER MANAGED BIOLOGICAL SYSTEMS
             └── granularity appropriate to the use case
                ↓
OBSERVATIONS / CARE / PRODUCTION / PROVENANCE
                ↓
DEVICES / SENSORS / LOCAL MODELS
                ↓
PRIVATE FARM M5POD / LOCAL DATA ENVIRONMENT
```

## Core principle

**The land record tells us where lawful stewardship and operating authority begin. The biological record tells us what living systems are being managed there and what evidence the lawful operator chooses to maintain about them.**

## Granularity

The registry MUST NOT assume one record per organism.

The appropriate unit depends on the biological system, legal environment and operational purpose.

| System | Example registry unit |
| --- | --- |
| Cattle | Individual animal, herd, breeding group |
| Sheep/goats | Individual animal where required; otherwise flock/group |
| Poultry | Flock, house, production group, or individual where justified |
| Potatoes | Field/crop cycle, seed lot, harvest lot |
| Wheat/corn/soy | Field/crop cycle, seed lot, harvest lot |
| Orchard | Orchard, block, variety group, individual tree where useful |
| Vineyard | Block/row/variety group |
| Bees | Apiary, hive, colony |
| Nursery/greenhouse | Batch, bench, variety/lot |
| Soil microbiology/research | Sample, zone, study cohort; never implied organism ownership |

## Minimum record relationship

A Biological Stewardship record should be able to identify:

- `record_ref`
- accountable `entity_ref`
- associated `land_ref` or operating-area reference
- `subject_type`
- `granularity`
- species/variety where applicable
- local identifier or lot identifier
- lifecycle or production state
- steward/operator authority reference
- private evidence reference
- provenance and timestamps
- device/sensor relationships where applicable
- public-safe projection policy

## Individual-animal example

```text
LAND / FARM
   ↓
HERD
   ↓
COW 1847
   ├── persistent animal record
   ├── collar assignment history
   ├── observations
   ├── breeding/care evidence
   ├── production events
   └── transfer or lifecycle events
```

The collar is not the cow's identity. A device can be replaced while the animal record persists.

## Crop example

```text
LAND / FIELD 7
   ↓
2027 POTATO CROP
   ├── seed lot
   ├── planting event
   ├── field observations
   ├── environmental evidence
   ├── input/provenance records
   ├── harvest event
   └── harvest/storage lots
```

The architecture does not create one TitleChain record per potato. It records the production unit at a useful and defensible granularity.

## Public and private boundary

### Public-safe layer may contain

- privacy-preserving entity/farm reference;
- land/operating-area reference;
- record type and granularity;
- provenance digest;
- lifecycle-event digest;
- conformance/version information;
- public source attribution.

### Private farm layer may contain

- exact location;
- raw sensor data;
- animal health/reproductive observations;
- crop-management details;
- yield/production data;
- farm economics;
- private supplier/customer information;
- veterinary or agronomic notes;
- model-derived features;
- credentials, keys and recovery material.

## Relationship to M5 economic records

The Biological Stewardship Registry may later supply permissioned evidence to production, provenance or economic workflows, but it does not automatically create a financial instrument, commodity contract, security, ownership interest or public disclosure.

```text
private crop or herd evidence
      ↓ authorized projection
production / provenance record
      ↓
separately classified lawful economic event
```

Each downstream right or transaction retains its own classification, authority, consent and recordkeeping requirements.

## Reference implementation 001 — Sovereign Herd

[Sovereign Herd](../norton-ranch-blueprint/sovereign-herd/README.md) is the first bounded implementation of this broader Biological Stewardship Registry.

It demonstrates persistent individual-animal records, herd relationships, serialized collar/device records, device reassignment without loss of animal history, local sensor ingestion, local behavior/baseline intelligence, farmer-controlled export and portability, and no mandatory vendor-cloud custody for the `LOCAL-FIRST` profile.

Future reference implementations may cover crop cycles, orchard blocks, hives, seed/harvest lots and other managed biological systems.

## Public-review questions

1. Which biological systems should use individual records and which should use cohorts/lots?
2. Which government or industry identifiers should be interoperable without becoming the M5 identity root?
3. What stewardship and care evidence should remain permanently private?
4. What production evidence may be selectively disclosed to buyers, regulators, insurers or research programs?
5. How should leased land, custom grazing, boarding and contract farming distinguish owner, steward and operator?
6. What lifecycle events should be common across livestock, crops, orchards and apiaries?
7. What independent conformance tests are required before a production implementation can claim compatibility?
