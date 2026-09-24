import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SIM = ROOT / "pilots" / "peoples-trust" / "simulations" / "nd-farmland-reference"
RECORD = SIM / "ND-FARM-SIM-001.sample.json"

def test_farmland_reference_simulation_exists():
    assert (SIM / "README.md").is_file()
    assert RECORD.is_file()

def test_farmland_reference_record_is_public_synthetic():
    record = json.loads(RECORD.read_text(encoding="utf-8"))
    assert record["simulation_id"] == "ND-FARM-SIM-001"
    assert record["status"] == "SAMPLE-DATA SIMULATION"
    privacy = record["privacy"]
    assert privacy["public_synthetic"] is True
    assert privacy["source_trust_name_published"] is False
    assert privacy["beneficial_owner_published"] is False
    assert privacy["exact_county_published"] is False
    assert privacy["exact_acreage_published"] is False
    assert privacy["exact_purchase_price_published"] is False
    assert privacy["source_operator_name_published"] is False
