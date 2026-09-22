#!/usr/bin/env python3
from pathlib import Path
import json, csv

ROOT=Path(__file__).resolve().parents[2]
MOD=ROOT/"shadow-m5index"
records=[]
for p in sorted((MOD/"data/canonical").glob("*/*.json")):
    records.append(json.loads(p.read_text()))

rows=[]
for r in records:
    rows.append({
        "asset_id":r["asset_id"],"name":r["identity"].get("name"),
        "city":r["identity"].get("city"),"state":r["identity"].get("state"),
        "primary_sector":r["primary_sector"],"sector_tags":";".join(r["sector_tags"]),
        "disposition_state":r.get("disposition",{}).get("Disposition_State"),
        "transaction_proof_state":r.get("disposition",{}).get("Transaction_Proof_State"),
        "consideration_usd":r.get("disposition",{}).get("Consideration_USD"),
        "research_priority":r.get("research",{}).get("research_priority"),
        "evidence_state":r.get("research",{}).get("evidence_state"),
        "completion_pct":r.get("research",{}).get("completion_pct"),
        "canonical_url":r["canonical_url"],
    })
reg=MOD/"registry"; reg.mkdir(exist_ok=True)
(reg/"asset-index.json").write_text(json.dumps(rows,indent=2,ensure_ascii=False,default=str)+"\n")
with (reg/"assets.jsonl").open("w",encoding="utf-8") as f:
    for r in records: f.write(json.dumps(r,ensure_ascii=False,default=str)+"\n")
with (reg/"asset-index.csv").open("w",newline="",encoding="utf-8") as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)

for sector in ["government","cre","farmland"]:
    out=MOD/"public"/sector; out.mkdir(parents=True,exist_ok=True)
    items=[x for x in rows if sector in x["sector_tags"].split(";")]
    (out/"index.json").write_text(json.dumps(items,indent=2,ensure_ascii=False,default=str)+"\n")
print(f"Built indexes for {len(records)} assets.")
