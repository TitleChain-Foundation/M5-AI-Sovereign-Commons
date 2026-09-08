"""
M5 AI Governor — provider-neutral cost/context/policy control plane.

This reference code demonstrates the common adapter contract used by the
M5 provider adapters (OpenAI, Anthropic, ...). Provider pricing/context facts
embedded in adapter modules are dated configuration, not M5 canonical truth,
and must be revalidated against current provider documentation before use.
"""

from __future__ import annotations

from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Protocol, Literal
import json
import math
import os

Risk = Literal["routine", "balanced", "complex", "frontier"]


class GovernorError(RuntimeError):
    """Raised whenever the governor must fail closed (deny the call).

    This includes policy stops (context/budget limits) as well as any
    condition where the governor cannot establish ground truth about prior
    spend (missing/corrupt/unreadable cost ledger). In all such cases the
    call is denied rather than allowed to proceed on an assumption.
    """


@dataclass(frozen=True)
class ModelSpec:
    provider: str
    model: str
    context_tokens: int
    max_output_tokens: int

    input_usd_per_mtok: float
    output_usd_per_mtok: float
    cache_read_usd_per_mtok: float | None = None
    cache_write_usd_per_mtok: float | None = None
    cache_write_extended_usd_per_mtok: float | None = None

    cache_write_label: str = "cache_write"
    cache_write_extended_label: str = "cache_write_extended"

    batch_multiplier: float = 0.5
    flex_multiplier: float = 1.0
    fast_multiplier: float = 1.0

    long_context_threshold_tokens: int | None = None
    long_context_input_multiplier: float = 1.0
    long_context_output_multiplier: float = 1.0

    # Optional M5 operational ceiling lower than the provider context maximum.
    working_input_ceiling_tokens: int | None = None

    supports_effort: bool = False
    thinking_mode: str = "provider_default"
    privacy_class: str = "standard"
    reviewed_at: str = ""
    source_ref: str = ""
    notes: str = ""


@dataclass
class NormalizedUsage:
    provider: str
    model: str
    fresh_input_tokens: int
    cached_input_tokens: int
    cache_write_tokens: int
    cache_write_extended_tokens: int
    output_tokens: int
    reasoning_tokens: int = 0
    metered_extras_usd: float = 0.0

    @property
    def total_input_tokens(self) -> int:
        return (
            self.fresh_input_tokens
            + self.cached_input_tokens
            + self.cache_write_tokens
            + self.cache_write_extended_tokens
        )


@dataclass
class PriceBreakdown:
    provider: str
    model: str
    mode: str
    total_input_tokens: int
    fresh_input_tokens: int
    cached_input_tokens: int
    cache_write_tokens: int
    cache_write_extended_tokens: int
    output_tokens: int
    reasoning_tokens: int
    cache_hit_rate: float
    cache_write_label: str
    cache_write_extended_label: str
    over_long_context_threshold: bool
    fresh_input_usd: float
    cache_read_usd: float
    cache_write_usd: float
    cache_write_extended_usd: float
    output_usd: float
    metered_extras_usd: float
    long_context_penalty_usd: float
    total_usd: float


@dataclass
class GovernorConfig:
    max_call_usd: float = float(os.getenv("M5_AI_MAX_CALL_USD", "5.00"))
    daily_budget_usd: float = float(os.getenv("M5_AI_DAILY_BUDGET_USD", "25.00"))
    monthly_budget_usd: float = float(os.getenv("M5_AI_MONTHLY_BUDGET_USD", "300.00"))
    warning_context_fraction: float = float(os.getenv("M5_AI_WARNING_CONTEXT_FRACTION", "0.70"))
    hard_context_fraction: float = float(os.getenv("M5_AI_HARD_CONTEXT_FRACTION", "0.90"))
    default_max_output_tokens: int = int(os.getenv("M5_AI_DEFAULT_MAX_OUTPUT_TOKENS", "8000"))
    log_path: str = os.getenv("M5_AI_COST_LOG", "./logs/m5_ai_costs.jsonl")


class ProviderAdapter(Protocol):
    provider_name: str

    def model_spec(self, model: str) -> ModelSpec: ...
    def count_input_tokens(self, payload: dict[str, Any]) -> int: ...
    def normalize_usage(self, response: Any, model: str) -> NormalizedUsage: ...
    def choose_model(self, risk: Risk) -> str: ...
    def prepare_payload(
        self,
        *,
        input: Any,
        risk: Risk,
        model: str | None = None,
        **kwargs: Any,
    ) -> dict[str, Any]: ...


def _service_multiplier(spec: ModelSpec, mode: str) -> float:
    mode = (mode or "standard").lower()
    if mode in {"standard", "default", "auto"}:
        return 1.0
    if mode == "batch":
        return spec.batch_multiplier
    if mode == "flex":
        return spec.flex_multiplier
    if mode in {"fast", "priority"}:
        return spec.fast_multiplier
    raise GovernorError(f"Unknown service mode {mode!r}")


def price_usage(spec: ModelSpec, u: NormalizedUsage, mode: str = "standard") -> PriceBreakdown:
    sm = _service_multiplier(spec, mode)
    total_input = u.total_input_tokens
    over = bool(
        spec.long_context_threshold_tokens is not None
        and total_input > spec.long_context_threshold_tokens
    )
    im = spec.long_context_input_multiplier if over else 1.0
    om = spec.long_context_output_multiplier if over else 1.0

    cache_read_rate = spec.cache_read_usd_per_mtok
    if cache_read_rate is None:
        cache_read_rate = spec.input_usd_per_mtok

    cache_write_rate = spec.cache_write_usd_per_mtok
    if cache_write_rate is None:
        cache_write_rate = spec.input_usd_per_mtok

    cache_ext_rate = spec.cache_write_extended_usd_per_mtok
    if cache_ext_rate is None:
        cache_ext_rate = cache_write_rate

    # Base costs without provider long-context repricing.
    fresh_base = u.fresh_input_tokens / 1e6 * spec.input_usd_per_mtok
    cached_base = u.cached_input_tokens / 1e6 * cache_read_rate
    write_base = u.cache_write_tokens / 1e6 * cache_write_rate
    write_ext_base = u.cache_write_extended_tokens / 1e6 * cache_ext_rate
    output_base = u.output_tokens / 1e6 * spec.output_usd_per_mtok

    no_long = (fresh_base + cached_base + write_base + write_ext_base + output_base) * sm
    actual = (
        (fresh_base + cached_base + write_base + write_ext_base) * im
        + output_base * om
    ) * sm

    return PriceBreakdown(
        provider=u.provider,
        model=u.model,
        mode=mode,
        total_input_tokens=total_input,
        fresh_input_tokens=u.fresh_input_tokens,
        cached_input_tokens=u.cached_input_tokens,
        cache_write_tokens=u.cache_write_tokens,
        cache_write_extended_tokens=u.cache_write_extended_tokens,
        output_tokens=u.output_tokens,
        reasoning_tokens=u.reasoning_tokens,
        cache_hit_rate=round(u.cached_input_tokens / max(total_input, 1), 4),
        cache_write_label=spec.cache_write_label,
        cache_write_extended_label=spec.cache_write_extended_label,
        over_long_context_threshold=over,
        fresh_input_usd=round(fresh_base * im * sm, 6),
        cache_read_usd=round(cached_base * im * sm, 6),
        cache_write_usd=round(write_base * im * sm, 6),
        cache_write_extended_usd=round(write_ext_base * im * sm, 6),
        output_usd=round(output_base * om * sm, 6),
        metered_extras_usd=round(u.metered_extras_usd, 6),
        long_context_penalty_usd=round(actual - no_long, 6),
        total_usd=round(actual + u.metered_extras_usd, 6),
    )


def conservative_worst_case(
    spec: ModelSpec,
    input_tokens: int,
    max_output_tokens: int,
    mode: str = "standard",
) -> float:
    sm = _service_multiplier(spec, mode)
    over = bool(
        spec.long_context_threshold_tokens is not None
        and input_tokens > spec.long_context_threshold_tokens
    )
    im = spec.long_context_input_multiplier if over else 1.0
    om = spec.long_context_output_multiplier if over else 1.0
    return round(
        (
            input_tokens / 1e6 * spec.input_usd_per_mtok * im
            + max_output_tokens / 1e6 * spec.output_usd_per_mtok * om
        ) * sm,
        6,
    )


def _period_spend(path: Path, period: str) -> float:
    """Sum logged spend for the current UTC day or month.

    Fails closed: if the ledger exists but cannot be read, or contains any
    line that is not valid, complete JSON with the fields this function
    depends on, a precise GovernorError is raised instead of silently
    skipping the offending record. Silently skipping malformed/incomplete
    entries would let the governor undercount prior spend and admit calls
    that should have been blocked by the daily/monthly budget stop.
    """
    if not path.exists():
        return 0.0

    try:
        raw = path.read_text(encoding="utf-8")
    except OSError as exc:
        raise GovernorError(
            f"Cost ledger at {path} could not be read ({exc.__class__.__name__}: {exc}). "
            "Failing closed instead of assuming zero prior spend."
        ) from exc

    now = datetime.now(timezone.utc)
    total = 0.0
    required_fields = ("timestamp", "total_usd")

    for line_number, raw_line in enumerate(raw.splitlines(), start=1):
        line = raw_line.strip()
        if not line:
            # Blank/trailing lines are formatting artifacts, not data records.
            continue

        try:
            row = json.loads(line)
        except json.JSONDecodeError as exc:
            raise GovernorError(
                f"Cost ledger at {path} is malformed at line {line_number}: {exc}. "
                "Failing closed instead of skipping the corrupt record."
            ) from exc

        if not isinstance(row, dict):
            raise GovernorError(
                f"Cost ledger at {path} line {line_number} must be a JSON object, "
                f"got {type(row).__name__}. Failing closed instead of skipping the record."
            )

        missing = [field for field in required_fields if field not in row]
        if missing:
            raise GovernorError(
                f"Cost ledger at {path} line {line_number} is incomplete: missing "
                f"required field(s) {missing}. Failing closed instead of skipping the record."
            )

        try:
            ts = datetime.fromisoformat(str(row["timestamp"]).replace("Z", "+00:00"))
        except (ValueError, TypeError) as exc:
            raise GovernorError(
                f"Cost ledger at {path} line {line_number} has an unparseable "
                f"timestamp {row['timestamp']!r}: {exc}. "
                "Failing closed instead of skipping the record."
            ) from exc

        if ts.tzinfo is None:
            # A timezone-naive timestamp is ambiguous: there is no way to know
            # which UTC instant it names, so comparing it against "today"/"this
            # month" in UTC could silently misattribute spend to the wrong
            # period. Fail closed instead of guessing.
            raise GovernorError(
                f"Cost ledger at {path} line {line_number} has a timezone-naive "
                f"timestamp {row['timestamp']!r}. Failing closed instead of guessing "
                "which timezone it was recorded in; day/month accounting requires an "
                "unambiguous, timezone-aware timestamp."
            )
        # `log_price()` always writes UTC timestamps. Normalize every record to
        # UTC before comparing so a differently-offset (but still valid,
        # timezone-aware) timestamp is bucketed by the correct UTC calendar
        # day/month rather than by whatever raw date happens to appear in the
        # string.
        ts = ts.astimezone(timezone.utc)

        try:
            amount = float(row["total_usd"])
        except (TypeError, ValueError) as exc:
            raise GovernorError(
                f"Cost ledger at {path} line {line_number} has a non-numeric "
                f"total_usd {row['total_usd']!r}: {exc}. "
                "Failing closed instead of skipping the record."
            ) from exc

        if not math.isfinite(amount):
            raise GovernorError(
                f"Cost ledger at {path} line {line_number} has a non-finite "
                f"total_usd {row['total_usd']!r}. Failing closed instead of letting a "
                "NaN/Infinity value poison the accumulated spend total."
            )

        if amount < 0:
            raise GovernorError(
                f"Cost ledger at {path} line {line_number} has a negative "
                f"total_usd {row['total_usd']!r}. Failing closed instead of letting a "
                "negative value reduce the accumulated spend total."
            )

        if period == "day" and ts.date() != now.date():
            continue
        if period == "month" and (ts.year, ts.month) != (now.year, now.month):
            continue
        total += amount

    return total


def preflight(
    adapter: ProviderAdapter,
    payload: dict[str, Any],
    *,
    config: GovernorConfig | None = None,
    mode: str = "standard",
    itpm_limit: int | None = None,
    otpm_limit: int | None = None,
) -> dict[str, Any]:
    cfg = config or GovernorConfig()
    model = str(payload["model"])
    spec = adapter.model_spec(model)
    input_tokens = adapter.count_input_tokens(payload)
    max_output = int(
        payload.get("max_tokens")
        or payload.get("max_output_tokens")
        or cfg.default_max_output_tokens
    )

    if max_output > spec.max_output_tokens:
        raise GovernorError(
            f"{model}: requested max output {max_output:,} exceeds model maximum "
            f"{spec.max_output_tokens:,}."
        )

    if input_tokens + max_output > spec.context_tokens:
        raise GovernorError(
            f"{model}: {input_tokens:,} input + {max_output:,} output exceeds "
            f"{spec.context_tokens:,} context."
        )

    fraction_ceiling = int(spec.context_tokens * cfg.hard_context_fraction)
    hard = spec.working_input_ceiling_tokens or fraction_ceiling
    hard = min(hard, fraction_ceiling)

    if input_tokens > hard:
        raise GovernorError(
            f"{model}: {input_tokens:,} input exceeds M5 working ceiling {hard:,}. "
            "Retrieve, compact, or split before sending."
        )

    if itpm_limit is not None and input_tokens > itpm_limit:
        raise GovernorError(
            f"{model}: {input_tokens:,} input exceeds configured ITPM/TPM guard "
            f"{itpm_limit:,}."
        )
    if otpm_limit is not None and max_output > otpm_limit:
        raise GovernorError(
            f"{model}: requested {max_output:,} max output exceeds configured OTPM guard "
            f"{otpm_limit:,}."
        )

    wc = conservative_worst_case(spec, input_tokens, max_output, mode)
    if wc > cfg.max_call_usd:
        raise GovernorError(
            f"Per-call budget stop: worst-case ${wc:.2f} exceeds ${cfg.max_call_usd:.2f}."
        )

    # Budget stops are projections, not just a check of spend already logged:
    # a single worst-case call can push cumulative spend over the cap even
    # when prior logged spend alone is still under it. Reject *before* the
    # call is made whenever prior spend + this call's worst case would
    # exceed the daily or monthly ceiling.
    path = Path(cfg.log_path)
    day = _period_spend(path, "day")
    month = _period_spend(path, "month")

    projected_day = day + wc
    projected_month = month + wc

    if projected_day > cfg.daily_budget_usd:
        raise GovernorError(
            f"Daily budget stop: projected spend ${projected_day:.2f} "
            f"(${day:.2f} already spent today + ${wc:.2f} worst-case for this call) "
            f"exceeds ${cfg.daily_budget_usd:.2f}."
        )
    if projected_month > cfg.monthly_budget_usd:
        raise GovernorError(
            f"Monthly budget stop: projected spend ${projected_month:.2f} "
            f"(${month:.2f} already spent this month + ${wc:.2f} worst-case for this call) "
            f"exceeds ${cfg.monthly_budget_usd:.2f}."
        )

    return {
        "provider": spec.provider,
        "model": model,
        "input_tokens": input_tokens,
        "max_output_tokens": max_output,
        "context_tokens": spec.context_tokens,
        "context_fraction": round(input_tokens / spec.context_tokens, 4),
        "warning": input_tokens >= int(spec.context_tokens * cfg.warning_context_fraction),
        "working_ceiling_tokens": hard,
        "long_context_threshold_tokens": spec.long_context_threshold_tokens,
        "would_cross_long_context_threshold": bool(
            spec.long_context_threshold_tokens is not None
            and input_tokens > spec.long_context_threshold_tokens
        ),
        "itpm_limit": itpm_limit,
        "otpm_limit": otpm_limit,
        "worst_case_usd": wc,
        "day_spend_before_call": round(day, 4),
        "month_spend_before_call": round(month, 4),
        "projected_day_spend_usd": round(projected_day, 4),
        "projected_month_spend_usd": round(projected_month, 4),
    }


def log_price(
    p: PriceBreakdown,
    *,
    config: GovernorConfig | None = None,
    tag: str | None = None,
    response_id: str | None = None,
):
    cfg = config or GovernorConfig()
    path = Path(cfg.log_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    row = {
        "timestamp": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
        "response_id": response_id,
        "tag": tag,
        **asdict(p),
    }
    with path.open("a", encoding="utf-8") as f:
        f.write(json.dumps(row, separators=(",", ":")) + "\n")
