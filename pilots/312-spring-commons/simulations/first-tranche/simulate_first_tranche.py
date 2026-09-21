#!/usr/bin/env python3
"""Offline, non-authoritative evaluator for the Spring Commons tranche fixture."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

HERE = Path(__file__).resolve().parent
DEFAULT_FIXTURE = (
    HERE.parent.parent
    / "examples"
    / "PPT-EZ-CA-0001-first-tranche-simulation.json"
)
EXTERNAL_GATES = {
    "EXTERNAL_AUTHORITY",
    "REGULATED_PROVIDER",
    "PROFESSIONAL_JUDGMENT",
    "HUMAN_FIDUCIARY",
}
ACCEPTED_EXTERNAL_STATUS = "EVIDENCED_AUTHORITY"
ACCEPTED_INTERNAL_STATUSES = {"SIMULATED_PASS", "EVIDENCED_AUTHORITY"}


def _canonical_digest(record: dict[str, Any]) -> str:
    payload = json.dumps(record, sort_keys=True, separators=(",", ":")).encode()
    return f"sha256:{hashlib.sha256(payload).hexdigest()}"


def _checkpoint_satisfied(checkpoint: dict[str, Any], evidence: dict[str, Any]) -> bool:
    status = checkpoint["status"]
    gate_type = checkpoint["gate_type"]
    if gate_type in EXTERNAL_GATES:
        if status != ACCEPTED_EXTERNAL_STATUS or not checkpoint["evidence_refs"]:
            return False
        return all(
            ref in evidence
            and evidence[ref]["authoritative"]
            and not evidence[ref]["synthetic"]
            and evidence[ref]["status"] == "CURRENT"
            for ref in checkpoint["evidence_refs"]
        )
    return status in ACCEPTED_INTERNAL_STATUSES


def evaluate(record: dict[str, Any]) -> dict[str, Any]:
    """Evaluate fixture gates without authorizing or executing any transaction."""
    safety = record["safety"]
    safe_mode = (
        safety["synthetic"] is True
        and safety["authority_effect"] == "NONE"
        and safety["network_write"] is False
        and safety["financial_movement"] is False
    )
    if not safe_mode:
        raise ValueError("Public simulation must remain synthetic and write-disabled")

    evidence = {item["evidence_id"]: item for item in record["evidence_catalog"]}
    required = [item for item in record["checkpoints"] if item["required"]]
    unresolved = [
        item["checkpoint_id"]
        for item in required
        if not _checkpoint_satisfied(item, evidence)
    ]
    decision = "HOLD" if unresolved else "READY_FOR_AUTHORIZED_HUMAN_REVIEW"

    return {
        "receipt_id": f"{record['simulation_id']}-RECEIPT",
        "receipt_version": "1.0",
        "simulation_id": record["simulation_id"],
        "project_id": record["project_id"],
        "tranche_id": record["tranche"]["tranche_id"],
        "fixture_digest": _canonical_digest(record),
        "decision": decision,
        "execution_authorized": False,
        "authority_effect": "NONE",
        "network_write_performed": False,
        "financial_movement_performed": False,
        "required_checkpoint_count": len(required),
        "satisfied_checkpoint_count": len(required) - len(unresolved),
        "unresolved_checkpoint_ids": unresolved,
        "current_state": record["state_machine"]["current_state"],
        "requested_state": record["state_machine"]["requested_state"],
        "notices": [
            "Synthetic developer demonstration only.",
            "A ready result routes evidence to authorized humans; it never approves closing, source-chain activation, escrow release, draw authorization, settlement, or legal state.",
            "Authoritative external records and executed instruments control their respective domains.",
            "Targets and modeled values are not achieved impact or investment performance.",
        ],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("fixture", nargs="?", type=Path, default=DEFAULT_FIXTURE)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    record = json.loads(args.fixture.read_text())
    receipt = evaluate(record)
    rendered = json.dumps(receipt, indent=2) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered)
    else:
        print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
