#!/usr/bin/env python3
from pathlib import Path
import json
import qrcode
import qrcode.image.svg

ROOT=Path(__file__).resolve().parents[2]
MOD=ROOT/"shadow-m5index"
qrdir=MOD/"qr"; qrdir.mkdir(exist_ok=True)
rows=json.loads((MOD/"registry/asset-index.json").read_text())
existing_registry_path=MOD/"registry/qr-registry.json"
existing_registry={}
if existing_registry_path.exists():
    existing_registry={
        item["asset_id"]: item
        for item in json.loads(existing_registry_path.read_text())
    }
registry=[]
for r in rows:
    aid=r["asset_id"]; url=r["canonical_url"]
    png_path=qrdir/f"{aid}.png"; svg_path=qrdir/f"{aid}.svg"
    existing=existing_registry.get(aid)
    current=(
        existing
        and existing.get("canonical_url") == url
        and png_path.exists()
        and svg_path.exists()
    )
    if not current:
        qr=qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_M,box_size=8,border=4)
        qr.add_data(url); qr.make(fit=True)
        qr.make_image(fill_color="black",back_color="white").save(png_path)
        qrcode.make(url,image_factory=qrcode.image.svg.SvgPathImage).save(svg_path)
    registry.append({"asset_id":aid,"canonical_url":url,"qr_png":f"qr/{aid}.png","qr_svg":f"qr/{aid}.svg","status":"active"})
(MOD/"registry/qr-registry.json").write_text(json.dumps(registry,indent=2)+"\n")
print(f"Generated {len(registry)} property QRs.")
