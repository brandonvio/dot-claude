.PHONY: install uninstall clean update-constitution help

# Default target
help:
	@echo "Available targets:"
	@echo "  make install              - Install agents and commands to ~/.claude/"
	@echo "  make uninstall            - Remove installed agents and commands from ~/.claude/"
	@echo "  make update-constitution  - Update constitution URL from settings.json"
	@echo "  make clean                - Remove backup files"
	@echo "  make help                 - Show this help message"

# Install agents and commands to user's .claude directory
install-claude-user-folder:
	@echo "Installing dot-claude configuration..."
	@echo "Creating directories..."
	@mkdir -p ~/.claude/agents
	@mkdir -p ~/.claude/commands
	@echo "Copying agents..."
	@cp -v ./agents/*.md ~/.claude/agents/
	@echo "Copying commands..."
	@cp -v ./commands/*.md ~/.claude/commands/
	@echo ""
	@echo "✓ Installation complete!"
	@echo "  - Agents installed to: ~/.claude/agents/"
	@echo "  - Commands installed to: ~/.claude/commands/"
	@echo ""
	@echo "To update your settings, copy .claude/settings.local.json to ~/.claude/"

# Uninstall agents and commands from user's .claude directory
uninstall:
	@echo "Uninstalling dot-claude configuration..."
	@echo "Removing agents..."
	@rm -fv ~/.claude/agents/*.md
	@echo "Removing commands..."
	@rm -fv ~/.claude/commands/*.md
	@echo ""
	@echo "✓ Uninstallation complete!"
	@echo "Note: ~/.claude/agents/ and ~/.claude/commands/ directories were preserved"

# Update constitution URL in all agent and command files from settings.json
update-constitution:
	@./scripts/update-constitution-url.sh

# Clean up any backup files
clean:
	@echo "Cleaning backup files..."
	@find ./agents -name "*.md~" -delete -o -name "*.md.bak" -delete
	@find ./commands -name "*.md~" -delete -o -name "*.md.bak" -delete
	@echo "✓ Cleanup complete!"

sync-to-targets:
	uv run ./src/sync_to_targets.py