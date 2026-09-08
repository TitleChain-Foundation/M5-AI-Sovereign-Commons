import copy
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
]


def load_pair(name):
    schema = json.loads((SCHEMA_DIR / f"{name}.schema.json").read_text())
    example = json.loads((EXAMPLE_DIR / f"{name}.example.json").read_text())
    return schema, example


def validator(schema):
    return Draft202012Validator(schema, format_checker=FormatChecker())


def test_exactly_eight_named_schemas_and_examples():
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

