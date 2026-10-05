# Sovereign Herd — Local Architecture

## Reference stack

```text
COLLAR / SENSOR
 IMU · location · optional temperature/proximity
        ↓
LOCAL FARM RADIO
 LoRa/LoRaWAN · BLE · other conforming local link
        ↓
FARM GATEWAY
        ↓
LOCAL COMPUTE
        ↓
PRIVATE TIME-SERIES / EVENT STORE
        ↓
FEATURE EXTRACTION
        ↓
LOCAL BEHAVIOR / BASELINE MODELS
        ↓
ALERT / REVIEW QUEUE
        ↓
FARMER / AUTHORIZED OPERATOR
```

External internet is optional for ordinary local monitoring.

## Data classes

### Public-safe
- schema/version;
- anonymized or privacy-preserving entity reference;
- device model reference;
- firmware/SBOM digest;
- conformance profile;
- assignment event digest;
- public source attribution.

### Private
- raw sensor streams;
- exact location history;
- individual animal behavioral history;
- breeding/reproductive observations;
- veterinary notes;
- farm economics;
- credentials and keys;
- model features derived from private data.

## Observation envelope

Every observation should preserve:

- `observation_id`
- `animal_ref`
- `device_ref`
- `observed_at`
- `sensor_type`
- `unit`
- `value` or payload reference
- `source`
- `quality`
- `local_clock_state`
- `ingested_at`

Derived records additionally preserve:
- algorithm/model identifier;
- version;
- feature-window start/end;
- confidence or score where meaningful;
- source observation references;
- inference timestamp.

## Baseline engine

The preferred local intelligence pattern is:

1. use public/open data and validated methods for a generic starting classifier;
2. learn farm and herd context;
3. build an individual baseline for each animal;
4. surface significant deviations for review;
5. allow the farmer/veterinarian to correct or label outcomes;
6. preserve the correction as new evidence rather than erasing provenance.

## Security

The reference implementation should use:
- encrypted storage where practical;
- authenticated device/gateway enrollment;
- signed manifests where available;
- role-bound administrative actions;
- local audit logs;
- export receipts;
- backup/recovery chosen by the farmer.

No public GitHub repository should contain production credentials or farm telemetry.
