---
description: Execute the implementation planning workflow using the plan template to generate design artifacts.
---

Given the implementation details provided as an argument, do this:

1. Run `.specify/scripts/bash/setup-plan.sh --json` from the repo root and parse JSON for FEATURE_SPEC, IMPL_PLAN, SPECS_DIR, BRANCH. All future file paths must be absolute.
2. Read and analyze the feature specification to understand:
   - The feature requirements and user stories
   - Functional and non-functional requirements
   - Success criteria and acceptance criteria
   - Any technical constraints or dependencies mentioned

3. Read and internalize the constitution at `.specify/memory/constitution.md` to understand the four non-negotiable core principles that must guide all planning decisions.

4. Execute the implementation plan template with constitutional compliance:
   - Load `.specify/templates/plan-template.md` (already copied to IMPL_PLAN path)
   - Set Input path to FEATURE_SPEC
   - Run the Execution Flow (main) function steps 1-10
   - Apply constitutional principles throughout all planning phases:
     * Radical Simplicity: Choose simplest viable solutions, reject complexity increases
     * Fail Fast Philosophy: Plan for immediate failure when assumptions violated, no defensive fallbacks
     * Comprehensive Type Safety: Mandate type hints in all planned code components
     * Structured Data Models: Plan dataclasses/Pydantic for all data structures, no loose dictionaries
   - The template is self-contained and executable
   - Follow error handling and gate checks as specified
   - Let the template guide artifact generation in $SPECS_DIR:
     * Phase 0 generates research.md (with constitutional constraints applied)
     * Phase 1 generates data-model.md (using structured models only), contracts/
     * Phase 2 generates tasks.md (with constitutional compliance requirements)
   - Incorporate user-provided details from arguments into Technical Context: $ARGUMENTS
   - Enforce constitutional compliance at each phase gate
   - Update Progress Tracking as you complete each phase

5. Verify execution completed with constitutional compliance:
   - Check Progress Tracking shows all phases complete
   - Ensure all required artifacts were generated
   - Confirm no ERROR states in execution
   - Validate that all planned solutions adhere to constitutional principles
   - Verify no complexity violations exist in the final plan

6. Report results with branch name, file paths, generated artifacts, and constitutional compliance summary.

Use absolute paths with the repository root for all file operations to avoid path issues.
