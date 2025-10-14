---
description: Execute tasks from a tasks.md file using the task-executor agent for systematic implementation
argument-hint: "path/to/tasks.md"
allowed-tools: Read, Agent
---

Execute all tasks from a specified tasks.md file using the task-executor agent for controlled, section-by-section implementation with quality controls and user oversight.

This command integrates with the spec-driven development workflow by:
1. Validating the specified tasks.md file exists
2. Invoking the task-executor agent to systematically execute tasks
3. Following constitutional principles during implementation
4. Enforcing code quality standards (linting, formatting, testing)
5. Requiring user confirmation between sections

Steps:
1. Validate that $1 (tasks.md file path) is provided
   - If no argument provided, show usage: "Usage: /implement <path/to/tasks.md>"

2. Check if the tasks.md file exists at the specified path
   - Convert relative paths to absolute paths based on current working directory
   - If file doesn't exist, show error: "Tasks file not found: $1"
   - Provide helpful suggestions like checking common locations (specs/*/tasks.md)

3. Read and validate the tasks.md file content
   - Ensure the file contains actionable tasks with checkbox format
   - If no tasks found, inform user: "No executable tasks found in $1"

4. Invoke the task-executor agent with the tasks file
   - Pass the full absolute path to the tasks.md file
   - The task-executor will handle constitutional compliance and quality controls
   - User will be prompted for confirmation between each section

5. Provide guidance on the execution process
   - Explain that work will be done section-by-section with user oversight
   - Mention that code quality checks (flake8, black, tests) will be enforced
   - Note that constitutional principles will be followed throughout

Usage Examples:
- `/implement specs/ORCH-508/single-table-refactor-lambdas/tasks.md`
- `/implement .claude/commands/tasks.md`
- `/implement tasks.md` (if in current directory)

The task-executor agent will:
- Work through tasks systematically, one section at a time
- Apply constitutional principles from `.specify/memory/constitution.md`
- Run quality checks (linting, formatting, testing) after each section
- Wait for user confirmation before proceeding to next section
- Update task checkmarks only after user approval
- Maintain controlled progress with full user oversight

Note: This command requires the task-executor agent to be available in `.claude/agents/task-executor.md`