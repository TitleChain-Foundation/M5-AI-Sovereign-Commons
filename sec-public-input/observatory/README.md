# Automated SEC Public Comment Observatory

**Docket:** SEC File No. S7-2026-30, Transfer Agent Rules

**Public dashboard:**  
<https://titlechain-foundation.github.io/M5-AI-Sovereign-Commons/sec-observatory/>

The observatory checks the official SEC docket every hour. When a filing appears,
the public dashboard records the exact docket metadata supplied by the SEC, the
official source URL, retrieval time, media type, and SHA-256 digest.

The observatory does not rehost a comment as though the Foundation were its
publisher. The official SEC filing remains the controlling source.

## Analysis states

Every filing has one of two analysis states:

- **Automated signal scan — not human reviewed:** deterministic keyword matching
  identifies possible review topics. It does not claim to summarize the
  commenter's position.
- **Human-reviewed summary:** an attributable review record is bound to the
  collected filing by its analysis-text digest and has been approved for public
  release.

Automated signals never become human-reviewed summaries automatically.

## Update process

The [Pages workflow](../../.github/workflows/publish-sec-observatory.yml):

1. retrieves the official SEC docket;
2. fails closed if the docket is empty or its structure is no longer recognized;
3. reuses the prior public record for unchanged filings;
4. fetches and hashes newly listed filings;
5. performs a full source refresh at least every 24 hours;
6. validates human review records against collected source text;
7. builds `feed.json` and the public dashboard; and
8. deploys the generated site without committing generated or private source
   material to the repository.

The workflow can also be run manually from GitHub Actions.

## Local validation

```bash
python -m pip install -r sec-public-input/observatory/requirements.txt
python -m unittest discover -s sec-public-input/observatory/tests -v
python sec-public-input/observatory/update_observatory.py \
  --output /tmp/sec-observatory
```

The collector uses a descriptive user agent, fetches only the official docket
and comment URLs, and pauses between new-source requests.

## Publication boundaries

- The SEC docket controls.
- Filing frequency is not a vote or consensus signal.
- Automated topics are not findings, summaries, or endorsements.
- Human-reviewed summaries remain interpretations and link to the official
  filing.
- No API keys, private comments, personal case files, or unpublished review
  drafts belong in this directory.
