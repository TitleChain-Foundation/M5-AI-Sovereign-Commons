"""Shared test helpers for the M5 AI Governor test suite.

Not a test module itself (no `test_` functions/classes), so pytest will not
collect it, but it is importable by test modules because pytest inserts the
`tests/` directory onto `sys.path` when collecting test files from a
directory with no `__init__.py`.
"""
from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from m5_governor import ModelSpec


class FakeAdapter:
    """Minimal stand-in for the parts of `ProviderAdapter` that `preflight()`
    actually calls (`model_spec`, `count_input_tokens`). The remaining
    protocol members raise if exercised, since preflight tests should never
    reach them.
    """

    provider_name = "fake"

    def __init__(self, spec: ModelSpec, input_tokens: int):
        self._spec = spec
        self._input_tokens = input_tokens

    def model_spec(self, model: str) -> ModelSpec:
        return self._spec

    def count_input_tokens(self, payload: dict[str, Any]) -> int:
        return self._input_tokens

    def normalize_usage(self, response: Any, model: str):
        raise NotImplementedError

    def choose_model(self, risk: str) -> str:
        raise NotImplementedError

    def prepare_payload(self, **kwargs: Any) -> dict[str, Any]:
        raise NotImplementedError


def flat_rate_spec() -> ModelSpec:
    """A ModelSpec with a flat $1/Mtok input and output rate and no
    long-context cliff, so `conservative_worst_case()` reduces to exactly
    `(input_tokens + max_output_tokens) / 1e6` dollars -- easy to reason
    about precisely in budget-projection tests.
    """
    return ModelSpec(
        provider="fake",
        model="flat-rate",
        context_tokens=10_000_000,
        max_output_tokens=5_000_000,
        input_usd_per_mtok=1.0,
        output_usd_per_mtok=1.0,
    )


def write_ledger_lines(path: Path, lines: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def ledger_record(total_usd: float, when: datetime | None = None) -> str:
    ts = when or datetime.now(timezone.utc)
    return json.dumps({
        "timestamp": ts.isoformat().replace("+00:00", "Z"),
        "total_usd": total_usd,
    })


def a_day_in_current_month_other_than_today() -> datetime:
    """A UTC timestamp guaranteed to fall in the current year/month but on a
    different calendar date than "today", so it contributes to the monthly
    spend total in tests without also contributing to the daily total.
    """
    now = datetime.now(timezone.utc)
    day = 15 if now.day != 15 else 16
    return now.replace(day=day)
