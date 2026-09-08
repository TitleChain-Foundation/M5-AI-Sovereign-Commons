"""
M5-Anthropic reference adapter.

Provider facts verified 2026-09-06 against official Claude Platform documentation.
This is a reference adapter; provider enrollment in the M5 Sovereign Network is separate.

Draft-for-Comment provider-fact boundary
-----------------------------------------
Every `ModelSpec` this adapter exposes is a dated snapshot of provider-published
pricing/context facts, not M5 canonical truth. `model_spec()` enforces that
boundary at runtime: it refuses to serve any spec that does not carry a
`reviewed_at` date and a `source_ref` citation, so a spec added without
provenance fails closed instead of silently being trusted.
"""

from __future__ import annotations
from typing import Any
import os

from m5_governor import (
    ModelSpec, NormalizedUsage, GovernorConfig, GovernorError,
    preflight, price_usage, log_price, Risk
)

SOURCE = "https://platform.claude.com/docs/en/about-claude/pricing"

MODEL_SPECS = {
    "claude-haiku-4-5": ModelSpec(
        provider="anthropic", model="claude-haiku-4-5",
        context_tokens=200_000, max_output_tokens=64_000,
        input_usd_per_mtok=1.00, output_usd_per_mtok=5.00,
        cache_read_usd_per_mtok=0.10,
        cache_write_usd_per_mtok=1.25,
        cache_write_extended_usd_per_mtok=2.00,
        cache_write_label="5m_cache_write",
        cache_write_extended_label="1h_cache_write",
        supports_effort=False,
        thinking_mode="extended_optional",
        reviewed_at="2026-09-06", source_ref=SOURCE,
    ),
    "claude-haiku-4-5-20251001": ModelSpec(
        provider="anthropic", model="claude-haiku-4-5-20251001",
        context_tokens=200_000, max_output_tokens=64_000,
        input_usd_per_mtok=1.00, output_usd_per_mtok=5.00,
        cache_read_usd_per_mtok=0.10,
        cache_write_usd_per_mtok=1.25,
        cache_write_extended_usd_per_mtok=2.00,
        cache_write_label="5m_cache_write",
        cache_write_extended_label="1h_cache_write",
        supports_effort=False,
        thinking_mode="extended_optional",
        reviewed_at="2026-09-06", source_ref=SOURCE,
    ),
    "claude-sonnet-5": ModelSpec(
        provider="anthropic", model="claude-sonnet-5",
        context_tokens=1_000_000, max_output_tokens=128_000,
        input_usd_per_mtok=2.00, output_usd_per_mtok=10.00,
        cache_read_usd_per_mtok=0.20,
        cache_write_usd_per_mtok=2.50,
        cache_write_extended_usd_per_mtok=4.00,
        cache_write_label="5m_cache_write",
        cache_write_extended_label="1h_cache_write",
        supports_effort=True, thinking_mode="adaptive_default",
        reviewed_at="2026-09-06", source_ref=SOURCE,
    ),
    "claude-opus-5": ModelSpec(
        provider="anthropic", model="claude-opus-5",
        context_tokens=1_000_000, max_output_tokens=128_000,
        input_usd_per_mtok=5.00, output_usd_per_mtok=25.00,
        cache_read_usd_per_mtok=0.50,
        cache_write_usd_per_mtok=6.25,
        cache_write_extended_usd_per_mtok=10.00,
        cache_write_label="5m_cache_write",
        cache_write_extended_label="1h_cache_write",
        supports_effort=True, thinking_mode="adaptive_default",
        reviewed_at="2026-09-06", source_ref=SOURCE,
    ),
    "claude-fable-5-1": ModelSpec(
        provider="anthropic", model="claude-fable-5-1",
        context_tokens=1_000_000, max_output_tokens=128_000,
        input_usd_per_mtok=10.00, output_usd_per_mtok=50.00,
        cache_read_usd_per_mtok=0.25,
        cache_write_usd_per_mtok=12.50,
        cache_write_extended_usd_per_mtok=20.00,
        cache_write_label="5m_cache_write",
        cache_write_extended_label="1h_cache_write",
        supports_effort=True, thinking_mode="adaptive_always_on",
        privacy_class="retention_review_required",
        reviewed_at="2026-09-06", source_ref=SOURCE,
    ),
}

_VALID_EFFORT_LEVELS = {"low", "medium", "high"}


def _get(obj: Any, name: str, default: Any = 0) -> Any:
    if obj is None:
        return default
    if isinstance(obj, dict):
        return obj.get(name, default)
    return getattr(obj, name, default)


def _assert_model_spec_has_provenance(spec: ModelSpec) -> None:
    """Enforce the Draft-for-Comment provider-fact boundary.

    A `ModelSpec` exposed by this adapter is a dated snapshot of pricing and
    context facts published by the provider, not M5 canonical truth. Callers
    need to be able to tell that from the spec itself. Fail closed rather
    than silently pricing/preflighting a call against a spec that carries no
    review date or citation.
    """
    if not spec.reviewed_at or not spec.source_ref:
        raise GovernorError(
            f"Model spec for {spec.provider}/{spec.model} is missing required "
            "provenance (reviewed_at and/or source_ref). Refusing to serve "
            "unverified provider facts: this adapter's pricing/context data "
            "is a dated snapshot, not M5 canonical truth, and every spec must "
            "carry its review date and source before it can be trusted."
        )


def _non_negative_int(value: Any, field_name: str) -> int:
    """Coerce a raw usage field to a non-negative int, failing closed on
    non-numeric or negative values instead of silently accepting them.

    A negative or non-numeric token/request count in a provider usage report
    is internally inconsistent; pricing it anyway could under- or over-charge
    silently, so the governor refuses to price the response at all.
    """
    try:
        n = int(value)
    except (TypeError, ValueError) as exc:
        raise GovernorError(
            f"Claude usage field {field_name!r} is not an integer: {value!r}. "
            "Refusing to price a response with an unparseable usage field."
        ) from exc
    if n < 0:
        raise GovernorError(
            f"Claude usage field {field_name!r} is negative ({n}). Refusing "
            "to price a response with an internally inconsistent usage report."
        )
    return n


class AnthropicAdapter:
    provider_name = "anthropic"

    def __init__(self, client: Any):
        self.client = client

    def model_spec(self, model: str) -> ModelSpec:
        if model not in MODEL_SPECS:
            raise GovernorError(
                f"Unknown/unverified Claude model {model!r}. "
                f"Known models: {sorted(MODEL_SPECS)}."
            )
        spec = MODEL_SPECS[model]
        _assert_model_spec_has_provenance(spec)
        return spec

    def choose_model(self, risk: Risk) -> str:
        routes = {
            "routine": "claude-haiku-4-5",
            "balanced": "claude-sonnet-5",
            "complex": "claude-opus-5",
            "frontier": "claude-fable-5-1",
        }
        try:
            return routes[risk]
        except KeyError:
            raise GovernorError(
                f"Unknown risk tier {risk!r}; expected one of {sorted(routes)}."
            ) from None

    def prepare_payload(
        self,
        *,
        input: Any,
        risk: Risk = "balanced",
        model: str | None = None,
        max_tokens: int = 8_000,
        effort: str | None = None,
        system: Any | None = None,
        cache_ttl: str | None = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        if input is None or (isinstance(input, (str, list, tuple)) and len(input) == 0):
            raise GovernorError("prepare_payload() requires non-empty `input`.")
        if not isinstance(max_tokens, int) or isinstance(max_tokens, bool) or max_tokens <= 0:
            raise GovernorError(
                f"max_tokens must be a positive integer, got {max_tokens!r}."
            )

        model = model or self.choose_model(risk)
        spec = self.model_spec(model)
        messages = [{"role": "user", "content": input}] if isinstance(input, str) else input
        payload = {"model": model, "max_tokens": max_tokens, "messages": messages, **kwargs}
        if system is not None:
            payload["system"] = system
        if spec.supports_effort:
            if effort is not None and effort not in _VALID_EFFORT_LEVELS:
                raise GovernorError(
                    f"effort must be one of {sorted(_VALID_EFFORT_LEVELS)}, got {effort!r}."
                )
            payload["output_config"] = {
                **payload.get("output_config", {}),
                "effort": effort or ("high" if risk == "frontier" else "low"),
            }
        elif effort is not None:
            raise GovernorError(
                f"{model} does not support an effort/thinking-budget override "
                f"(thinking_mode={spec.thinking_mode!r}); pass effort=None."
            )
        if cache_ttl:
            if cache_ttl not in {"5m", "1h"}:
                raise GovernorError("cache_ttl must be '5m' or '1h'")
            payload["cache_control"] = {"type": "ephemeral", "ttl": cache_ttl}
        return payload

    def count_input_tokens(self, payload: dict[str, Any]) -> int:
        allowed = {
            "model", "messages", "system", "tools", "tool_choice",
            "thinking", "output_config", "cache_control",
        }
        counted = self.client.messages.count_tokens(
            **{k: v for k, v in payload.items() if k in allowed}
        )
        return int(_get(counted, "input_tokens", 0))

    def normalize_usage(self, response: Any, model: str) -> NormalizedUsage:
        usage = _get(response, "usage", {})
        creation = _get(usage, "cache_creation", {}) or {}

        fresh = _non_negative_int(_get(usage, "input_tokens", 0) or 0, "input_tokens")
        read = _non_negative_int(
            _get(usage, "cache_read_input_tokens", 0) or 0, "cache_read_input_tokens"
        )
        total_write = _non_negative_int(
            _get(usage, "cache_creation_input_tokens", 0) or 0, "cache_creation_input_tokens"
        )
        w5 = _non_negative_int(
            _get(creation, "ephemeral_5m_input_tokens", 0) or 0, "ephemeral_5m_input_tokens"
        )
        w1 = _non_negative_int(
            _get(creation, "ephemeral_1h_input_tokens", 0) or 0, "ephemeral_1h_input_tokens"
        )

        if w5 + w1 == 0 and total_write:
            # Older/partial responses may report only the aggregate; treat it
            # as a 5-minute write, matching the provider's default TTL.
            w5 = total_write
        elif total_write and (w5 + w1) != total_write:
            raise GovernorError(
                f"Claude usage cache_creation breakdown ({w5} 5m + {w1} 1h = "
                f"{w5 + w1}) does not match cache_creation_input_tokens "
                f"({total_write}). Refusing to guess which figure is "
                "authoritative for a response with an internally "
                "inconsistent usage report."
            )

        out = _non_negative_int(_get(usage, "output_tokens", 0) or 0, "output_tokens")
        details = _get(usage, "output_tokens_details", {}) or {}
        thinking = _non_negative_int(
            _get(details, "thinking_tokens", 0) or 0, "thinking_tokens"
        )

        tools = _get(usage, "server_tool_use", {}) or {}
        web_search_requests = _non_negative_int(
            _get(tools, "web_search_requests", 0) or 0, "web_search_requests"
        )

        return NormalizedUsage(
            provider="anthropic", model=model,
            fresh_input_tokens=fresh,
            cached_input_tokens=read,
            cache_write_tokens=w5,
            cache_write_extended_tokens=w1,
            output_tokens=out,
            reasoning_tokens=thinking,
            metered_extras_usd=web_search_requests * 0.01,
        )


class GuardedClaude:
    def __init__(self, client: Any, config: GovernorConfig | None = None):
        self.client = client
        self.config = config or GovernorConfig()
        self.adapter = AnthropicAdapter(client)

    def respond(self, *, input: Any, risk: Risk = "balanced", model: str | None = None,
                tag: str | None = None, **kwargs: Any):
        payload = self.adapter.prepare_payload(input=input, risk=risk, model=model, **kwargs)
        selected = payload["model"]

        # Organization limits vary. Prefer explicitly configured live limits in production.
        itpm = int(os.getenv("ANTHROPIC_ITPM_LIMIT", "0") or 0) or None
        otpm = int(os.getenv("ANTHROPIC_OTPM_LIMIT", "0") or 0) or None

        report = preflight(
            self.adapter, payload, config=self.config,
            itpm_limit=itpm, otpm_limit=otpm,
        )
        response = self.client.messages.create(**payload)
        usage = self.adapter.normalize_usage(response, selected)
        priced = price_usage(self.adapter.model_spec(selected), usage)
        log_price(priced, config=self.config, tag=tag, response_id=str(_get(response, "id", "") or ""))
        return response, report, priced
