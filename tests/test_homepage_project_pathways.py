from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"

EXPECTED_SEQUENCE = [
    "GSA / CRE",
    "312 Spring Commons",
    "FARMLAND / REDEVELOPMENT",
    "America's People's Trust Farmland",
    "GLOBAL DEVELOPMENT PROJECT",
    "Global UN Commons",
]

REQUIRED_PATHS = [
    ROOT / "pilots" / "312-spring-commons" / "README.md",
    ROOT / "pilots" / "peoples-trust" / "README.md",
    ROOT / "pilots" / "global-un-commons" / "README.md",
    ROOT / "pilots" / "global-un-commons" / "visuals" / "README.md",
    ROOT / "sec-public-input" / "README.md",
    ROOT / "docs" / "PILOT-SEC-RFI-CROSSWALK.md",
]


def test_homepage_development_categories_and_projects_are_present_and_ordered():
    text = README.read_text(encoding="utf-8")
    positions = [text.index(name) for name in EXPECTED_SEQUENCE]
    assert positions == sorted(positions), (
        "Homepage must preserve: "
        "GSA / CRE -> 312 Spring Commons -> "
        "FARMLAND / REDEVELOPMENT -> People's Trust Farmland -> "
        "GLOBAL DEVELOPMENT PROJECT -> Global UN Commons"
    )


def test_core_project_and_sec_roots_exist():
    missing = [str(path.relative_to(ROOT)) for path in REQUIRED_PATHS if not path.exists()]
    assert not missing, "Missing public project/SEC roots: " + ", ".join(missing)


def test_featured_pathways_have_exact_category_hierarchy():
    import re

    text = README.read_text(encoding="utf-8").split("## Featured project pathways\n", 1)[1]
    text = text.split("## Featured public research\n", 1)[0]
    headings = re.findall(r"^(#{3,4}) \*\*(.+?)\*\*$", text, re.MULTILINE)
    assert headings == [
        ("###", "GSA / CRE"),
        ("####", "312 Spring Commons — California"),
        ("###", "FARMLAND / REDEVELOPMENT"),
        ("####", "America's People's Trust Farmland"),
        ("###", "GLOBAL DEVELOPMENT PROJECT"),
        ("####", "Global UN Commons — UN-NY-0001"),
    ]


def test_project_navigation_images_resolve():
    import re

    for page in [README, ROOT / "pilots" / "README.md"]:
        images = re.findall(r"!\[[^\]]*\]\(([^)]+)\)", page.read_text(encoding="utf-8"))
        assert images
        for target in images:
            if not target.startswith(("https://", "http://")):
                assert (page.parent / target).is_file(), f"{page}: missing image {target}"
