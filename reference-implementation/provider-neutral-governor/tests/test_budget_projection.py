"""Regression tests: `preflight()` must reject a call whenever prior logged
spend for the day/month *plus this call's worst-case cost* would exceed the
configured budget cap -- not only when prior spend alone is already at/over
the cap.

Before this fix, the check was effectively `day_spend >= daily_budget_usd`
(and the monthly equivalent), which ignores the pending call entirely. That
let a single expensive call push cumulative spend over budget without ever
being blocked, since the check only looked backward at what was already
logged, not forward at what this call could cost.
"""
from __future__ import annotations

import pytest

from m5_governor import GovernorConfig, GovernorError, conservative_worst_case, preflight

from _helpers import FakeAdapter, a_day_in_current_month_other_than_today, flat_rate_spec, ledger_record, write_ledger_lines


def _payload(max_output_tokens: int) -> dict:
    return {"model": "flat-rate", "max_output_tokens": max_output_tokens}


def test_daily_budget_rejects_when_projection_exceeds_cap(tmp_path):
    spec = flat_rate_spec()
    ledger = tmp_path / "costs.jsonl"
    write_ledger_lines(ledger, [ledger_record(20.0)])  # $20 already spent today

    # Worst case for this call: (3,000,000 + 3,000,000) / 1e6 * $1 = $6.00.
    wc = conservative_worst_case(spec, 3_000_000, 3_000_000)
    assert wc == pytest.approx(6.0)  # sanity check: $20 + $6 = $26 > $25 cap

    adapter = FakeAdapter(spec, input_tokens=3_000_000)
    cfg = GovernorConfig(
        max_call_usd=100.0, daily_budget_usd=25.0, monthly_budget_usd=1000.0,
        log_path=str(ledger),
    )

    with pytest.raises(GovernorError, match=r"Daily budget stop"):
        preflight(adapter, _payload(3_000_000), config=cfg)


def test_daily_budget_allows_when_projection_within_cap(tmp_path):
    spec = flat_rate_spec()
    ledger = tmp_path / "costs.jsonl"
    write_ledger_lines(ledger, [ledger_record(18.0)])  # $18 already spent today

    adapter = FakeAdapter(spec, input_tokens=3_000_000)
    cfg = GovernorConfig(
        max_call_usd=100.0, daily_budget_usd=25.0, monthly_budget_usd=1000.0,
        log_path=str(ledger),
    )

    report = preflight(adapter, _payload(3_000_000), config=cfg)
    assert report["worst_case_usd"] == pytest.approx(6.0)
    assert report["day_spend_before_call"] == pytest.approx(18.0)
    assert report["projected_day_spend_usd"] == pytest.approx(24.0)


def test_regression_prior_spend_alone_under_cap_but_projection_over_cap(tmp_path):
    """Prior spend ($24) is comfortably under the $25 cap on its own -- the
    pre-fix check (`day >= daily_budget_usd`) would have let this call
    through. The pending call's own worst case ($2) pushes the projected
    total to $26, which must now be rejected pre-call.
    """
    spec = flat_rate_spec()
    ledger = tmp_path / "costs.jsonl"
    write_ledger_lines(ledger, [ledger_record(24.0)])

    adapter = FakeAdapter(spec, input_tokens=1_000_000)
    cfg = GovernorConfig(
        max_call_usd=100.0, daily_budget_usd=25.0, monthly_budget_usd=1000.0,
        log_path=str(ledger),
    )

    with pytest.raises(GovernorError, match=r"Daily budget stop"):
        preflight(adapter, _payload(1_000_000), config=cfg)  # worst case == $2.00


def test_monthly_budget_rejects_when_projection_exceeds_cap(tmp_path):
    spec = flat_rate_spec()
    ledger = tmp_path / "costs.jsonl"
    other_day = a_day_in_current_month_other_than_today()
    write_ledger_lines(ledger, [ledger_record(296.0, when=other_day)])

    adapter = FakeAdapter(spec, input_tokens=3_000_000)
    cfg = GovernorConfig(
        max_call_usd=100.0, daily_budget_usd=1000.0, monthly_budget_usd=300.0,
        log_path=str(ledger),
    )

    with pytest.raises(GovernorError, match=r"Monthly budget stop"):
        preflight(adapter, _payload(3_000_000), config=cfg)  # worst case == $6.00


def test_monthly_budget_allows_when_projection_within_cap(tmp_path):
    spec = flat_rate_spec()
    ledger = tmp_path / "costs.jsonl"
    other_day = a_day_in_current_month_other_than_today()
    write_ledger_lines(ledger, [ledger_record(200.0, when=other_day)])

    adapter = FakeAdapter(spec, input_tokens=3_000_000)
    cfg = GovernorConfig(
        max_call_usd=100.0, daily_budget_usd=1000.0, monthly_budget_usd=300.0,
        log_path=str(ledger),
    )

    report = preflight(adapter, _payload(3_000_000), config=cfg)
    assert report["month_spend_before_call"] == pytest.approx(200.0)
    assert report["projected_month_spend_usd"] == pytest.approx(206.0)


def test_per_call_cap_still_enforced_independently_of_period_budgets(tmp_path):
    """The per-call worst-case stop must still fire on its own, even with an
    empty ledger and generous daily/monthly budgets.
    """
    spec = flat_rate_spec()
    ledger = tmp_path / "costs.jsonl"  # no prior spend logged at all

    adapter = FakeAdapter(spec, input_tokens=3_000_000)
    cfg = GovernorConfig(
        max_call_usd=5.0, daily_budget_usd=1000.0, monthly_budget_usd=1000.0,
        log_path=str(ledger),
    )

    with pytest.raises(GovernorError, match=r"Per-call budget stop"):
        preflight(adapter, _payload(3_000_000), config=cfg)  # worst case == $6.00
