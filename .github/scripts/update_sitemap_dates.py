#!/usr/bin/env python3
"""Generate _data/git_lastmod.yml from git history for each content file."""

import os
import subprocess


def get_content_files():
    """Get all tracked .md and .html content files."""
    output = subprocess.check_output(
        ["git", "ls-files", "*.md", "*.html", "**/*.md", "**/*.html"],
        text=True,
    ).strip()
    return [f for f in output.split("\n") if f] if output else []


def get_last_modified(filepath):
    """Get the last commit date for a file in YYYY-MM-DD format."""
    result = subprocess.run(
        ["git", "log", "-1", "--format=%aI", "--", filepath],
        capture_output=True, text=True,
    )
    date = result.stdout.strip()
    return date[:10] if date else None


def yaml_key(s):
    """Quote a YAML key if needed."""
    return f'"{s}"' if any(c in s for c in ":/{}[].,") else s


def main():
    os.makedirs("_data", exist_ok=True)

    files = get_content_files()
    lastmod = {}
    for f in files:
        date = get_last_modified(f)
        if date:
            lastmod[f] = date

    with open("_data/git_lastmod.yml", "w") as out:
        out.write("# Auto-generated from git history — do not edit by hand.\n\n")
        for path in sorted(lastmod):
            out.write(f"{yaml_key(path)}: {lastmod[path]}\n")

    print(f"Updated _data/git_lastmod.yml with {len(lastmod)} entries")


if __name__ == "__main__":
    main()
