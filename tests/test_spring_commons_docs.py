import json
import re
from pathlib import Path
from urllib.parse import unquote

from jsonschema import Draft202012Validator


ROOT = Path(__file__).resolve().parents[1]
PROJECT = ROOT / "pilots" / "312-spring-commons"
SCHEMA = PROJECT / "schemas" / "m5-jurisdictional-capital-provenance.schema.json"
EXAMPLE = PROJECT / "examples" / "PPT-EZ-CA-0001-jurisdictional-capital-provenance-example.json"
LANDING_PAGES = [
    PROJECT / "documents" / "README.md",
    PROJECT / "documents" / "images" / "README.md",
    PROJECT / "documents" / "public" / "README.md",
    PROJECT / "documents" / "summaries" / "README.md",
    PROJECT / "examples" / "README.md",
    PROJECT / "schemas" / "README.md",
    PROJECT / "update-notes" / "README.md",
]
MARKDOWN_LINK = re.compile(r"(?<!!)\[[^\]]*\]\(([^)]+)\)")


def test_spring_commons_schema_and_example_validate():
    schema = json.loads(SCHEMA.read_text())
    example = json.loads(EXAMPLE.read_text())

    assert schema["$schema"] == "https://json-schema.org/draft/2020-12/schema"
    assert schema["$id"] == (
        "https://raw.githubusercontent.com/TitleChain-Foundation/"
        "M5-AI-Sovereign-Commons/main/pilots/312-spring-commons/schemas/"
        "m5-jurisdictional-capital-provenance.schema.json"
    )
    Draft202012Validator.check_schema(schema)
    Draft202012Validator(schema).validate(example)


def test_spring_commons_machine_artifacts_have_human_landing_pages():
    assert all(path.is_file() for path in LANDING_PAGES)

    overview = (PROJECT / "README.md").read_text()
    assert "[schema guide](./schemas/README.md)" in overview
    assert "[example guide](./examples/README.md)" in overview
    assert "[Browse the human-readable document library" in overview


def test_local_markdown_links_resolve():
    missing = []
    for markdown in ROOT.rglob("*.md"):
        if ".git" in markdown.parts:
            continue
        for raw_target in MARKDOWN_LINK.findall(markdown.read_text(errors="replace")):
            target = raw_target.strip().strip("<>")
            if not target or target.startswith(("#", "http://", "https://", "mailto:", "tel:")):
                continue
            relative_path = unquote(target.split("#", 1)[0])
            if relative_path and not (markdown.parent / relative_path).resolve().exists():
                missing.append(f"{markdown.relative_to(ROOT)} -> {target}")

    assert not missing, "Missing local Markdown links:\n" + "\n".join(missing)
