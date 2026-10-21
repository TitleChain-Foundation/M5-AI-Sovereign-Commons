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
    record = iam.init_pod(pod, "Ada <b>", attested=True, accept_cyrus=True)
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
    iam.init_pod(pod, attested=True, accept_cyrus=True)
    with pytest.raises(iam.PodError):
        iam.init_pod(pod, attested=True, accept_cyrus=True)


def test_verify_detects_changed_record_and_ledger(iam, tmp_path):
    pod = tmp_path / "pod"
    iam.init_pod(pod, attested=True, accept_cyrus=True)
    record = pod / "M0-M5IAM-000" / "iam.json"
    record.write_text(record.read_text().replace("SELF_ATTESTED_NOT_VERIFIED", "VERIFIED"))
    result = iam.verify_pod(pod)
    assert result["status"] == "FAIL" and any("iam.json" in item for item in result["problems"])

    other = tmp_path / "other"
    iam.init_pod(other, attested=True, accept_cyrus=True)
    ledger = other / "M0-M5IAM-000" / "ledger" / "events.jsonl"
    lines = ledger.read_text().splitlines()
    ledger.write_text("\n".join([lines[0], *lines[2:]]) + "\n")
    assert iam.verify_pod(other)["status"] == "FAIL"


def test_export_and_cli(iam, tmp_path, capsys):
    pod = tmp_path / "pod"
    assert iam.main(["init", "--pod", str(pod)]) == 2
    assert iam.main(["init", "--pod", str(pod), "--i-am-human", "--accept-cyrus"]) == 0
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
    packaged.init_pod(tmp_path / "pod", attested=True, accept_cyrus=True)
    assert packaged.verify_pod(tmp_path / "pod")["status"] == "PASS"


IMPL = ROOT / "reference-implementation" / "m5-iam-free"


def test_attestation_has_three_matching_parts(iam, tmp_path):
    pod = tmp_path / "pod"
    iam.init_pod(pod, "Ada", attested=True, accept_cyrus=True, chain="wyomingchain.eth")
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
    assert machine["signatures"] == [] and machine["signature_slots"]["holder"] == "RESERVED_NOT_SIGNED"
    assert machine["signature_slots"]["approving_agency"] == "RESERVED_NOT_SIGNED"
    assert iam.verify_pod(pod)["files_checked"] == 8  # includes consent/consent.json
    cert = json.loads((pod / "M0-M5IAM-000" / "registry" / "certificate-iam-origin.json").read_text())
    assert cert["status"] == "SAMPLE_NOT_ISSUED" and cert["sample"] is True and cert["issued_by"] is None
    receipt = json.loads((pod / "M0-M5IAM-000" / "registry" / "registry-receipt.json").read_text())
    assert receipt["status"] == "SIMULATED_NOT_ANCHORED" and receipt["anchored"] is False and receipt["network_write"] is False
    assert receipt["ref_id"] == "TCR-IAM-" + receipt["commitment_sha256"][:12].upper()
    assert cert["title_no"] == receipt["ref_id"]
    assert cert["registry_commitment_sha256"] == receipt["commitment_sha256"]


def test_catalog_lists_fifty_chains_free_products_and_unactivated_accounts():
    catalog = json.loads((IMPL / "iam-catalog.json").read_text())
    chains = [c["chain"] for c in catalog["chains"]]
    assert len(chains) == len(set(chains)) == 50
    assert "michiganstatechain.eth" in chains and "georgiastatechain.eth" in chains
    for group in catalog["products"]:
        for item in group["items"]:
            assert item["url"].startswith("https://") and item["license"]
    assert [a["tier"] for a in catalog["accounts"]] == ["M1", "M2", "M3", "M4", "M5"]
    assert [p["name"] for p in catalog["protocols"]["items"]] == ["M5-x401", "M5-x402", "M5-OpenAPI", "M5Scan", "M5Index", "M5Pay", "CYRUS Protocol", "TitleChain Registry"]


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
        good = {"name": "Ada", "chain": "wyomingchain.eth", "attest": True, "accept_cyrus": True}
        assert post(good, origin=None)[0] == 403
        assert post(good, origin="https://example.com")[0] == 403
        assert post(good, kind="text/plain")[0] == 403
        assert post({**good, "attest": "yes"})[0] == 409
        assert post({**good, "chain": "nowherechain.eth"})[0] == 409
        assert not (tmp_path / "pod").exists()
        status, state = post(good)
        assert status == 200 and state["record"]["status"] == "IAM ONLY" and state["check"]["status"] == "PASS"
        assert state["consent"]["cyrus_protocol"]["status"] == "ACCEPTED"
        assert state["consent"]["right_to_refuse"]["status"] == "NOT_SELECTED"
        assert post(good)[0] == 409

        def consent(body, origin=base):
            request = urllib.request.Request(base + "/api/consent", data=json.dumps(body).encode(),
                                             headers={"Content-Type": "application/json", "Origin": origin}, method="POST")
            try:
                with urllib.request.urlopen(request) as response:
                    return response.status, json.loads(response.read())
            except urllib.error.HTTPError as error:
                return error.code, None

        assert consent({"right_to_refuse": True}, origin="https://example.com")[0] == 403
        status, state = consent({"right_to_refuse": True})
        assert status == 200 and state["consent"]["right_to_refuse"]["status"] == "SELECTED_NOT_ACTIVATED"
        assert state["consent"]["right_to_refuse"]["activated"] is False
        assert state["check"]["status"] == "PASS"
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


def test_cyrus_protocol_is_required_and_refusal_is_selected_not_activated(iam, tmp_path):
    with pytest.raises(iam.PodError):
        iam.init_pod(tmp_path / "no-cyrus", "Ada", attested=True)
    assert not (tmp_path / "no-cyrus").exists()
    pod = tmp_path / "pod"
    iam.init_pod(pod, "Ada", attested=True, accept_cyrus=True)
    consent = iam.load_consent(pod)
    assert consent["cyrus_protocol"]["status"] == "ACCEPTED" and consent["cyrus_protocol"]["required"] is True
    assert "No slavery, servitude or forced labour" in consent["cyrus_protocol"]["basic_rights"]
    assert consent["cyrus_protocol"]["sovereign_rights"] == ["Identity", "Data", "Privacy", "Self-determination", "Portability"]
    assert consent["right_to_refuse"] == {**consent["right_to_refuse"], "selected": False, "status": "NOT_SELECTED", "activated": False}
    terms = (pod / iam.LAYER / "attestation" / "human-terms.md").read_text()
    assert "I accept the CYRUS Protocol" in terms and "activates only when my credentials are verified" in terms

    changed = iam.set_refusal(pod, True)
    assert changed["right_to_refuse"]["status"] == "SELECTED_NOT_ACTIVATED" and changed["right_to_refuse"]["activated"] is False
    assert len(changed["history"]) == 2
    events = iam.read_events(pod / iam.LAYER)
    assert [e["type"] for e in events if e["path"] == "consent/consent.json"] == ["CONSENT_RECORDED", "REFUSAL_SELECTED"]
    assert iam.verify_pod(pod)["status"] == "PASS"
    (pod / iam.LAYER / "consent" / "consent.json").write_text("{}")
    assert iam.verify_pod(pod)["status"] == "FAIL"


def test_certificate_states_protocol_commons_licences_and_usage(iam, tmp_path, capsys):
    pod = tmp_path / "pod"
    assert iam.main(["init", "--pod", str(pod), "--i-am-human", "--accept-cyrus", "--select-refusal"]) == 0
    cert = json.loads((pod / iam.LAYER / "registry" / "certificate-iam-origin.json").read_text())
    assert cert["cyrus_protocol"]["status"] == "ACCEPTED"
    assert cert["right_to_refuse"]["status"] == "SELECTED_NOT_ACTIVATED"
    assert cert["commons"]["software_license"] == "Apache-2.0" and cert["commons"]["standard_license"] == "CC-BY-4.0"
    assert cert["usage"]["can_authorize"] == [] and cert["status"] == "SAMPLE_NOT_ISSUED"
    capsys.readouterr()
    assert iam.main(["consent", "--pod", str(pod), "--right-to-refuse", "unselect"]) == 0
    assert json.loads(capsys.readouterr().out) == {"cyrus_protocol": "ACCEPTED", "right_to_refuse": "NOT_SELECTED"}
    assert iam.verify_pod(pod)["status"] == "PASS"


def test_starter_kit_lists_m5_tools_with_licences_and_official_sources():
    kit = json.loads((IMPL / "iam-catalog.json").read_text())["starter_kit"]
    ids = [tool["id"] for tool in kit["tools"]]
    assert len(ids) == len(set(ids)) == 7
    for tool in kit["tools"]:
        assert all(c.islower() or c.isdigit() or c == "-" for c in tool["id"]), tool["id"]
        assert tool["m5_name"].startswith("M5 ")
        for part in tool["components"]:
            assert part["license"] and part["version"]
            assert part["download"].startswith("https://") and part["source"].startswith("https://")
    assert "not affiliated" in kit["names_note"]


def test_kit_acceptance_writes_words_certificates_and_record_into_the_pod(iam, tmp_path):
    pod = tmp_path / "pod"
    iam.init_pod(pod, "Ada", attested=True, accept_cyrus=True)
    record = iam.accept_kit(pod, ["office", "ai-agent"], "Ada Lovelace", now="2026-10-21T00:00:00Z")
    layer = pod / "M0-M5IAM-000"
    terms = (layer / "software" / "kit-terms.md").read_text()
    assert "Ada Lovelace" in terms and "LibreOffice" in terms and "they do not grant it" in " ".join(terms.split())
    assert [c["m5_tool"] for c in record["certificates"]] == ["M5 AI Agent", "M5 Office"]
    assert record["signature"] == {"method": "TYPED_NAME", "cryptographic": False}
    assert record["registry"] == "SIMULATED_NOT_ANCHORED" and record["network_write"] is False
    office = json.loads((layer / "registry" / "certificate-software-office.json").read_text())
    assert office["status"] == "SAMPLE_NOT_ISSUED" and office["issued_by"] is None
    assert office["licences"] == ["MPL-2.0"] and office["share_alike"] is True
    assert office["title_no"].startswith("SAMPLE-SW-") and office["holder"] == "Ada"
    agent = json.loads((layer / "registry" / "certificate-software-ai-agent.json").read_text())
    assert [p["name"] for p in agent["powered_by"]] == ["Hermes Agent", "Ollama"] and agent["share_alike"] is False
    assert iam.load_kit(pod)["record"]["kit_terms_sha256"] == record["kit_terms_sha256"]
    assert iam.verify_pod(pod)["status"] == "PASS"


def test_kit_refuses_unknown_tools_an_empty_kit_and_a_missing_signature(iam, tmp_path):
    pod = tmp_path / "pod"
    iam.init_pod(pod, "Ada", attested=True, accept_cyrus=True)
    for tools, name in [([], "Ada"), (["office", "not-a-tool"], "Ada"), (["office"], "   ")]:
        with pytest.raises(iam.PodError):
            iam.accept_kit(pod, tools, name)
    assert not (pod / "M0-M5IAM-000" / "software" / "kit-record.json").exists()
    assert iam.load_kit(pod) is None


def test_app_records_the_kit_only_from_its_own_page(tmp_path):
    app = load("m5_iam_app_kit", IMPL / "m5_iam_app.py")
    server = ThreadingHTTPServer(("127.0.0.1", 0), app.Handler)
    app.Handler.pod, app.Handler.port = tmp_path / "pod", server.server_address[1]
    threading.Thread(target=server.serve_forever, daemon=True).start()
    base = f"http://127.0.0.1:{app.Handler.port}"

    def post(path, body, origin=base):
        request = urllib.request.Request(base + path, data=json.dumps(body).encode(),
                                         headers={"Content-Type": "application/json", "Origin": origin}, method="POST")
        try:
            with urllib.request.urlopen(request) as response:
                return response.status, json.loads(response.read())
        except urllib.error.HTTPError as error:
            return error.code, None

    try:
        kit = {"tools": ["office", "wallet"], "name": "Ada", "accept": True}
        assert post("/api/kit", kit)[0] == 409  # no pod yet
        assert post("/api/attest", {"name": "Ada", "chain": "wyomingchain.eth", "attest": True, "accept_cyrus": True})[0] == 200
        assert post("/api/kit", kit, origin="https://example.com")[0] == 403
        assert post("/api/kit", {**kit, "accept": False})[0] == 409
        assert post("/api/kit", {**kit, "tools": "office"})[0] == 409
        status, state = post("/api/kit", kit)
        assert status == 200 and state["check"]["status"] == "PASS"
        assert [c["m5_tool"] for c in state["kit"]["certificates"]] == ["M5 Office", "M5 Self-Custody Wallet"]
    finally:
        server.shutdown()
