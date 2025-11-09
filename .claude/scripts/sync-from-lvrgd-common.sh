#!/bin/bash
# Sync changes from lvrgd-common back to dot-claude

SYNC_SCRIPT="/Users/brandon/code/projects/dot-claude/.claude/scripts/sync_from_target.py"
SOURCE_DIR="/Users/brandon/code/projects/lvrgd/lvrgd-common/.claude"

python3 "$SYNC_SCRIPT" "$SOURCE_DIR"
