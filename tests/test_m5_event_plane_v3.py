import json
from pathlib import Path

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]

PAIRS = [
    ('m5-jurisdiction-binding', 'm5-jurisdiction-binding'),
    ('m5-credential-trust-record', 'm5-credential-trust-record'),
    ('m5-event-envelope', 'm5-event-envelope'),
    ('orbitalys-threat-vector', 'orbitalys-threat-vector'),
    ('m5-service-event-manifest', 'm5-service-event-manifest'),
    ('m5-canonical-context-envelope', 'm5-canonical-context-envelope'),
    ('m5-sovereign-provider-endpoint', 'm5-sovereign-provider-endpoint'),
    ('provider-plugin-manifest', 'provider-plugin-manifest'),
    ('m5-intelligence-request', 'm5-intelligence-request-laya-local'),
    ('m5-intelligence-routing-receipt', 'm5-intelligence-routing-receipt-laya'),
    ('m5-transaction-footprint', 'm5-transaction-footprint-property'),
    ('m5-commerce-receipt', 'm5-commerce-receipt-laya-local'),
]


def load_json(path):
    return json.loads(path.read_text())


def test_v3_pairs_validate():
    for schema_name, example_name in PAIRS:
        schema = load_json(ROOT / 'schemas' / f'{schema_name}.schema.json')
        example = load_json(ROOT / 'examples' / f'{example_name}.example.json')
        Draft202012Validator.check_schema(schema)
        Draft202012Validator(schema, format_checker=FormatChecker()).validate(example)


def test_context_v2_has_no_wrapper():
    schema = load_json(ROOT / 'schemas' / 'm5-canonical-context-envelope.schema.json')
    assert 'wrapper' not in schema['required']
    for required in ('instrument_state', 'jurisdiction_binding', 'authority_state'):
        assert required in schema['required']


def test_orbitalys_cannot_change_authority():
    example = load_json(ROOT / 'examples' / 'orbitalys-threat-vector.example.json')
    assert example['authority_effect'] == 'NONE'


def test_free_public_event_is_zero_billed():
    example = load_json(ROOT / 'examples' / 'm5-event-envelope.example.json')
    m = example['data']['metering']
    assert m['billing_policy'] == 'FREE_PUBLIC'
    assert m['billed_amount_usd'] == '0.00'
    assert float(m['notional_service_value_usd']) >= 0


def test_provider_account_is_provider_capable_type():
    example = load_json(ROOT / 'examples' / 'm5-sovereign-provider-endpoint.example.json')
    assert example['provider']['account_type'] in {'M5BOU','M5BOB','M5BOI','M5BOG'}


def test_jurisdiction_binding_uses_chain_and_external_sources():
    example = load_json(ROOT / 'examples' / 'm5-jurisdiction-binding.example.json')
    assert example['chain_ref']
    assert example['external_authority_refs']
    assert example['credential_refs']
