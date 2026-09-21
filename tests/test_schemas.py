import copy
import hashlib
import json
from pathlib import Path

import pytest
from jsonschema import Draft202012Validator, FormatChecker
from jsonschema.exceptions import SchemaError


ROOT = Path(__file__).resolve().parents[1]
SCHEMA_DIR = ROOT / "schemas"
EXAMPLE_DIR = ROOT / "examples"
NAMES = [
    "provider-plugin-manifest",
    "governance-receipt",
    "m5-aimod-hardware-profile",
    "m5-sovereign-provider-endpoint",
    "m5-canonical-context-envelope",
    "m5-aimod-model-artifact",
    "m5-aispace-capability-manifest",
    "m5-human-experience-boundary",
    "m5-human-refusal-profile",
]


def load_pair(name):
    schema = json.loads((SCHEMA_DIR / f"{name}.schema.json").read_text())
    example = json.loads((EXAMPLE_DIR / f"{name}.example.json").read_text())
    return schema, example


def validator(schema):
    return Draft202012Validator(schema, format_checker=FormatChecker())


def test_exactly_nine_named_schemas_and_examples():
    assert sorted(path.stem.removesuffix(".schema") for path in SCHEMA_DIR.glob("*.schema.json")) == sorted(NAMES)
    assert sorted(path.stem.removesuffix(".example") for path in EXAMPLE_DIR.glob("*.example.json")) == sorted(NAMES)


@pytest.mark.parametrize("name", NAMES)
def test_schema_is_draft_2020_12_and_example_validates(name):
    schema, example = load_pair(name)
    assert schema["$schema"] == "https://json-schema.org/draft/2020-12/schema"
    Draft202012Validator.check_schema(schema)
    validator(schema).validate(example)


@pytest.mark.parametrize("name", NAMES)
def test_missing_required_top_level_field_is_rejected(name):
    schema, example = load_pair(name)
    for field in schema["required"]:
        invalid = copy.deepcopy(example)
        del invalid[field]
        assert not validator(schema).is_valid(invalid), f"{name} accepted missing {field}"


@pytest.mark.parametrize("name", NAMES)
def test_unknown_top_level_field_is_rejected(name):
    schema, example = load_pair(name)
    invalid = copy.deepcopy(example)
    invalid["unexpected_field"] = True
    assert not validator(schema).is_valid(invalid)


def test_governance_receipt_rejects_ai_or_nondeterministic_canon_decision():
    schema, example = load_pair("governance-receipt")
    invalid = copy.deepcopy(example)
    invalid["m5canon_decision"]["deterministic"] = False
    assert not validator(schema).is_valid(invalid)


@pytest.mark.parametrize("name", ["provider-plugin-manifest", "m5-sovereign-provider-endpoint"])
def test_provider_records_reject_endorsement_claim(name):
    schema, example = load_pair(name)
    invalid = copy.deepcopy(example)
    invalid["provider"]["endorsed"] = True
    assert not validator(schema).is_valid(invalid)


def test_capability_manifest_rejects_m5canon_control_as_capability():
    schema, example = load_pair("m5-aispace-capability-manifest")
    invalid = copy.deepcopy(example)
    invalid["function_ids"] = ["M5CANON.ACTION.AUTHORIZE.v1"]
    assert not validator(schema).is_valid(invalid)


def test_refusal_profile_is_human_controlled_and_source_pinned():
    schema, example = load_pair("m5-human-refusal-profile")

    delegated_to_agent = copy.deepcopy(example)
    delegated_to_agent["human_controlled"] = False
    assert not validator(schema).is_valid(delegated_to_agent)

    changed_source = copy.deepcopy(example)
    changed_source["protocol_evidence"]["publication_sha256"] = "0" * 64
    assert not validator(schema).is_valid(changed_source)

    changed_intent = copy.deepcopy(example)
    changed_intent["protocol_evidence"]["publication_intent"] = "patent_grant"
    assert not validator(schema).is_valid(changed_intent)

    changed_license = copy.deepcopy(example)
    changed_license["protocol_evidence"]["repository_license"] = "public-domain"
    assert not validator(schema).is_valid(changed_license)


def test_refusal_profile_fails_closed_and_requires_offline_evidence():
    schema, example = load_pair("m5-human-refusal-profile")

    permissive = copy.deepcopy(example)
    permissive["enforcement"]["unresolved_signal_action"] = "allow"
    assert not validator(schema).is_valid(permissive)

    missing_offline_ledger = copy.deepcopy(example)
    del missing_offline_ledger["verification"]["offline_ledger_ref"]
    assert not validator(schema).is_valid(missing_offline_ledger)


def test_member_supplied_refusal_projection_excludes_ownership_key():
    schema, _ = load_pair("m5-human-refusal-profile")
    example = json.loads(
        (EXAMPLE_DIR / "member-supplied" / "m5pod-sovereign-self-refusal.json").read_text()
    )
    validator(schema).validate(example)

    artifact = example["member_artifacts"][0]
    assert artifact["public_identifier"] == "#0045"
    assert artifact["assertion_basis"] == "member_supplied_unverified"
    assert artifact["ownership_key_included"] is False
    assert artifact["authority_effect"] == "none"
    asset = EXAMPLE_DIR / "member-supplied" / artifact["display_asset_ref"]
    assert hashlib.sha256(asset.read_bytes()).hexdigest() == artifact["display_asset_sha256"]

    unsafe = copy.deepcopy(example)
    unsafe["member_artifacts"][0]["ownership_key_included"] = True
    assert not validator(schema).is_valid(unsafe)


@pytest.mark.parametrize(
    ("name", "field"),
    [
        ("m5-aispace-capability-manifest", "refusal_controls"),
        ("m5-human-experience-boundary", "refusal_evaluation"),
    ],
)
def test_refusal_is_evaluated_before_capture(name, field):
    schema, example = load_pair(name)
    invalid = copy.deepcopy(example)
    invalid[field]["evaluated_pre_capture"] = False
    assert not validator(schema).is_valid(invalid)


def test_context_envelope_requires_all_twelve_dimensions():
    schema, example = load_pair("m5-canonical-context-envelope")
    dimensions = {
        "economic_class", "account_context", "title_container", "representation",
        "wrapper", "jurisdictional_security_state", "usc", "s_state", "sr_state",
        "external_classifications", "credentials_standing", "provenance",
    }
    assert dimensions <= set(schema["required"])
    for dimension in dimensions:
        invalid = copy.deepcopy(example)
        del invalid[dimension]
        assert not validator(schema).is_valid(invalid)

