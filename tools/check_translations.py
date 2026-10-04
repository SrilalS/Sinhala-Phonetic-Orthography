"""List the translations in docs/<lang>/ whose English source changed after they were translated.

    python tools/check_translations.py

Each translation starts with a comment that names its English source and that file's hash:

    <!-- translated from docs/02-vowel-signs.md sha256:272a0a424cd1 -->

The hash is the first 12 hex digits of the SHA-256 of the source with LF line endings.
Exits non-zero when a translation is out of date or its source is missing.
"""
import hashlib
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STAMP = re.compile(r"<!-- translated from (\S+) sha256:([0-9a-f]{12}) -->")


def source_hash(path: Path) -> str:
    text = path.read_bytes().replace(b"\r\n", b"\n")
    return hashlib.sha256(text).hexdigest()[:12]


def main():
    stale = 0
    for lang_dir in sorted(p for p in (ROOT / "docs").iterdir() if p.is_dir()):
        for doc in sorted(lang_dir.glob("*.md")):
            if doc.name == "README.md":
                continue
            m = STAMP.match(doc.read_text(encoding="utf-8").lstrip("﻿"))
            name = doc.relative_to(ROOT).as_posix()
            if not m:
                print(f"no stamp   {name}")
                stale += 1
                continue
            src = ROOT / m.group(1)
            if not src.exists():
                print(f"missing    {name} (source {m.group(1)})")
                stale += 1
            elif source_hash(src) != m.group(2):
                print(f"outdated   {name} (source {m.group(1)} changed)")
                stale += 1
            else:
                print(f"up to date {name}")
    raise SystemExit(1 if stale else 0)


if __name__ == "__main__":
    main()
