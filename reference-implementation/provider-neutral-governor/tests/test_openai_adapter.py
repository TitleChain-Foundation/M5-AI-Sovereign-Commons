"""Regression tests for the M5-OpenAI adapter's token-counting/pricing glue."""
from __future__ import annotations

from types import SimpleNamespace

from m5_governor import price_usage
from providers.openai_adapter import MODEL_SPECS, OpenAIAdapter


class _Counter:
    def count(self, **kwargs):
        return SimpleNamespace(input_tokens=200_000)


class _Responses:
    input_tokens = _Counter()


class _FakeClient:
    responses = _Responses()


def _adapter() -> OpenAIAdapter:
    return OpenAIAdapter(_FakeClient())


def test_choose_model_routes_by_risk():
    adapter = _adapter()
    assert adapter.choose_model("routine") == "gpt-5.6-luna"
    assert adapter.choose_model("frontier") == "gpt-6-astra"


def test_count_input_tokens_uses_sdk_counter():
    adapter = _adapter()
    assert adapter.count_input_tokens({"model": "gpt-6-astra", "input": "x"}) == 200_000


def test_tpm_limit_by_tier():
    adapter = _adapter()
    assert adapter.tpm_limit("gpt-5.6-luna", 5) == 180_000_000
    assert adapter.tpm_limit("gpt-6-astra", 5) == 40_000_000


def test_normalize_usage_and_pricing():
    adapter = _adapter()
    usage_obj = SimpleNamespace(
        input_tokens=200_000,
        input_tokens_details=SimpleNamespace(cached_tokens=100_000, cache_write_tokens=20_000),
        output_tokens=10_000,
        output_tokens_details=SimpleNamespace(reasoning_tokens=2_000),
    )
    resp = SimpleNamespace(usage=usage_obj)

    u = adapter.normalize_usage(resp, "gpt-6-astra")
    assert u.fresh_input_tokens == 80_000
    assert u.cached_input_tokens == 100_000
    assert u.cache_write_tokens == 20_000

    p = price_usage(MODEL_SPECS["gpt-6-astra"], u)
    # .08*10 + .1*1 + .02*12.5 + .01*50 = 1.65
    assert abs(p.total_usd - 1.65) < 1e-9, p
