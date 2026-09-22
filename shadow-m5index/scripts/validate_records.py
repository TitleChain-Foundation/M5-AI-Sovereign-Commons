#!/usr/bin/env python3
from pathlib import Path
import json, sys
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[2]
MOD = ROOT / "shadow-m5index"
schema = json.loads((MOD/"schemas/asset.schema.json").read_text())
validator = Draft202012Validator(schema)

paths = sorted((MOD/"data/canonical").glob("*/*.json"))
seen=set()
errors=[]
for path in paths:
    data=json.loads(path.read_text())
    aid=data.get("asset_id")
    if aid in seen:
        errors.append(f"duplicate asset_id: {aid}")
    seen.add(aid)
    for e in validator.iter_errors(data):
        errors.append(f"{path}: {e.message}")
    if data.get("research",{}).get("evidence_state") == "CANONICAL" and not data.get("evidence"):
        errors.append(f"{aid}: canonical evidence state without evidence entries")
    text=json.dumps(data).lower()
    for forbidden in ["social_security_number","ssn","personal_account_number","password"]:
        if forbidden in text:
            errors.append(f"{aid}: private-field token detected: {forbidden}")

if errors:
    print("\n".join(errors))
    sys.exit(1)
print(f"Validated {len(paths)} SHADOW asset records.")
