#!/usr/bin/env python3
"""Local-only Sovereign Herd manifest provisioner.

Synthetic/reference utility. No network calls.
"""
from __future__ import annotations

import argparse
import json
import uuid
from datetime import datetime, timezone
from pathlib import Path


NAMESPACE = uuid.UUID("6ed58b77-c15b-4d43-b735-6c4729c1f2cb")


def stable_ref(prefix: str, *parts: str) -> str:
    material = "|".join(parts)
    return f"{prefix}:{uuid.uuid5(NAMESPACE, material)}"


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def build(entity_ref: str, farm_ref: str, rows: list[dict]) -> dict:
    animals = []
    devices = {}
    assignments = []

    for row in rows:
        local_id = str(row["local_id"]).strip()
        animal_ref = stable_ref("m5animal", entity_ref, farm_ref, local_id)

        animal = {
            "schema_version": "0.1",
            "animal_ref": animal_ref,
            "entity_ref": entity_ref,
            "farm_ref": farm_ref,
            "species": row.get("species", "Bos taurus"),
            "local_id": local_id,
            "sex": row.get("sex", "unknown"),
            "birth_date": row.get("birth_date"),
            "record_state": "active",
        }
        animals.append({k: v for k, v in animal.items() if v is not None})

        serial = row.get("device_serial")
        if serial:
            serial = str(serial).strip()
            device_ref = stable_ref("m5device", entity_ref, serial)
            devices[device_ref] = {
                "schema_version": "0.1",
                "device_ref": device_ref,
                "serial": serial,
                "status": "assigned",
                "capabilities": ["passive-monitoring"],
            }
            assignments.append({
                "schema_version": "0.1",
                "assignment_ref": stable_ref("m5assign", entity_ref, animal_ref, device_ref),
                "entity_ref": entity_ref,
                "animal_ref": animal_ref,
                "device_ref": device_ref,
                "assigned_at": utc_now(),
                "authority_ref": "LOCAL-OPERATOR-AUTHORITY-REQUIRED",
                "reason": "Initial manifest provisioning",
            })

    return {
        "schema_version": "0.1",
        "generated_at": utc_now(),
        "entity_ref": entity_ref,
        "farm_ref": farm_ref,
        "animals": animals,
        "devices": list(devices.values()),
        "assignments": assignments,
        "privacy_notice": "Reference manifest only. Keep real farm data in an authorized private environment.",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--entity", required=True)
    parser.add_argument("--farm", required=True)
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()

    rows = json.loads(args.input.read_text(encoding="utf-8"))
    if not isinstance(rows, list):
        raise SystemExit("Input must be a JSON array.")

    output = build(args.entity, args.farm, rows)
    args.output.write_text(json.dumps(output, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {args.output} with {len(output['animals'])} animals, "
          f"{len(output['devices'])} devices and {len(output['assignments'])} assignments.")


if __name__ == "__main__":
    main()
