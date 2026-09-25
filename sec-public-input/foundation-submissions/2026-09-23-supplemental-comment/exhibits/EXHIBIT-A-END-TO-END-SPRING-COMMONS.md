# Exhibit A - End-to-End 312 Spring Commons Reference Transaction

> **© 2026 TitleChain Foundation.** Part of the Foundation's written submission
> to the SEC on File No. S7-2026-30 (emailed September 23, 2026; pending SEC
> posting). Licensed under CC-BY-4.0 with required attribution. TitleChain
> Foundation, M5 and related marks are not licensed, and no patent rights are
> granted. See [NOTICE](../NOTICE.md). *This notice is added by the repository and
> is not part of the submitted text.*

**Reference:** PPT-EZ-CA-0001 / 312 Spring Commons\
**Repository baseline:** M5-AI-Sovereign-Commons `3a7b4b79b23399e9c362a124ca87f433a36321a3`\
**Status:** Submission exhibit; reference transaction remains demonstration-only.

## A1. Transaction thesis

The simulation tests whether a government/public asset can move through a reconstructable chain without allowing a blockchain, token, wallet, AI model, or internal M5 label to replace the authoritative legal act.

```text
PUBLIC ASSET IDENTIFIED
-> authoritative source/title evidence
-> jurisdiction + public owner
-> disposition pathway
-> accountable agency/office
-> authorized human(s)
-> required approvals
-> HOLD until external evidence
-> conveyance instrument
-> execution + recording
-> authoritative title state
-> project/stewardship rights
-> capital/debt/instrument layer
-> regulated recordkeeping where applicable
-> on/off-chain settlement + reconciliation
-> operating contracts/productive assets
-> continuing compliance/evidence
-> correction / transfer / redemption / exit
```

Across every stage:

`HUMAN/ENTITY -> CAPACITY -> AUTHORITY -> POLICY -> APPROVAL -> EXECUTION -> AUTHORITATIVE RECORD -> RECEIPT`

## A2. Separate record domains

| Domain | What it establishes | Must not be silently replaced by |
|---|---|---|
| Physical/public title | Recorded ownership and conveyance state | token balance, wallet, simulation |
| Government authority | Power to dispose/approve/sign | AI output, namespace, credential alone |
| Stewardship/operations | Bounded operating rights | fee title |
| Debt/capital | Financing obligations and rights | property title |
| Securities, if any | Issuer/holder rights and restrictions | project membership |
| Transfer-agent record | Registered holder state where applicable | wallet balance alone |
| Banking/settlement | Authoritative movement of funds on the applicable rail | blockchain evidence alone |
| Blockchain/evidence | integrity, event, provenance, reconciliation evidence | legal authority |
| Productive assets | equipment/services/output state | title to the underlying land |

## A3. Demonstrated control behavior

The repository's fit-gap review correctly treats `SIMULATED_PASS` as an internal rule result and `PENDING_EXTERNAL` as missing authoritative evidence. A simulation cannot self-advance because code passed.

The reference transaction therefore uses the state path:

`IDENTIFIED -> SOURCE_VERIFIED -> AUTHORITY_MAPPED -> APPROVALS_REQUIRED -> HOLD -> APPROVED -> EXECUTED -> RECORDED -> AUDITED`

Exception states: `REJECTED`, `REVOKED`, `DISPUTED`, `SUPERSEDED`.

## A4. Financing and settlement

The simulation keeps capital provenance and settlement separate from title. Material funding events should preserve entity, authority, source-of-funds, jurisdiction path, regulated route, destination, governing instrument, and reconciliation evidence.

Illustrative architecture:

`capital source -> lawful vehicle/account -> eligibility/authority -> subscription/financing instrument -> bank or permitted digital rail -> escrow/project account -> draw approval -> payee -> settlement evidence -> reconciliation -> project/evidence update`

A successful blockchain event does not prove that bank settlement occurred. A bank transfer does not prove that a title transfer occurred. Each authoritative domain remains independently evidenced and linked.

## A5. Mandatory disclosure

> This reference transaction demonstrates the technical, authority, evidence and approval workflow. It does not represent government authorization, agency participation, completed title transfer, live settlement, regulated-provider appointment, or independent validation unless corresponding evidence is explicitly identified.
