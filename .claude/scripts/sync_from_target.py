#!/usr/bin/env python3
"""Sync changes from a target .claude directory back to dot-claude."""

import sys
from pathlib import Path
import shutil


def sync_file_back(source: Path, dest_dir: Path) -> None:
    """Copy a file from source back to destination directory."""
    dest_file = dest_dir / source.name
    shutil.copy2(source, dest_file)
    print(f"Synced {source.name} <- {source}")


def sync_directory_back(source: Path, dest_dir: Path) -> None:
    """Copy/overwrite a directory from source back to destination."""
    dest = dest_dir / source.name

    if dest.exists():
        shutil.rmtree(dest)

    shutil.copytree(source, dest)
    print(f"Synced {source.name}/ <- {source}/")


def main() -> None:
    """Sync from target .claude directory back to dot-claude."""
    if len(sys.argv) < 2:
        print("Error: Target .claude directory path required.")
        print("Usage: python sync_from_target.py /path/to/target/.claude")
        print("")
        print("Example:")
        print("  python sync_from_target.py /Users/brandon/code/projects/lvrgd/lvrgd-common/.claude")
        sys.exit(1)

    source_claude_dir = Path(sys.argv[1])

    if not source_claude_dir.exists():
        print(f"Error: Source directory does not exist: {source_claude_dir}")
        sys.exit(1)

    if not source_claude_dir.is_dir():
        print(f"Error: Source is not a directory: {source_claude_dir}")
        sys.exit(1)

    if source_claude_dir.name != ".claude":
        print(f"Error: Source directory must be named '.claude', got: {source_claude_dir.name}")
        sys.exit(1)

    # Find dot-claude project root (go up from scripts directory)
    script_dir = Path(__file__).parent
    dot_claude_root = script_dir.parent.parent
    dest_claude_dir = dot_claude_root / ".claude"

    if not dest_claude_dir.exists():
        print(f"Error: Destination .claude directory not found: {dest_claude_dir}")
        sys.exit(1)

    print(f"\n=== Syncing from {source_claude_dir} ===")
    print(f"=== to {dest_claude_dir} ===\n")

    # Sync files
    source_constitution = source_claude_dir / "constitution.md"
    source_settings = source_claude_dir / "settings.json"

    if source_constitution.exists():
        sync_file_back(source_constitution, dest_claude_dir)
    else:
        print(f"Warning: constitution.md not found in source")

    if source_settings.exists():
        sync_file_back(source_settings, dest_claude_dir)
    else:
        print(f"Warning: settings.json not found in source")

    # Sync directories
    source_agents = source_claude_dir / "agents"
    source_commands = source_claude_dir / "commands"
    source_scripts = source_claude_dir / "scripts"

    if source_agents.exists():
        sync_directory_back(source_agents, dest_claude_dir)
    else:
        print(f"Warning: agents/ directory not found in source")

    if source_commands.exists():
        sync_directory_back(source_commands, dest_claude_dir)
    else:
        print(f"Warning: commands/ directory not found in source")

    if source_scripts.exists():
        sync_directory_back(source_scripts, dest_claude_dir)
    else:
        print(f"Warning: scripts/ directory not found in source")

    print(f"\n✓ Sync complete: {source_claude_dir} -> {dest_claude_dir}")
    print(f"\nNext steps:")
    print(f"  1. Review changes in {dest_claude_dir}")
    print(f"  2. Test any modified agents/commands")
    print(f"  3. Commit changes if desired")
    print(f"  4. Run src/sync_to_targets.py to propagate to all targets")


if __name__ == "__main__":
    main()
