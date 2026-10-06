# Sovereign Herd — Implementation Roadmap

## Phase 0 — Public review

- publish profile and schemas;
- license-audit candidate datasets;
- define animal/device vocabularies;
- select passive sensor requirements;
- define export/conformance tests.

## Phase 1 — Synthetic local pilot

- create synthetic farm/entity;
- import synthetic herd;
- import synthetic device batch;
- assign/reassign collars;
- ingest synthetic observations;
- run a local behavior classifier or rules engine;
- create deviation alerts;
- export full farm-controlled package.

## Phase 2 — Bench pilot

- connect one or more real sensor devices in a non-production test;
- validate clocks, units, sampling rates, gateway buffering, offline behavior, and power behavior;
- prove no mandatory cloud dependency for `LOCAL-FIRST`.

## Phase 3 — Consented small-farm pilot

- signed participant agreement;
- explicit data boundaries;
- local storage;
- passive sensing only;
- farmer review;
- veterinarian review where health/fertility interpretations are evaluated;
- no public release of private telemetry.

## Phase 4 — OEM package

- private-label manufacturer profile;
- signed batch manifest;
- gateway image;
- local installer workflow;
- QR/batch claim;
- bulk herd provisioning;
- swap/repair workflow;
- export/migration test.

## Phase 5 — Independent conformance

Test:
- two hardware vendors;
- two local storage/runtime implementations;
- export/import round trip;
- device replacement;
- internet outage;
- model upgrade;
- corrupted manifest;
- revoked operator role;
- lost/replaced gateway;
- farm termination/migration.

## Success criteria

Sovereign Herd should not claim production conformance until a farmer can:
1. operate locally;
2. retrieve history locally;
3. replace a device without losing animal history;
4. export data without vendor permission;
5. migrate to another conforming provider;
6. prove which records are sensor facts, inferences, and human corrections.
