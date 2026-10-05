# Sovereign Herd OEM / Private-Label Program

## Purpose

Allow hardware manufacturers, distributors, integrators, cooperatives, and local agriculture businesses to package compatible livestock devices without requiring a proprietary central data monopoly.

## Manufacturer hierarchy

```text
MANUFACTURER / PRIVATE-LABEL ENTITY
        ↓
PRODUCT FAMILY
        ↓
DEVICE MODEL
        ↓
FIRMWARE / SBOM VERSION
        ↓
PRODUCTION BATCH
        ↓
DEVICE SERIAL
        ↓
SHIPMENT MANIFEST
        ↓
FARM CLAIM
        ↓
ANIMAL ASSIGNMENT
```

## Minimum device manifest

Each serialized unit should expose or accompany:
- manufacturer reference;
- private-label brand, if any;
- device model;
- serial number;
- hardware revision;
- firmware version;
- firmware/SBOM digest where supported;
- radio technology;
- sensor capabilities;
- provisioning public key or equivalent identity method where supported;
- manufacturing/batch date;
- warranty/service reference;
- conformance profile/version.

No private key should be placed in a public registry.

## Bulk provisioning

A 500-device shipment can use one signed manifest.

The farm:
1. claims the shipment;
2. imports the herd manifest;
3. assigns device serials to animal records;
4. begins local ingest;
5. replaces or reassigns devices while preserving history.

## Interoperability requirement

A device provider should document:
- how raw sensor data can be obtained locally;
- field units and sampling rates;
- clock behavior;
- radio/gateway requirements;
- local API/protocol;
- firmware update method;
- export format;
- end-of-service behavior.

A vendor that only exposes derived results through a mandatory proprietary cloud may still integrate as an external service, but should not claim the full `LOCAL-FIRST` profile.

## Certification language

Until a formal Foundation conformance process exists, public material should say:
- `M5-compatible draft implementation`, or
- `implements the draft Sovereign Herd profile`

and should not say:
- `M5 certified`,
- `TitleChain Foundation approved`,
- `government approved`,
unless such status is actually granted.
