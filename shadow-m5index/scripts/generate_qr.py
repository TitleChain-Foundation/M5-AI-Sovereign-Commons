#!/usr/bin/env python3
from pathlib import Path
import json
import qrcode
import qrcode.image.svg

ROOT=Path(__file__).resolve().parents[2]
MOD=ROOT/"shadow-m5index"
qrdir=MOD/"qr"; qrdir.mkdir(exist_ok=True)
rows=json.loads((MOD/"registry/asset-index.json").read_text())
registry=[]
for r in rows:
    aid=r["asset_id"]; url=r["canonical_url"]
    qr=qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_M,box_size=8,border=4)
    qr.add_data(url); qr.make(fit=True)
    qr.make_image(fill_color="black",back_color="white").save(qrdir/f"{aid}.png")
    qrcode.make(url,image_factory=qrcode.image.svg.SvgPathImage).save(qrdir/f"{aid}.svg")
    registry.append({"asset_id":aid,"canonical_url":url,"qr_png":f"qr/{aid}.png","qr_svg":f"qr/{aid}.svg","status":"active"})
(MOD/"registry/qr-registry.json").write_text(json.dumps(registry,indent=2)+"\n")
print(f"Generated {len(registry)} property QRs.")
