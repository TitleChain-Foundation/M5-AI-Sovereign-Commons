from test_commons_handoff import c,example,NOW
import pytest
from jsonschema import ValidationError


@pytest.mark.parametrize('field,value',[
 ('ai_service_price_usd','0.01'),('billable',True),('service_metering','TOKENS'),('usage_cap',1000),
 ('payment_required',True),('subscription_required',True),('telemetry_required',True),
 ('hosted_routing_required',True),('network_required_for_inference',True),
 ('periodic_account_check_required',True),('paid_fallback_default',True),
 ('diagnostics_disable_preserves_inference',False),('account_suspension_disables_local_inference',True),
 ('export_supported',False),('delete_supported',False)])
def test_tier_one_rejects_rental_and_lockout_conditions(field,value):
    e=example('m5-bom-sovereign-baseline');e[field]=value
    with pytest.raises(ValidationError):c.validate('m5-bom-sovereign-baseline',e)


def test_optional_infrastructure_costs_do_not_change_service_price():
    e=example('m5-bom-sovereign-baseline')
    e['infrastructure_estimate']={'device_amortization_usd':'10.00','purchased_energy_usd':'0.00','storage_usd':'2.00','network_usd':'3.00'}
    c.validate('m5-bom-sovereign-baseline',e)
    assert e['ai_service_price_usd']=='0.00'
    for diagnostics in ['OFF','LOCAL_OPT_IN']:
        e['diagnostics']=diagnostics;c.validate('m5-bom-sovereign-baseline',e)


def test_paid_escalation_requires_current_scoped_opt_in_and_budget():
    request={'principal_ref':'SYN-HUMAN','provider_ref':'SYN-PROVIDER','purpose':'analysis','data_scope':'SYN-DATA','quoted_usd':'1.00','quote_expires_at':'2026-09-24T00:00:00Z'}
    consent={**request,'status':'APPROVED','effective_at':'2026-09-23T00:00:00Z','expires_at':'2026-09-24T00:00:00Z','budget_usd':'2.00'}
    assert not c.paid_compute_allowed(None,request,NOW)
    assert c.paid_compute_allowed(consent,request,NOW)
    for field,value in [('status','REVOKED'),('budget_usd','0.50'),('provider_ref','OTHER'),('data_scope','OTHER'),('expires_at','2026-09-22T00:00:00Z')]:
        assert not c.paid_compute_allowed({**consent,field:value},request,NOW)
    for field,value in [('quoted_usd','NaN'),('quoted_usd','Infinity'),('quote_expires_at','2026-09-22T00:00:00Z')]:
        assert not c.paid_compute_allowed(consent,{**request,field:value},NOW)
