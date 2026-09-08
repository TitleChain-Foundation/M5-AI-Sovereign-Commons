# Pilot and SEC Request-for-Input Crosswalk

**Status:** Informative Draft for Public Comment  
**Version:** 0.1  
**Reviewed:** September 7, 2026

## Boundary

This crosswalk identifies questions that the synthetic
[People's Trust Public Conformance Pilot](PEOPLES-TRUST-PUBLIC-PILOT.md) can
help examine. It does not claim that the SEC has adopted, approved, requested,
or endorsed an M5 design.

The referenced pilot uses synthetic records only. Nothing here asserts that an
owner, seller, operator, transfer agent, regulator, or agency has agreed to
participate, or that an acquisition or securities offering exists.

The authoritative proposal is:

- U.S. Securities and Exchange Commission, **Transfer Agent Rules**
- Release No. **34-106246**
- File No. **S7-2026-30**
- Federal Register citation **91 FR 56946**
- Published September 4, 2026
- Comments due November 3, 2026 according to the current Federal Register record

The official proposal controls over this summary.

## Theme crosswalk

| Proposal and public-review theme | Pilot evidence | Question for reviewers |
| --- | --- | --- |
| Registration, contacts, entity structure, and control | Versioned entity, signer, role, standing, and revocation records | Which facts must be public, regulator-only, or confidential? |
| Operational capacity and service providers | Dependency and provider inventory with accountable owners | Which dependencies are material and how should failures be reported? |
| Electronic instructions and receipt | Distinct draft, submit, receive, accept, reject, execute, post, and correct states | What event creates which legal or operational consequence? |
| Securityholder and wallet association | Private verified identity binding plus public-safe reference | How can association be proved without publishing unnecessary PII? |
| Authoritative master record | Explicit authoritative-record declaration and reconciliation | How should linked ledgers avoid becoming competing masters? |
| Distributed-ledger and electronic records | Signed association, policy, execution, posting, and correction receipts | What evidence is required beyond a chain event? |
| Timestamps, journals, controls, and audit | Ordered lifecycle events and privacy-filtered views | Which clocks and records control when systems disagree? |
| Retention and corrections | Differentiated retention, append-only correction, supersession, and legal hold | What must be retained for the life of an issue? |
| Safeguards and incident response | Access policy, separation of duties, recovery, compromised-device, and incident tests | Which independent assessments are necessary? |
| Transfer restrictions | Machine-readable restriction linked to the authoritative legal source and exception authority | How are ambiguity, change, waiver, and removal handled? |
| Portability and successor transfer | Continuously exportable package with reconciliation evidence | What minimum package allows an accountable successor to resume service? |
| Small-entity burden | Reusable schemas, evidence inventories, and conformance fixtures | Which requirements reduce duplication without creating a false safe harbor? |

## Core demonstration assertions

The pilot asks reviewers to test these propositions:

1. Classification occurs before regulated execution.
2. Wallet or key possession does not create authority.
3. Private credentials do not replace governmental registration.
4. The accountable transfer agent remains responsible where transfer-agent
   regulation applies.
5. One authoritative state can be maintained while linked systems provide
   evidence and automation.
6. Rejection, exception, correction, and supersession are first-class states.
7. Restrictions must preserve their authoritative source and change history.
8. Current state and material history must be portable to an authorized
   successor.

These are proposed control principles, not descriptions of current law in
every jurisdiction.

## Public questions

### Regulators and transfer agents

1. Which record is authoritative for each legally relevant state?
2. What evidence should bind a wallet to a registered holder?
3. Which regulated statuses must be checked before capability is exposed?
4. What information should be publicly visible versus regulator-only?
5. How should rejected, frozen, corrected, court-ordered, and superseded events
   be represented?
6. What conformance tests would aid examination without creating a safe harbor?

### States, counties, and title professionals

1. Which official record controls each title or severable-right event?
2. Can public-safe filing and fee receipts improve reconciliation without
   replacing the official record?
3. What proves authority to sign or convey?
4. How should title, lease, crop, water, mineral, easement, and operator rights
   remain independently represented?

### Operators and communities

1. Which decisions require qualified local operational authority?
2. Which operational details must remain confidential?
3. How should succession and continuity be tested?
4. Which stewardship measures are useful and which create unreasonable burden?

### Standards and technology reviewers

1. What minimum schemas are needed for authoritative-record declarations,
   identity bindings, restrictions, decisions, and corrections?
2. Which identifiers remain stable across provider, wallet, chain, or transfer
   agent changes?
3. How can credential status be proved without exposing private evidence?
4. Which fixtures and tests are implementation-neutral?

## Submission handling

Public comments must use synthetic or already public evidence. Private
credentials, identity records, privileged analysis, confidential transaction
materials, security-sensitive topology, and unreported vulnerabilities must use
an approved private channel.
