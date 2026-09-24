# Farmland Financial Classification, Escrow & Fiduciary Update

**Date:** September 24, 2026\
**Applies to:** `AG-PILOT-001 / ND-FARM-SIM-001`

This update imports the latest Spring Commons matrix pattern into the Farmland /
Redevelopment lane.

## New control

Before any financial or economic instrument activates, resolve the:

**Authority + Jurisdiction + Capital Provenance + Instrument Classification Matrix**

The matrix must identify:

- underlying asset;
- underlying right;
- instrument;
- intent;
- issuer/obligor;
- holder/participant;
- state-law path;
- federal securities path;
- CFTC/commodity-derivatives path;
- banking/escrow path;
- transfer-agent/trustee/fiduciary function;
- authoritative record;
- source and destination capital path;
- privacy class;
- correction/succession path.

State, SEC and CFTC lanes may be separate or overlapping. Classification follows
the actual instrument and transaction, not a project label or digital wrapper.

## Bounded money functions

The simulation now distinguishes:

1. acquisition/title closing escrow;
2. securities subscription/impoundment escrow if applicable;
3. capital-improvement draw account if applicable;
4. farm operating account;
5. stewardship reserve;
6. distribution/waterfall account if applicable; and
7. tax/insurance/debt-service reserve if applicable.

Each account has a defined purpose, authorized actors, release conditions,
authoritative bank/escrow record and prohibited use.

## Regulated / fiduciary participants

The project selects participants by function, including title/closing provider,
bank/escrow provider, issuer, transfer agent, trustee/fiduciary, broker-dealer,
custodian, FCM/DCM/CPO/CTA or swap intermediary, lender/collateral agent and
local farm operator when the final structure actually requires them.

TitleChain/M5 coordinates policy, provenance and reconciliation; it does not
silently become any of those regulated or fiduciary roles.
