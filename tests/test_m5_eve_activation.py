from test_commons_handoff import c,example,action_fixture,NOW
import pytest
from jsonschema import ValidationError


@pytest.mark.parametrize('field',['principal_ref','credential','delegation','approval','namespace_binding_refs','compatibility'])
def test_activation_requires_bounded_context(field):
    e=example('m5-eve-activation');del e[field]
    with pytest.raises(ValidationError):c.validate('m5-eve-activation',e)


@pytest.mark.parametrize('state',['REVOKED','SUSPENDED','EXPIRED','PENDING'])
def test_inactive_activation_cannot_execute(state):
    a,e,j,r=action_fixture();e['lifecycle_state']=state
    assert not c.authorize(a,e,j,r.get,NOW,'LAYA_LOCAL')


def test_expired_activation_cannot_execute():
    a,e,j,r=action_fixture();e['expires_at']='2026-09-22T00:00:00Z'
    assert not c.authorize(a,e,j,r.get,NOW,'LAYA_LOCAL')
