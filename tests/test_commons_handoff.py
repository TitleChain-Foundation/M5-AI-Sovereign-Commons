import copy
from datetime import datetime, UTC
import importlib.util
from pathlib import Path
import re

import pytest
from jsonschema import ValidationError

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('commons_contracts', ROOT/'reference-implementation/commons-contracts/contracts.py')
c = importlib.util.module_from_spec(spec)
spec.loader.exec_module(c)
NOW = datetime(2026, 9, 23, 12, tzinfo=UTC)


def example(name): return c.load(f'examples/{name}.example.json')


@pytest.mark.parametrize('changes', [dict(billable=True), dict(billed_amount_usd='100.00')])
def test_free_public_rejects_billing(changes):
    e=example('m5-event-envelope');e['data']['metering'].update(changes)
    with pytest.raises(ValidationError): c.validate('m5-event-envelope',e)


@pytest.mark.parametrize('schema', ['m5-sovereign-provider-endpoint','provider-plugin-manifest'])
@pytest.mark.parametrize('value',[None,''])
def test_unit_provider_rejects_null_or_empty_delegation(schema,value):
    e=example(schema);e['provider'].update(account_type='M5BOU',parent_account_ref=value,delegation_ref=value)
    with pytest.raises(ValidationError): c.validate(schema,e)


@pytest.mark.parametrize('changes',[dict(external_allowed=True),dict(local_required=False)])
def test_local_only_rejects_remote_contradictions(changes):
    e=example('m5-intelligence-request-laya-local');e.update(changes)
    with pytest.raises(ValidationError): c.validate('m5-intelligence-request',e)


def test_local_receipt_rejects_payment():
    e=example('m5-commerce-receipt-laya-local');e['payment']={'method':'x402','state':'FINAL','amount':'100.00'}
    with pytest.raises(ValidationError): c.validate('m5-commerce-receipt',e)


@pytest.mark.parametrize('gate',['credential','delegation','jurisdiction','approval','provider_standing','provider_capability','endpoint'])
@pytest.mark.parametrize('state',['MISSING','PENDING','REVOKED','EXPIRED','DISPUTED','UNRESOLVED','DENIED'])
def test_authorized_action_rejects_unresolved_gate(gate,state):
    e=example('m5-action-authorization');e[gate]['status']=state
    with pytest.raises(ValidationError): c.validate('m5-action-authorization',e)


def test_policy_and_execution_cannot_contradict_authority():
    e=example('m5-action-authorization');e['policy_result']='DENY'
    with pytest.raises(ValidationError): c.validate('m5-action-authorization',e)
    e['authorized']=False;e['executed']=True
    with pytest.raises(ValidationError): c.validate('m5-action-authorization',e)


def established_fixture():
    j=example('m5-jurisdiction-binding');j['status']='ACTIVE';j['verified_at']='2026-09-23T00:00:00Z'
    records={}
    for b in j['namespace_bindings']:
        b.update(status='ESTABLISHED',standing='GOOD_STANDING',authority_basis='INDEPENDENT_AUTHORITY_EVIDENCE',
                 authority_evidence_refs=[b['binding_id']+'-AUTH'],registration_provenance_refs=[b['binding_id']+'-REG'],
                 validation_record_ref=b['binding_id']+'-VALID',validated_at=j['verified_at'],evidence_hashes=['sha256:'+'0'*64])
        for ref,kind in [(b['authority_evidence_refs'][0],'AUTHORITY'),(b['registration_provenance_refs'][0],'REGISTRATION'),(b['validation_record_ref'],'VALIDATION')]:
            records[ref]={**b,'kind':kind,'status':'VALID','digest':b['evidence_hashes'][0]}
    return j,records


def test_namespaces_distinct_with_multiple_roles_and_no_inheritance():
    j,records=established_fixture();c.validate('m5-jurisdiction-binding',j)
    assert len({b['canonical_entity_ref'] for b in j['namespace_bindings']})==3
    assert [b['namespace_class'] for b in j['namespace_bindings']]==['INTERNATIONAL_ORGANIZATION','MUNICIPALITY','STATE']
    assert all(c.resolve_namespace(b,records.get,NOW) for b in j['namespace_bindings'])
    records['SYN-NS-NYC-AUTH']['namespace']='newyorkchain.eth'
    assert not c.resolve_namespace(j['namespace_bindings'][1],records.get,NOW)


@pytest.mark.parametrize('basis',['TECHNICAL_CONTROL_ONLY','IDENTIFIER_ONLY','UNRESOLVED'])
def test_namespace_technical_control_or_identifier_is_not_authority(basis):
    j,_=established_fixture();j['namespace_bindings'][0]['authority_basis']=basis
    with pytest.raises(ValidationError):c.validate('m5-jurisdiction-binding',j)


def test_unverified_namespace_and_external_identifier_fail_closed():
    j=example('m5-jurisdiction-binding');j['namespace_bindings'][0]['status']='ESTABLISHED'
    with pytest.raises(ValidationError):c.validate('m5-jurisdiction-binding',j)
    j=example('m5-jurisdiction-binding');j['external_identifiers'][0]['authority_effect']='GRANT'
    with pytest.raises(ValidationError):c.validate('m5-jurisdiction-binding',j)
    for field in ['issuer_ref','source_ref']:
        j=example('m5-jurisdiction-binding');del j['external_identifiers'][0][field]
        with pytest.raises(ValidationError):c.validate('m5-jurisdiction-binding',j)


@pytest.mark.parametrize('mutation',[dict(status='REVOKED'),dict(disputed=True),dict(superseded_by='SYN-NEW'),dict(expires_at='2026-09-22T00:00:00Z')])
def test_namespace_lifecycle_blocks_resolution(mutation):
    j,records=established_fixture();b=j['namespace_bindings'][0];b.update(mutation)
    assert not c.resolve_namespace(b,records.get,NOW)


def test_missing_independent_evidence_cannot_be_fixed_by_json():
    j,_=established_fixture()
    assert not c.resolve_namespace(j['namespace_bindings'][0],lambda ref:None,NOW)


def action_fixture():
    j,records=established_fixture();a=example('m5-action-authorization');e=example('m5-eve-activation')
    records[e['activation_id']]={**e,'status':'VALID'}
    records[a['decision_ref']]={**a,'effective_at':e['effective_at'],'expires_at':e['expires_at']}
    records[a['credential']['evidence_ref']]={**a['credential'],'principal_ref':a['principal_ref'],
       'capability_refs':[a['capability_ref']],'resource_refs':[a['resource_ref']],'purposes':[a['purpose']],
       'provider_ref':a['provider_ref'],'approver_ref':'SYN-ACCOUNTABLE-HUMAN',
       'verified_gate_types':['credential','delegation','jurisdiction','approval','provider_standing','provider_capability','endpoint']}
    return a,e,j,records


def test_replaceable_runtime_does_not_change_authority():
    a,e,j,r=action_fixture()
    assert c.authorize(a,e,j,r.get,NOW,'LAYA_LOCAL')
    assert c.authorize(a,e,j,r.get,NOW,'JEV_HOSTED')
    a.update(policy_result='DENY',authorized=False,payment_success=True)
    a['model_result']['confidence']=1
    assert not c.authorize(a,e,j,r.get,NOW,'JEV_HOSTED')


def test_activation_revocation_is_resolved_on_each_action():
    a,e,j,r=action_fixture()
    assert c.authorize(a,e,j,r.get,NOW,'LAYA_LOCAL')
    r[e['activation_id']]['status']='REVOKED'
    assert not c.authorize(a,e,j,r.get,NOW,'LAYA_LOCAL')


@pytest.mark.parametrize('change',['credential_expired','principal_mismatch','capability_outside','namespace_unresolved','approval_denied'])
def test_payment_does_not_bypass_activation_gates(change):
    a,e,j,r=action_fixture();a['payment_success']=True
    if change=='credential_expired':r[a['credential']['evidence_ref']]['expires_at']='2026-09-22T00:00:00Z'
    if change=='principal_mismatch':a['principal_ref']='OTHER'
    if change=='capability_outside':a['capability_ref']='M5CAP.OTHER.v1'
    if change=='namespace_unresolved':j['namespace_bindings'][1]['status']='UNRESOLVED'
    if change=='approval_denied':a['approval']['status']='DENIED'
    assert not c.authorize(a,e,j,r.get,NOW,'LAYA_LOCAL')


def test_cloud_event_attributes_and_source():
    e=example('m5-event-envelope');assert all(re.fullmatch('[a-z0-9]+',k) for k in e)
    e['source']='not a valid URI reference'
    with pytest.raises(ValidationError): c.validate('m5-event-envelope',e)


def test_entire_catalog_resolves_and_each_meter_produces_receipt():
    registry=c.load('m5-openapi/metering/meters.example.yaml')
    catalog=c.load('m5-openapi/pricing/reference-catalog-v1.example.json')
    meters={m['slug']:m for m in registry['meters']}
    assert len(meters)==len(registry['meters'])
    for product in catalog['products']:
        if product['default_billing_policy']=='LOCAL_SOVEREIGN':
            assert product['meter'] is None
            continue
        meter=meters[product['meter']];event=example('m5-event-envelope')
        event['type']=meter['event_type'];event['data']['metering'].update(meter_id=meter['slug'],
            product_id=product['product_id'],reference_unit_price_usd=product['reference_unit_price_usd'],
            notional_service_value_usd=product['reference_unit_price_usd'],waived_amount_usd=product['reference_unit_price_usd'])
        c.validate('m5-event-envelope',event)
        receipt=c.SyntheticMeter().consume(event)
        assert receipt['meter']==meter['slug'] and receipt['billed_amount_usd']=='0.00'
        c.validate('m5-commerce-receipt',receipt)


def test_deduplication_and_conflicting_replay():
    e=example('m5-event-envelope');consumer=c.SyntheticMeter()
    assert consumer.consume(e)==consumer.consume(e)
    assert len(consumer.seen)==1
    e['data']['units']=2
    with pytest.raises(ValueError):consumer.consume(e)


def test_denied_attempt_metered_never_billed():
    e=example('m5-event-envelope');e['data']['event_phase']='DENIED'
    r=c.SyntheticMeter().consume(e)
    assert r['execution_result']=='DENIED' and not r['billable'] and r['payment'] is None


def test_local_inference_has_no_meter_or_receipt_dependency():
    e=example('m5-event-envelope');e['data']['compute_class']='SOVEREIGN_LOCAL';del e['data']['metering']
    assert c.SyntheticMeter().consume(e) is None
    e['data']['metering']=example('m5-event-envelope')['data']['metering']
    with pytest.raises(ValidationError):c.validate('m5-event-envelope',e)


def test_correction_requires_existing_prior_event_without_mutating_it():
    old=example('m5-event-envelope');e=copy.deepcopy(old);e['id']='SYN-CORRECTION';e['data']['event_phase']='CORRECTED'
    with pytest.raises(ValidationError):c.validate('m5-event-envelope',e)
    e['data']['corrects_event_id']=old['id']
    assert not c.validate_correction(e,{})
    assert c.validate_correction(e,{old['id']:old})
    assert old==example('m5-event-envelope')


def test_migration_explicit_mapping_hold_reject_and_preserve_original():
    old=c.load('tests/fixtures/canonical-context-v1.example.json');before=copy.deepcopy(old)
    assert c.migrate_context(old,{})['status']=='HOLD'
    mappings={k:{'status':'known','value':'SYN-EXPLICIT-'+k,'source_refs':['SYN-REVIEWED-EVIDENCE']}
              for k in ['title_state','instrument_state','jurisdiction_binding','authority_state']}
    result=c.migrate_context(old,mappings)
    assert result['status']=='MIGRATE' and old==before
    assert len(result['record'])==15
    mappings['authority_state']['status']='disputed'
    assert c.migrate_context(old,mappings)['status']=='HOLD'
    del old['wrapper']
    assert c.migrate_context(old,mappings)['status']=='REJECT'


@pytest.mark.parametrize('name',['m5-commerce-receipt-laya-local','m5-intelligence-routing-receipt-laya'])
def test_version_pins_reject_latest(name):
    e=example(name);e['versions']['runtime_version']='latest'
    schema='m5-commerce-receipt' if 'commerce' in name else 'm5-intelligence-routing-receipt'
    with pytest.raises(ValidationError):c.validate(schema,e)


def test_orbitalys_cannot_grant_authority():
    e=example('orbitalys-threat-vector');e['authority_effect']='GRANT'
    with pytest.raises(ValidationError):c.validate('orbitalys-threat-vector',e)


@pytest.mark.parametrize('change',['self_approval','wrong_policy_resource','missing_policy','wrong_gate_type','other_provider','wrong_live_agent'])
def test_resolved_evidence_must_match_exact_action(change):
    a,e,j,r=action_fixture()
    if change=='self_approval':r[a['approval']['evidence_ref']]['approver_ref']=a['agent_ref']
    if change=='wrong_policy_resource':r[a['decision_ref']]['resource_ref']='SYN-OTHER'
    if change=='missing_policy':del r[a['decision_ref']]
    if change=='wrong_gate_type':r[a['credential']['evidence_ref']]['verified_gate_types']=['approval']
    if change=='other_provider':r[a['credential']['evidence_ref']]['provider_ref']='SYN-OTHER'
    if change=='wrong_live_agent':r[e['activation_id']]['agent_id']='SYN-OTHER'
    assert not c.authorize(a,e,j,r.get,NOW,'LAYA_LOCAL')


def test_m4_underlying_links_and_titles_are_required():
    e=example('m5-transaction-footprint-property');e['instrument']['underlying_links']=[]
    with pytest.raises(ValidationError):c.validate('m5-transaction-footprint',e)
    e=example('m5-transaction-footprint-property');e['instrument']['underlying_links'][0]['titleholder_ref']=''
    with pytest.raises(ValidationError):c.validate('m5-transaction-footprint',e)


def test_public_function_references_resolve_to_existing_namespace():
    pattern=r'M5(?:CAP|CANON)\.[A-Z_.]+\.v[1-9][0-9]*'
    registered=set(re.findall(pattern,(ROOT/'docs/M5CANON-FUNCTION-NAMESPACE.md').read_text()))
    for path in (ROOT/'examples').glob('*.json'):
        assert set(re.findall(pattern,path.read_text())) <= registered, path.name


def test_agent_cannot_request_a_canon_control_as_capability():
    e=example('m5-eve-activation');e['capability_refs']=['M5CANON.ACTION.AUTHORIZE.v1']
    with pytest.raises(ValidationError):c.validate('m5-eve-activation',e)
