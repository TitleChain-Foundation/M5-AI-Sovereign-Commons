"""Regression tests for shared M5 governor pricing/worst-case math.

These exercise `price_usage()` and `conservative_worst_case()` in isolation
from any provider adapter, using a synthetic `ModelSpec`.
"""
from __future__ import annotations

from m5_governor import ModelSpec, NormalizedUsage, conservative_worst_case, price_usage


def _spec() -> ModelSpec:
    return ModelSpec(
        provider="openai", model="test",
        context_tokens=1_050_000, max_output_tokens=128_000,
        input_usd_per_mtok=10.0, output_usd_per_mtok=50.0,
        cache_read_usd_per_mtok=1.0, cache_write_usd_per_mtok=12.5,
        long_context_threshold_tokens=272_000,
        long_context_input_multiplier=2.0,
        long_context_output_multiplier=1.5,
        batch_multiplier=0.5, flex_multiplier=0.5, fast_multiplier=2.0,
    )


def _usage() -> NormalizedUsage:
    return NormalizedUsage(
        provider="openai", model="test",
        fresh_input_tokens=272_001, cached_input_tokens=0,
        cache_write_tokens=0, cache_write_extended_tokens=0,
        output_tokens=30_000,
    )


def test_long_context_pricing_and_penalty():
    p = price_usage(_spec(), _usage())
    assert p.over_long_context_threshold
    assert abs(p.total_usd - 7.69002) < 1e-9, p
    assert abs(p.long_context_penalty_usd - 3.47001) < 1e-9, p


def test_batch_mode_pricing():
    batch = price_usage(_spec(), _usage(), mode="batch")
    assert abs(batch.total_usd - 3.84501) < 1e-9, batch


def test_conservative_worst_case():
    wc = conservative_worst_case(_spec(), 260_000, 8_000)
    assert abs(wc - 3.0) < 1e-9, wc
