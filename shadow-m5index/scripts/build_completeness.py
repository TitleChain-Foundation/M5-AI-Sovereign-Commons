#!/usr/bin/env python3
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parents[2]
MOD=ROOT/"shadow-m5index"
for p in sorted((MOD/"data/canonical").glob("*/*.json")):
    d=json.loads(p.read_text())
    c=d.setdefault("research",{}).setdefault("checklist",{})
    pct=round(sum(bool(v) for v in c.values())/len(c)*100) if c else 0
    d["research"]["completion_pct"]=pct
    p.write_text(json.dumps(d,indent=2,ensure_ascii=False,default=str)+"\n")
print("Recomputed research completion.")
