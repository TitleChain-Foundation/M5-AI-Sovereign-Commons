#!/usr/bin/env python3
"""Validate a synthetic M5-x402 exchange without verifying or settling payment."""

from __future__ import annotations

import json
import sys
from datetime import datetime
from pathlib import Path
from typing import Any
from urllib.parse import parse_qsl, urlencode, urlsplit, urlunsplit

from jsonschema import Draft202012Validator, FormatChecker
from jsonschema.exceptions import ValidationError

HERE = Path(__file__).resolve().parent
PROJECT = HERE.parent.parent.parent
sys.path.insert(0, str(HERE.parent))

from canonical import canonical_digest, verify_bound_artifact  # noqa: E402
from simulate_first_tranche import _decision_context_errors  # noqa: E402

DECISION_CONTEXT_SCHEMA_PATH = PROJECT / "schemas" / "m5canon-decision-context.schema.json"
MANIFEST_SCHEMA_PATH = PROJECT / "schemas" / "spring-commons-human-terms-manifest.schema.json"
AUTHORITY_SCOPE_FIELDS = (
    "credential_refs",
    "credential_state",
    "delegation_refs",
    "delegation_state",
    "mandate_ref",
    "mandate_state",
    "revocation_state",
)


def _validate_or_value_error(
    validator: Draft202012Validator,
    record: Any,
    label: str,
) -> None:
    try:
        validator.validate(record)
    except ValidationError as error:
        raise ValueError(f"{label} schema validation failed: {error.message}") from error


def _normalize_resource(value: str) -> str:
    parsed = urlsplit(value)
    if parsed.scheme not in {"http", "https"} or not parsed.hostname or parsed.username or parsed.password:
        raise ValueError("outer request resource must be an absolute HTTP(S) URI without userinfo")
    port = parsed.port
    host = parsed.hostname.lower()
    if port and not ((parsed.scheme.lower() == "http" and port == 80) or (parsed.scheme.lower() == "https" and port == 443)):
        host = f"{host}:{port}"
    path = parsed.path or "/"
    query = urlencode(sorted(parse_qsl(parsed.query, keep_blank_values=True)))
    return urlunsplit((parsed.scheme.lower(), host, path, query, ""))


def _timestamp(value: str) -> datetime:
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def _fingerprint(
    requirement: dict[str, Any],
    info: dict[str, Any],
    request_method: str,
    request_resource: str,
    decision_context: dict[str, Any],
    x402_version: Any,
    payment_identifier: dict[str, Any],
) -> dict[str, Any]:
    declared = info["request_fingerprint"]
    taxonomy = decision_context["taxonomy"]
    authority = decision_context["account_authority"]
    return {
        "x402_version": x402_version,
        "payment_id": declared["payment_id"],
        "payment_identifier_digest": canonical_digest(payment_identifier),
        "http_method": request_method.upper(),
        "resource": _normalize_resource(request_resource),
        "scheme": requirement["scheme"],
        "network": requirement["network"],
        "asset": requirement["asset"],
        "amount": requirement["amount"],
        "pay_to": requirement["payTo"],
        "max_timeout_seconds": requirement["maxTimeoutSeconds"],
        "accepted_extra_digest": canonical_digest(requirement.get("extra", {})),
        "issued_at": declared["issued_at"],
        "expires_at": declared["expires_at"],
        "operation_id": declared["operation_id"],
        "taxonomy_profile_id": taxonomy["profile_id"],
        "taxonomy_version": taxonomy["version"],
        "taxonomy_digest": taxonomy["digest"],
        "decision_context_digest": info["decision_context"]["digest"],
        "asset_classification_digest": canonical_digest(decision_context["asset_classification"]),
        "external_legal_classification_digest": canonical_digest(decision_context["external_legal_classification"]),
        "jurisdiction_graph_digest": canonical_digest(decision_context["jurisdiction_graph"]),
        "account_authority_digest": canonical_digest(authority),
        "credential_delegation_mandate_digest": canonical_digest(
            {field: authority[field] for field in AUTHORITY_SCOPE_FIELDS}
        ),
        "institutional_route_digest": canonical_digest(decision_context["institutional_route"]),
        "receipt_access_policy_digest": canonical_digest(decision_context["receipt_access_policy"]),
    }


def _verify_artifact_bindings(info: dict[str, Any]) -> dict[str, Any]:
    contract_ids = set()
    for name in ("contract", "human_terms", "machine_policy", "executable_plan", "decision_context"):
        binding = info[name]
        contract_ids.add(binding["contract_id"])
        verify_bound_artifact(HERE, binding.get("uri"), binding.get("digest"), PROJECT, name)
    if len(contract_ids) != 1:
        raise ValueError("Ricardian layers do not share one contract identifier")

    manifest_binding = info["human_terms"]
    manifest_path = verify_bound_artifact(
        HERE, manifest_binding.get("uri"), manifest_binding.get("digest"), PROJECT, "human_terms"
    )
    manifest = json.loads(manifest_path.read_text())
    manifest_schema = json.loads(MANIFEST_SCHEMA_PATH.read_text())
    _validate_or_value_error(
        Draft202012Validator(manifest_schema, format_checker=FormatChecker()),
        manifest,
        "human-terms manifest",
    )
    if (
        manifest["contract_id"] != manifest_binding["contract_id"]
        or manifest["artifact_id"] != manifest_binding["id"]
        or manifest["artifact_version"] != manifest_binding["version"]
        or manifest["supersession_history"] != manifest_binding["supersession_history"]
    ):
        raise ValueError("human-terms binding does not match its manifest identity")
    expected_document_ids = [f"DOC-{number:02d}" for number in range(1, 24)]
    document_ids = [document["id"] for document in manifest["documents"]]
    document_uris = [document["uri"] for document in manifest["documents"]]
    if document_ids != expected_document_ids or len(document_uris) != len(set(document_uris)):
        raise ValueError("human-terms manifest must identify unique ordered DOC-01 through DOC-23")
    for document in manifest["documents"]:
        verify_bound_artifact(
            manifest_path.parent,
            document.get("uri"),
            document.get("digest"),
            PROJECT,
            f"manifest document {document.get('id', 'UNRESOLVED')}",
        )

    context_binding = info["decision_context"]
    context_path = verify_bound_artifact(
        HERE,
        context_binding.get("uri"),
        context_binding.get("digest"),
        PROJECT,
        "decision_context",
    )
    context = json.loads(context_path.read_text())
    context_schema = json.loads(DECISION_CONTEXT_SCHEMA_PATH.read_text())
    _validate_or_value_error(
        Draft202012Validator(context_schema, format_checker=FormatChecker()),
        context,
        "decision context",
    )
    if (
        context["context_id"] != context_binding["id"]
        or context["version"] != context_binding["version"]
        or context["supersession_history"] != context_binding["supersession_history"]
    ):
        raise ValueError("decision-context binding does not match its artifact identity")
    taxonomy = context["taxonomy"]
    taxonomy_path = verify_bound_artifact(
        context_path.parent,
        taxonomy.get("uri"),
        taxonomy.get("digest"),
        PROJECT,
        "taxonomy",
    )
    taxonomy_record = json.loads(taxonomy_path.read_text())
    if (
        taxonomy_record.get("profile_id") != taxonomy["profile_id"]
        or taxonomy_record.get("version") != taxonomy["version"]
        or taxonomy_record.get("authority_effect") != "NONE"
        or taxonomy_record.get("status") != "DRAFT_PROFILE"
    ):
        raise ValueError("taxonomy binding does not match the pilot-scoped draft profile")
    return context


def _simulate(
    payment_required: dict[str, Any],
    payment_payload: dict[str, Any],
    schema: dict[str, Any],
    *,
    request_method: str,
    request_resource: str,
    observed_at: str,
    clock_source: str,
) -> dict[str, Any]:
    """Model the x402 retry and M5 pre-settlement gates in public dry-run mode."""
    if clock_source != "FIXTURE_SIMULATION_TIME_UNTRUSTED":
        raise ValueError("public simulator accepts only explicitly untrusted fixture time")
    required_extension = payment_required["extensions"]["m5-ricardian"]
    payload_extension = payment_payload["extensions"]["m5-ricardian"]
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    _validate_or_value_error(validator, required_extension, "PaymentRequired M5 extension")
    _validate_or_value_error(validator, payload_extension, "PaymentPayload M5 extension")

    if payment_required.get("x402Version") != 2 or payment_payload.get("x402Version") != 2:
        raise ValueError("x402 version must be v2")
    required_payment_identifier = payment_required.get("extensions", {}).get("payment-identifier")
    payload_payment_identifier = payment_payload.get("extensions", {}).get("payment-identifier")
    if required_payment_identifier != payload_payment_identifier or not isinstance(required_payment_identifier, dict):
        raise ValueError("payment-identifier extension echo mismatch")

    requirement = payment_required["accepts"][0]
    accepted = payment_payload["accepted"]
    core_fields = ("scheme", "network", "amount", "asset", "payTo", "maxTimeoutSeconds")
    if any(requirement[field] != accepted[field] for field in core_fields):
        raise ValueError("x402 accepted terms do not match PaymentRequired")
    if requirement.get("extra", {}) != accepted.get("extra", {}):
        raise ValueError("x402 accepted extra terms do not match PaymentRequired")

    required_info = required_extension["info"]
    payload_info = payload_extension["info"]
    if required_info != payload_info:
        raise ValueError("M5 Ricardian extension echo mismatch")
    if payment_required["resource"]["url"] != payment_payload["resource"]["url"]:
        raise ValueError("x402 resource echo mismatch")
    if _normalize_resource(payment_required["resource"]["url"]) != _normalize_resource(request_resource):
        raise ValueError("PaymentRequired resource does not match the actual outer request")
    decision_context = _verify_artifact_bindings(required_info)
    if _fingerprint(
        requirement,
        required_info,
        request_method,
        request_resource,
        decision_context,
        payment_required["x402Version"],
        required_payment_identifier,
    ) != required_info["request_fingerprint"]:
        raise ValueError("M5 request fingerprint mismatch")
    fingerprint = required_info["request_fingerprint"]
    issued_at = _timestamp(fingerprint["issued_at"])
    expires_at = _timestamp(fingerprint["expires_at"])
    observed = _timestamp(observed_at)
    if expires_at <= issued_at:
        raise ValueError("M5 request expiry must follow issuance")
    if (expires_at - issued_at).total_seconds() > fingerprint["max_timeout_seconds"]:
        raise ValueError("M5 request expiry exceeds maxTimeoutSeconds")
    if observed < issued_at or observed > expires_at:
        raise ValueError("M5 request is not within its validity window")

    marker = required_info["token_representation"]
    if marker["asset_code"] == requirement["asset"] or marker["settlement_eligibility"] != "NOT_A_SETTLEMENT_ASSET":
        raise ValueError("no-value project marker cannot be a settlement asset")

    authority = required_info["authority"]
    safety = required_info["execution_safety"]
    blockers = []
    if authority["credential_state"] != "CURRENT":
        blockers.append("CREDENTIAL_NOT_CURRENT")
    if authority["approval_state"] != "APPROVED":
        blockers.append("ACCOUNTABLE_APPROVAL_MISSING")
    if not authority["evidence_refs"]:
        blockers.append("AUTHORITATIVE_EVIDENCE_MISSING")
    context_authority = decision_context["account_authority"]
    for field in ("credential_state", "delegation_state", "mandate_state"):
        if context_authority[field] != "CURRENT":
            blockers.append(f"{field.upper()}_NOT_CURRENT")
    if context_authority["revocation_state"] != "NOT_REVOKED":
        blockers.append("AUTHORITY_REVOCATION_STATE_UNRESOLVED")
    if decision_context["asset_classification"]["classification_state"] != "CURRENT":
        blockers.append("ASSET_CLASSIFICATION_UNRESOLVED")
    if decision_context["external_legal_classification"]["status"] != "CURRENT":
        blockers.append("EXTERNAL_LEGAL_CLASSIFICATION_UNRESOLVED")
    if decision_context["jurisdiction_graph"]["status"] != "CURRENT":
        blockers.append("JURISDICTION_GRAPH_UNRESOLVED")
    if decision_context["institutional_route"]["status"] != "CURRENT":
        blockers.append("INSTITUTIONAL_ROUTE_UNRESOLVED")
    context_errors, context_unresolved = _decision_context_errors(
        decision_context,
        {},
        observed_at,
    )
    blockers.extend(f"DECISION_CONTEXT_INVALID: {detail}" for detail in context_errors)
    blockers.extend(f"DECISION_CONTEXT_UNRESOLVED: {detail}" for detail in context_unresolved)
    if safety["synthetic"]:
        blockers.append("SYNTHETIC_MODE")
    if not payment_payload["payload"].get("settleable", False):
        blockers.append("PAYLOAD_NOT_SETTLEABLE")
    if payment_payload["payload"].get("signature") is None:
        blockers.append("SIGNATURE_MISSING")

    payment_id = required_info["request_fingerprint"]["payment_id"]
    return {
        "simulation": "M5-X402-001-draft",
        "payment_id": payment_id,
        "request_fingerprint_digest": canonical_digest(required_info["request_fingerprint"]),
        "decision_context_digest": required_info["decision_context"]["digest"],
        "clock_source": clock_source,
        "trusted_clock": False,
        "http_status": 402,
        "decision": "HOLD",
        "verify_called": False,
        "settle_called": False,
        "network_write_performed": False,
        "financial_movement_performed": False,
        "numscript_plan": required_info["executable_plan"]["id"],
        "token_id": marker["token_id"],
        "token_valuation_status": marker["valuation_status"],
        "blockers": blockers,
    }


def simulate(
    payment_required: dict[str, Any],
    payment_payload: dict[str, Any],
    schema: dict[str, Any],
    *,
    request_method: str,
    request_resource: str,
    observed_at: str,
    clock_source: str,
) -> dict[str, Any]:
    """Fail closed with one public ValueError contract for malformed inputs."""
    try:
        return _simulate(
            payment_required,
            payment_payload,
            schema,
            request_method=request_method,
            request_resource=request_resource,
            observed_at=observed_at,
            clock_source=clock_source,
        )
    except ValueError:
        raise
    except (KeyError, IndexError, TypeError, AttributeError) as error:
        raise ValueError(f"malformed x402 input: {error}") from error


def main() -> int:
    required = json.loads((HERE / "payment-required.example.json").read_text())
    payload = json.loads((HERE / "payment-payload.example.json").read_text())
    schema = json.loads((HERE / "m5-x402-extension.schema.json").read_text())
    info = required["extensions"]["m5-ricardian"]["info"]
    print(json.dumps(simulate(
        required,
        payload,
        schema,
        request_method="POST",
        request_resource=required["resource"]["url"],
        observed_at=info["request_fingerprint"]["issued_at"],
        clock_source="FIXTURE_SIMULATION_TIME_UNTRUSTED",
    ), indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
