"""Regression tests for explicit validation/fail-closed behavior added to the
M5-Anthropic adapter: unknown risk/model handling, invalid prepare_payload
inputs, the Draft-for-Comment provider-fact provenance boundary on
`model_spec()`, and rejection of negative/inconsistent usage fields in
`normalize_usage()`.
"""
from __future__ import annotations

from types import SimpleNamespace

import pytest

from m5_governor import GovernorError, ModelSpec
from providers.anthropic_adapter import (
    AnthropicAdapter,
    MODEL_SPECS,
    _assert_model_spec_has_provenance,
)


class _FakeClient:
    pass


def _adapter() -> AnthropicAdapter:
    return AnthropicAdapter(_FakeClient())


# -- choose_model / model_spec: unknown risk/model handling -----------------

def test_choose_model_rejects_unknown_risk():
    adapter = _adapter()
    with pytest.raises(GovernorError, match=r"Unknown risk tier 'urgent'"):
        adapter.choose_model("urgent")


def test_model_spec_rejects_unknown_model():
    adapter = _adapter()
    with pytest.raises(GovernorError, match=r"Unknown/unverified Claude model"):
        adapter.model_spec("claude-nonexistent")


def test_model_spec_enforces_provenance_boundary():
    """A spec missing reviewed_at/source_ref must fail closed, even though it
    is otherwise well-formed. This directly exercises the Draft-for-Comment
    provider-fact boundary rather than only checking existing, valid specs.
    """
    unverified = ModelSpec(
        provider="anthropic", model="claude-hypothetical",
        context_tokens=100_000, max_output_tokens=8_000,
        input_usd_per_mtok=1.0, output_usd_per_mtok=1.0,
        # reviewed_at and source_ref intentionally left at their "" defaults.
    )
    with pytest.raises(GovernorError, match=r"missing required provenance"):
        _assert_model_spec_has_provenance(unverified)


def test_all_shipped_model_specs_pass_the_provenance_boundary():
    for spec in MODEL_SPECS.values():
        _assert_model_spec_has_provenance(spec)  # must not raise


# -- prepare_payload: invalid input handling ---------------------------------

def test_prepare_payload_rejects_empty_input():
    adapter = _adapter()
    with pytest.raises(GovernorError, match=r"non-empty `input`"):
        adapter.prepare_payload(input="", risk="balanced")
    with pytest.raises(GovernorError, match=r"non-empty `input`"):
        adapter.prepare_payload(input=[], risk="balanced")


def test_prepare_payload_rejects_non_positive_max_tokens():
    adapter = _adapter()
    with pytest.raises(GovernorError, match=r"max_tokens must be a positive integer"):
        adapter.prepare_payload(input="hi", risk="balanced", max_tokens=0)
    with pytest.raises(GovernorError, match=r"max_tokens must be a positive integer"):
        adapter.prepare_payload(input="hi", risk="balanced", max_tokens=-100)


def test_prepare_payload_rejects_invalid_effort_value():
    adapter = _adapter()
    with pytest.raises(GovernorError, match=r"effort must be one of"):
        adapter.prepare_payload(input="hi", risk="balanced", model="claude-sonnet-5", effort="extreme")


def test_prepare_payload_rejects_effort_for_model_that_does_not_support_it():
    adapter = _adapter()
    with pytest.raises(GovernorError, match=r"does not support an effort"):
        adapter.prepare_payload(input="hi", risk="routine", model="claude-haiku-4-5", effort="high")


def test_prepare_payload_accepts_valid_effort_for_supported_model():
    adapter = _adapter()
    payload = adapter.prepare_payload(
        input="hi", risk="balanced", model="claude-sonnet-5", effort="high"
    )
    assert payload["output_config"]["effort"] == "high"


# -- normalize_usage: negative / non-numeric / inconsistent fields ----------

def _usage_response(**usage_fields):
    return SimpleNamespace(usage=SimpleNamespace(**usage_fields))


def test_normalize_usage_rejects_negative_field():
    adapter = _adapter()
    resp = _usage_response(input_tokens=-5, output_tokens=10)
    with pytest.raises(GovernorError, match=r"'input_tokens' is negative"):
        adapter.normalize_usage(resp, "claude-sonnet-5")


def test_normalize_usage_rejects_non_numeric_field():
    adapter = _adapter()
    resp = _usage_response(input_tokens="lots", output_tokens=10)
    with pytest.raises(GovernorError, match=r"'input_tokens' is not an integer"):
        adapter.normalize_usage(resp, "claude-sonnet-5")


def test_normalize_usage_rejects_inconsistent_cache_breakdown():
    adapter = _adapter()
    resp = _usage_response(
        input_tokens=100,
        output_tokens=10,
        cache_creation_input_tokens=50,
        cache_creation=SimpleNamespace(
            ephemeral_5m_input_tokens=10,
            ephemeral_1h_input_tokens=10,  # 10 + 10 = 20 != 50
        ),
    )
    with pytest.raises(GovernorError, match=r"cache_creation breakdown"):
        adapter.normalize_usage(resp, "claude-sonnet-5")


def test_normalize_usage_accepts_consistent_cache_breakdown():
    adapter = _adapter()
    resp = _usage_response(
        input_tokens=100,
        output_tokens=10,
        cache_creation_input_tokens=20,
        cache_creation=SimpleNamespace(
            ephemeral_5m_input_tokens=15,
            ephemeral_1h_input_tokens=5,  # 15 + 5 == 20, consistent
        ),
    )
    u = adapter.normalize_usage(resp, "claude-sonnet-5")
    assert u.cache_write_tokens == 15
    assert u.cache_write_extended_tokens == 5


def test_normalize_usage_falls_back_to_aggregate_when_breakdown_absent():
    adapter = _adapter()
    resp = _usage_response(
        input_tokens=100,
        output_tokens=10,
        cache_creation_input_tokens=30,  # no per-TTL breakdown at all
    )
    u = adapter.normalize_usage(resp, "claude-sonnet-5")
    assert u.cache_write_tokens == 30
    assert u.cache_write_extended_tokens == 0
