"""Build the downloadable Norton Ranch Blueprint M5POD starter package.

Reads the package manifest, copies the listed repository paths into a single
ZIP that preserves repository-relative layout (so every relative link in the
package keeps working), and adds START-HERE.md plus PACKAGE-CHECKSUMS.sha256.

The output is deterministic: identical inputs produce an identical ZIP.
Uses only the Python standard library and performs no network calls.
"""
import argparse
import hashlib
import json
from pathlib import Path
import zipfile

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / 'pilots' / 'norton-ranch-blueprint' / 'm5pod-package.manifest.json'
FIXED_TIME = (1980, 1, 1, 0, 0, 0)
SKIP_PARTS = {'__pycache__', '.pytest_cache', '.DS_Store'}

START_HERE = """# Norton Ranch Blueprint — START HERE

**Version {version}** · {status}

> **License state: UNREGISTERED COMMONS STARTER.**
> This download is not a licensed M5POD. It becomes part of a licensed M5POD
> only after you register, register your farm or ranch entity, and activate
> the M5 tools.

1. Read the guide: `pilots/norton-ranch-blueprint/M5POD-PACKAGE.md`
2. Verify the files: `shasum -a 256 -c PACKAGE-CHECKSUMS.sha256`
3. Try it locally (no network):

   ```bash
   cd reference-implementation/sovereign-herd
   python3 provision_herd.py --entity m5ent:synthetic:red-river-ranch \\
     --farm m5farm:synthetic:red-river:001 \\
     --input sample-herd.json --output herd-manifest.generated.json
   ```

4. When you are ready, register and activate: https://m5bank.app/

The machine-readable package manifest is
`pilots/norton-ranch-blueprint/m5pod-package.manifest.json`.
"""


def load_manifest():
    return json.loads(MANIFEST.read_text(encoding='utf-8'))


def package_files(manifest):
    paths = set()
    for entries in manifest['layers'].values():
        for entry in entries:
            source = ROOT / entry
            if not source.exists():
                raise FileNotFoundError(f'manifest path missing: {entry}')
            candidates = source.rglob('*') if source.is_dir() else [source]
            for path in candidates:
                if path.is_file() and not SKIP_PARTS.intersection(path.parts) and path.suffix != '.pyc':
                    paths.add(path.relative_to(ROOT).as_posix())
    paths.add(MANIFEST.relative_to(ROOT).as_posix())
    return sorted(paths)


def write_entry(archive, name, data):
    info = zipfile.ZipInfo(name, date_time=FIXED_TIME)
    info.compress_type = zipfile.ZIP_DEFLATED
    info.external_attr = 0o644 << 16
    archive.writestr(info, data)


def build(output_dir):
    manifest = load_manifest()
    base = f"{manifest['package_id']}-v{manifest['version']}"
    files = package_files(manifest)
    contents = {name: (ROOT / name).read_bytes() for name in files}
    contents['START-HERE.md'] = START_HERE.format(
        version=manifest['version'], status=manifest['status']).encode('utf-8')
    checksums = ''.join(f'{hashlib.sha256(data).hexdigest()}  {name}\n'
                        for name, data in sorted(contents.items()))
    contents['PACKAGE-CHECKSUMS.sha256'] = checksums.encode('utf-8')
    output_dir.mkdir(parents=True, exist_ok=True)
    zip_path = output_dir / f'{base}.zip'
    with zipfile.ZipFile(zip_path, 'w') as archive:
        for name in sorted(contents):
            write_entry(archive, f'{base}/{name}', contents[name])
    digest = hashlib.sha256(zip_path.read_bytes()).hexdigest()
    (output_dir / f'{base}.zip.sha256').write_text(f'{digest}  {zip_path.name}\n')
    print(json.dumps({'package': zip_path.name, 'files': len(contents), 'sha256': digest}, indent=2))
    return zip_path


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--output-dir', type=Path, default=ROOT / 'dist')
    build(parser.parse_args().output_dir)
