#!/usr/bin/env python3
"""Review helper only. This script never auto-promotes a public submission to CANONICAL."""
from pathlib import Path
import json, sys, hashlib, datetime

if len(sys.argv) != 2:
    raise SystemExit("usage: promote_submission.py submission.json")
p=Path(sys.argv[1])
d=json.loads(p.read_text())
d["reviewed_at"]=datetime.datetime.now(datetime.timezone.utc).isoformat()
d["review_state"]="REVIEW_REQUIRED"
print(json.dumps(d,indent=2))
