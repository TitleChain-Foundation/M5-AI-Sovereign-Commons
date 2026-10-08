import hashlib
import importlib.util
import json
from pathlib import Path
import zipfile

ROOT = Path(__file__).resolve().parents[1]
PILOT = ROOT / "pilots" / "norton-ranch-blueprint"


def load_builder():
    spec = importlib.util.spec_from_file_location("build_norton_package", ROOT / "tools" / "build_norton_package.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_manifest_declares_unregistered_state_and_activation_steps():
    manifest = json.loads((PILOT / "m5pod-package.manifest.json").read_text(encoding="utf-8"))
    assert manifest["license_state"] == "UNREGISTERED_COMMONS_STARTER"
    assert "not create a licensed M5POD" in manifest["license_state_notice"]
    assert [step["step"] for step in manifest["activation_required"]] == [1, 2, 3, 4, 5]
    assert manifest["runtime"]["network_required"] is False
    assert manifest["runtime"]["packaged_desktop_installer"] is False


def test_package_builds_deterministically_with_valid_checksums(tmp_path):
    builder = load_builder()
    first = builder.build(tmp_path / "a")
    second = builder.build(tmp_path / "b")
    assert first.read_bytes() == second.read_bytes()
    with zipfile.ZipFile(first) as archive:
        base = first.stem + "/"
        names = archive.namelist()
        assert all(name.startswith(base) for name in names)
        files = {name[len(base):]: archive.read(name) for name in names}
    for required in [
        "START-HERE.md",
        "PACKAGE-CHECKSUMS.sha256",
        "pilots/norton-ranch-blueprint/README.md",
        "pilots/norton-ranch-blueprint/M5POD-PACKAGE.md",
        "pilots/norton-ranch-blueprint/m5pod-package.manifest.json",
        "reference-implementation/sovereign-herd/provision_herd.py",
        "schemas/m5-biological-stewardship-record.schema.json",
        "LICENSE.md",
    ]:
        assert required in files, required
    assert b"not a licensed M5POD" in files["START-HERE.md"]
    for line in files["PACKAGE-CHECKSUMS.sha256"].decode().splitlines():
        digest, name = line.split("  ", 1)
        assert hashlib.sha256(files[name]).hexdigest() == digest, name


def test_package_guide_states_license_boundary_and_act_status():
    text = (PILOT / "M5POD-PACKAGE.md").read_text(encoding="utf-8")
    assert "not a licensed M5POD until you register and activate" in text
    assert "not enacted" in text
