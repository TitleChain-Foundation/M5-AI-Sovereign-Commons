# M5 AI Governor — Provider-Neutral Reference Implementation

Provider-neutral cost/context/policy control plane, plus reference adapters
for OpenAI and Anthropic. Provider pricing/context facts embedded in the
adapters are dated configuration snapshots, not M5 canonical truth, and must
be revalidated against current provider documentation before use.

## Install

Dependencies are declared in `pyproject.toml` (PEP 621 `[project.dependencies]`
/ `[project.optional-dependencies]`) rather than a `requirements.txt`. From
this directory:

```bash
python -m pip install .          # runtime deps only: openai, anthropic
python -m pip install ".[dev]"   # also adds pytest for running tests
```

## Run tests

From this directory (`reference-implementation/provider-neutral-governor/`):

```bash
python -m pytest
```

No `PYTHONPATH` export is required: `pyproject.toml` sets
`[tool.pytest.ini_options] pythonpath = ["."]`, so pytest adds this directory
to `sys.path` for the run and `import m5_governor` / `import providers`
resolve on their own. `[tool.setuptools] py-modules`/`packages.find` in the
same file make `pip install .` package `m5_governor.py` and `providers/`
explicitly (setuptools' flat-layout auto-discovery would otherwise omit the
standalone `m5_governor.py` module), while excluding `tests/`.

## Layout

- `m5_governor.py` — shared control plane: pricing, context/budget preflight
  checks, and the JSONL cost ledger reader/writer.
- `providers/openai_adapter.py`, `providers/anthropic_adapter.py` — per-provider
  model specs, payload preparation, and usage normalization.
- `tests/` — pytest regression suite, including focused coverage for
  projected daily/monthly budget enforcement (`test_budget_projection.py`)
  and fail-closed cost-ledger integrity handling (`test_ledger_integrity.py`).
