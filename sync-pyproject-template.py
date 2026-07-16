#!/usr/bin/env python3
"""Sync the dependency versions from `docs/pyproject.toml` into the
`template/docs/pyproject.toml.jinja` Copier template, so the template
stays in sync with the dependency versions used by this repo.

It is intended to be run from the root of the repository, e.g.::

    python3 sync-pyproject-template.py

It is also invoked by the `.github/workflows/update-python-dependencies.yaml`
workflow right after `uv lock --upgrade` and the `sync-pyproject` action
have updated `docs/pyproject.toml`.
"""

from __future__ import annotations

import re
import sys
import tomllib
from pathlib import Path

# Resolve paths relative to the repository root (this script's own
# directory), so the script works regardless of the current CWD.
ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "docs" / "pyproject.toml"
TARGET = ROOT / "template" / "docs" / "pyproject.toml.jinja"

# Matches a `dependencies = [ ... ]` block (multiline) in the template.
DEPENDENCIES_RE = re.compile(
    r"^dependencies = \[\n(?:    [^\n]*\n)*?\]",
    re.MULTILINE,
)


def read_dependencies(path: Path) -> list[str]:
    with path.open("rb") as f:
        data = tomllib.load(f)
    try:
        return data["project"]["dependencies"]
    except KeyError:
        raise SystemExit(f"{path}: missing [project].dependencies") from None


def format_block(deps: list[str]) -> str:
    return "dependencies = [\n" + "".join(f'    "{dep}",\n' for dep in deps) + "]"


def sync(source: Path = SOURCE, target: Path = TARGET) -> None:
    deps = read_dependencies(source)
    new_block = format_block(deps)

    content = target.read_text()
    new_content, n = DEPENDENCIES_RE.subn(new_block, content, count=1)
    if n != 1:
        raise SystemExit(
            f"{target}: expected to replace 1 dependencies block, replaced {n}"
        )

    if new_content == content:
        print(f"{target}: already up to date")
        return

    target.write_text(new_content)
    print(f"{target}: synced dependencies from {source}")


def main() -> int:
    sync()
    return 0


if __name__ == "__main__":
    sys.exit(main())
