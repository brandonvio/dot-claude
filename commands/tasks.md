---
description: Generate an actionable, dependency-ordered tasks.md for the feature based on available design artifacts.
---

Given the context provided as an argument, do this:

1. Run `.specify/scripts/bash/check-task-prerequisites.sh --json` from repo root and parse FEATURE_DIR and AVAILABLE_DOCS list. All paths must be absolute.
2. Load and analyze available design documents with constitutional awareness:
   - Always read plan.md for tech stack and libraries
   - Reference `.specify/memory/constitution.md` to understand non-negotiable implementation principles
   - IF EXISTS: Read data-model.md for entities (must use structured data models)
   - IF EXISTS: Read contracts/ for API endpoints
   - IF EXISTS: Read research.md for technical decisions

   Note: Not all projects have all documents. For example:
   - CLI tools might not have contracts/
   - Simple libraries might not need data-model.md
   - Generate tasks based on what's available, always applying constitutional principles

3. Generate tasks following the template with constitutional compliance:
   - Use `.specify/templates/tasks-template.md` as the base
   - Replace example tasks with actual tasks based on:
     * **Setup tasks**: Project init, dependencies, linting (with type checking tools)
     * **Test tasks [P]**: One per contract, one per integration scenario (all with type hints)
     * **Core tasks**: One per entity (using dataclasses/Pydantic), service, CLI command, endpoint
     * **Integration tasks**: DB connections, middleware, logging (fail-fast implementations)
     * **Polish tasks [P]**: Unit tests (with comprehensive type hints), performance, docs
   - Ensure all tasks enforce constitutional principles in their implementation requirements

4. Task generation rules with constitutional requirements:
   - Each contract file → contract test task marked [P] (with comprehensive type hints)
   - Each entity in data-model → model creation task marked [P] (using Pydantic/dataclasses only)
   - Each endpoint → implementation task (not parallel if shared files, fail-fast error handling)
   - Each user story → integration test marked [P] (with type safety throughout)
   - Different files = can be parallel [P]
   - Same file = sequential (no [P])
   - All tasks must specify constitutional compliance requirements in their descriptions

5. Order tasks by dependencies:
   - Setup before everything
   - Tests before implementation (TDD)
   - Models before services
   - Services before endpoints
   - Core before integration
   - Everything before polish

6. Include parallel execution examples:
   - Group [P] tasks that can run together
   - Show actual Task agent commands

7. Create FEATURE_DIR/tasks.md with constitutional enforcement:
   - Correct feature name from implementation plan
   - Numbered tasks (T001, T002, etc.)
   - Clear file paths for each task
   - Dependency notes
   - Parallel execution guidance
   - Constitutional compliance requirements embedded in each task description
   - Explicit reminders about simplicity, type hints, structured data models, and fail-fast approaches

Context for task generation: $ARGUMENTS

The tasks.md should be immediately executable with constitutional compliance - each task must be specific enough that an LLM can complete it following all non-negotiable principles without additional context.
