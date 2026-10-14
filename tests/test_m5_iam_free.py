import hashlib
from http.server import ThreadingHTTPServer
import threading
import urllib.request
import urllib.error
import importlib.util
import json
from pathlib import Path
import zipfile

import pytest

ROOT = Path(__file__).resolve().parents[1]
GUIDE = ROOT / "m5-pod" / "iam-free"


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@pytest.fixture
def iam():
    return load("m5_iam", ROOT / "reference-implementation" / "m5-iam-free" / "m5_iam.py")


def test_init_requires_human_attestation(iam, tmp_path):
    with pytest.raises(iam.PodError):
        iam.init_pod(tmp_path / "pod", "Ada")
    assert not (tmp_path / "pod").exists()


def test_init_creates_iam_only_unverified_pod(iam, tmp_path):
    pod = tmp_path / "pod"
    record = iam.init_pod(pod, "Ada <b>", attested=True)
    assert record["account_sku"] == "M5IAM-000"
    assert record["status"] == "IAM ONLY"
    assert record["identity_status"] == "SELF_ATTESTED_NOT_VERIFIED"
    assert record["tcid"] is None and record["can_authorize"] == []
    layer = pod / "M0-M5IAM-000"
    for name in ["attestation", "identifiers", "receive", "registry", "ledger", "m5agent"]:
        assert (layer / name).is_dir()
    assert (pod / "m5readme.md").exists() and (pod / "m5agent" / "m5readme.md").exists()
    attestation = json.loads((layer / "attestation" / "human-attestation.json").read_text())
    assert attestation["verified"] is False
    identifiers = json.loads((layer / "identifiers" / "identifiers.json").read_text())
    assert identifiers["tcid"] is None and identifiers["local_id"].startswith("local-iam:")
    page = (pod / "m5-iam.html").read_text()
    assert "Ada &lt;b&gt;" in page and "http" not in page
    assert iam.verify_pod(pod)["status"] == "PASS"


def test_init_refuses_to_overwrite(iam, tmp_path):
    pod = tmp_path / "pod"
    iam.init_pod(pod, attested=True)
    with pytest.raises(iam.PodError):
        iam.init_pod(pod, attested=True)


def test_verify_detects_changed_record_and_ledger(iam, tmp_path):
    pod = tmp_path / "pod"
    iam.init_pod(pod, attested=True)
    record = pod / "M0-M5IAM-000" / "iam.json"
    record.write_text(record.read_text().replace("SELF_ATTESTED_NOT_VERIFIED", "VERIFIED"))
    result = iam.verify_pod(pod)
    assert result["status"] == "FAIL" and any("iam.json" in item for item in result["problems"])

    other = tmp_path / "other"
    iam.init_pod(other, attested=True)
    ledger = other / "M0-M5IAM-000" / "ledger" / "events.jsonl"
    lines = ledger.read_text().splitlines()
    ledger.write_text("\n".join([lines[0], *lines[2:]]) + "\n")
    assert iam.verify_pod(other)["status"] == "FAIL"


def test_export_and_cli(iam, tmp_path, capsys):
    pod = tmp_path / "pod"
    assert iam.main(["init", "--pod", str(pod)]) == 2
    assert iam.main(["init", "--pod", str(pod), "--i-am-human"]) == 0
    assert iam.main(["verify", "--pod", str(pod)]) == 0
    assert iam.main(["status", "--pod", str(pod)]) == 0
    assert iam.main(["export", "--pod", str(pod), "--output", str(tmp_path / "out.zip")]) == 0
    capsys.readouterr()
    with zipfile.ZipFile(tmp_path / "out.zip") as archive:
        assert "pod/M0-M5IAM-000/iam.json" in archive.namelist()


def test_reference_code_makes_no_network_calls():
    source = (ROOT / "reference-implementation" / "m5-iam-free" / "m5_iam.py").read_text()
    for banned in ["urllib", "http.client", "socket", "requests", "subprocess"]:
        assert banned not in source, banned


def test_manifest_declares_free_unverified_starter():
    manifest = json.loads((GUIDE / "m5iam-package.manifest.json").read_text(encoding="utf-8"))
    assert manifest["license_state"] == "UNREGISTERED_COMMONS_STARTER"
    assert manifest["account"]["price"] == "FREE"
    assert manifest["account"]["identity_status_after_init"] == "SELF_ATTESTED_NOT_VERIFIED"
    assert manifest["runtime"]["network_required"] is False
    text = (GUIDE / "M5IAM-FREE-PACKAGE.md").read_text(encoding="utf-8")
    assert "not a verified identity" in text


def test_package_builds_deterministically_and_runs_from_the_zip(tmp_path):
    builder = load("build_iam_package", ROOT / "tools" / "build_iam_package.py")
    first = builder.build(tmp_path / "a")
    second = builder.build(tmp_path / "b")
    assert first.read_bytes() == second.read_bytes()
    with zipfile.ZipFile(first) as archive:
        base = first.stem + "/"
        files = {name[len(base):]: archive.read(name) for name in archive.namelist()}
        archive.extractall(tmp_path / "unzipped")
    for required in ["START-HERE.md", "PACKAGE-CHECKSUMS.sha256", "LICENSE.md",
                     "m5-pod/iam-free/M5IAM-FREE-PACKAGE.md",
                     "m5-pod/iam-free/m5iam-package.manifest.json",
                     "reference-implementation/m5-iam-free/m5_iam.py"]:
        assert required in files, required
    for line in files["PACKAGE-CHECKSUMS.sha256"].decode().splitlines():
        digest, name = line.split("  ", 1)
        assert hashlib.sha256(files[name]).hexdigest() == digest, name
    packaged = load("packaged_m5_iam", tmp_path / "unzipped" / first.stem
                    / "reference-implementation" / "m5-iam-free" / "m5_iam.py")
    packaged.init_pod(tmp_path / "pod", attested=True)
    assert packaged.verify_pod(tmp_path / "pod")["status"] == "PASS"


IMPL = ROOT / "reference-implementation" / "m5-iam-free"


def test_attestation_has_three_matching_parts(iam, tmp_path):
    pod = tmp_path / "pod"
    iam.init_pod(pod, "Ada", attested=True, chain="wyomingchain.eth")
    folder = pod / "M0-M5IAM-000" / "attestation"
    terms = (folder / "human-terms.md").read_text()
    machine = json.loads((folder / "human-attestation.json").read_text())
    check = json.loads((folder / "executable-check.json").read_text())
    assert "I, Ada, state that I am a living human being" in terms and "wyomingchain.eth" in terms
    assert machine["human_terms_sha256"] == hashlib.sha256(terms.encode()).hexdigest()
    assert machine["executable_check_sha256"] == hashlib.sha256((folder / "executable-check.json").read_bytes()).hexdigest()
    assert machine["contract_id"] == check["contract_id"]
    assert machine["authority_effect"] == check["authority_effect"] == "NONE"
    assert machine["chain"]["status"] == "SELF_SELECTED_NOT_VERIFIED"
    assert iam.verify_pod(pod)["files_checked"] == 6
    receipt = json.loads((pod / "M0-M5IAM-000" / "registry" / "registry-receipt.json").read_text())
    assert receipt["status"] == "SIMULATED_NOT_ANCHORED" and receipt["anchored"] is False and receipt["network_write"] is False
    assert receipt["ref_id"] == "TCR-IAM-" + receipt["commitment_sha256"][:12].upper()


def test_catalog_lists_fifty_chains_free_products_and_unactivated_accounts():
    catalog = json.loads((IMPL / "iam-catalog.json").read_text())
    chains = [c["chain"] for c in catalog["chains"]]
    assert len(chains) == len(set(chains)) == 50
    assert "michiganstatechain.eth" in chains and "georgiastatechain.eth" in chains
    for group in catalog["products"]:
        for item in group["items"]:
            assert item["url"].startswith("https://") and item["license"]
    assert [a["tier"] for a in catalog["accounts"]] == ["M1", "M2", "M3", "M4", "M5"]


def test_app_accepts_the_form_only_from_its_own_page(tmp_path):
    app = load("m5_iam_app", IMPL / "m5_iam_app.py")
    assert app.HOST == "127.0.0.1"
    for banned in ["urllib", "http.client", "requests", "subprocess"]:
        assert banned not in (IMPL / "m5_iam_app.py").read_text(), banned
    server = ThreadingHTTPServer(("127.0.0.1", 0), app.Handler)
    app.Handler.pod, app.Handler.port = tmp_path / "pod", server.server_address[1]
    threading.Thread(target=server.serve_forever, daemon=True).start()
    base = f"http://127.0.0.1:{app.Handler.port}"

    def post(body, origin=base, kind="application/json"):
        headers = {"Content-Type": kind}
        if origin:
            headers["Origin"] = origin
        request = urllib.request.Request(base + "/api/attest", data=json.dumps(body).encode(), headers=headers, method="POST")
        try:
            with urllib.request.urlopen(request) as response:
                return response.status, json.loads(response.read())
        except urllib.error.HTTPError as error:
            return error.code, None

    try:
        good = {"name": "Ada", "chain": "wyomingchain.eth", "attest": True}
        assert post(good, origin=None)[0] == 403
        assert post(good, origin="https://example.com")[0] == 403
        assert post(good, kind="text/plain")[0] == 403
        assert post({**good, "attest": "yes"})[0] == 409
        assert post({**good, "chain": "nowherechain.eth"})[0] == 409
        assert not (tmp_path / "pod").exists()
        status, state = post(good)
        assert status == 200 and state["record"]["status"] == "IAM ONLY" and state["check"]["status"] == "PASS"
        assert post(good)[0] == 409
    finally:
        server.shutdown()


def test_package_ships_the_app_and_an_executable_launcher(tmp_path):
    builder = load("build_iam_package_app", ROOT / "tools" / "build_iam_package.py")
    path = builder.build(tmp_path / "out")
    with zipfile.ZipFile(path) as archive:
        base = path.stem + "/reference-implementation/m5-iam-free/"
        names = archive.namelist()
        for required in ["app.html", "m5_iam_app.py", "iam-catalog.json", "Start M5 IAM.command", "Start M5 IAM.bat"]:
            assert base + required in names, required
        assert (archive.getinfo(base + "Start M5 IAM.command").external_attr >> 16) & 0o111


def test_demonstration_reproduces_the_published_digests():
    demo = load("reproduce", IMPL / "demo" / "reproduce.py")
    assert demo.main([]) == 0
