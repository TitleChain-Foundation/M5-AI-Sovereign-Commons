"""Regression tests: a malformed, incomplete, or unreadable cost ledger must
fail closed by raising a precise `GovernorError`, rather than silently
skipping the offending record.

Silently skipping a corrupt/incomplete ledger line would undercount prior
spend for the day/month and could let `preflight()` admit a call that the
daily/monthly budget stop should have blocked. Failing closed denies the
call instead of guessing.

This also covers `total_usd` values that could *poison* or *reduce* the
accumulated total (negative, NaN, +/-Infinity) and timestamp values that are
ambiguous (timezone-naive) or that must be normalized to UTC before being
bucketed into a day/month, rather than trusted at face value.
"""
from __future__ import annotations

import json
from datetime import datetime, timedelta, timezone

import pytest

from m5_governor import GovernorConfig, GovernorError, _period_spend, preflight

from _helpers import FakeAdapter, flat_rate_spec, ledger_record, write_ledger_lines


def test_missing_ledger_file_is_zero_spend_not_an_error(tmp_path):
    path = tmp_path / "absent.jsonl"
    assert _period_spend(path, "day") == 0.0
    assert _period_spend(path, "month") == 0.0


def test_blank_lines_are_tolerated(tmp_path):
    path = tmp_path / "costs.jsonl"
    write_ledger_lines(path, ["", ledger_record(1.5), "   ", ledger_record(2.5)])
    assert _period_spend(path, "day") == pytest.approx(4.0)


def test_malformed_json_line_fails_closed(tmp_path):
    path = tmp_path / "costs.jsonl"
    write_ledger_lines(path, [ledger_record(1.0), "{not valid json"])
    with pytest.raises(GovernorError, match=r"malformed at line 2"):
        _period_spend(path, "day")


def test_non_object_record_fails_closed(tmp_path):
    path = tmp_path / "costs.jsonl"
    write_ledger_lines(path, ["[1, 2, 3]"])
    with pytest.raises(GovernorError, match=r"JSON object"):
        _period_spend(path, "day")


def test_record_missing_required_field_fails_closed(tmp_path):
    path = tmp_path / "costs.jsonl"
    incomplete = json.dumps({"timestamp": "2026-09-07T00:00:00Z"})  # no total_usd
    write_ledger_lines(path, [incomplete])
    with pytest.raises(GovernorError, match=r"incomplete.*total_usd"):
        _period_spend(path, "day")


def test_non_numeric_total_usd_fails_closed(tmp_path):
    path = tmp_path / "costs.jsonl"
    bad = json.dumps({"timestamp": "2026-09-07T00:00:00Z", "total_usd": "oops"})
    write_ledger_lines(path, [bad])
    with pytest.raises(GovernorError, match=r"non-numeric"):
        _period_spend(path, "day")


def test_unparseable_timestamp_fails_closed(tmp_path):
    path = tmp_path / "costs.jsonl"
    bad = json.dumps({"timestamp": "not-a-timestamp", "total_usd": 1.0})
    write_ledger_lines(path, [bad])
    with pytest.raises(GovernorError, match=r"unparseable"):
        _period_spend(path, "day")


def test_unreadable_ledger_path_fails_closed(tmp_path):
    # A directory at the configured ledger path cannot be read as a file.
    path = tmp_path / "costs.jsonl"
    path.mkdir()
    with pytest.raises(GovernorError, match=r"could not be read"):
        _period_spend(path, "day")


# -- total_usd values that could reduce or poison the accumulated total ----

def test_negative_total_usd_fails_closed(tmp_path):
    path = tmp_path / "costs.jsonl"
    bad = json.dumps({"timestamp": "2026-09-07T00:00:00Z", "total_usd": -5.0})
    write_ledger_lines(path, [bad])
    with pytest.raises(GovernorError, match=r"negative"):
        _period_spend(path, "day")


def test_nan_total_usd_fails_closed(tmp_path):
    path = tmp_path / "costs.jsonl"
    # Python's json module parses the bare (non-standard but permitted)
    # NaN/Infinity/-Infinity tokens as float('nan')/float('inf')/float('-inf'),
    # and float()/int() coercion alone would happily accept them, so this must
    # be checked explicitly rather than relying on the earlier type coercion.
    line = '{"timestamp": "2026-09-07T00:00:00Z", "total_usd": NaN}'
    write_ledger_lines(path, [line])
    with pytest.raises(GovernorError, match=r"non-finite"):
        _period_spend(path, "day")


def test_positive_infinity_total_usd_fails_closed(tmp_path):
    path = tmp_path / "costs.jsonl"
    line = '{"timestamp": "2026-09-07T00:00:00Z", "total_usd": Infinity}'
    write_ledger_lines(path, [line])
    with pytest.raises(GovernorError, match=r"non-finite"):
        _period_spend(path, "day")


def test_negative_infinity_total_usd_fails_closed(tmp_path):
    path = tmp_path / "costs.jsonl"
    line = '{"timestamp": "2026-09-07T00:00:00Z", "total_usd": -Infinity}'
    write_ledger_lines(path, [line])
    with pytest.raises(GovernorError, match=r"non-finite"):
        _period_spend(path, "day")


def test_valid_positive_total_usd_still_accumulates(tmp_path):
    # Sanity check alongside the rejection tests above: legitimate positive
    # amounts on today's date must still sum normally.
    path = tmp_path / "costs.jsonl"
    write_ledger_lines(path, [ledger_record(3.0), ledger_record(4.5)])
    assert _period_spend(path, "day") == pytest.approx(7.5)


# -- ambiguous / non-UTC timestamps -----------------------------------------

def test_timezone_naive_timestamp_fails_closed(tmp_path):
    path = tmp_path / "costs.jsonl"
    naive = json.dumps({"timestamp": "2026-09-07T12:00:00", "total_usd": 1.0})
    write_ledger_lines(path, [naive])
    with pytest.raises(GovernorError, match=r"timezone-naive"):
        _period_spend(path, "day")


def test_non_utc_offset_timestamp_is_normalized_to_utc_before_bucketing(tmp_path):
    """A timezone-aware timestamp with a non-UTC offset must be bucketed by
    its UTC calendar day, not by whatever raw calendar date happens to appear
    in the string. Use an offset large enough (within the real-world +14:00 /
    -12:00 range) that the local calendar date is guaranteed to differ from
    the UTC calendar date, regardless of what time the test happens to run.
    """
    now = datetime.now(timezone.utc)
    # Shifting the clock backward (-12) crosses to the previous calendar date
    # when the UTC hour is in the first half of the day; shifting forward
    # (+14) crosses to the next calendar date when it's in the second half.
    offset_hours = -12 if now.hour < 12 else 14
    shifted = now.astimezone(timezone(timedelta(hours=offset_hours)))
    assert shifted.date() != now.date()  # sanity: the raw date really differs

    path = tmp_path / "costs.jsonl"
    write_ledger_lines(path, [ledger_record(9.0, when=shifted)])

    # Same instant as `now`, so it must count as spent today in UTC despite
    # the differing raw offset date.
    assert _period_spend(path, "day") == pytest.approx(9.0)


def test_corrupt_ledger_fails_closed_through_public_preflight_entry_point(tmp_path):
    path = tmp_path / "costs.jsonl"
    write_ledger_lines(path, ["{not valid json"])

    spec = flat_rate_spec()
    adapter = FakeAdapter(spec, input_tokens=1_000)
    cfg = GovernorConfig(
        max_call_usd=100.0, daily_budget_usd=25.0, monthly_budget_usd=300.0,
        log_path=str(path),
    )
    payload = {"model": "flat-rate", "max_output_tokens": 1_000}

    with pytest.raises(GovernorError, match=r"malformed"):
        preflight(adapter, payload, config=cfg)


def test_incomplete_ledger_fails_closed_through_public_preflight_entry_point(tmp_path):
    path = tmp_path / "costs.jsonl"
    write_ledger_lines(path, [json.dumps({"total_usd": 1.0})])  # no timestamp

    spec = flat_rate_spec()
    adapter = FakeAdapter(spec, input_tokens=1_000)
    cfg = GovernorConfig(
        max_call_usd=100.0, daily_budget_usd=25.0, monthly_budget_usd=300.0,
        log_path=str(path),
    )
    payload = {"model": "flat-rate", "max_output_tokens": 1_000}

    with pytest.raises(GovernorError, match=r"incomplete.*timestamp"):
        preflight(adapter, payload, config=cfg)
