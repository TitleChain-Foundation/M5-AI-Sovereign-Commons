"""
M5-OpenAI reference adapter for the shared M5 AI Governor.

Provider facts verified 2026-09-06 from official OpenAI API documentation.
M5-OpenAI is an M5-governed connector name; this file does not claim OpenAI has
completed M5 sovereign-network enrollment.
"""

from __future__ import annotations
from typing import Any
import json
import os
import urllib.request
import urllib.error

from m5_governor import (
    ModelSpec, NormalizedUsage, GovernorConfig, GovernorError,
    preflight, price_usage, log_price, Risk
)

OPENAI_MODEL_SOURCE = "https://developers.openai.com/api/docs/models"
ASTRA_SOURCE = "https://developers.openai.com/api/docs/models/gpt-6-astra"
SOL_SOURCE = "https://developers.openai.com/api/docs/models/gpt-5.6-sol"
TERRA_SOURCE = "https://developers.openai.com/api/docs/models/gpt-5.6-terra"
LUNA_SOURCE = "https://developers.openai.com/api/docs/models/gpt-5.6-luna"

MODEL_SPECS = {
    "gpt-6-astra": ModelSpec(
        provider="openai", model="gpt-6-astra",
        context_tokens=1_050_000, max_output_tokens=128_000,
        input_usd_per_mtok=10.00, output_usd_per_mtok=50.00,
        cache_read_usd_per_mtok=1.00,
        cache_write_usd_per_mtok=12.50,
        cache_write_label="30m_cache_write",
        batch_multiplier=0.5, flex_multiplier=0.5, fast_multiplier=2.0,
        long_context_threshold_tokens=272_000,
        long_context_input_multiplier=2.0,
        long_context_output_multiplier=1.5,
        working_input_ceiling_tokens=260_000,
        supports_effort=True,
        thinking_mode="reasoning_effort",
        reviewed_at="2026-09-06", source_ref=ASTRA_SOURCE,
    ),
    "gpt-5.6-sol": ModelSpec(
        provider="openai", model="gpt-5.6-sol",
        context_tokens=1_050_000, max_output_tokens=128_000,
        input_usd_per_mtok=4.00, output_usd_per_mtok=20.00,
        cache_read_usd_per_mtok=0.40,
        cache_write_usd_per_mtok=5.00,
        cache_write_label="30m_cache_write",
        batch_multiplier=0.5, flex_multiplier=0.5, fast_multiplier=2.0,
        long_context_threshold_tokens=272_000,
        long_context_input_multiplier=2.0,
        long_context_output_multiplier=1.5,
        working_input_ceiling_tokens=260_000,
        supports_effort=True,
        thinking_mode="reasoning_effort",
        reviewed_at="2026-09-06", source_ref=SOL_SOURCE,
        notes="Promotional pricing documented as available at least through 2026-11-21; revalidate after that date.",
    ),
    "gpt-5.6-terra": ModelSpec(
        provider="openai", model="gpt-5.6-terra",
        context_tokens=1_050_000, max_output_tokens=128_000,
        input_usd_per_mtok=2.00, output_usd_per_mtok=12.00,
        cache_read_usd_per_mtok=0.20,
        cache_write_usd_per_mtok=2.50,
        cache_write_label="30m_cache_write",
        batch_multiplier=0.5, flex_multiplier=0.5, fast_multiplier=2.0,
        long_context_threshold_tokens=272_000,
        long_context_input_multiplier=2.0,
        long_context_output_multiplier=1.5,
        working_input_ceiling_tokens=260_000,
        supports_effort=True,
        thinking_mode="reasoning_effort",
        reviewed_at="2026-09-06", source_ref=TERRA_SOURCE,
    ),
    "gpt-5.6-luna": ModelSpec(
        provider="openai", model="gpt-5.6-luna",
        context_tokens=1_050_000, max_output_tokens=128_000,
        input_usd_per_mtok=0.20, output_usd_per_mtok=1.20,
        cache_read_usd_per_mtok=0.02,
        cache_write_usd_per_mtok=0.25,
        cache_write_label="30m_cache_write",
        batch_multiplier=0.5, flex_multiplier=0.5, fast_multiplier=2.0,
        long_context_threshold_tokens=272_000,
        long_context_input_multiplier=2.0,
        long_context_output_multiplier=1.5,
        working_input_ceiling_tokens=260_000,
        supports_effort=True,
        thinking_mode="reasoning_effort",
        reviewed_at="2026-09-06", source_ref=LUNA_SOURCE,
    ),
}

# Published PAYG TPM values. Luna currently has a larger throughput schedule.
TPM_BY_TIER = {
    "gpt-6-astra": {1: 500_000, 2: 1_000_000, 3: 2_000_000, 4: 4_000_000, 5: 40_000_000},
    "gpt-5.6-sol": {1: 500_000, 2: 1_000_000, 3: 2_000_000, 4: 4_000_000, 5: 40_000_000},
    "gpt-5.6-terra": {1: 500_000, 2: 1_000_000, 3: 2_000_000, 4: 4_000_000, 5: 40_000_000},
    "gpt-5.6-luna": {1: 500_000, 2: 2_000_000, 3: 4_000_000, 4: 10_000_000, 5: 180_000_000},
}


def _get(obj: Any, name: str, default: Any = 0) -> Any:
    if obj is None:
        return default
    if isinstance(obj, dict):
        return obj.get(name, default)
    return getattr(obj, name, default)


class OpenAIAdapter:
    provider_name = "openai"

    def __init__(self, client: Any, api_key: str | None = None):
        self.client = client
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")

    def model_spec(self, model: str) -> ModelSpec:
        if model == "gpt-5.6":
            model = "gpt-5.6-sol"
        if model not in MODEL_SPECS:
            raise GovernorError(f"Unknown/unverified OpenAI model {model!r}")
        return MODEL_SPECS[model]

    def choose_model(self, risk: Risk) -> str:
        return {
            "routine": "gpt-5.6-luna",
            "balanced": "gpt-5.6-terra",
            "complex": "gpt-5.6-sol",
            "frontier": "gpt-6-astra",
        }[risk]

    def prepare_payload(
        self,
        *,
        input: Any,
        risk: Risk = "balanced",
        model: str | None = None,
        max_output_tokens: int = 8_000,
        effort: str | None = None,
        service_tier: str = "default",
        **kwargs: Any,
    ) -> dict[str, Any]:
        model = model or self.choose_model(risk)
        chosen_effort = effort or ("high" if risk in {"complex", "frontier"} else "low")
        return {
            "model": model,
            "input": input,
            "max_output_tokens": max_output_tokens,
            "reasoning": {"effort": chosen_effort},
            "service_tier": service_tier,
            **kwargs,
        }

    def count_input_tokens(self, payload: dict[str, Any]) -> int:
        allowed = {
            "model", "input", "instructions", "tools", "tool_choice",
            "reasoning", "text", "previous_response_id", "conversation",
            "prompt", "prompt_cache_key", "prompt_cache_options",
        }
        body = {k: v for k, v in payload.items() if k in allowed}

        # Prefer SDK support when present. A callable counter failure is
        # authoritative and must not be hidden by retrying through another path.
        responses = getattr(self.client, "responses", None)
        sub = getattr(responses, "input_tokens", None)
        counter = getattr(sub, "count", None)
        if callable(counter):
            result = counter(**body)
            return int(_get(result, "input_tokens", _get(result, "total_tokens", 0)))

        if not self.api_key:
            raise GovernorError(
                "Exact OpenAI preflight requires OPENAI_API_KEY or an SDK client "
                "supporting responses.input_tokens.count()."
            )

        req = urllib.request.Request(
            "https://api.openai.com/v1/responses/input_tokens",
            data=json.dumps(body).encode("utf-8"),
            headers={
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json",
            },
            method="POST",
        )
        try:
            with urllib.request.urlopen(req, timeout=60) as resp:
                data = json.load(resp)
        except urllib.error.HTTPError as e:
            detail = e.read().decode("utf-8", errors="replace")
            raise GovernorError(
                f"OpenAI token-count preflight failed ({e.code}): {detail[:500]}"
            ) from e

        for field in ("input_tokens", "total_tokens", "tokens"):
            if field in data:
                return int(data[field])
        raise GovernorError(f"Unexpected OpenAI token-count response: {list(data)}")

    def normalize_usage(self, response: Any, model: str) -> NormalizedUsage:
        usage = _get(response, "usage", {})
        details = _get(usage, "input_tokens_details", {}) or {}
        output_details = _get(usage, "output_tokens_details", {}) or {}

        total_input = int(_get(usage, "input_tokens", 0) or 0)
        cached = int(_get(details, "cached_tokens", 0) or 0)
        written = int(_get(details, "cache_write_tokens", 0) or 0)
        fresh = max(0, total_input - cached - written)

        return NormalizedUsage(
            provider="openai", model=model,
            fresh_input_tokens=fresh,
            cached_input_tokens=cached,
            cache_write_tokens=written,
            cache_write_extended_tokens=0,
            output_tokens=int(_get(usage, "output_tokens", 0) or 0),
            reasoning_tokens=int(_get(output_details, "reasoning_tokens", 0) or 0),
            metered_extras_usd=0.0,  # tool charges require tool-specific reconciliation
        )

    def tpm_limit(self, model: str, usage_tier: int) -> int | None:
        model = "gpt-5.6-sol" if model == "gpt-5.6" else model
        return TPM_BY_TIER.get(model, {}).get(usage_tier)


class GuardedOpenAI:
    def __init__(self, client: Any, config: GovernorConfig | None = None, api_key: str | None = None):
        self.client = client
        self.config = config or GovernorConfig()
        self.adapter = OpenAIAdapter(client, api_key=api_key)

    def respond(
        self,
        *,
        input: Any,
        risk: Risk = "balanced",
        model: str | None = None,
        tag: str | None = None,
        mode: str = "standard",
        **kwargs: Any,
    ):
        payload = self.adapter.prepare_payload(input=input, risk=risk, model=model, **kwargs)
        selected = payload["model"]
        tier = int(os.getenv("OPENAI_USAGE_TIER", "1"))
        tpm = self.adapter.tpm_limit(selected, tier)

        report = preflight(
            self.adapter, payload, config=self.config, mode=mode, itpm_limit=tpm
        )
        response = self.client.responses.create(**payload)
        usage = self.adapter.normalize_usage(response, selected)
        actual_tier = str(_get(response, "service_tier", mode) or mode)
        if actual_tier == "default":
            actual_tier = mode
        priced = price_usage(self.adapter.model_spec(selected), usage, mode=actual_tier)
        log_price(
            priced, config=self.config, tag=tag,
            response_id=str(_get(response, "id", "") or "")
        )
        return response, report, priced
