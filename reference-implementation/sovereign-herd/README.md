# Sovereign Herd Reference Implementation

**Status:** Draft, local-only provisioning utility
**License target:** Apache-2.0 under the repository license map

This starter implementation proves one narrow thing: a farm can take an entity reference plus a local herd manifest and produce stable animal/device/assignment records without calling an external service.

It is not a behavior classifier, veterinary system, device driver, blockchain client, or production registry.

## Run

```bash
python provision_herd.py \
  --entity m5ent:synthetic:red-river-ranch \
  --farm m5farm:synthetic:red-river:001 \
  --input sample-herd.json \
  --output herd-manifest.generated.json
```

The script:
- uses only the Python standard library;
- performs no network calls;
- creates deterministic UUID5-based local references;
- keeps animal identity separate from device identity;
- creates assignment records only when a device serial is supplied.

## Next code modules

Future public reference code can add:
- local SQLite/Parquet/time-series storage;
- device adapters;
- LoRaWAN gateway ingest;
- feature extraction;
- behavior classification;
- individual baseline engine;
- export package builder;
- conformance tests.

Production secrets and real farm data must not be committed.
