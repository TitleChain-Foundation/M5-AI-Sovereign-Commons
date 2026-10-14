# SEC regulatory record maintenance

Last verified in committed filing inventory: Oct. 8, 2026.
The deployed status overlay is refreshed from both SEC dockets on each successful build.

The existing public route is `/M5-AI-Sovereign-Commons/sec-observatory/`.
The Foundation record appears above the unchanged live S7-2026-30 observatory.
The automated official comments feed remains scoped to the transfer-agent docket;
the Foundation filing-status overlay checks both S7-2026-30 and S7-2026-35.
The public `foundation-status.json` supports read-only syndication to the main
Foundation website. Source records remain immutable in Git between reviewed changes. Foundation submissions and analysis
are explicitly separated from SEC proposal facts and official feed metadata.

## Single source of truth

Edit `observatory/foundation-record.json` for proceeding metadata and filing
statuses. `observatory/foundation_record.py` derives every public filing status
and timeline label. The README links to that rendered inventory rather than
maintaining another set of filing statuses.

| Proceeding | Releases | Proposal date | Comment deadline |
| --- | --- | --- | --- |
| S7-2026-30 | 34-106246 | Sept. 1, 2026 | Nov. 3, 2026 |
| S7-2026-35 | IA-7023; IC-36353 | Oct. 1, 2026 | 60 days after Federal Register publication |

Both are proposed rules. No calendar deadline is inferred for S7-2026-35.

## Official sources

- [S7-2026-30 SEC rulemaking](https://www.sec.gov/rules-regulations/2026/09/s7-2026-30)
- [S7-2026-30 SEC received comments](https://www.sec.gov/rules-regulations/public-comments/s7-2026-30)
- [SEC transfer-agent announcement](https://www.sec.gov/newsroom/press-releases/2026-81-sec-proposes-modernize-rules-registered-transfer-agents)
- [S7-2026-35 SEC rulemaking](https://www.sec.gov/rules-regulations/2026/10/s7-2026-35)
- [S7-2026-35 SEC received comments](https://www.sec.gov/rules-regulations/public-comments/s7-2026-35)
- [SEC custody announcement](https://www.sec.gov/newsroom/press-releases/2026-100-sec-proposal-would-address-how-investment-advisers-funds-can-custody-crypto-assets-under-federal)

Verified against both official SEC received-comments pages on Oct. 8, 2026.
The Sept. 5 Foundation filing and both Oct. 3 filings are SEC-posted.
The Sept. 23 supplement and Exhibits A-J remain pending independent matching.
Publication status is not endorsement or approval.

The runtime reconciler only marks a previously pending filing posted if an
SEC docket candidate matches date and commenter AND its extractable PDF text
exactly matches the local archived submission after whitespace normalization.
If PDF verification is blocked, status remains pending; never infer posting.
The original submitted PDFs remain authoritative Foundation archive copies.
A detached historical review no longer stops all publishing: it is retained
in Git but excluded from current public summaries with a warning.

## Filing inventory and storage

- Sept. 5 original: existing direct SEC PDF URL retained in the data file;
  foundational filing, not replaced by either supplement.
- Sept. 23 supplement and Technical Exhibits A–J: existing files retained under
  `foundation-submissions/2026-09-23-supplemental-comment/as-submitted/`.
- Oct. 3 S7-2026-30 supplement: canonical public PDF under
  `foundation-submissions/2026-10-03-s7-2026-30/`.
- Oct. 3 S7-2026-35 comment: canonical public PDF under
  `foundation-submissions/2026-10-03-s7-2026-35/`.

Oct. 3 PDFs are byte-for-byte copies of the supplied package. DOCX archive
copies reside in each submission's `source/` directory. Only inventoried PDFs
are copied into the Pages output; DOCX sources are not website downloads.
The supplied Markdown handoff is retained as `SEC_UPDATE_2026-10-03.md` for
content provenance, not executable instructions or a live status source.

## Posting procedure

Check the appropriate SEC received-comments page for the Foundation filing.
Do not infer posting from delivery, receipt, a press release or a local copy.
Once the exact filing is publicly listed, update only that filing's fields:

```json
"secPosted": true,
"secUrl": "https://www.sec.gov/comments/…"
```

Use the actual direct SEC comment URL, not the placeholder above. The renderer
then changes the status to **Posted on SEC.gov**, adds **View on SEC.gov**, and
retains **Read Foundation copy**. Preserve the submission date and local PDF.
No separate status string requires editing. Until then, both Oct. 3 filings show
**Submitted Oct. 3, 2026 — SEC posting pending**. Posting alone does not justify
changing substantive analysis or imply SEC endorsement, acceptance, review or
approval. Update `lastVerified` after a source check. Update the custody deadline
only when the SEC / Federal Register supplies a fixed deadline.

## Build and checks

The existing `update_observatory.py --output …` build renders this overview and
copies only the inventoried public PDFs. The Pages workflow runs that build
and also triggers when submission PDFs change. External sources use the existing
same-tab link policy.

Run observatory unit tests, the repository conformance suite, SHADOW validator,
public-release manifest check and `git diff --check` as documented in
`../tests/README.md`. No npm lint/typecheck/build commands exist in this Python
and static-HTML repository. Regenerate `MANIFEST.sha256` after final changes.

## Read-only Foundation site integration

GitHub Pages publishes `/sec-observatory/foundation-status.json` alongside
`feed.json`. The Foundation website (currently a separate website deployment)
can fetch the status JSON and display official SEC links, lastVerified, warnings,
and filing-status badges. Do not mark the main Foundation site integrated until
its own deploy has been updated and visually verified. See the repair ZIP README.
