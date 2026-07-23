#!/usr/bin/env python3
"""Install this PradaSlides skill into an explicitly selected agent skills directory."""

from __future__ import annotations

import argparse
import shutil
from datetime import datetime, timezone
from pathlib import Path


RUNTIME_ITEMS = ("SKILL.md", "agents", "scripts", "references", "assets")
IGNORE = shutil.ignore_patterns("__pycache__", "*.pyc", ".DS_Store", "Thumbs.db")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--target",
        required=True,
        help="Agent skills directory; installs to <target>/pradaslides",
    )
    parser.add_argument(
        "--replace",
        action="store_true",
        help="Back up an existing installation, then install the current version",
    )
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    source = Path(__file__).resolve().parents[1]
    target_root = Path(args.target).expanduser().resolve()
    destination = target_root / "pradaslides"
    missing = [name for name in RUNTIME_ITEMS if not (source / name).exists()]
    if missing:
        raise SystemExit("Skill source is incomplete: " + ", ".join(missing))

    if destination.exists() and not args.replace:
        raise SystemExit(
            f"Destination already exists: {destination}\n"
            "Re-run with --replace to create a backup before installation."
        )

    backup: Path | None = None
    if destination.exists():
        stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
        backup = target_root / f"pradaslides.backup-{stamp}"
        if backup.exists():
            raise SystemExit(f"Backup path unexpectedly exists: {backup}")

    print(f"Source:      {source}")
    print(f"Destination: {destination}")
    if backup:
        print(f"Backup:      {backup}")
    print("Included:    " + ", ".join(RUNTIME_ITEMS))
    print("Excluded:    internal research outside the skill directory")
    if args.dry_run:
        print("Dry run; no files changed.")
        return 0

    target_root.mkdir(parents=True, exist_ok=True)
    if backup:
        destination.rename(backup)
    destination.mkdir()
    try:
        for name in RUNTIME_ITEMS:
            item = source / name
            output = destination / name
            if item.is_dir():
                shutil.copytree(item, output, ignore=IGNORE)
            else:
                shutil.copy2(item, output)
    except Exception:
        if destination.exists():
            shutil.rmtree(destination)
        if backup and backup.exists():
            backup.rename(destination)
        raise

    print("PradaSlides installed successfully.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
