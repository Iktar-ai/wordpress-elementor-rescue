#!/usr/bin/env python3
"""Read-only public skill-package checks. No external services or site access."""

from pathlib import Path
from urllib.parse import unquote, urlsplit
import re
import sys
import zipfile

ROOT = Path(__file__).resolve().parent.parent
README = ROOT / "README.md"
CLAUDE_ZIP = ROOT / "dist/repair-wordpress-elementor-claude.zip"
CODEX_SKILL = ROOT / "skills/repair-wordpress-elementor/SKILL.md"
CLAUDE_SKILL = ROOT / "claude/skills/repair-wordpress-elementor/SKILL.md"
ERRORS = []


def check(condition, message):
    if not condition:
        ERRORS.append(message)


for file in (README, ROOT / "LICENSE", ROOT / "CHANGELOG.md", CODEX_SKILL, CLAUDE_SKILL, CLAUDE_ZIP):
    check(file.is_file(), f"Required file missing: {file.relative_to(ROOT)}")

for skill in (CODEX_SKILL, CLAUDE_SKILL):
    if skill.exists():
        check(
            skill.read_text(encoding="utf-8").startswith("---\nname: repair-wordpress-elementor\n"),
            f"Incorrect skill frontmatter: {skill.relative_to(ROOT)}",
        )

if README.exists():
    markdown = README.read_text(encoding="utf-8")
    for target in re.findall(r"\]\(([^)]+)\)", markdown):
        target = target.strip()
        if target.startswith(("https://", "http://", "mailto:", "#")):
            continue
        pathname = unquote(urlsplit(target).path)
        candidate = (ROOT / pathname).resolve()
        check(candidate.is_relative_to(ROOT), f"Link outside repository: {target}")
        if candidate.is_relative_to(ROOT):
            check(candidate.exists(), f"Broken README link: {target}")

if CLAUDE_ZIP.exists():
    try:
        with zipfile.ZipFile(CLAUDE_ZIP) as archive:
            check(archive.testzip() is None, "Claude ZIP has a corrupt member")
            names = archive.namelist()
            check(
                any(name.endswith("/SKILL.md") for name in names),
                "Claude ZIP is missing the skill instructions",
            )
            check(
                any(name.endswith("/references/field-guide.md") for name in names),
                "Claude ZIP is missing the field guide",
            )
            for name in names:
                check(
                    not name.startswith("/") and ".." not in Path(name).parts,
                    f"Unsafe ZIP member path: {name}",
                )
    except (zipfile.BadZipFile, OSError) as exc:
        ERRORS.append(f"Cannot open Claude ZIP: {exc}")

if ERRORS:
    print("Package checks FAILED:")
    for error in ERRORS:
        print(f" - {error}")
    sys.exit(1)

print("Package checks PASS: links, skill entrypoints and Claude ZIP integrity.")
print("Scope: static packaging only; no live WordPress/Elementor repair tested.")
