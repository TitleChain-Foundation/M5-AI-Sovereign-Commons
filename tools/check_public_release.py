"""Reproducible manifest, JSON/schema, and targeted public-content checks.

Scans repository files (including nonignored additions), not git history or
untracked ignored private files. Binary files are hashed, not OCR-inspected.
Patterns detect specified secret/PII classes, not every possible disclosure.
Matches report path/rule/line only, never the sensitive value.
"""
import argparse
import hashlib
import json
from pathlib import Path
import re
import subprocess

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
PATTERNS = {
    'private-key-material': re.compile(r'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----'),
    'github-token': re.compile(r'\b(?:gh[pousr]_[A-Za-z0-9]{30,}|github_pat_[A-Za-z0-9_]{40,})\b'),
    'aws-access-key': re.compile(r'\b(?:AKIA|ASIA)[A-Z0-9]{16}\b'),
    'provider-secret': re.compile(r'\bsk-(?:proj-|ant-)?[A-Za-z0-9_-]{35,}\b'),
    'assigned-secret': re.compile(r'''(?i)(?:api[_-]?secret|private[_-]?key|mnemonic|seed_phrase)\s*["']?\s*[:=]\s*["'][A-Za-z0-9+/= _-]{24,}["']'''),
    'ssn-shaped': re.compile(r'\b\d{3}-\d{2}-\d{4}\b'),
    'assigned-private-identifier': re.compile(r'''(?i)["'](?:social_security_number|personal_account_number|tax_identifier)["']\s*:\s*["'][0-9 -]{6,}["']'''),
}


def repository_files():
    return sorted(set(subprocess.check_output(
        ['git','ls-files','--cached','--others','--exclude-standard','-z'],cwd=ROOT
    ).decode().strip('\0').split('\0')))


def scan_text(text):
    return [(rule,text.count('\n',0,m.start())+1) for rule,pattern in PATTERNS.items()
            for m in pattern.finditer(text)]


def check(write_manifest=False):
    files=repository_files();errors=[];ids={};json_count=0;schema_count=0;text_count=0
    manifest={}
    for name in files:
        if name=='MANIFEST.sha256':continue
        p=ROOT/name
        if not p.is_file():errors.append(f'missing repository file: {name}');continue
        if any(x in p.parts for x in ['__pycache__','.pytest_cache','.venv','.idea']) or p.suffix=='.pyc':
            errors.append(f'generated junk: {name}')
        raw=p.read_bytes();manifest[name]=hashlib.sha256(raw).hexdigest()
        try:text=raw.decode('utf-8')
        except UnicodeDecodeError:continue
        text_count+=1
        errors.extend(f'{name}:{line}: {rule}' for rule,line in scan_text(text))
        if p.suffix=='.json':
            try:data=json.loads(text)
            except ValueError as exc:errors.append(f'{name}: invalid JSON: {exc}');continue
            json_count+=1
            if isinstance(data,dict) and '$schema' in data and 'json-schema.org' in data['$schema']:
                try:Draft202012Validator.check_schema(data)
                except Exception as exc:errors.append(f'{name}: invalid schema: {exc}')
                schema_count+=1
                if '$id' in data:
                    if data['$id'] in ids:errors.append(f'duplicate schema id: {name}, {ids[data["$id"]]}')
                    ids[data['$id']]=name
    if write_manifest and not errors:
        (ROOT/'MANIFEST.sha256').write_text(''.join(f'{digest}  {name}\n' for name,digest in sorted(manifest.items())))
    try:
        lines=(ROOT/'MANIFEST.sha256').read_text().splitlines()
        expected=dict(line.split('  ',1)[::-1] for line in lines)
        if len(expected)!=len(lines):errors.append('duplicate manifest entries')
        if expected!=manifest:
            mismatched=[name for name in set(expected)|set(manifest) if expected.get(name)!=manifest.get(name)]
            errors.append('manifest differences: '+', '.join(sorted(mismatched)))
    except (ValueError,FileNotFoundError):errors.append('missing or malformed manifest')
    result={'status':'FAIL' if errors else 'PASS','files_hashed':len(manifest),
            'text_files_scanned':text_count,'json_files_parsed':json_count,'schemas_checked':schema_count,
            'duplicate_schema_ids_checked':len(ids),'errors':errors}
    print(json.dumps(result,indent=2))
    return not errors


if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--write-manifest',action='store_true')
    raise SystemExit(0 if check(parser.parse_args().write_manifest) else 1)
