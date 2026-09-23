# M5 OpenAPI Provider and Runtime Profiles

M5 distinguishes **core local runtimes** from **external providers**.

## Core local runtime

**Laya** belongs in M5POD as the resident local System 1 typed-decision engine.

See:

`docs/LAYA-LOCAL-SYSTEM-ONE-PROFILE.md`

It is not modeled as a marketplace dependency merely because the runtime may also have an upstream open-source project.

## External hosted System 1

**Jev** is an optional hosted System 1 provider for scale/task fit when policy permits.

See:

`docs/JEV-HOSTED-SYSTEM-ONE-PROFILE.md`

## Generative/frontier providers

Generative providers remain provider-neutral and are selected only when task shape, privacy, authority, policy, quality, cost, latency, and availability permit.

## Required provider facts

A public profile should be able to record:

- exact provider/project identity;
- capability;
- local/API mode;
- endpoint identity where applicable;
- model/runtime identifier;
- official license/terms source;
- official pricing/metering source;
- retention/privacy facts;
- self-host/open-weight status if officially supported;
- jurisdiction/data-residency facts;
- date last verified;
- M5 enrollment/credential state separately.

A provider/runtime is never an independent source of legal authority.
