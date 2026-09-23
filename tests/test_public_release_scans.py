import importlib.util
from pathlib import Path

spec=importlib.util.spec_from_file_location('public_scan',Path(__file__).resolve().parents[1]/'tools/check_public_release.py')
scanner=importlib.util.module_from_spec(spec);spec.loader.exec_module(scanner)


def test_scanner_detects_secret_and_pii_without_printing_value():
    samples=['-----BEGIN '+'PRIVATE KEY-----','ghp_'+'A'*36,'AKIA'+'A'*16,'sk-proj-'+'A'*40,
             '123'+'-45-'+'6789','"personal_account_number": "'+'1'*12+'"']
    assert all(scanner.scan_text(sample) for sample in samples)
    assert scanner.scan_text('SYN-M5HUM-001 and synthetic evidence refs')==[]
