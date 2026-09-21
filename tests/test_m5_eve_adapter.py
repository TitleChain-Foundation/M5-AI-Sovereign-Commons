from __future__ import annotations

import importlib.util
import sys
from dataclasses import replace
from datetime import UTC, datetime, timedelta
from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parents[1]
ADAPTER_PATH = ROOT / "m5-eve" / "reference" / "adapter.py"
SPEC = importlib.util.spec_from_file_location("m5_eve_adapter", ADAPTER_PATH)
assert SPEC and SPEC.loader
adapter = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = adapter
SPEC.loader.exec_module(adapter)

NOW = datetime(2026, 9, 20, 12, tzinfo=UTC)
DEFAULT = object()


def profile(**changes):
    base = adapter.DeploymentProfile(
        profile_id="test-profile",
        status="AUTHORIZED",
        context_type="BOU",
        context_id="PPT-EZ-CA-0001",
        context_lifecycle_state="AUTHORIZED",
        authority_effect="BOUNDED",
        transaction_posture="HOLD",
        capabilities={"public_source_read": True, "analysis": True},
        fail_closed=True,
    )
    return replace(base, **changes)


def request(**changes):
    base = adapter.ActionRequest(
        request_id="request-1",
        authenticated=True,
        principal_id="principal-1",
        context_type="BOU",
        context_id="PPT-EZ-CA-0001",
        capability="analysis",
        purpose="spring-commons-public-diligence",
        resource="sec-public-input",
        jurisdiction="US-CA",
        approvals=("project-reviewer",),
    )
    return replace(base, **changes)


def grant(**changes):
    base = adapter.ContextGrant(
        grant_id="grant-1",
        principal_id="principal-1",
        context_type="BOU",
        context_id="PPT-EZ-CA-0001",
        status="AUTHORIZED",
        authority_source="project-role-register:entry-1",
        effective_at=NOW - timedelta(days=1),
        expires_at=NOW + timedelta(days=1),
    )
    return replace(base, **changes)


def delegation(**changes):
    base = adapter.Delegation(
        delegation_id="delegation-1",
        issuer_id="institution-1",
        principal_id="principal-1",
        context_type="BOU",
        context_id="PPT-EZ-CA-0001",
        capability="analysis",
        purpose="spring-commons-public-diligence",
        resource_scope=("sec-public-input",),
        jurisdictions=("US-CA",),
        required_approvals=("project-reviewer",),
        authority_source="delegation-register:entry-1",
        status="AUTHORIZED",
        effective_at=NOW - timedelta(days=1),
        expires_at=NOW + timedelta(days=1),
    )
    return replace(base, **changes)


def evaluate(*, configured=None, asked=None, context_grant=DEFAULT, delegated=DEFAULT):
    return adapter.M5EvePreflight(configured or profile()).evaluate(
        asked or request(),
        context_grant=grant() if context_grant is DEFAULT else context_grant,
        delegation=delegation() if delegated is DEFAULT else delegated,
        now=NOW,
    )


def test_bounded_public_analysis_can_pass_all_checks():
    receipt = evaluate()
    assert receipt.decision == adapter.Decision.ALLOW
    assert receipt.reason_codes == ("ALL_CONFIGURED_CHECKS_PASSED",)
    assert len(receipt.digest()) == 64


@pytest.mark.parametrize(
    ("configured", "reason"),
    [
        (profile(status="SPECIFIED"), "DEPLOYMENT_NOT_AUTHORIZED"),
        (profile(context_lifecycle_state="SUSPENDED"), "CONTEXT_NOT_AUTHORIZED"),
        (profile(authority_effect="NONE"), "NO_BOUNDED_AUTHORITY_EFFECT"),
        (profile(capabilities={"analysis": False}), "CAPABILITY_DISABLED"),
        (profile(fail_closed=False), "PROFILE_NOT_FAIL_CLOSED"),
    ],
)
def test_profile_failures_do_not_allow(configured, reason):
    receipt = evaluate(configured=configured)
    assert receipt.decision != adapter.Decision.ALLOW
    assert reason in receipt.reason_codes


def test_repository_example_profile_is_default_deny():
    configured = adapter.load_profile(ROOT / "m5-eve" / "deployment-profile.example.json")
    receipt = evaluate(configured=configured)
    assert receipt.decision == adapter.Decision.HOLD
    assert "DEPLOYMENT_NOT_AUTHORIZED" in receipt.reason_codes
    assert "CAPABILITY_DISABLED" in receipt.reason_codes


@pytest.mark.parametrize(
    ("asked", "reason"),
    [
        (request(authenticated=False), "APPLICATION_SESSION_NOT_AUTHENTICATED"),
        (request(context_type="UNKNOWN"), "UNKNOWN_ACCOUNT_CONTEXT_TYPE"),
        (request(context_id="other-project"), "REQUEST_OUTSIDE_DEPLOYMENT_CONTEXT"),
        (request(evidence_receipt_required=False), "EVIDENCE_RECEIPT_REQUIRED"),
    ],
)
def test_request_boundary_failures_are_denied(asked, reason):
    receipt = evaluate(asked=asked)
    assert receipt.decision == adapter.Decision.DENY
    assert reason in receipt.reason_codes


def test_missing_context_grant_holds():
    receipt = evaluate(context_grant=None)
    assert receipt.decision == adapter.Decision.HOLD
    assert "CONTEXT_GRANT_MISSING" in receipt.reason_codes


@pytest.mark.parametrize(
    ("context_grant", "reason"),
    [
        (grant(principal_id="other"), "CONTEXT_GRANT_MISMATCH"),
        (grant(status="SUSPENDED"), "CONTEXT_GRANT_INACTIVE"),
        (grant(revoked=True), "CONTEXT_GRANT_INACTIVE"),
        (grant(expires_at=NOW), "CONTEXT_GRANT_OUTSIDE_EFFECTIVE_PERIOD"),
    ],
)
def test_invalid_context_grants_are_denied(context_grant, reason):
    receipt = evaluate(context_grant=context_grant)
    assert receipt.decision == adapter.Decision.DENY
    assert reason in receipt.reason_codes


def test_missing_delegation_holds():
    receipt = evaluate(delegated=None)
    assert receipt.decision == adapter.Decision.HOLD
    assert "DELEGATION_MISSING" in receipt.reason_codes


@pytest.mark.parametrize(
    ("delegated", "reason"),
    [
        (delegation(issuer_id="principal-1"), "SELF_OR_UNATTRIBUTED_DELEGATION"),
        (delegation(principal_id="other"), "DELEGATION_CONTEXT_MISMATCH"),
        (delegation(capability="drafting"), "DELEGATION_CAPABILITY_MISMATCH"),
        (delegation(purpose="other-purpose"), "DELEGATION_PURPOSE_MISMATCH"),
        (delegation(resource_scope=("other-resource",)), "RESOURCE_OUTSIDE_DELEGATED_SCOPE"),
        (delegation(jurisdictions=("US-NY",)), "JURISDICTION_OUTSIDE_DELEGATED_SCOPE"),
        (delegation(status="REVOKED"), "DELEGATION_INACTIVE"),
        (delegation(expires_at=NOW), "DELEGATION_OUTSIDE_EFFECTIVE_PERIOD"),
    ],
)
def test_invalid_delegations_are_denied(delegated, reason):
    receipt = evaluate(delegated=delegated)
    assert receipt.decision == adapter.Decision.DENY
    assert reason in receipt.reason_codes


def test_missing_required_coapproval_holds():
    receipt = evaluate(asked=request(approvals=()))
    assert receipt.decision == adapter.Decision.HOLD
    assert "REQUIRED_APPROVALS_MISSING" in receipt.reason_codes


def test_spring_commons_consequential_action_is_disabled():
    asked = request(capability="financial_movement")
    delegated = delegation(capability="financial_movement")
    receipt = evaluate(asked=asked, delegated=delegated)
    assert receipt.decision == adapter.Decision.DENY
    assert "CAPABILITY_DISABLED" in receipt.reason_codes
    assert "TRANSACTION_POSTURE_HOLD" in receipt.reason_codes


def test_consequential_action_requires_accountable_human_even_if_enabled():
    configured = profile(
        transaction_posture="CONDITIONAL",
        capabilities={"evidence_publish": True},
    )
    asked = request(capability="evidence_publish", resource="approved-report")
    delegated = delegation(
        capability="evidence_publish",
        resource_scope=("approved-report",),
    )
    receipt = evaluate(configured=configured, asked=asked, delegated=delegated)
    assert receipt.decision == adapter.Decision.ESCALATE
    assert "ACCOUNTABLE_HUMAN_APPROVAL_MISSING" in receipt.reason_codes


def test_consequential_action_can_pass_only_with_required_human_approval():
    configured = profile(
        transaction_posture="CONDITIONAL",
        capabilities={"evidence_publish": True},
    )
    asked = request(
        capability="evidence_publish",
        resource="approved-report",
        approvals=("project-reviewer", adapter.ACCOUNTABLE_HUMAN_APPROVAL),
    )
    delegated = delegation(
        capability="evidence_publish",
        resource_scope=("approved-report",),
    )
    receipt = evaluate(configured=configured, asked=asked, delegated=delegated)
    assert receipt.decision == adapter.Decision.ALLOW
