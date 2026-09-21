import copy
import hashlib
import importlib.util
import json
from pathlib import Path

import pytest
from jsonschema import Draft202012Validator


ROOT = Path(__file__).resolve().parents[1]
SIMULATION = ROOT / "pilots" / "312-spring-commons" / "simulations" / "first-tranche"
X402 = SIMULATION / "m5-x402"
NUMSCRIPT = SIMULATION / "numscript"
SCHEMA = json.loads((X402 / "m5-x402-extension.schema.json").read_text())
PAYMENT_REQUIRED = json.loads((X402 / "payment-required.example.json").read_text())
PAYMENT_PAYLOAD = json.loads((X402 / "payment-payload.example.json").read_text())
PROJECT = ROOT / "pilots" / "312-spring-commons"
TRANCHE_SCHEMA = json.loads((PROJECT / "schemas" / "m5-first-tranche-simulation.schema.json").read_text())
TRANCHE_FIXTURE = json.loads((PROJECT / "examples" / "PPT-EZ-CA-0001-first-tranche-simulation.json").read_text())
TRANCHE_RECEIPT = json.loads((SIMULATION / "receipts" / "PPT-EZ-CA-0001-first-tranche-receipt.json").read_text())


def m5_extension(document):
    return document["extensions"]["m5-ricardian"]


def digest(path):
    return "sha256:" + hashlib.sha256(path.read_bytes()).hexdigest()


def test_m5_x402_extension_schema_and_examples_validate():
    Draft202012Validator.check_schema(SCHEMA)
    validator = Draft202012Validator(SCHEMA)
    validator.validate(m5_extension(PAYMENT_REQUIRED))
    validator.validate(m5_extension(PAYMENT_PAYLOAD))


def test_x402_core_terms_and_m5_request_fingerprint_are_bound():
    requirement = PAYMENT_REQUIRED["accepts"][0]
    accepted = PAYMENT_PAYLOAD["accepted"]
    required_fingerprint = m5_extension(PAYMENT_REQUIRED)["info"]["request_fingerprint"]
    payload_fingerprint = m5_extension(PAYMENT_PAYLOAD)["info"]["request_fingerprint"]

    for key in ("scheme", "network", "amount", "asset", "payTo", "maxTimeoutSeconds"):
        assert accepted[key] == requirement[key]
    assert payload_fingerprint == required_fingerprint
    assert required_fingerprint["scheme"] == requirement["scheme"]
    assert required_fingerprint["network"] == requirement["network"]
    assert required_fingerprint["amount"] == requirement["amount"]
    assert required_fingerprint["asset"] == requirement["asset"]
    assert required_fingerprint["pay_to"] == requirement["payTo"]


def test_executable_binding_matches_numscript_digest():
    executable = m5_extension(PAYMENT_REQUIRED)["info"]["executable_plan"]
    assert executable["language"] == "Numscript"
    assert executable["digest"] == digest(NUMSCRIPT / "reserve-tranche.num")


def test_human_and_machine_bindings_match_repository_artifacts():
    info = m5_extension(PAYMENT_REQUIRED)["info"]
    project = ROOT / "pilots" / "312-spring-commons"
    assert info["contract"]["digest"] == digest(
        project / "documents" / "public" / "DOC-02-Conditional-Capital-Commitment-Letter.pdf"
    )
    assert info["human_terms"]["digest"] == digest(
        project / "documents" / "public" / "DOC-01-Master-Deal-Term-Sheet.pdf"
    )
    assert info["machine_policy"]["digest"] == digest(
        project / "schemas" / "m5-first-tranche-simulation.schema.json"
    )


def test_no_value_marker_is_not_the_payment_asset():
    info = m5_extension(PAYMENT_REQUIRED)["info"]
    marker = info["token_representation"]
    requirement = PAYMENT_REQUIRED["accepts"][0]

    assert marker["valuation_status"] == "NO_ASSIGNED_MONETARY_VALUE"
    assert marker["settlement_eligibility"] == "NOT_A_SETTLEMENT_ASSET"
    assert marker["fee_title_effect"] == "NONE"
    assert marker["asset_code"] != requirement["asset"]

    invalid = copy.deepcopy(m5_extension(PAYMENT_REQUIRED))
    invalid["info"]["request_fingerprint"]["asset"] = "M5MARKER"
    assert not Draft202012Validator(SCHEMA).is_valid(invalid)


def test_public_payload_cannot_be_settled_or_claim_authority():
    payload = PAYMENT_PAYLOAD["payload"]
    safety = m5_extension(PAYMENT_PAYLOAD)["info"]["execution_safety"]
    authority = m5_extension(PAYMENT_PAYLOAD)["info"]["authority"]

    assert payload["simulationOnly"] is True
    assert payload["signature"] is None
    assert payload["authorization"] is None
    assert payload["settleable"] is False
    assert safety == {
        "synthetic": True,
        "authority_effect": "NONE",
        "network_write": False,
        "financial_movement": False,
        "settlement_status": "NOT_SUBMITTED",
    }
    assert authority["credential_state"] == "PENDING_EXTERNAL"
    assert authority["approval_state"] == "PENDING_EXTERNAL"


def test_numscript_keeps_money_and_marker_assets_separate():
    reserve = (NUMSCRIPT / "reserve-tranche.num").read_text()
    draw = (NUMSCRIPT / "release-draw.num").read_text()
    marker = (NUMSCRIPT / "register-marker.num").read_text()

    assert "M5MARKER" not in reserve
    assert "M5MARKER" not in draw
    assert "send [M5MARKER 1]" in marker
    assert '"NO_ASSIGNED_MONETARY_VALUE"' in marker
    assert '"NOT_A_SETTLEMENT_ASSET"' in marker
    assert "source = @world" not in reserve
    assert "source = @world" not in draw


def test_tranche_fixture_validates_and_receipt_is_reproducible():
    Draft202012Validator.check_schema(TRANCHE_SCHEMA)
    Draft202012Validator(TRANCHE_SCHEMA).validate(TRANCHE_FIXTURE)

    module_path = SIMULATION / "simulate_first_tranche.py"
    spec = importlib.util.spec_from_file_location("simulate_first_tranche", module_path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)

    assert module.evaluate(TRANCHE_FIXTURE) == TRANCHE_RECEIPT
    assert TRANCHE_RECEIPT["decision"] == "HOLD"
    assert TRANCHE_RECEIPT["execution_authorized"] is False
    assert TRANCHE_RECEIPT["financial_movement_performed"] is False


def test_m5_x402_exchange_holds_before_provider_calls():
    module_path = X402 / "simulate_m5_x402.py"
    spec = importlib.util.spec_from_file_location("simulate_m5_x402", module_path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)

    result = module.simulate(PAYMENT_REQUIRED, PAYMENT_PAYLOAD, SCHEMA)
    assert result["http_status"] == 402
    assert result["decision"] == "HOLD"
    assert result["verify_called"] is False
    assert result["settle_called"] is False
    assert result["network_write_performed"] is False
    assert result["financial_movement_performed"] is False
    assert result["token_valuation_status"] == "NO_ASSIGNED_MONETARY_VALUE"


def test_m5_x402_rejects_tampered_client_echo():
    tampered = copy.deepcopy(PAYMENT_PAYLOAD)
    tampered["extensions"]["m5-ricardian"]["info"]["request_fingerprint"]["amount"] = "1"

    module_path = X402 / "simulate_m5_x402.py"
    spec = importlib.util.spec_from_file_location("simulate_m5_x402_tamper", module_path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)

    with pytest.raises(ValueError, match="echo mismatch"):
        module.simulate(PAYMENT_REQUIRED, tampered, SCHEMA)
