# Entity Activation and Pricing — M5 Implementation

> Commercial implementation note. Not part of the price-neutral ICSN standard.

## Registration sequence

```text
PERSON
  ↓
M5IAM / TCID / M5HUM
  ↓
PRIVATE M5POD
  ↓
M5-CV / ROLE / AUTHORITY
  ↓
EXISTING OR NEW LEGAL BUSINESS ENTITY
  ↓
M5 BUSINESS ENTITY REGISTRATION
  ↓
FARM NAMESPACE + JURISDICTION
  ↓
FARM / HERD / ANIMAL / DEVICE TOOLS
```

## Legal-entity boundary

M5 registration does not replace government incorporation, assumed-name filing, livestock identification, tax registration, licensing, veterinary requirements, or other external legal obligations.

If the farmer already operates an LLC, corporation, cooperative, partnership, trust, sole proprietorship, or other lawful structure, M5 can record that external entity and the accountable authority relationship.

## Proposed annual base

**M5 Farm/Business Entity: $840/year proposed**

This represents a business entry tier equivalent to $70/month, billed annually.

Suggested included capability:
- entity namespace;
- authority mapping;
- business M5POD context;
- farm and location registry;
- herd registry;
- animal registry;
- device/fleet registry;
- assignment lifecycle;
- bulk import/export;
- local reference software;
- conformance manifests.

## Per-animal pricing

**Required M5 software rent: $0/cow/month.**

A commercial provider may separately charge for:
- collar hardware;
- gateway/local compute;
- installation;
- replacement;
- warranty;
- connectivity;
- support;
- specialist analytics;
- data migration;
- veterinary or breeding services.

The farmer should be able to terminate an optional service without losing lawful access to exportable farm records and history.

## Large-herd provisioning

A single farm entity can provision hundreds or thousands of animals from a signed or validated manifest.

The registry should not require a separate checkout or subscription contract for every animal.
