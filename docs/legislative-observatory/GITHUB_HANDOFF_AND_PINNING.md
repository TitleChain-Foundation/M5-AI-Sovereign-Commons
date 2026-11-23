# GitHub-first Legislative Observatory handoff

**Status:** implementation instructions, not a completed GitHub commit or deployment. **Scope:** legislative Observatory only. Date: 2026-11-21 release baseline (updated handoff 2026-11-22).

## Repository ownership and source of truth

1. Target public Commons repository: `TitleChain-Foundation/M5-AI-Sovereign-Commons` (verify branch and deployed site build paths before changing anything). Preserve `site/`, routing, SEC Observatory, existing content, and history.
2. Canonical Foundation model act: `TitleChain-Foundation/icsn-standards/legislation/sovereign-compute-access-act/OFFICIAL-TEXT.md`. The November 18, 2026 Draft v2 was retrieved from `main` with Git **blob SHA** `b3880be1d1ade136e5eb451d483ec31848075945`. A blob SHA is **not** the repository commit SHA. Resolve and record the full commit for a permalink. Never overwrite this model act with a summary.
3. The Base44-generated markdown files in this release are **proposed content and handoff documentation**, not congressional primary sources. Keep them in `docs/legislative-observatory/` (or a verified existing Observatory documentation directory). Their source filenames must remain traceable. Where Base44 content differs from congressional text, the official source prevails and differences go into an evidence issue.
4. Keep proposed legislation, official congressional records, Foundation analysis, and outreach separate in data fields and UI.

## Proposed GitHub layout (adapt to existing repo conventions)

```
docs/legislative-observatory/
  README_START_HERE.md
  BASE44_IMPLEMENTATION.md
  OBSERVATORY_PAGE_COPY.md
  EVIDENCE_REGISTER.md
  OUTREACH_DRAFT.md
  GITHUB_HANDOFF_AND_PINNING.md
  HR2347_BAAJA_PINNED_RECORD.md
```

Add site routes/components only after inspecting the actual Commons router and deploy configuration. Do not create duplicate `/observatory/` or replace `/sec-observatory/`.

## Required pinned public records

### SCAA
- Display: **Foundation model legislation · Draft v2 · NOT INTRODUCED**.
- Note: no congressional bill number, sponsor, committee referral or introduction. The Foundation seeks review by incoming members of the 120th Congress in 2027; this is an **objective**, not a completed congressional action.
- Link to the canonical draft and its full-commit permalink. Record its source commit, blob SHA, last-verified time and future revisions separately.

### H.R. 2347 → BAAJA
- Display primary headline **H.R. 2347 — From the Survivor Justice Tax Prevention Act to BAAJA**.
- Preserve the original House-passed survivor legislation and the Senate substitute as **separate official version records**; the **bill number H.R. 2347 did not change**. Do not describe BAAJA as a newly numbered bill.
- Pin a prominent section **Survivor tax relief retained — Division C, §3001**. This section reference must be checked against the **exact Senate-passed text including adopted amendments** before the UI quotes or claims to reproduce its final wording.
- The November 19 Senate vote was **62–33, five not voting**; this is Senate passage, **not proof of enactment**.
- Provide links to: original House-engrossed text https://www.govinfo.gov/app/details/BILLS-119hr2347eh ; congressional bill history https://www.congress.gov/bill/119th-congress/house-bill/2347 ; Senate vote https://www.senate.gov/legislative/LIS/roll_call_votes/vote1192/vote_119_2_00270.htm .
- Record the exact Senate-passed text's official GovInfo package/version identifier and hash once verified; **do not silently use the introduced amendment text as the final passed text**.
- Any standalone survivor bill in the 120th Congress is a **future proposal**, not a reintroduced bill until a member formally introduces it; a future introduction gets its own new number.

## GitHub delivery workflow

1. Read-only inspect the target repo's `README`, routing, Observatory components, data schemas, SEC Observatory and deployment config; capture current HEAD commit.
2. Create an issue describing scope, official evidence links, no-go items, and acceptance criteria. Cross-link the existing SCAA canonical repository without copying its legal text into an unversioned page.
3. Prepare a feature branch and PR with **separate commits** for (a) Base44 documentation, (b) pinned evidence records, (c) site UI/navigation. No direct `main` edits.
4. Attach exact source-permalinks and review flags. Include screenshots and route tests in PR description.
5. Validate accessibility, source/version separation, 17-family scientific content untouched, SEC Observatory unchanged, and no claims of enacted law or SCAA introduction.
6. Request Foundation approval and legal/editorial source verification before merging or deployment. No autonomous push, merge or deployment without explicit authorization.

## Minimum PR acceptance criteria

- BAAJA displayed as the Senate substitute to **the same H.R. 2347**, with original survivor bill retained and linked.
- Division C §3001 visibly pinned, with precise version and verification status.
- SCAA clearly **not introduced**; 2027 outreach intent not presented as a sponsorship commitment.
- Existing SEC routes and submissions unaffected.
- All Base44 markdown documents checked in with provenance, no unexplained content replacement.
- Source links resolve, checks pass, exact diff and approvals recorded.
