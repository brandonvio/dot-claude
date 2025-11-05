#!/usr/bin/env python3
"""Sync constitution and folders to target .claude directories."""

from pathlib import Path
import shutil


def load_targets(targets_file: Path) -> list[Path]:
    """Load target paths from targets file."""
    return [
        Path(line.strip())
        for line in targets_file.read_text().splitlines()
        if line.strip()
    ]


def sync_file(source: Path, target_dir: Path) -> None:
    """Copy a file to target directory."""
    target_file = target_dir / source.name
    shutil.copy2(source, target_file)
    print(f"Copied {source.name} -> {target_file}")


def sync_directory(source: Path, target_dir: Path) -> None:
    """Copy/overwrite a directory to target location."""
    target = target_dir / source.name

    if target.exists():
        shutil.rmtree(target)

    shutil.copytree(source, target)
    print(f"Synced {source.name}/ -> {target}/")


def main() -> None:
    """Sync constitution and folders to all targets."""
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    claude_dir = project_root / ".claude"

    targets_file = project_root / "targets.txt"
    constitution = claude_dir / "constitution.md"
    agents_dir = claude_dir / "agents"
    commands_dir = claude_dir / "commands"
    scripts_dir = claude_dir / "scripts"

    targets = load_targets(targets_file)

    for target in targets:
        print(f"\n=== Syncing to {target} ===")

        sync_file(constitution, target)
        sync_directory(agents_dir, target)
        sync_directory(commands_dir, target)
        sync_directory(scripts_dir, target)

    print(f"\n✓ Synced to {len(targets)} target(s)")


if __name__ == "__main__":
    main()
