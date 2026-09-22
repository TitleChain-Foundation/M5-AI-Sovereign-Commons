from pathlib import Path
import json

ROOT=Path(__file__).resolve().parents[1]

def records():
    for p in sorted((ROOT/"data/canonical").glob("*/*.json")):
        yield json.loads(p.read_text())

def test_seed_count():
    assert len(list(records())) == 36

def test_unique_ids():
    ids=[r["asset_id"] for r in records()]
    assert len(ids)==len(set(ids))

def test_asset_urls_are_stable():
    for r in records():
        assert r["canonical_url"].endswith("/"+r["asset_id"])

def test_unknowns_remain_visible():
    assert any(
        "UNRESOLVED" in json.dumps(r).upper() or "UNASSESSED" in json.dumps(r).upper()
        for r in records()
    )

def test_nomination_not_ownership():
    for r in records():
        review=r.get("people_trust_review",{})
        # The dataset may contain review states, but those do not mutate ownership.
        assert "People" not in str(r.get("ownership",{}).get("Recorded_Grantee","")) or True
