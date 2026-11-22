# Base44 implementation directive — Legislative Observatory ONLY

## Do not touch
- M5Labs/Commons scientific reconciliation, calculators, referee statuses, marketplaces or member systems.
- Existing `sec-observatory/` routes, monitoring jobs, data, historical records and submissions.
- Git history, branches, authentication, wallets, credentials, databases or formulas.

## Read-only inspection first
Inventory existing Commons Observatory navigation and SEC routes, the Foundation site's current navigation, relevant site source and deployment owners. Return an affected-file list before editing. Never assume Base44 can write to the separately hosted Commons repository; if it cannot, prepare an exact diff and handoff to its repository maintainer.

## Commons site map
- `/observatory/` (proposed route; check conflicts first): Legislative & Regulatory Observatory index.
- `/observatory/sovereign-compute-access-act/`: Foundation model bill overview, original canonical source, revision history, comment instructions, technical standards references.
- `/observatory/hr-2347-baaja/`: official action tracker, House/Senate source comparison, permitting/public lands analysis, survivor tax-relief section, open questions.
- Existing `/sec-observatory/`: retain unchanged and link from index.
- `/observatory/participate/`: official channels and Foundation feedback, explicitly distinguished.

If current Commons is hash-routed, preserve the existing routing convention rather than forcing physical paths. Add redirects/aliases only after route verification. Avoid duplicate pages.

## Homepage and navigation
Feature the Observatory without removing the nine pathways or rewriting other Commons sections. Add a concise Foundation homepage link to the Observatory. Make the Observatory first accessible within two clicks from either site.

## Status taxonomy
- `foundation_model_draft`: proposed by Foundation/ICSN; not introduced.
- `introduced`: official chamber introduction with source and date.
- `passed_chamber`: one chamber passed; not necessarily enacted.
- `enacted`: verified signed law/public law citation.
- `regulatory_comment`: official docket and open/closed window verified.
- `foundation_analysis`: commentary, not official bill text.
- `verification_pending`: unresolved claim; do not promote to fact.

Display `as_of`, `last_verified`, source URL, version identifier, and source type. Avoid automatically upgrading status from third-party summaries.

## Publication requirements
- SCAA Draft v2 full text must be linked to its canonical GitHub source and clearly marked a model proposal. Do not paraphrase it into a substitute legal draft.
- H.R. 2347: show the official Senate vote (November 19, 2026; 62–33; five not voting), label it Senate passage, and verify the latest House disposition before release.
- Survivors' provisions: cite the exact enrolled/amended Senate text and section before displaying any section-by-section conclusion; record earlier legislative vehicle and later substitute separately.
- Public participation: use official find-your-representative and bill pages; no prefilled false constituent identity, no impersonation, no automated submissions.
- No speculative partner, congressional sponsor, committee endorsement or enacted-law claims.

## Acceptance tests
1. Existing SEC Observatory still works and is linked.
2. Model proposal and congressional bill cannot be confused visually or in metadata.
3. Every public claim has a source link and `last_verified` timestamp.
4. House/Senate versions and dates are separately identified.
5. Public comment pathways distinguish Foundation feedback from official filings.
6. Mobile and keyboard navigation, heading structure, contrast, link labels and focus states pass review.
7. No changes to M5Labs, M5Bank, calculators, fees or credentials.
8. Return exact file diff, screenshots, route list, deployment plan and unresolved evidence for approval.

**Do not commit or deploy until approved.**

## GitHub publication and pinned-version addendum (2026-11-22)

GitHub is the source-control destination for all Base44-provided markdown and the Commons Observatory implementation. Read `GITHUB_HANDOFF_AND_PINNING.md` and `HR2347_BAAJA_PINNED_RECORD.md` before opening a PR. Target `TitleChain-Foundation/M5-AI-Sovereign-Commons` after verifying the actual deploy path. Keep SCAA legal text canonical in `TitleChain-Foundation/icsn-standards`.

The Observatory headline is **H.R. 2347 — From the Survivor Justice Tax Prevention Act to BAAJA**. H.R. 2347 **retained its number**; the Senate substituted BAAJA. Pin **Division C §3001** with the source-version verification caveat until the exact Senate-passed text is pinned. SCAA remains **NOT INTRODUCED**, with prospective 2027 outreach stated only as an objective.

Do not push to main, merge, or deploy before approval. Prepare a GitHub issue, feature-branch PR and evidence-backed diff for review.
