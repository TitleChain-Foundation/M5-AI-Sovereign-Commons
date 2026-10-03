import copy
import importlib.util
import json
import socket
from pathlib import Path

import pytest
from jsonschema import Draft202012Validator


ROOT = Path(__file__).resolve().parents[1]
DEMO = ROOT / "pilots" / "dagny-bank-of-me"
FIXTURE = json.loads((DEMO / "examples" / "dagny-mixed-value-exchange.json").read_text())
FIXTURE_SCHEMA = json.loads((DEMO / "schemas" / "m5-vx-demo.schema.json").read_text())
RECEIPT_SCHEMA = json.loads(
    (DEMO / "schemas" / "m5-value-receipt-bundle.schema.json").read_text()
)
COMMITTED_RECEIPT = json.loads(
    (DEMO / "receipts" / "dagny-mixed-value-exchange.receipt.json").read_text()
)


def load_module():
    path = DEMO / "simulate_m5_vx.py"
    spec = importlib.util.spec_from_file_location("simulate_m5_vx", path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


MODULE = load_module()


def test_fixture_and_generated_receipts_validate():
    Draft202012Validator.check_schema(FIXTURE_SCHEMA)
    Draft202012Validator(FIXTURE_SCHEMA).validate(FIXTURE)
    bundle = MODULE.simulate(FIXTURE)
    Draft202012Validator.check_schema(RECEIPT_SCHEMA)
    Draft202012Validator(RECEIPT_SCHEMA).validate(bundle)
    assert bundle["agreed_total"] == bundle["leg_total"] == {
        "amount": "100.00",
        "currency": "USD",
    }
    assert bundle["consideration_reconciled"] is True
    assert bundle["exchange_resource"] == FIXTURE["resource"]
    assert {receipt["settlement_type"] for receipt in bundle["receipts"]} == {
        "DIGITAL",
        "CASH",
        "ASSET",
        "SERVICE",
    }
    assert bundle == COMMITTED_RECEIPT


def test_simulation_is_write_disabled_and_digital_stops_before_provider():
    bundle = MODULE.simulate(FIXTURE)
    assert bundle["execution_safety"] == {
        "synthetic": True,
        "authority_effect": "NONE",
        "network_write": False,
        "financial_movement": False,
        "real_world_resource_movement": False,
    }
    digital = next(
        receipt for receipt in bundle["receipts"] if receipt["settlement_type"] == "DIGITAL"
    )
    assert digital["simulation_outcome"] == "402_HOLD_BEFORE_PROVIDER"
    assert digital["digital_settlement_terms"] == {
        "settlement_asset": "M5USD_SIM",
        "fx_quote": FIXTURE["legs"][0]["digital_terms"]["fx_quote"],
        "fee_allocations_bps": FIXTURE["legs"][0]["digital_terms"][
            "fee_allocations_bps"
        ],
        "total_fee_bps": 1200,
        "gross_amount": {"amount": "40.00", "currency": "USD"},
        "fee_amount": {"amount": "4.80", "currency": "USD"},
        "net_amount": {"amount": "35.20", "currency": "USD"},
    }
    assert all(receipt["state"] == "PROPOSED" for receipt in bundle["receipts"])


def test_cash_is_evidence_only_and_scanner_remains_unselected():
    cash = next(leg for leg in FIXTURE["legs"] if leg["settlement_type"] == "CASH")
    receipt = next(
        receipt
        for receipt in MODULE.simulate(FIXTURE)["receipts"]
        if receipt["settlement_type"] == "CASH"
    )
    assert cash["evidence"]["capture_method"] == "CAMERA_OCR"
    assert cash["evidence"]["scanner_tool"] is None
    assert cash["evidence"]["serial_capture"] is False
    assert cash["evidence"]["image_capture"] == "OPTIONAL_PRIVATE"
    assert receipt["titlechain_reference"] is None
    assert cash["evidence"]["private_refs"][0] not in json.dumps(receipt)
    assert receipt["evidence_refs"] == [
        MODULE.canonical_digest(cash["evidence"]["private_refs"][0])
    ]


def test_party_values_are_not_platform_appraisals():
    receipts = MODULE.simulate(FIXTURE)["receipts"]
    for settlement_type in ("ASSET", "SERVICE"):
        leg = next(
            leg for leg in FIXTURE["legs"] if leg["settlement_type"] == settlement_type
        )
        receipt = next(
            receipt
            for receipt in receipts
            if receipt["settlement_type"] == settlement_type
        )
        assert leg["policy_context"] == "policy:M5-VX-PARTY-AGREED-VALUE-DRAFT"
        assert receipt["policy_context"] == leg["policy_context"]
    serialized = json.dumps(receipts).lower()
    assert "appraisal" not in serialized
    assert "appraised" not in serialized


def test_consideration_direction_is_buyer_to_seller():
    receipts = MODULE.simulate(FIXTURE)["receipts"]
    assert all(
        receipt["provider_tcid"] == "tcid:synthetic:demo-buyer"
        and receipt["receiver_tcid"] == "tcid:synthetic:dagny-seller"
        for receipt in receipts
    )
    assert all(
        receipt["exchange_resource_reference"]
        == FIXTURE["resource"]["resource_reference"]
        for receipt in receipts
    )


def test_simulation_does_not_open_network_socket(monkeypatch):
    def fail_network(*_args, **_kwargs):
        raise AssertionError("simulation attempted a network call")

    monkeypatch.setattr(socket, "socket", fail_network)
    monkeypatch.setattr(socket, "create_connection", fail_network)
    MODULE.simulate(FIXTURE)


def test_fee_rounding_preserves_gross_value():
    fixture = copy.deepcopy(FIXTURE)
    digital = next(
        leg for leg in fixture["legs"] if leg["settlement_type"] == "DIGITAL"
    )
    digital["agreed_value"]["amount"] = "40.05"
    digital["digital_terms"]["fee_allocations_bps"] = [
        {"allocation": "synthetic_half", "bps": 5000}
    ]
    fixture["agreed_total"]["amount"] = "100.05"
    receipt = next(
        receipt
        for receipt in MODULE.simulate(fixture)["receipts"]
        if receipt["settlement_type"] == "DIGITAL"
    )
    terms = receipt["digital_settlement_terms"]
    assert terms["fee_amount"]["amount"] == "20.03"
    assert terms["net_amount"]["amount"] == "20.02"


def test_unbalanced_or_duplicate_legs_fail_closed():
    unbalanced = copy.deepcopy(FIXTURE)
    unbalanced["legs"][0]["agreed_value"]["amount"] = "39.00"
    with pytest.raises(ValueError, match="does not equal"):
        MODULE.simulate(unbalanced)

    duplicate = copy.deepcopy(FIXTURE)
    duplicate["legs"][1]["leg_id"] = duplicate["legs"][0]["leg_id"]
    with pytest.raises(ValueError, match="identifiers must be unique"):
        MODULE.simulate(duplicate)

    excessive_fees = copy.deepcopy(FIXTURE)
    excessive_fees["legs"][0]["digital_terms"]["fee_allocations_bps"].append(
        {"allocation": "invalid_extra_fee", "bps": 9000}
    )
    with pytest.raises(ValueError, match="exceed 10000 bps"):
        MODULE.simulate(excessive_fees)

    unrelated_party = copy.deepcopy(FIXTURE)
    unrelated_party["legs"][1]["to_tcid"] = "tcid:synthetic:unrelated"
    with pytest.raises(ValueError, match="must match the exchange parties"):
        MODULE.simulate(unrelated_party)


def test_cash_cannot_gain_digital_provider_terms():
    invalid = copy.deepcopy(FIXTURE)
    cash = next(leg for leg in invalid["legs"] if leg["settlement_type"] == "CASH")
    digital = next(
        leg for leg in invalid["legs"] if leg["settlement_type"] == "DIGITAL"
    )
    cash["digital_terms"] = digital["digital_terms"]
    assert not Draft202012Validator(FIXTURE_SCHEMA).is_valid(invalid)


def test_receipt_schema_rejects_invalid_cash_and_digital_outcomes():
    bundle = MODULE.simulate(FIXTURE)
    invalid_cash = copy.deepcopy(bundle)
    cash = next(
        receipt
        for receipt in invalid_cash["receipts"]
        if receipt["settlement_type"] == "CASH"
    )
    cash["titlechain_reference"] = "titlechain:invalid:cash"
    assert not Draft202012Validator(RECEIPT_SCHEMA).is_valid(invalid_cash)

    invalid_digital = copy.deepcopy(bundle)
    digital = next(
        receipt
        for receipt in invalid_digital["receipts"]
        if receipt["settlement_type"] == "DIGITAL"
    )
    digital["simulation_outcome"] = "SIMULATED_ACKNOWLEDGEMENT_ONLY"
    assert not Draft202012Validator(RECEIPT_SCHEMA).is_valid(invalid_digital)

    raw_private_ref = copy.deepcopy(bundle)
    raw_private_ref["receipts"][0]["evidence_refs"] = ["m5pod:private:locator"]
    assert not Draft202012Validator(RECEIPT_SCHEMA).is_valid(raw_private_ref)


def test_bundle_verifier_rejects_tampering():
    tampered = copy.deepcopy(MODULE.simulate(FIXTURE))
    tampered["receipts"][0]["agreed_value"] = "39.00"
    with pytest.raises(ValueError, match="does not reconcile"):
        MODULE.verify_bundle(tampered)
