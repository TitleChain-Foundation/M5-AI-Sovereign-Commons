"""Fail-closed reference preflight for an M5 Eve member workspace.

This module demonstrates bounded policy behavior. It does not authenticate a
person, issue a credential, grant authority, or connect to a production system.
"""

from __future__ import annotations

import hashlib
import json
from dataclasses import asdict, dataclass
from datetime import UTC, datetime
from enum import StrEnum
from pathlib import Path
from typing import Any


ACCOUNT_CONTEXT_TYPES = frozenset({"BOM", "BOU", "BOB", "BOI", "BOG"})
CONSEQUENTIAL_CAPABILITIES = frozenset(
    {
        "evidence_publish",
        "external_submit",
        "legal_signature",
        "financial_commitment",
        "financial_movement",
        "title_or_registry_write",
        "procurement_award",
        "construction_or_physical_action",
    }
)
TRANSACTION_CAPABILITIES = CONSEQUENTIAL_CAPABILITIES - {"evidence_publish"}
ACCOUNTABLE_HUMAN_APPROVAL = "accountable-human"


class Decision(StrEnum):
    ALLOW = "ALLOW"
    HOLD = "HOLD"
    DENY = "DENY"
    ESCALATE = "ESCALATE"


@dataclass(frozen=True)
class ContextGrant:
    grant_id: str
    principal_id: str
    context_type: str
    context_id: str
    status: str
    authority_source: str
    effective_at: datetime
    expires_at: datetime
    revoked: bool = False


@dataclass(frozen=True)
class Delegation:
    delegation_id: str
    issuer_id: str
    principal_id: str
    context_type: str
    context_id: str
    capability: str
    purpose: str
    resource_scope: tuple[str, ...]
    jurisdictions: tuple[str, ...]
    required_approvals: tuple[str, ...]
    authority_source: str
    status: str
    effective_at: datetime
    expires_at: datetime
    revoked: bool = False


@dataclass(frozen=True)
class ActionRequest:
    request_id: str
    authenticated: bool
    principal_id: str
    context_type: str
    context_id: str
    capability: str
    purpose: str
    resource: str
    jurisdiction: str
    approvals: tuple[str, ...] = ()
    evidence_receipt_required: bool = True


@dataclass(frozen=True)
class DeploymentProfile:
    profile_id: str
    status: str
    context_type: str
    context_id: str
    context_lifecycle_state: str
    authority_effect: str
    transaction_posture: str
    capabilities: dict[str, bool]
    fail_closed: bool


@dataclass(frozen=True)
class DecisionReceipt:
    request_id: str
    profile_id: str
    decision: Decision
    reason_codes: tuple[str, ...]
    principal_id: str
    context_type: str
    context_id: str
    capability: str
    evaluated_at: str
    policy_version: str = "M5EVE.PREFLIGHT.v1"

    def digest(self) -> str:
        payload = json.dumps(asdict(self), sort_keys=True, separators=(",", ":"))
        return hashlib.sha256(payload.encode("utf-8")).hexdigest()


class M5EvePreflight:
    """Evaluate a request without consulting or delegating to a model."""

    def __init__(self, profile: DeploymentProfile) -> None:
        self.profile = profile

    def evaluate(
        self,
        request: ActionRequest,
        *,
        context_grant: ContextGrant | None,
        delegation: Delegation | None,
        now: datetime | None = None,
    ) -> DecisionReceipt:
        evaluated_at = now or datetime.now(UTC)
        reasons: list[str] = []
        decision = Decision.ALLOW
        precedence = {
            Decision.ALLOW: 0,
            Decision.HOLD: 1,
            Decision.ESCALATE: 2,
            Decision.DENY: 3,
        }

        def stop(result: Decision, reason: str) -> None:
            nonlocal decision
            if precedence[result] > precedence[decision]:
                decision = result
            reasons.append(reason)

        if not self.profile.fail_closed:
            stop(Decision.DENY, "PROFILE_NOT_FAIL_CLOSED")
        if not request.authenticated or not request.principal_id:
            stop(Decision.DENY, "APPLICATION_SESSION_NOT_AUTHENTICATED")
        if request.context_type not in ACCOUNT_CONTEXT_TYPES:
            stop(Decision.DENY, "UNKNOWN_ACCOUNT_CONTEXT_TYPE")
        if (
            request.context_type != self.profile.context_type
            or request.context_id != self.profile.context_id
        ):
            stop(Decision.DENY, "REQUEST_OUTSIDE_DEPLOYMENT_CONTEXT")
        if self.profile.status != "AUTHORIZED":
            stop(Decision.HOLD, "DEPLOYMENT_NOT_AUTHORIZED")
        if self.profile.context_lifecycle_state != "AUTHORIZED":
            stop(Decision.HOLD, "CONTEXT_NOT_AUTHORIZED")
        if self.profile.authority_effect != "BOUNDED":
            stop(Decision.HOLD, "NO_BOUNDED_AUTHORITY_EFFECT")
        if not self.profile.capabilities.get(request.capability, False):
            stop(Decision.HOLD, "CAPABILITY_DISABLED")
        if (
            self.profile.transaction_posture == "HOLD"
            and request.capability in TRANSACTION_CAPABILITIES
        ):
            stop(Decision.DENY, "TRANSACTION_POSTURE_HOLD")
        if (
            request.capability in CONSEQUENTIAL_CAPABILITIES
            and ACCOUNTABLE_HUMAN_APPROVAL not in request.approvals
        ):
            stop(Decision.ESCALATE, "ACCOUNTABLE_HUMAN_APPROVAL_MISSING")
        if not request.evidence_receipt_required:
            stop(Decision.DENY, "EVIDENCE_RECEIPT_REQUIRED")

        self._check_context_grant(request, context_grant, evaluated_at, stop)
        self._check_delegation(request, delegation, evaluated_at, stop)

        return DecisionReceipt(
            request_id=request.request_id,
            profile_id=self.profile.profile_id,
            decision=decision,
            reason_codes=tuple(dict.fromkeys(reasons or ["ALL_CONFIGURED_CHECKS_PASSED"])),
            principal_id=request.principal_id,
            context_type=request.context_type,
            context_id=request.context_id,
            capability=request.capability,
            evaluated_at=evaluated_at.astimezone(UTC).isoformat(),
        )

    @staticmethod
    def _check_context_grant(
        request: ActionRequest,
        grant: ContextGrant | None,
        now: datetime,
        stop: Any,
    ) -> None:
        if grant is None:
            stop(Decision.HOLD, "CONTEXT_GRANT_MISSING")
            return
        if (
            grant.principal_id != request.principal_id
            or grant.context_type != request.context_type
            or grant.context_id != request.context_id
        ):
            stop(Decision.DENY, "CONTEXT_GRANT_MISMATCH")
        if grant.revoked or grant.status in {"REVOKED", "SUSPENDED", "EXPIRED"}:
            stop(Decision.DENY, "CONTEXT_GRANT_INACTIVE")
        elif grant.status != "AUTHORIZED":
            stop(Decision.HOLD, "CONTEXT_GRANT_NOT_AUTHORIZED")
        if not grant.authority_source:
            stop(Decision.HOLD, "CONTEXT_AUTHORITY_SOURCE_MISSING")
        if now < grant.effective_at or now >= grant.expires_at:
            stop(Decision.DENY, "CONTEXT_GRANT_OUTSIDE_EFFECTIVE_PERIOD")

    @staticmethod
    def _check_delegation(
        request: ActionRequest,
        delegation: Delegation | None,
        now: datetime,
        stop: Any,
    ) -> None:
        if delegation is None:
            stop(Decision.HOLD, "DELEGATION_MISSING")
            return
        if not delegation.issuer_id or delegation.issuer_id == request.principal_id:
            stop(Decision.DENY, "SELF_OR_UNATTRIBUTED_DELEGATION")
        if (
            delegation.principal_id != request.principal_id
            or delegation.context_type != request.context_type
            or delegation.context_id != request.context_id
        ):
            stop(Decision.DENY, "DELEGATION_CONTEXT_MISMATCH")
        if delegation.capability != request.capability:
            stop(Decision.DENY, "DELEGATION_CAPABILITY_MISMATCH")
        if delegation.purpose != request.purpose:
            stop(Decision.DENY, "DELEGATION_PURPOSE_MISMATCH")
        if request.resource not in delegation.resource_scope:
            stop(Decision.DENY, "RESOURCE_OUTSIDE_DELEGATED_SCOPE")
        if request.jurisdiction not in delegation.jurisdictions:
            stop(Decision.DENY, "JURISDICTION_OUTSIDE_DELEGATED_SCOPE")
        if delegation.revoked or delegation.status in {"REVOKED", "SUSPENDED", "EXPIRED"}:
            stop(Decision.DENY, "DELEGATION_INACTIVE")
        elif delegation.status != "AUTHORIZED":
            stop(Decision.HOLD, "DELEGATION_NOT_AUTHORIZED")
        if not delegation.authority_source:
            stop(Decision.HOLD, "DELEGATION_AUTHORITY_SOURCE_MISSING")
        if now < delegation.effective_at or now >= delegation.expires_at:
            stop(Decision.DENY, "DELEGATION_OUTSIDE_EFFECTIVE_PERIOD")
        missing = set(delegation.required_approvals) - set(request.approvals)
        if missing:
            stop(Decision.HOLD, "REQUIRED_APPROVALS_MISSING")


def load_profile(path: Path) -> DeploymentProfile:
    """Load the small subset of a deployment profile used by this adapter."""
    data = json.loads(path.read_text(encoding="utf-8"))
    context = data["account_context"]
    controls = data["required_controls"]
    return DeploymentProfile(
        profile_id=data["profile_id"],
        status=data["status"],
        context_type=context["type"],
        context_id=context["id"],
        context_lifecycle_state=context["lifecycle_state"],
        authority_effect=context["authority_effect"],
        transaction_posture=data["transaction_posture"],
        capabilities=data["capabilities"],
        fail_closed=controls["fail_closed"],
    )
