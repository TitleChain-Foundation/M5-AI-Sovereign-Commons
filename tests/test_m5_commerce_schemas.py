import json
from pathlib import Path

import jsonschema

ROOT = Path(__file__).resolve().parents[1]

PAIRS = [
    ("m5-intelligence-request.schema.json", "m5-intelligence-request-laya-local.example.json"),
    ("m5-intelligence-routing-receipt.schema.json", "m5-intelligence-routing-receipt-laya.example.json"),
    ("m5-transaction-footprint.schema.json", "m5-transaction-footprint-property.example.json"),
    ("m5-commerce-receipt.schema.json", "m5-commerce-receipt-laya-local.example.json"),
]


def test_new_examples_validate():
    for schema_name, example_name in PAIRS:
        schema = json.loads((ROOT / "schemas" / schema_name).read_text())
        example = json.loads((ROOT / "examples" / example_name).read_text())
        jsonschema.Draft202012Validator.check_schema(schema)
        jsonschema.validate(instance=example, schema=schema)


def test_local_laya_example_is_non_billable():
    receipt = json.loads((ROOT / "examples" / "m5-commerce-receipt-laya-local.example.json").read_text())
    assert receipt["runtime"] == "LAYA_LOCAL"
    assert receipt["entitlement_type"] == "LOCAL_SOVEREIGN"
    assert receipt["billable"] is False
    assert receipt["payment"] is None
    assert receipt["price_quote"]["quoted_total"] == "0.00"


def test_m4_instrument_preserves_underlying_m3_reference():
    footprint = json.loads((ROOT / "examples" / "m5-transaction-footprint-property.example.json").read_text())
    instrument = footprint["instrument"]
    assert instrument["m5_class"] == "M4"
    assert instrument["underlying_links"]
    for link in instrument["underlying_links"]:
        assert link["asset_ref"]
        assert link["titleholder_ref"]
        assert link["authority_evidence_ref"]


def test_m1_fee_does_not_mutate_m3_asset_class():
    footprint = json.loads((ROOT / "examples" / "m5-transaction-footprint-property.example.json").read_text())
    assert footprint["m5_asset_class"] == "M3"
    assert all(fee["m5_class"] == "M1" for fee in footprint["fee_events"])
