"""Reproducible demonstration of the free M5 IAM starting pod.

Creates a pod with a fixed name, chain, time and identifier in a temporary
folder, then prints the SHA-256 of every file it wrote. Anyone running this
release gets the same digests, which are stored in expected-digests.json.
Standard library only; no network calls; nothing is written outside the
temporary folder unless --keep is given.

    python3 reproduce.py                 # run and compare with expected digests
    python3 reproduce.py --keep DIR      # also keep the evidence in DIR
    python3 reproduce.py --write-expected  # maintainers: refresh after a code change
"""
import argparse
import hashlib
import json
from pathlib import Path
import shutil
import sys
import tempfile

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))

import m5_iam  # noqa: E402

FIXED = {'display_name': 'Demo Human', 'chain': 'wyomingchain.eth',
         'now': '2026-10-13T00:00:00Z', 'local_id': 'local-iam:00000000-0000-4000-8000-000000000000'}
EXPECTED = HERE / 'expected-digests.json'


def run(folder):
    pod = Path(folder) / 'M5POD-IAM-demo'
    m5_iam.init_pod(pod, FIXED['display_name'], attested=True, now=FIXED['now'],
                    local_id=FIXED['local_id'], chain=FIXED['chain'])
    digests = {path.relative_to(pod).as_posix(): hashlib.sha256(path.read_bytes()).hexdigest()
               for path in sorted(pod.rglob('*')) if path.is_file()}
    return pod, digests, m5_iam.verify_pod(pod)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument('--keep', type=Path, help='copy the generated evidence to this folder')
    parser.add_argument('--write-expected', action='store_true')
    args = parser.parse_args(argv)
    with tempfile.TemporaryDirectory() as tmp:
        pod, digests, check = run(tmp)
        if args.keep:
            shutil.copytree(pod, args.keep / pod.name, dirs_exist_ok=True)
    if args.write_expected:
        EXPECTED.write_text(json.dumps({'inputs': FIXED, 'digests': digests}, indent=2) + '\n', encoding='utf-8')
        print(f'wrote {EXPECTED.name} with {len(digests)} digests')
        return 0
    expected = json.loads(EXPECTED.read_text(encoding='utf-8'))['digests']
    mismatched = sorted(name for name in set(expected) | set(digests) if expected.get(name) != digests.get(name))
    result = {'verify': check['status'], 'files': len(digests), 'matches_expected': not mismatched,
              'mismatched': mismatched}
    print(json.dumps(result, indent=2))
    return 0 if check['status'] == 'PASS' and not mismatched else 1


if __name__ == '__main__':
    sys.exit(main())
