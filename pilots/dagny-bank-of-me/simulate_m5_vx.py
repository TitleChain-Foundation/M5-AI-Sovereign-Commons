#!/usr/bin/env python3
"""Emit deterministic, write-disabled M5-VX receipts for the Dagny demo."""

from __future__ import annotations

import argparse
import hashlib
import json
from decimal import ROUND_HALF_UP, Decimal
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator, FormatChecker

HERE = Path(__file__).resolve().parent
DEFAULT_FIXTURE = HERE / "examples" / "dagny-mixed-value-exchange.json"
FIXTURE_SCHEMA = HERE / "schemas" / "m5-vx-demo.schema.json"
RECEIPT_SCHEMA = HERE / "schemas" / "m5-value-receipt-bundle.schema.json"


def canonical_digest(value: Any) -> str:
    encoded = json.dumps(
        value,
        ensure_ascii=False,
        separators=(",", ":"),
        sort_keys=True,
    ).encode()
    return f"sha256:{hashlib.sha256(encoded).hexdigest()}"


def load_json(path: Path) -> Any:
    return json.loads(path.read_text())


def validate(record: Any, schema_path: Path, label: str) -> None:
    schema = load_json(schema_path)
    Draft202012Validator.check_schema(schema)
    errors = sorted(
        Draft202012Validator(
            schema,
            format_checker=FormatChecker(),
        ).iter_errors(record),
        key=lambda error: list(error.absolute_path),
    )
    if errors:
        details = "; ".join(
            f"{'.'.join(str(part) for part in error.absolute_path) or '$'}: {error.message}"
            for error in errors
        )
        raise ValueError(f"{label} validation failed: {details}")


def money(amount: Decimal, currency: str) -> dict[str, str]:
    return {"amount": f"{amount:.2f}", "currency": currency}


def simulate(record: dict[str, Any]) -> dict[str, Any]:
    validate(record, FIXTURE_SCHEMA, "fixture")
    currency = record["agreed_total"]["currency"]
    agreed_total = Decimal(record["agreed_total"]["amount"])
    leg_total = sum(
        (Decimal(leg["agreed_value"]["amount"]) for leg in record["legs"]),
        Decimal("0"),
    )
    if any(leg["agreed_value"]["currency"] != currency for leg in record["legs"]):
        raise ValueError("all leg valuation currencies must match the agreed total")
    if leg_total != agreed_total:
        raise ValueError(
            f"leg total {leg_total:.2f} does not equal agreed total {agreed_total:.2f}"
        )
    leg_ids = [leg["leg_id"] for leg in record["legs"]]
    if len(leg_ids) != len(set(leg_ids)):
        raise ValueError("leg identifiers must be unique")
    exchange_parties = {record["provider_tcid"], record["receiver_tcid"]}
    if len(exchange_parties) != 2:
        raise ValueError("exchange parties must be distinct")
    for leg in record["legs"]:
        if {leg["from_tcid"], leg["to_tcid"]} != exchange_parties:
            raise ValueError(
                f"{leg['leg_id']} counterparties must match the exchange parties"
            )

    receipts = []
    for leg in record["legs"]:
        settlement_type = leg["settlement_type"]
        fee_components = leg.get("digital_terms", {}).get(
            "transaction_fee_components", []
        )
        if any(item["applied"] and item["bps"] is None for item in fee_components):
            raise ValueError(
                f"{leg['leg_id']} applied fee components require a numeric bps rate"
            )
        total_fee_bps = sum(
            item["bps"] for item in fee_components if item["applied"]
        )
        if total_fee_bps > 10000:
            raise ValueError(f"{leg['leg_id']} applied fees exceed 10000 bps")
        outcome = (
            leg["digital_terms"]["x402_result"]
            if settlement_type == "DIGITAL"
            else "SIMULATED_ACKNOWLEDGEMENT_ONLY"
        )
        payload = {
            "receipt_id": f"M5VR-{record['simulation_id']}-{leg['leg_id']}",
            "event_id": f"M5VX-EVENT-{leg['leg_id']}",
            "exchange_id": record["exchange_id"],
            "provider_tcid": leg["from_tcid"],
            "receiver_tcid": leg["to_tcid"],
            "resource_type": record["resource"]["resource_type"],
            "settlement_type": settlement_type,
            "exchange_resource_reference": record["resource"]["resource_reference"],
            "resource_reference": leg["resource_reference"],
            "quantity": leg["quantity"],
            "agreed_value": f"{Decimal(leg['agreed_value']['amount']):.2f}",
            "valuation_currency": leg["agreed_value"]["currency"],
            "evidence_refs": [
                canonical_digest(reference)
                for reference in leg["evidence"]["private_refs"]
            ],
            "credential_context": leg["credential_context"],
            "jurisdiction_context": leg["jurisdiction_context"],
            "policy_context": leg["policy_context"],
            "provider_attestation": leg["acknowledgement"]["provider"],
            "receiver_attestation": leg["acknowledgement"]["receiver"],
            "created_at": record["created_at"],
            "accepted_at": record["created_at"],
            "m5pod_record_ref": f"m5pod:target:{leg['leg_id']}",
            "titlechain_reference": (
                f"titlechain:target:{leg['leg_id']}"
                if settlement_type == "ASSET"
                else None
            ),
            "state": "PROPOSED",
            "simulation_outcome": outcome,
        }
        if settlement_type == "DIGITAL":
            gross = Decimal(leg["agreed_value"]["amount"])
            fee = (
                gross * Decimal(total_fee_bps) / Decimal(10000)
            ).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
            net = gross - fee
            if fee + net != gross:
                raise ValueError(f"{leg['leg_id']} fee reconciliation failed")
            payload["digital_settlement_terms"] = {
                "payment_wrapper": leg["digital_terms"]["payment_wrapper"],
                "m5_extension": leg["digital_terms"]["m5_extension"],
                "adapter": leg["digital_terms"]["adapter"],
                "provider_candidate": leg["digital_terms"]["provider_candidate"],
                "provider_status": leg["digital_terms"]["provider_status"],
                "settlement_asset": leg["digital_terms"]["settlement_asset"],
                "fx_quote": leg["digital_terms"]["fx_quote"],
                "transaction_fee_components": fee_components,
                "allocation_basis": leg["digital_terms"]["allocation_basis"],
                "allocation_route": leg["digital_terms"]["allocation_route"],
                "total_fee_bps": total_fee_bps,
                "gross_amount": money(gross, currency),
                "fee_amount": money(fee, currency),
                "net_amount": money(net, currency),
            }
        payload["receipt_hash"] = canonical_digest(payload)
        receipts.append(payload)

    bundle = {
        "schema_version": "0.1-draft",
        "receipt_class": "PUBLIC_SYNTHETIC_NON_AUTHORITATIVE",
        "simulation_id": record["simulation_id"],
        "exchange_id": record["exchange_id"],
        "provider_tcid": record["provider_tcid"],
        "receiver_tcid": record["receiver_tcid"],
        "execution_safety": record["execution_safety"],
        "exchange_resource": record["resource"],
        "agreed_total": money(agreed_total, currency),
        "leg_total": money(leg_total, currency),
        "consideration_reconciled": True,
        "receipts": receipts,
        "notices": [
            "SIMULATION — NO VALUE OR AUTHORITY MOVED.",
            "CASH evidence does not tokenize physical currency.",
            "ASSET and SERVICE values are party-agreed, not M5 appraisals.",
            "The DIGITAL leg stops at 402 HOLD before any provider call.",
            "Community and jurisdiction destinations are not hidden swap fees or automatic deductions from principal.",
        ],
    }
    bundle["bundle_hash"] = canonical_digest(bundle)
    validate(bundle, RECEIPT_SCHEMA, "receipt bundle")
    verify_bundle(bundle)
    return bundle


def verify_bundle(bundle: dict[str, Any]) -> None:
    validate(bundle, RECEIPT_SCHEMA, "receipt bundle")
    currency = bundle["agreed_total"]["currency"]
    agreed_total = Decimal(bundle["agreed_total"]["amount"])
    leg_total = sum(
        (Decimal(receipt["agreed_value"]) for receipt in bundle["receipts"]),
        Decimal("0"),
    )
    if any(receipt["valuation_currency"] != currency for receipt in bundle["receipts"]):
        raise ValueError("receipt valuation currencies must match the agreed total")
    if leg_total != agreed_total or Decimal(bundle["leg_total"]["amount"]) != leg_total:
        raise ValueError("receipt consideration does not reconcile to the agreed total")
    for receipt in bundle["receipts"]:
        claimed_hash = receipt["receipt_hash"]
        preimage = {key: value for key, value in receipt.items() if key != "receipt_hash"}
        if canonical_digest(preimage) != claimed_hash:
            raise ValueError(f"{receipt['receipt_id']} hash mismatch")
    claimed_bundle_hash = bundle["bundle_hash"]
    bundle_preimage = {
        key: value for key, value in bundle.items() if key != "bundle_hash"
    }
    if canonical_digest(bundle_preimage) != claimed_bundle_hash:
        raise ValueError("bundle hash mismatch")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--fixture", type=Path, default=DEFAULT_FIXTURE)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--verify", type=Path)
    args = parser.parse_args()
    if args.verify:
        verify_bundle(load_json(args.verify))
        print(f"Verified {args.verify}")
        return 0
    bundle = simulate(load_json(args.fixture))
    rendered = json.dumps(bundle, indent=2) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered)
    else:
        print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
