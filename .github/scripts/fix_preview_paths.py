"""Adapt root-relative local links in generated preview files for project Pages."""
from pathlib import Path
import re

site = Path("_site")
prefix = "/Dokidex-Preview"
count = 0

for file in site.rglob("*"):
    if not file.is_file() or file.suffix.lower() not in {".html", ".css", ".js", ".json"}:
        continue
    original = file.read_text(encoding="utf-8", errors="replace")
    updated = original
    # Root-relative URLs in HTML attributes, CSS strings, and JS strings.
    updated = re.sub(
        r"""(?P<quote>["'])(?P<path>/(?!/|Dokidex-Preview(?:/|["']))[^"'\s<>]*)""",
        lambda m: m.group("quote") + prefix + m.group("path"),
        updated,
    )
    # CSS url(/assets/...) or url(/images/...) without quotes.
    updated = re.sub(
        r"url\(\s*(/(?!/|Dokidex-Preview(?:/|\)))[^\s)'\"]+)\s*\)",
        lambda m: "url(" + prefix + m.group(1) + ")",
        updated,
    )
    if updated != original:
        file.write_text(updated, encoding="utf-8")
        count += 1

print(f"Adjusted root-relative links in {count} preview files")
