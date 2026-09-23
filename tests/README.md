# Tests and Validation

![Read the context before the tests](../assets/section-review-path.svg)

This folder contains the public schema-conformance tests. The broader
provider-neutral governor regression suite remains beside its implementation so
reviewers can inspect code and evidence together.

Tests provide reproducible evidence for bounded cases. A passing result does
not establish that a record is true, an actor has authority, a deployment is
secure, a system complies with law, or the release is production-ready.

## Explore this section

| Test surface | What it checks | Location |
| --- | --- | --- |
| Schema and example pairs | Explicitly inventoried schema/example pairs, Draft 2020-12 validity, required fields, unknown fields, and selected fail-closed cases | [Schema tests](test_schemas.py) |
| SHADOW M5Index seed | Imported-source fingerprints, normalized workbook surfaces, IDs, evidence posture, scores, queues, and Spring Commons boundaries | [SHADOW tests](test_shadow_m5index.py) |
| M5 Eve authority adapter | Authentication/context separation, delegation scope, lifecycle, approvals, disabled capabilities, and Spring Commons default-deny behavior | [M5 Eve tests](test_m5_eve_adapter.py) |
| Provider-neutral governor | Budget projection, ledger integrity, provider adapters, and shared control behavior | [Governor tests](../reference-implementation/provider-neutral-governor/tests/) |
| Recorded release evidence | Dated results, scope, and explicit non-claims | [Validation report](../VALIDATION-REPORT.md) |

## Run the focused public suite

From the repository root:

```text
python -m pytest tests reference-implementation/provider-neutral-governor/tests
```

Review failures against the relevant [standard](../standards/README.md),
[schema](../schemas/README.md), and [synthetic example](../examples/README.md)
before proposing a change.

## Commons handoff and M5BOM acceptance

Run `python -m pytest -q` with Python 3.12 and requirements-dev.txt installed.
Additional coverage: [handoff tests](test_commons_handoff.py),
[M5-Eve activation](test_m5_eve_activation.py),
[M5BOM baseline](test_m5_bom_baseline.py). These are synthetic conformance tests;
device/runtime deployment, signature verification and payment rails are not
implemented or certified here.

The complete CI gate also includes SHADOW and SEC observatory test directories:

```sh
python -m pip install -r requirements-dev.txt -r sec-public-input/observatory/requirements.txt
M5_REQUIRE_NUMSCRIPT=1 python -m pytest -q -p no:cacheprovider tests reference-implementation/provider-neutral-governor/tests shadow-m5index/tests sec-public-input/observatory/tests
python shadow-m5index/scripts/validate_records.py
python tools/check_public_release.py
git diff --check
```

Numscript v0.0.25 is required; CI installs the checksum-pinned artifact. The
release checker scans specified secret/PII patterns in repository text and
verifies all file hashes. It does not inspect git history or OCR binary media.
Use `python tools/check_public_release.py --write-manifest` after final edits
and cleanup, then rerun verification without that option.
