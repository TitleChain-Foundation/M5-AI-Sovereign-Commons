import copy
import importlib.util
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

import pytest
from jsonschema import Draft202012Validator, FormatChecker


ROOT = Path(__file__).resolve().parents[1]
SIMULATION = ROOT / "pilots" / "312-spring-commons" / "simulations" / "first-tranche"
X402 = SIMULATION / "m5-x402"
NUMSCRIPT = SIMULATION / "numscript"
SCHEMA = json.loads((X402 / "m5-x402-extension.schema.json").read_text())
PAYMENT_REQUIRED = json.loads((X402 / "payment-required.example.json").read_text())
PAYMENT_PAYLOAD = json.loads((X402 / "payment-payload.example.json").read_text())
PROJECT = ROOT / "pilots" / "312-spring-commons"
TRANCHE_SCHEMA = json.loads((PROJECT / "schemas" / "m5-first-tranche-simulation.schema.json").read_text())
RECEIPT_SCHEMA = json.loads((PROJECT / "schemas" / "m5-first-tranche-receipt.schema.json").read_text())
DECISION_CONTEXT_SCHEMA = json.loads((PROJECT / "schemas" / "m5canon-decision-context.schema.json").read_text())
MANIFEST_SCHEMA = json.loads((PROJECT / "schemas" / "spring-commons-human-terms-manifest.schema.json").read_text())
PROVENANCE_SCHEMA = json.loads((PROJECT / "schemas" / "m5-jurisdictional-capital-provenance.schema.json").read_text())
TRANCHE_FIXTURE = json.loads((PROJECT / "examples" / "PPT-EZ-CA-0001-first-tranche-simulation.json").read_text())
DECISION_CONTEXT = json.loads((PROJECT / "examples" / "PPT-EZ-CA-0001-m5canon-decision-context.json").read_text())
TRANCHE_RECEIPT = json.loads((SIMULATION / "receipts" / "PPT-EZ-CA-0001-first-tranche-receipt.json").read_text())
MANIFEST = json.loads((SIMULATION / "manifests" / "SPRING-COMMONS-DOC-SET-01-23.v0.6-draft.json").read_text())
PROVENANCE = json.loads((PROJECT / "examples" / "PPT-EZ-CA-0001-jurisdictional-capital-provenance-example.json").read_text())
sys.path.insert(0, str(SIMULATION))

from canonical import (  # noqa: E402
    canonical_digest,
    draft_asset_policy_blockers,
    file_digest,
    jurisdiction_graph_errors,
)


def m5_extension(document):
    return document["extensions"]["m5-ricardian"]


def load_module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


TRANCHE_MODULE = load_module("simulate_first_tranche", SIMULATION / "simulate_first_tranche.py")
X402_MODULE = load_module("simulate_m5_x402", X402 / "simulate_m5_x402.py")


def simulate_x402(required=PAYMENT_REQUIRED, payload=PAYMENT_PAYLOAD, **overrides):
    fingerprint = m5_extension(required)["info"]["request_fingerprint"]
    arguments = {
        "request_method": "POST",
        "request_resource": required["resource"]["url"],
        "observed_at": fingerprint["issued_at"],
        "clock_source": "FIXTURE_SIMULATION_TIME_UNTRUSTED",
    }
    arguments.update(overrides)
    return X402_MODULE.simulate(required, payload, SCHEMA, **arguments)


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
    assert required_fingerprint["max_timeout_seconds"] == requirement["maxTimeoutSeconds"]
    assert required_fingerprint["http_method"] == "POST"
    assert required_fingerprint["resource"] == PAYMENT_REQUIRED["resource"]["url"]
    assert required_fingerprint["issued_at"] < required_fingerprint["expires_at"]


def test_executable_binding_matches_numscript_digest():
    executable = m5_extension(PAYMENT_REQUIRED)["info"]["executable_plan"]
    assert executable["language"] == "Numscript"
    assert executable["digest"] == file_digest((X402 / executable["uri"]).resolve())


def test_human_and_machine_bindings_match_repository_artifacts():
    info = m5_extension(PAYMENT_REQUIRED)["info"]
    bindings = [info[name] for name in ("contract", "human_terms", "machine_policy", "executable_plan")]
    assert {binding["contract_id"] for binding in bindings} == {
        "PPT-EZ-CA-0001-ILLUSTRATIVE-PRIVATE-TRANCHE-01"
    }
    for binding in bindings:
        path = (X402 / binding["uri"]).resolve()
        assert path.is_file()
        assert binding["digest"] == file_digest(path)
        assert binding["supersession_history"] == {
            "supersedes": [],
            "superseded_by": None,
        }


def test_human_terms_manifest_identifies_and_hashes_all_23_documents():
    binding = m5_extension(PAYMENT_REQUIRED)["info"]["human_terms"]
    manifest_path = (X402 / binding["uri"]).resolve()
    assert binding["digest"] == file_digest(manifest_path)
    assert MANIFEST["artifact_id"] == binding["id"]
    assert MANIFEST["artifact_version"] == binding["version"]
    assert MANIFEST["contract_id"] == binding["contract_id"]
    assert MANIFEST["supersession_history"] == binding["supersession_history"]
    Draft202012Validator.check_schema(MANIFEST_SCHEMA)
    Draft202012Validator(MANIFEST_SCHEMA).validate(MANIFEST)
    assert [item["id"] for item in MANIFEST["documents"]] == [
        f"DOC-{number:02d}" for number in range(1, 24)
    ]
    for document in MANIFEST["documents"]:
        path = (manifest_path.parent / document["uri"]).resolve()
        assert path.is_file()
        assert document["digest"] == file_digest(path)


def test_human_terms_manifest_rejects_duplicate_or_escaping_members():
    duplicate = copy.deepcopy(MANIFEST)
    duplicate["documents"][1]["id"] = "DOC-01"
    assert [item["id"] for item in duplicate["documents"]] != [f"DOC-{number:02d}" for number in range(1, 24)]
    escaping = copy.deepcopy(MANIFEST)
    escaping["documents"][0]["uri"] = "../../../../outside.pdf"
    assert not Draft202012Validator(MANIFEST_SCHEMA).is_valid(escaping)


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


def test_numscript_programs_are_checked_and_executed():
    executable = shutil.which("numscript")
    if executable is None:
        if os.environ.get("M5_REQUIRE_NUMSCRIPT") == "1":
            pytest.fail("numscript v0.0.25 is required by conformance CI")
        pytest.skip("numscript v0.0.25 is installed by the conformance CI workflow")
    version = subprocess.run([executable, "--version"], check=True, capture_output=True, text=True)
    assert "0.0.25" in version.stdout
    for program in sorted(NUMSCRIPT.glob("*.num")):
        inputs = json.loads(program.with_suffix(".num.inputs.json").read_text())
        assert inputs["variables"]["terms_digest"] == file_digest(
            SIMULATION / "manifests" / "SPRING-COMMONS-DOC-SET-01-23.v0.6-draft.json"
        )
        assert inputs["variables"]["policy_digest"] == file_digest(
            PROJECT / "schemas" / "m5-first-tranche-simulation.schema.json"
        )
        subprocess.run([executable, "check", str(program)], check=True, capture_output=True, text=True)
        subprocess.run(
            [executable, "run", "--inputs", str(program.with_suffix(".num.inputs.json")), str(program)],
            check=True,
            capture_output=True,
            text=True,
        )


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
    Draft202012Validator.check_schema(RECEIPT_SCHEMA)
    Draft202012Validator(RECEIPT_SCHEMA, format_checker=FormatChecker()).validate(TRANCHE_RECEIPT)

    assert TRANCHE_MODULE.evaluate(TRANCHE_FIXTURE) == TRANCHE_RECEIPT
    assert TRANCHE_RECEIPT["decision"] == "HOLD"
    assert TRANCHE_RECEIPT["execution_authorized"] is False
    assert TRANCHE_RECEIPT["financial_movement_performed"] is False
    assert TRANCHE_RECEIPT["ordering"] == {
        "timestamp": "2026-09-20T00:00:00Z",
        "sequence": 0,
        "anchor": "GENESIS",
        "previous_receipt_digest": None,
    }
    assert {item["function_id"] for item in TRANCHE_RECEIPT["m5canon"]["functions"]} == {
        "M5CANON.PRINCIPAL.RESOLVE.v1",
        "M5CANON.CREDENTIAL.VERIFY.v1",
        "M5CANON.DELEGATION.VERIFY.v1",
        "M5CANON.JURISDICTION.RESOLVE.v1",
        "M5CANON.POLICY.EVALUATE.v1",
        "M5CANON.APPROVAL.VERIFY.v1",
        "M5CANON.ACTION.AUTHORIZE.v1",
        "M5CANON.RECEIPT.COMMIT.v1",
    }


def test_decision_context_and_provenance_bindings_validate():
    Draft202012Validator.check_schema(DECISION_CONTEXT_SCHEMA)
    Draft202012Validator(DECISION_CONTEXT_SCHEMA, format_checker=FormatChecker()).validate(DECISION_CONTEXT)
    binding = TRANCHE_FIXTURE["decision_context"]
    path = (PROJECT / "examples" / binding["uri"]).resolve()
    assert binding["digest"] == file_digest(path)
    taxonomy = DECISION_CONTEXT["taxonomy"]
    taxonomy_path = (path.parent / taxonomy["uri"]).resolve()
    assert taxonomy["digest"] == file_digest(taxonomy_path)
    assert DECISION_CONTEXT["authority_effect"] == "NONE"
    Draft202012Validator.check_schema(PROVENANCE_SCHEMA)
    Draft202012Validator(PROVENANCE_SCHEMA, format_checker=FormatChecker()).validate(PROVENANCE)
    assert PROVENANCE["event_state"] == "REVIEW_REQUIRED"
    assert PROVENANCE["source_chain_activation"]["activated"] is False
    assert PROVENANCE["source_chain_activation"]["unresolved_preconditions"]


@pytest.mark.parametrize(
    "record",
    [[], {"tranche": "bad"}, None, "bad", {"simulation_id": None}, {"project_id": 7}, {"receipt_context": {"timestamp": "not-a-date"}}],
)
def test_tranche_evaluator_never_throws_for_malformed_json_shapes(record):
    receipt = TRANCHE_MODULE.evaluate(record)
    Draft202012Validator(RECEIPT_SCHEMA, format_checker=FormatChecker()).validate(receipt)
    assert receipt["decision"] == "HOLD"
    assert receipt["observations"]["validation_status"] == "INVALID_UNRESOLVED"


def test_receipt_schema_binds_each_function_id_to_its_exact_uri():
    tampered = copy.deepcopy(TRANCHE_RECEIPT)
    tampered["m5canon"]["functions"][0]["function_uri"] = "urn:m5:function:m5canon:receipt:commit:v1"
    assert not Draft202012Validator(RECEIPT_SCHEMA).is_valid(tampered)


def test_receipt_access_defaults_to_deny_and_requires_credentials_and_log():
    with pytest.raises(PermissionError, match="denied"):
        TRANCHE_MODULE.render_receipt_view(
            TRANCHE_RECEIPT,
            DECISION_CONTEXT,
            grantee_ref="UNKNOWN",
            credential_refs=set(),
            jurisdiction_refs=set(),
            access_purpose="AUTHORIZED_EXAMINATION",
            access_log_ref="ACCESS-LOG-001",
            observed_at="2026-09-20T00:00:00Z",
        )
    with pytest.raises(PermissionError, match="credential"):
        TRANCHE_MODULE.render_receipt_view(
            TRANCHE_RECEIPT,
            DECISION_CONTEXT,
            grantee_ref="AUTHORIZED-REGULATOR-ROLE-TBD",
            credential_refs=set(),
            jurisdiction_refs={"JNR:US"},
            access_purpose="AUTHORIZED_EXAMINATION",
            access_log_ref="ACCESS-LOG-001",
            observed_at="2026-09-20T00:00:00Z",
        )
    view = TRANCHE_MODULE.render_receipt_view(
        TRANCHE_RECEIPT,
        DECISION_CONTEXT,
        grantee_ref="AUTHORIZED-REGULATOR-ROLE-TBD",
        credential_refs={"CREDENTIAL-AUTHORIZED-REGULATOR"},
        jurisdiction_refs={"JNR:US"},
        access_purpose="AUTHORIZED_EXAMINATION",
        access_log_ref="ACCESS-LOG-001",
        observed_at="2026-09-20T00:00:00Z",
    )
    assert view["access_log_ref"] == "ACCESS-LOG-001"
    assert set(view["view"]) == set(view["field_scope"])
    assert "receipt_id" not in view["view"]


def test_public_receipt_view_excludes_authority_details():
    view = TRANCHE_MODULE.render_receipt_view(
        TRANCHE_RECEIPT,
        DECISION_CONTEXT,
        grantee_ref="PUBLIC",
        credential_refs=set(),
        jurisdiction_refs=set(),
        access_purpose="PUBLIC_SYNTHETIC_REVIEW",
        access_log_ref="ACCESS-LOG-PUBLIC-001",
        observed_at="2026-09-20T00:00:00Z",
    )
    assert set(view["view"]) == {"decision", "safety", "public_exceptions"}
    assert "actor_authority" not in view["view"]


def test_receipt_access_enforces_jurisdiction_validity_and_revocation():
    arguments = {
        "receipt": TRANCHE_RECEIPT,
        "decision_context": DECISION_CONTEXT,
        "grantee_ref": "AUTHORIZED-REGULATOR-ROLE-TBD",
        "credential_refs": {"CREDENTIAL-AUTHORIZED-REGULATOR"},
        "jurisdiction_refs": set(),
        "access_purpose": "AUTHORIZED_EXAMINATION",
        "access_log_ref": "ACCESS-LOG-001",
        "observed_at": "2026-09-20T00:00:00Z",
    }
    with pytest.raises(PermissionError, match="jurisdiction"):
        TRANCHE_MODULE.render_receipt_view(**arguments)
    arguments["jurisdiction_refs"] = {"JNR:US"}
    arguments["observed_at"] = "2026-09-19T23:59:59Z"
    with pytest.raises(PermissionError, match="not yet effective"):
        TRANCHE_MODULE.render_receipt_view(**arguments)
    revoked = copy.deepcopy(DECISION_CONTEXT)
    revoked["receipt_access_policy"]["grants"][1]["revocation_ref"] = "REVOCATION-001"
    arguments["decision_context"] = revoked
    arguments["observed_at"] = "2026-09-20T00:00:00Z"
    with pytest.raises(PermissionError, match="revoked"):
        TRANCHE_MODULE.render_receipt_view(**arguments)


def test_draft_taxonomy_m1_m3_and_m4_invariants():
    utility = {
        "m5_class": "M1", "classification_state": "CURRENT",
        "source_asset_refs": ["M3-PATENT-001"], "creates_title": False,
        "transfers_source_asset": False, "investment_rights": False,
    }
    assert draft_asset_policy_blockers(utility, "BOB") == []
    utility["investment_rights"] = True
    assert "M4_CLASSIFICATION_REVIEW_REQUIRED" in draft_asset_policy_blockers(utility, "BOB")
    titled = {"m5_class": "M3", "classification_state": "CURRENT", "title_evidence_refs": []}
    assert "M3_TITLE_PROVENANCE_REQUIRED" in draft_asset_policy_blockers(titled, "BOB")
    security = {"m5_class": "M4", "classification_state": "CURRENT"}
    assert "M4_ACCOUNT_NOT_PERMITTED" in draft_asset_policy_blockers(security, "BOM")


def test_draft_taxonomy_m2_routes_and_m5_isolation():
    spot = {"m5_class": "M2", "classification_state": "CURRENT", "activity": "SPOT", "required_route_actions": ["COMMODITY_PROVENANCE_VERIFY"]}
    derivative = {"m5_class": "M2", "classification_state": "CURRENT", "activity": "DERIVATIVE", "required_route_actions": []}
    assert draft_asset_policy_blockers(spot, "BOU") == []
    assert "M2_DERIVATIVE_ROUTE_REQUIRED" in draft_asset_policy_blockers(derivative, "BOI")
    sovereign = {"m5_class": "M5", "classification_state": "CURRENT", "destination_account_domain": "M1", "retail_access": True}
    blockers = draft_asset_policy_blockers(sovereign, "BOG")
    assert "M5_DIRECT_LOWER_CLASS_POSTING_PROHIBITED" in blockers
    assert "M5_RETAIL_ACCESS_PROHIBITED" in blockers


def test_jurisdiction_graph_preserves_native_terms_and_tribal_independence():
    graph = copy.deepcopy(DECISION_CONTEXT["jurisdiction_graph"])
    graph["nodes"].append({"jurisdiction_id": "JNR:US-TRIBAL-EXAMPLE", "canonical_name": "Example Tribal Nation", "native_name": "Example Tribal Nation", "normalized_level": "TRIBAL_INDIGENOUS", "native_level_term": "Tribal Nation"})
    graph["relationships"].append({"from_ref": "JNR:US-TRIBAL-EXAMPLE", "to_ref": "JNR:US-CA", "relationship_type": "GEOGRAPHIC_OVERLAP_OR_COMPACT"})
    assert jurisdiction_graph_errors(graph) == []
    graph["relationships"][-1]["relationship_type"] = "SUBDIVISION_OF"
    assert "Tribal Nation cannot be reduced to a state subdivision" in jurisdiction_graph_errors(graph)


def test_dttc_cannot_be_substituted_for_external_market_infrastructure():
    context = copy.deepcopy(DECISION_CONTEXT)
    requirement = next(item for item in context["institutional_route"]["requirements"] if item["participant_ref"] == "M5-DTTC")
    requirement["institution_identifier"] = "DTC"
    errors, _ = TRANCHE_MODULE._decision_context_errors(context)
    assert any("institution or function semantics mismatch" in error for error in errors)


def test_required_route_identity_cannot_be_replaced_as_a_tuple():
    context = copy.deepcopy(DECISION_CONTEXT)
    requirement = next(item for item in context["institutional_route"]["requirements"] if item["requirement_id"] == "ROUTE-REQ-DTTC")
    requirement.update({
        "participant_ref": "DTC",
        "organization_type": "CLEARING_INFRASTRUCTURE",
        "institution_identifier": "DTC",
        "function": "EXTERNAL_SECURITIES_DEPOSITORY",
        "required_action": "SETTLEMENT",
    })
    errors, _ = TRANCHE_MODULE._decision_context_errors(context)
    assert any("ROUTE-REQ-DTTC institution or function semantics mismatch" in error for error in errors)


def test_current_authority_and_routes_require_resolved_authoritative_evidence():
    context = copy.deepcopy(DECISION_CONTEXT)
    authority = context["account_authority"]
    authority.update({"credential_state": "CURRENT", "delegation_state": "CURRENT", "mandate_state": "CURRENT", "revocation_state": "NOT_REVOKED", "evidence_refs": ["FAKE-EVIDENCE"]})
    context["asset_classification"]["classification_state"] = "CURRENT"
    context["external_legal_classification"].update({"status": "CURRENT", "evidence_refs": ["FAKE-EVIDENCE"]})
    context["jurisdiction_graph"].update({"status": "CURRENT", "evidence_refs": ["FAKE-EVIDENCE"]})
    context["institutional_route"]["status"] = "CURRENT"
    for requirement in context["institutional_route"]["requirements"]:
        requirement.update({"status": "CURRENT", "evidence_refs": ["FAKE-EVIDENCE"]})
    errors, _ = TRANCHE_MODULE._decision_context_errors(context, {})
    assert any("resolved authoritative evidence" in error for error in errors)
    assert any("evidence is unresolved or non-authoritative" in error for error in errors)


def test_missing_provider_and_revoked_authority_fail_closed(monkeypatch):
    context = copy.deepcopy(DECISION_CONTEXT)
    context["institutional_route"]["requirements"] = [
        item for item in context["institutional_route"]["requirements"]
        if item["requirement_id"] != "ROUTE-REQ-ESCROW"
    ]
    context["account_authority"]["credential_state"] = "REVOKED"
    monkeypatch.setattr(TRANCHE_MODULE, "_load_decision_context", lambda record: (context, []))
    receipt = TRANCHE_MODULE.evaluate(copy.deepcopy(TRANCHE_FIXTURE))
    assert receipt["decision"] == "HOLD"
    assert receipt["execution_authorized"] is False
    assert any("missing required institutional route" in item["detail"] for item in receipt["exceptions"])


@pytest.mark.parametrize(
    ("mutation", "expected_detail"),
    [
        (lambda item: item["documents"].append(copy.deepcopy(item["documents"][0])), "duplicate document_id"),
        (lambda item: item["evidence_catalog"].append(copy.deepcopy(item["evidence_catalog"][0])), "duplicate evidence_id"),
        (lambda item: item["checkpoints"].append(copy.deepcopy(item["checkpoints"][0])), "duplicate checkpoint_id"),
        (lambda item: item["checkpoints"][0]["source_documents"].append("DOC-99"), "unresolved source_document"),
        (lambda item: item["checkpoints"][4]["evidence_refs"].append("UNKNOWN-EVIDENCE"), "unresolved evidence_ref"),
        (lambda item: item["checkpoints"][4].update(evidence_refs=[]), "requires evidence"),
        (lambda item: item["checkpoints"][0].update(gate_type="external_authority"), "is not one of"),
        (lambda item: [checkpoint.update(required=False) for checkpoint in item["checkpoints"]], "does not contain items"),
    ],
)
def test_tranche_evaluator_fails_closed_on_malformed_or_unresolved_input(mutation, expected_detail):
    fixture = copy.deepcopy(TRANCHE_FIXTURE)
    mutation(fixture)
    receipt = TRANCHE_MODULE.evaluate(fixture)
    Draft202012Validator(RECEIPT_SCHEMA, format_checker=FormatChecker()).validate(receipt)
    assert receipt["decision"] == "HOLD"
    assert receipt["execution_authorized"] is False
    assert receipt["observations"]["validation_status"] == "INVALID_UNRESOLVED"
    assert any(expected_detail in exception["detail"] for exception in receipt["exceptions"])


def test_m5_x402_exchange_holds_before_provider_calls():
    result = simulate_x402()
    assert result["http_status"] == 402
    assert result["decision"] == "HOLD"
    assert result["verify_called"] is False
    assert result["settle_called"] is False
    assert result["network_write_performed"] is False
    assert result["financial_movement_performed"] is False
    assert result["token_valuation_status"] == "NO_ASSIGNED_MONETARY_VALUE"
    assert result["trusted_clock"] is False
    assert result["clock_source"] == "FIXTURE_SIMULATION_TIME_UNTRUSTED"
    with pytest.raises(ValueError, match="untrusted fixture time"):
        simulate_x402(clock_source="TRUSTED_SERVER_CLOCK")


def test_m5_x402_rejects_tampered_client_echo():
    tampered = copy.deepcopy(PAYMENT_PAYLOAD)
    tampered["extensions"]["m5-ricardian"]["info"]["request_fingerprint"]["amount"] = "1"

    with pytest.raises(ValueError, match="echo mismatch"):
        simulate_x402(payload=tampered)


def test_m5_x402_timeout_is_part_of_the_canonical_fingerprint():
    original_digest = canonical_digest(m5_extension(PAYMENT_REQUIRED)["info"]["request_fingerprint"])
    required = copy.deepcopy(PAYMENT_REQUIRED)
    payload = copy.deepcopy(PAYMENT_PAYLOAD)
    required["accepts"][0]["maxTimeoutSeconds"] = 600
    payload["accepted"]["maxTimeoutSeconds"] = 600
    with pytest.raises(ValueError, match="fingerprint mismatch"):
        simulate_x402(required, payload)

    fingerprint = m5_extension(required)["info"]["request_fingerprint"]
    fingerprint["max_timeout_seconds"] = 600
    m5_extension(payload)["info"]["request_fingerprint"]["max_timeout_seconds"] = 600
    assert canonical_digest(fingerprint) != original_digest


@pytest.mark.parametrize("target", ["version", "payment_identifier", "extra"])
def test_m5_x402_binds_version_payment_identifier_and_extra(target):
    required = copy.deepcopy(PAYMENT_REQUIRED)
    payload = copy.deepcopy(PAYMENT_PAYLOAD)
    if target == "version":
        required["x402Version"] = payload["x402Version"] = 1
    elif target == "payment_identifier":
        required["extensions"]["payment-identifier"]["info"]["id"] = "other_payment_identifier"
        payload["extensions"]["payment-identifier"]["info"]["id"] = "other_payment_identifier"
    else:
        required["accepts"][0]["extra"]["numscriptAsset"] = "EUR/2"
        payload["accepted"]["extra"]["numscriptAsset"] = "EUR/2"
    with pytest.raises(ValueError, match="x402 version|fingerprint mismatch"):
        simulate_x402(required, payload)


@pytest.mark.parametrize(
    "field",
    [
        "taxonomy_digest",
        "decision_context_digest",
        "asset_classification_digest",
        "external_legal_classification_digest",
        "jurisdiction_graph_digest",
        "account_authority_digest",
        "credential_delegation_mandate_digest",
        "institutional_route_digest",
        "receipt_access_policy_digest",
    ],
)
def test_m5_x402_rejects_changed_decision_context_fingerprint(field):
    required = copy.deepcopy(PAYMENT_REQUIRED)
    payload = copy.deepcopy(PAYMENT_PAYLOAD)
    for document in (required, payload):
        m5_extension(document)["info"]["request_fingerprint"][field] = "sha256:" + "0" * 64
    with pytest.raises(ValueError, match="fingerprint mismatch"):
        simulate_x402(required, payload)


@pytest.mark.parametrize(
    ("request_method", "request_resource"),
    [
        ("GET", PAYMENT_REQUIRED["resource"]["url"]),
        ("POST", "https://sandbox.invalid/spring-commons/tranche-01/other"),
    ],
)
def test_m5_x402_binds_actual_outer_request(request_method, request_resource):
    with pytest.raises(ValueError, match="outer request|fingerprint mismatch"):
        simulate_x402(request_method=request_method, request_resource=request_resource)


def test_m5_x402_rejects_expired_request():
    with pytest.raises(ValueError, match="validity window"):
        simulate_x402(observed_at="2026-09-20T00:05:01Z")


def test_m5_x402_rejects_uri_digest_mismatch():
    required = copy.deepcopy(PAYMENT_REQUIRED)
    payload = copy.deepcopy(PAYMENT_PAYLOAD)
    for document in (required, payload):
        document["extensions"]["m5-ricardian"]["info"]["contract"]["digest"] = "sha256:" + "0" * 64
    with pytest.raises(ValueError, match="URI and digest"):
        simulate_x402(required, payload)
