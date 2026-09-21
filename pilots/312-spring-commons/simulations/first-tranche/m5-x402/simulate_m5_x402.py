#!/usr/bin/env python3
"""Validate a synthetic M5-x402 exchange without verifying or settling payment."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator

HERE = Path(__file__).resolve().parent


def _canonical(value: Any) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":")).encode()


def _fingerprint(requirement: dict[str, Any], info: dict[str, Any]) -> dict[str, Any]:
    declared = info["request_fingerprint"]
    return {
        "payment_id": declared["payment_id"],
        "http_method": declared["http_method"],
        "resource": declared["resource"],
        "scheme": requirement["scheme"],
        "network": requirement["network"],
        "asset": requirement["asset"],
        "amount": requirement["amount"],
        "pay_to": requirement["payTo"],
        "operation_id": declared["operation_id"],
    }


def simulate(payment_required: dict[str, Any], payment_payload: dict[str, Any], schema: dict[str, Any]) -> dict[str, Any]:
    """Model the x402 retry and M5 pre-settlement gates in public dry-run mode."""
    required_extension = payment_required["extensions"]["m5-ricardian"]
    payload_extension = payment_payload["extensions"]["m5-ricardian"]
    validator = Draft202012Validator(schema)
    validator.validate(required_extension)
    validator.validate(payload_extension)

    requirement = payment_required["accepts"][0]
    accepted = payment_payload["accepted"]
    core_fields = ("scheme", "network", "amount", "asset", "payTo", "maxTimeoutSeconds")
    if any(requirement[field] != accepted[field] for field in core_fields):
        raise ValueError("x402 accepted terms do not match PaymentRequired")

    required_info = required_extension["info"]
    payload_info = payload_extension["info"]
    if required_info != payload_info:
        raise ValueError("M5 Ricardian extension echo mismatch")
    if _fingerprint(requirement, required_info) != required_info["request_fingerprint"]:
        raise ValueError("M5 request fingerprint mismatch")

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
        "request_fingerprint_digest": "sha256:" + hashlib.sha256(
            _canonical(required_info["request_fingerprint"])
        ).hexdigest(),
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


def main() -> int:
    required = json.loads((HERE / "payment-required.example.json").read_text())
    payload = json.loads((HERE / "payment-payload.example.json").read_text())
    schema = json.loads((HERE / "m5-x402-extension.schema.json").read_text())
    print(json.dumps(simulate(required, payload, schema), indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
