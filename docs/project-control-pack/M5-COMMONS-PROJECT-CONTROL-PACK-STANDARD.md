# M5 Commons Project Control Pack Standard

**Status:** Informative architecture / public-review standard\
**Version:** 0.1\
**Date:** September 24, 2026

## Purpose

Every Commons project should answer the same control questions in the same
order, even when the underlying asset, jurisdiction, regulator, capital
structure and participants differ.

The rule is:

> **Same control pack. Same matrices. Different project-specific answers.**

This prevents Spring Commons, Farmland and Global UN Commons from evolving into
three unrelated documentation systems.

## Canonical project control pack

Every public simulation should expose these eight control surfaces:

1. **Asset / Right / Source-of-Truth Matrix**
2. **Authority + Jurisdiction + Capital Provenance Matrix**
3. **Financial Instrument + Regulatory Routing Matrix**
4. **Participant Role + Eligibility + Credential Matrix**
5. **Escrow + Treasury + Custody + Fiduciary Matrix**
6. **Transfer + Restriction + Correction + Succession Matrix**
7. **Risk + Disclosure + Public/Private Evidence Boundary**
8. **Simulation State Machine + Conformance Tests**

A project may already contain these controls inside a larger document set.
Where it does, do not duplicate documents unnecessarily. Publish a project
control index mapping these eight controls to the authoritative project files.

## Shared project-control sequence

```text
ASSET / RIGHT
        ↓
AUTHORITY
        ↓
JURISDICTION
        ↓
PARTICIPANT
        ↓
INSTRUMENT
        ↓
REGULATORY ROUTING
        ↓
ESCROW / TREASURY / FIDUCIARY FUNCTION
        ↓
EXECUTION
        ↓
AUTHORITATIVE RECORD
        ↓
TITLECHAIN / M5 EVIDENCE + RECONCILIATION
        ↓
CORRECTION / SUCCESSION / PORTABILITY
```

No later layer may silently create the authority of an earlier layer.

## Project adapters

### GSA / CRE — 312 Spring Commons

The control pack maps primarily to the existing Spring DOC-01–DOC-23 package,
especially:

- DOC-10 evidence/digital records;
- DOC-15 risk/disclosure;
- DOC-16 Ricardian/machine policy;
- DOC-17 Authority + Jurisdiction + Capital Provenance Matrix;
- DOC-18 rights/UCC separation;
- DOC-20 credential/privacy;
- DOC-21 benchmark methodology;
- DOC-22 due-process channel; and
- DOC-23 source-of-funds/entity/jurisdiction/public-transaction graph.

Do not create a parallel second legal-document package.

### FARMLAND / REDEVELOPMENT — People's Trust

Use `AG-PILOT-001 / ND-FARM-SIM-001` as the first full project-control example.

The farmland project should explicitly publish all eight matrices because its
current public material is smaller than Spring's 23-document package.

### GLOBAL DEVELOPMENT PROJECT — Global UN Commons

Use the same eight controls but treat jurisdiction as plural and
project-specific.

The Global simulation must distinguish:

- host-country / host-city real-property and development law;
- contracting institution;
- multilateral/international organization status where actually relevant;
- capital-source jurisdictions;
- instrument jurisdiction;
- regulated intermediaries;
- applicable local, national and cross-border rules; and
- technical jurisdiction namespaces.

The project must not imply United Nations endorsement, authority or immunity.

## Common naming

Each project should expose a `PROJECT-CONTROL-INDEX.md` that answers:

| Control | Where is it answered? | Current state |
| --- | --- | --- |
| Asset/right/source-of-truth | project-specific link | DRAFT / VERIFIED / TBD |
| Authority/jurisdiction/capital provenance | project-specific link | ... |
| Instrument/regulatory routing | project-specific link | ... |
| Participant eligibility/credentials | project-specific link | ... |
| Escrow/treasury/fiduciary | project-specific link | ... |
| Transfer/restriction/correction/succession | project-specific link | ... |
| Risk/disclosure/privacy | project-specific link | ... |
| State machine/tests | project-specific link | ... |

This gives the public, engineering agents, counsel, regulators and reviewers one
predictable way to inspect every project.
