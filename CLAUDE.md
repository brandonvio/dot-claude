# CLAUDE.md

A comprehensive configuration and automation framework for Claude Code that enables custom agents, slash commands, and constitutional development principles through shareable `.claude` directories.

## Overview

**dot-claude** is a configuration management system for Claude Code projects that brings the power of custom AI agents, workflow automation commands, and enforceable coding standards to your development process. Think of it as a dotfiles system for AI-assisted development - shareable, versionable, and project-specific.

The project provides:
- **14 Specialized AI Agents**: Pre-built expert agents for code review, documentation generation, testing, refactoring, and constitutional compliance
- **14 Slash Commands**: Quick-access workflow automation for commits, reviews, documentation generation, and task execution
- **Constitutional Development Framework**: A non-negotiable set of coding principles enforced through agents and commands
- **Multi-Project Sync**: Python utility to deploy configurations across multiple projects simultaneously
- **Make-based Automation**: Simple installation and management through Makefile targets

This enables consistent code quality, automated standard enforcement, rapid context switching between tasks, and shareable AI workflows that version control alongside your code.

## Constitution Compliance

**CRITICAL: All code in this directory MUST strictly adhere to the project constitution.**

Read and reference the project constitution at: `.claude/constitution.md`

### Core Constitutional Principles (NON-NEGOTIABLE)

1. **Radical Simplicity**: Always implement the simplest solution. Never make code more complicated than needed.

2. **Fail Fast Philosophy**: Systems should fail immediately when assumptions are violated. No defensive fallback code unless explicitly requested.

3. **Comprehensive Type Safety**: Use type hints everywhere - ALL code including tests, lambda functions, services, and models.

4. **Structured Data Models**: Always use dataclasses or Pydantic models. Never pass around dictionaries for structured data.

5. **Dependency Injection**: All services must inject dependencies through `__init__`. ALL dependencies are REQUIRED parameters (no Optional, no defaults). NEVER create dependencies inside constructors.

6. **SOLID Principles**: Strictly adhere to Single Responsibility, Open/Closed, Liskov Substitution, Interface Segregation, and Dependency Inversion.

**All developers working in this directory must read and follow `.claude/constitution.md` without exception.**

## Architecture

### Structure

```
dot-claude/
├── .claude/                    # Main configuration directory
│   ├── constitution.md         # Development principles (non-negotiable)
│   ├── agents/                 # 14 specialized AI agents
│   │   ├── agent-command-generator.md
│   │   ├── agent-generator.md
│   │   ├── claude-md-generator.md
│   │   ├── claude-md-updater.md
│   │   ├── code-reviewer.md
│   │   ├── commit-agent.md
│   │   ├── constitution-code-reviewer.md
│   │   ├── constitution-spec-generator.md
│   │   ├── constitution-task-executor.md
│   │   ├── constitution-task-generator.md
│   │   ├── pydantic-refactor-specialist.md
│   │   ├── readme-generator.md
│   │   ├── schema-generator.md
│   │   └── slash-command-generator.md
│   └── commands/               # 14 slash commands
│       ├── code-review.md
│       ├── commit.md
│       ├── execute-tasks.md
│       ├── fast-work.md
│       ├── format-md.md
│       ├── generate-agent.md
│       ├── generate-claude-md.md
│       ├── generate-command.md
│       ├── generate-mr-doc.md
│       ├── generate-readme.md
│       ├── generate-spec.md
│       ├── generate-tasks.md
│       ├── pythonic-refactor.md
│       └── work.md
├── src/
│   └── sync_to_targets.py     # Multi-project sync utility
├── docs/                       # Documentation and specs
│   ├── specs/                  # Design specifications
│   └── pull-request-summaries/ # PR documentation
├── targets.txt                 # Project sync destinations
├── Makefile                    # Installation and management commands
├── .gitignore                  # Git ignore patterns
└── README.md                   # User-facing documentation
```

**Constitutional Compliance**: The architecture follows Single Responsibility (agents for specific tasks, commands for specific workflows), Open/Closed (extensible through new agents/commands), and Interface Segregation (focused tool access per agent/command). The sync utility demonstrates proper dependency injection patterns.

### Components

#### Core Configuration (.claude/)

**Purpose**: Central configuration directory containing all agents, commands, and constitutional principles

**Functionality**:
- Defines development constitution (coding standards and principles)
- Houses all agent definitions (specialized AI experts)
- Contains all slash command definitions (workflow automation)
- Configures permissions and tool access via settings.json

**Dependencies**: None - pure markdown and JSON configuration

**Usage**: Deployed to project `.claude/` directories or `~/.claude/` user directory

**Constitutional Notes**: Simple file-based configuration, no complex logic. Type-safe through structured markdown frontmatter.

#### Specialized Agents (.claude/agents/)

**Purpose**: Pre-built expert AI agents for specific development tasks

**Key Agents**:
- **code-reviewer**: Comprehensive code quality, security, architecture, and testing review
- **commit-agent**: Intelligent conventional commit message generation
- **claude-md-generator**: Generates comprehensive CLAUDE.md documentation for folders
- **claude-md-updater**: Updates existing CLAUDE.md files with new information
- **readme-generator**: Creates GitHub-ready README.md files
- **constitution-spec-generator**: Creates technical specifications from requirements
- **constitution-task-generator**: Breaks specifications into actionable tasks
- **constitution-task-executor**: Implements tasks following constitutional principles
- **constitution-code-reviewer**: Audits code against constitutional compliance
- **pydantic-refactor-specialist**: Refactors Python code to use Pydantic models
- **schema-generator**: Generates data schemas (Pydantic/dataclass models)
- **agent-generator**: Creates new custom agents
- **agent-command-generator**: Generates custom slash commands
- **slash-command-generator**: Alternative command generator

**Functionality**: Each agent has focused expertise, specific tool access, and detailed system prompts defining their role and process

**Dependencies**: Claude Code platform with specific tool permissions (Read, Write, Bash, Grep, Glob, Task)

**Usage**: Invoked by Claude Code based on context or explicitly through commands/user requests

**Constitutional Notes**: Each agent follows Single Responsibility Principle. Tool access minimized per agent needs. Clear, simple instructions without defensive complexity.

#### Slash Commands (.claude/commands/)

**Purpose**: Quick-access workflow automation for common development tasks

**Key Commands**:
- **/commit**: Auto-commit with smart conventional messages
- **/code-review**: Review current branch changes
- **/work**: Full spec-task-execute-review cycle from prompt
- **/fast-work**: Lightweight task execution workflow
- **/execute-tasks**: Execute constitutional tasks with review loop
- **/generate-tasks**: Generate tasks from constitution and requirements
- **/generate-spec**: Generate technical specification from requirements
- **/generate-readme**: Generate README.md for a directory
- **/generate-claude-md**: Generate CLAUDE.md for a folder
- **/generate-agent**: Create a new custom agent
- **/generate-command**: Create a new slash command
- **/pythonic-refactor**: Refactor Python code with Pydantic
- **/generate-mr-doc**: Generate merge request documentation
- **/format-md**: Format markdown files

**Functionality**: Commands delegate to specialized agents using the Task tool, providing streamlined workflows with argument validation

**Dependencies**: Specialized agents (injected via Task tool invocation)

**Usage**: Type slash command in Claude Code conversation, optionally with arguments

**Constitutional Notes**: Commands are simple orchestrators - they validate input and delegate to agents. No complex business logic in commands themselves.

#### Sync Utility (src/sync_to_targets.py)

**Purpose**: Synchronizes constitution, agents, commands, and scripts to multiple target projects

**Functionality**:
- Reads target paths from `targets.txt`
- Copies constitution.md to all targets
- Syncs agents/ directory (overwrites existing)
- Syncs commands/ directory (overwrites existing)
- Syncs scripts/ directory if present
- Provides progress feedback for each sync operation

**Dependencies**:
- `pathlib.Path`: File path operations
- `shutil`: File and directory copying

**Usage**: Run via `make sync-to-targets` or `uv run ./src/sync_to_targets.py`

**Constitutional Notes**:
- ✅ Full type hints on all functions
- ✅ Simple, straightforward implementation
- ✅ Fails fast if paths are invalid (no defensive checks)
- ✅ No optional dependencies - all parameters required
- ✅ Single Responsibility: only syncs files, doesn't modify them

#### Makefile

**Purpose**: Build automation and installation management

**Functionality**:
- `make install-claude-user-folder`: Install to `~/.claude/` user directory
- `make uninstall`: Remove from user directory
- `make update-constitution`: Update constitution URLs in all files
- `make sync-to-targets`: Deploy to all projects in targets.txt
- `make clean`: Remove backup files
- `make help`: Display available commands

**Dependencies**: Standard Unix utilities (mkdir, cp, rm, find)

**Usage**: Run make targets from project root

**Constitutional Notes**: Simple, declarative automation. Each target has single responsibility. No complex logic.

#### Constitution (.claude/constitution.md)

**Purpose**: Non-negotiable development principles enforced across all code

**Functionality**:
- Defines 7 core principles (Radical Simplicity, Fail Fast, Type Safety, Structured Models, Dependency Injection, Unit Testing, SOLID)
- Specifies code quality gates (ruff formatting, zero linting violations)
- Establishes testing requirements (mocking strategies, type hints in tests)
- Sets governance rules (principles are NON-NEGOTIABLE)

**Dependencies**: None - referenced by all agents and commands

**Usage**: Read by agents during code generation/review, enforced in all development work

**Constitutional Notes**: This IS the constitution - meta-reference. Version controlled, explicit, simple.

#### Targets Configuration (targets.txt)

**Purpose**: Define target project directories for multi-project sync

**Functionality**: Plain text file listing absolute paths to `.claude` directories, one per line

**Dependencies**: None

**Usage**: Read by sync utility to determine sync destinations

**Constitutional Notes**: Simplest possible format - plain text paths. No parsing complexity.

## Development

### Setup

**Prerequisites**:
- Claude Code (latest version)
- Python 3.11+ (for sync utility)
- Git (for version control)
- Make (for build automation)
- uv (Python package runner, optional but recommended)

**Installation Steps**:

```bash
# Clone the repository
git clone https://github.com/yourusername/dot-claude.git
cd dot-claude

# Option 1: Install to user-level Claude Code directory
make install-claude-user-folder

# Option 2: Add target projects and sync
echo "/path/to/project/.claude" >> targets.txt
make sync-to-targets
```

### Commands

**Installation & Management**:
```bash
# Install agents and commands to ~/.claude/
make install-claude-user-folder

# Uninstall from user directory
make uninstall

# Update constitution URLs in all files
make update-constitution

# Sync to all target projects
make sync-to-targets

# Clean backup files
make clean

# Show available commands
make help
```

**Direct Sync Utility**:
```bash
# Run sync utility directly with uv
uv run ./src/sync_to_targets.py

# Or with Python
python3 src/sync_to_targets.py
```

### Workflows

#### Creating Custom Agents

1. **Use Generator**: `/generate-agent "description of agent purpose"`
2. **Or Manual Creation**:
   - Create new `.md` file in `.claude/agents/`
   - Add YAML frontmatter (name, description, tools, model, color)
   - Define system prompt with role, process, and examples
   - Reference constitution for coding standards
   - Specify minimal tool access needed
3. **Test**: Invoke agent in Claude Code conversation
4. **Deploy**: Run `make sync-to-targets`

#### Creating Custom Commands

1. **Use Generator**: `/generate-command "command purpose"`
2. **Or Manual Creation**:
   - Create new `.md` file in `.claude/commands/`
   - Add YAML frontmatter (name, description, argument-hint, allowed-tools)
   - Define usage, steps, and expected behavior
   - Use Task tool to delegate to agents
3. **Test**: Run command with `/command-name`
4. **Deploy**: Run `make sync-to-targets`

#### Multi-Project Management

1. **Update Main Configuration**:
   ```bash
   vim .claude/constitution.md
   vim .claude/agents/my-agent.md
   ```

2. **Sync to All Projects**:
   ```bash
   make sync-to-targets
   ```

3. **Commit in Target Projects**:
   ```bash
   cd /path/to/project
   git add .claude/
   git commit -m "chore: update dot-claude configuration"
   git push
   ```

#### Constitutional Development Cycle

1. **Generate Spec**: `/generate-spec "requirements"`
2. **Generate Tasks**: `/generate-tasks`
3. **Execute Tasks**: `/execute-tasks` (runs executor + reviewer loop)
4. **Or Full Workflow**: `/work "implement feature X"` (spec→tasks→execute→review loop)
5. **Commit**: `/commit` when approved

### Code Standards

**All code in this project follows constitutional principles:**

- **Type Hints**: Required in ALL Python code (src/sync_to_targets.py demonstrates full type coverage)
- **Simplicity**: Keep solutions simple and maintainable (agents and commands are straightforward orchestrators)
- **Fail Fast**: Let systems fail when assumptions are violated (sync utility doesn't check if paths exist defensively)
- **Models**: Use Pydantic/dataclasses for structured data (currently using simple data structures - Path objects)
- **Dependency Injection**: Inject all dependencies, no creation in constructors (sync utility is functional, no classes)
- **SOLID**: Follow all SOLID principles in design (each agent/command has single responsibility)

**Markdown Standards**:
- YAML frontmatter for all agents and commands
- Clear section headers and structure
- Code examples in fenced blocks
- Reference constitution in agent prompts

**File Organization**:
- Agents in `.claude/agents/`
- Commands in `.claude/commands/`
- Utilities in `src/`
- Documentation in `docs/`

## Configuration

### Environment Variables

**None required** - dot-claude is configuration-based, not runtime-dependent.

### Configuration Files

**.claude/constitution.md**:
- Defines non-negotiable coding principles
- Referenced by all agents during code generation/review
- Synced to all target projects
- Version: 3.2.0 (as of 2025-01-17)

**targets.txt**:
- Lists target project `.claude` directories for sync
- One absolute path per line
- Format: `/absolute/path/to/project/.claude`
- Ignored by git (in .gitignore as `targets*`)

**.gitignore**:
- Excludes credentials, local data, personal settings
- Ignores targets* files (project-specific sync targets)
- Excludes OS files (.DS_Store, etc.)

### Dependencies

**Internal Dependencies**:
- `.claude/constitution.md`: Referenced by all agents and commands
- `.claude/agents/*`: Invoked by commands via Task tool
- `targets.txt`: Used by sync utility

**External Dependencies**:
- Python 3.11+ standard library (pathlib, shutil)
- Claude Code platform (for agents and commands)
- Make (build automation)
- Git (version control)
- uv (optional, for Python script execution)

**Injection Pattern**:
Commands inject agent dependencies through Task tool invocation. Agents receive tool access through Claude Code platform configuration (specified in frontmatter). Sync utility is functional (no DI needed - pure functions).

## Usage Examples

### Install to User Directory

```bash
cd /path/to/dot-claude
make install-claude-user-folder
# Agents and commands now available in ALL Claude Code projects
```

### Set Up Multi-Project Sync

```bash
# Create targets file
cat > targets.txt << EOF
/Users/you/projects/app1/.claude
/Users/you/projects/app2/.claude
/Users/you/projects/lib1/.claude
EOF

# Deploy to all targets
make sync-to-targets
```

### Use Slash Commands

```bash
# In Claude Code conversation:
/commit
/code-review
/work Add authentication service with JWT tokens
/generate-readme src/auth
/generate-claude-md src/services
```

### Customize Constitution

```bash
# Edit constitution
vim .claude/constitution.md

# Update all references
make update-constitution

# Deploy to projects
make sync-to-targets
```

### Create Custom Agent

```bash
# In Claude Code:
/generate-agent "SQL query optimizer that analyzes and improves database queries"

# Or manually:
cat > .claude/agents/sql-optimizer.md << 'EOF'
---
name: sql-optimizer
description: Analyzes and optimizes SQL queries. Use for database performance tuning.
tools: Read, Write, Grep, Glob
model: us.anthropic.claude-sonnet-4-5-20250929-v1:0
color: blue
---

You are an SQL optimization expert...
EOF

# Deploy
make sync-to-targets
```

### Execute Constitutional Workflow

```bash
# In Claude Code:
/work Implement user profile service with Redis caching

# This automatically:
# 1. Generates specification (constitution-spec-generator)
# 2. Creates tasks (constitution-task-generator)
# 3. Executes tasks (constitution-task-executor)
# 4. Reviews code (constitution-code-reviewer)
# 5. Refines until approved or max iterations
# 6. Produces approval document or refinement tasks
```

### Sync Utility Direct Usage

```python
# src/sync_to_targets.py demonstrates:
from pathlib import Path
import shutil

def sync_file(source: Path, target_dir: Path) -> None:
    """Copy a file to target directory."""
    target_file = target_dir / source.name
    shutil.copy2(source, target_file)
    print(f"Copied {source.name} -> {target_file}")

# Full type hints, simple implementation, fails fast
```

## Notes

### Important Considerations

- **Constitution is Central**: All agents and commands reference and enforce constitutional principles
- **Version Control**: The `.claude` directory should be version controlled with your project
- **User vs Project Level**: User-level install (`~/.claude/`) makes agents/commands available globally; project-level (`.claude/` in repo) provides project-specific configuration
- **Sync is Destructive**: `make sync-to-targets` OVERWRITES existing agents/commands/constitution in target projects
- **Git Ignore Targets**: The `targets.txt` file is ignored by git - it's personal to each developer
- **Agent Tool Access**: Agents only have access to tools specified in their frontmatter (principle of least privilege)
- **Command Delegation**: Commands should orchestrate, not implement - delegate complex work to agents

### Known Limitations

- Sync utility has no rollback mechanism (manual git revert needed if issues occur)
- Maximum 5 iterations in review-refine loop (configurable in `/work` command)
- No automated testing framework for agents/commands (manual testing required)
- No validation of agent/command YAML frontmatter (Claude Code handles this)
- Targets file must use absolute paths (relative paths not supported)

### Best Practices

1. **Agent Design**:
   - Single responsibility per agent
   - Minimal tool access
   - Clear, specific descriptions for invocation context
   - Always reference constitution in system prompt

2. **Command Design**:
   - Validate input before delegation
   - Use Task tool for complex operations
   - Provide clear usage examples
   - Give feedback on success/failure

3. **Constitution Management**:
   - Keep constitution versioned and dated
   - Sync after any constitution updates
   - Document principle additions/changes
   - Review agents for constitutional compliance

4. **Multi-Project Sync**:
   - Test changes in one project before syncing to all
   - Commit `.claude/` changes in each project separately
   - Review diffs after sync to catch unexpected changes
   - Keep targets.txt updated as projects are added/removed

5. **Constitutional Development**:
   - Use `/work` for new features requiring specification
   - Use `/execute-tasks` for existing task files
   - Review approval/refinement documents after execution
   - Commit only after constitutional approval granted

### Troubleshooting Tips

**Agents Not Available**:
- Check Claude Code can read `.claude/agents/` directory
- Verify YAML frontmatter is valid
- Ensure file has `.md` extension

**Commands Not Working**:
- Check YAML frontmatter has `allowed-tools` field
- Verify command file in `.claude/commands/`
- Test with `/` prefix (e.g., `/commit`, not `commit`)

**Sync Failing**:
- Verify targets.txt paths are absolute
- Check target directories exist (or will be created)
- Ensure write permissions on target directories
- Run with Python directly to see full errors: `python3 src/sync_to_targets.py`

**Constitutional Review Failing**:
- Check `.claude/constitution.md` exists and is readable
- Verify code follows all 7 constitutional principles
- Review linting output (run `ruff check` if available)
- Check for complexity violations (functions >10 cyclomatic complexity)

### Constitutional Reminders

- **Simplicity First**: If an agent or command seems complex, simplify it
- **Type Everything**: Even simple scripts need type hints (see sync_to_targets.py)
- **Let It Fail**: Don't add defensive checks unless explicitly needed
- **Inject Dependencies**: Commands inject agents via Task tool, not by creating them
- **Single Responsibility**: Each agent/command does ONE thing well
- **Reference Constitution**: Always point developers to `.claude/constitution.md`

---

**Built with Claude Code** | **Version**: 3.2.0 | **Last Updated**: 2025-01-17
