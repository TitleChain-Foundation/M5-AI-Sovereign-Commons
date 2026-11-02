# Commons website source synchronization

The GitHub Markdown files remain the source of truth. The existing Pages workflow publishes the current front pages, the SEC Observatory and a generated documentation library in one artifact. This change does not approve a draft, activate an account, issue a credential or publish private M5POD contents.

## Content selection and provenance

`site/content-map.json` explicitly selects the 68 documents already referenced by the Commons front doors and primary hubs. `scripts/build_commons_library.py` generates their readers at `library/<source path without .md>.html`. The library index also links to the remaining tracked Markdown files on GitHub; those files are not promoted into new featured content.

Each reader links to its source at the build commit and records the source-byte SHA-256. Source status, disclaimers, simulations and limitations remain visible. Generated `library/source-map.json` lists the exact source edition, destination and disposition. It also reports unresolved source references; the current selected set has none.

The narrow `M5-POD-PACKAGE.md` documentation alias resolves to the existing `M5POD-PACKAGE.md`. Account names, machine identifiers, SKUs, signed records and canonical actor categories are not renamed.

## Navigation and safety

`site/commons-library.js` adds one Documentation entry to each of the five HTML front pages and redirects only selected links for this repository's current main/build revision. External repositories, unselected documents, code and historical revisions retain their source destinations. The adapter runs again when the existing application changes routes. If its map cannot load, the original GitHub links remain usable.

The builder uses pinned Markdown dependencies. Raw HTML permits only disclosure tags and line breaks, with all source attributes removed; other raw HTML is escaped. Unsafe link schemes are rejected. Source files must be tracked and contained in the repository. Generated headings use a `doc-` prefix; Markdown heading links are rewritten accordingly. Linked images are copied from tracked public source assets; code and attachments retain GitHub destinations. The reader uses a restrictive content security policy and local CSS/JavaScript.

Tables, code blocks, currency and escaped brackets are verified explicitly. The selected DOC-23 text uses escaped literal jurisdiction brackets, not TeX equations. This reader does not introduce a mathematical engine or claim arbitrary mathematical-publication conformance. Future sources needing specialized formula/diagram rendering require a reviewed extension before selection.

The secondary front pages retain their pre-existing React/ReactDOM/Babel CDN dependency. This change does not replace their runtime or redesign their layout. The generated documentation reader itself requires no CDN scripts, fonts or API service.

## Local validation

From a preserved checkout on a dedicated branch:

```sh
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-dev.txt -r sec-public-input/observatory/requirements.txt
python -m unittest discover -s tests -p test_commons_library.py -v
```

Build a fresh preview outside the source tree:

```sh
mkdir -p ../commons-site-preview
cp -R site/. ../commons-site-preview/
python scripts/build_commons_library.py --output ../commons-site-preview
python -m http.server 8000 --directory ../commons-site-preview
```

Visit `http://localhost:8000/` and `http://localhost:8000/library/`. Generated source hashes identify exact bytes. Local uncommitted source edits are previews; only a reviewed clean commit should be deployed as a source edition.

Run the existing full conformance command with the repository-pinned Numscript installed:

```sh
M5_REQUIRE_NUMSCRIPT=1 python -m pytest -q -p no:cacheprovider tests reference-implementation/provider-neutral-governor/tests shadow-m5index/tests sec-public-input/observatory/tests
python shadow-m5index/scripts/validate_records.py
python tools/check_public_release.py
```

After deliberate source edits, update `MANIFEST.sha256` with `python tools/check_public_release.py --write-manifest`, review its diff, then rerun the check. Do not check in the generated preview, local environment or private exports.

## Review and rollback

Prepare one focused PR containing the builder, explicit source map, shared adapter, reader assets, workflow integration, tests and manifest update. The existing deployment workflow remains the sole Pages publisher; its permissions and hourly Observatory schedule are unchanged. A PR and passing local checks do not authorize deployment.

Rollback through a reviewed revert of this change and rerun the existing Pages workflow. The original Markdown sources and original GitHub destinations remain intact. After deployment, verify the source-map commit, selected reader hashes, local links/anchors and the legacy alias on the custom domain; verify the SEC Observatory is still present.
