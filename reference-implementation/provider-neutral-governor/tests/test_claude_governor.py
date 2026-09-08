"""Regression tests for the M5-Anthropic (Claude) adapter's pricing tables."""
from __future__ import annotations

from m5_governor import NormalizedUsage, price_usage
from providers.anthropic_adapter import MODEL_SPECS


def _usage() -> NormalizedUsage:
    return NormalizedUsage(
        provider="anthropic",
        model="claude-sonnet-5",
        fresh_input_tokens=100_000,
        cached_input_tokens=200_000,
        cache_write_tokens=50_000,
        cache_write_extended_tokens=10_000,
        output_tokens=20_000,
        reasoning_tokens=5_000,
    )


def test_standard_pricing_and_cache_metadata():
    p = price_usage(MODEL_SPECS["claude-sonnet-5"], _usage())
    assert abs(p.total_usd - 0.605) < 1e-9, p
    assert p.total_input_tokens == 360_000
    assert p.cache_hit_rate == round(200_000 / 360_000, 4)
    assert p.cache_write_label == "5m_cache_write"
    assert p.cache_write_extended_label == "1h_cache_write"


def test_model_spec_context_and_output_ceilings():
    fable = MODEL_SPECS["claude-fable-5-1"]
    assert fable.context_tokens == 1_000_000
    assert fable.max_output_tokens == 128_000
    assert fable.cache_read_usd_per_mtok == 0.25

    haiku = MODEL_SPECS["claude-haiku-4-5"]
    assert haiku.context_tokens == 200_000
    assert haiku.max_output_tokens == 64_000


def test_batch_mode_pricing():
    pb = price_usage(MODEL_SPECS["claude-sonnet-5"], _usage(), mode="batch")
    assert abs(pb.total_usd - 0.3025) < 1e-9, pb
