---
description: Generate individual test commands in Makefile for all test files
allowed-tools: Glob, Read, Write
---

Generate individual test commands in the Makefile for all test_*.py files found in the tests/ directory. This allows engineers to run specific tests using make targets like `make test_service_name` instead of remembering full pytest paths.

Steps:
1. Scan the tests/ directory recursively for all test_*.py files
2. Read the current Makefile to preserve existing content
3. Generate make targets for each test file using the pattern `test_{filename}`
4. Handle duplicate filenames by adding directory context (e.g., `test_service_name_submodule`)
5. Update the Makefile with the new individual test targets in an auto-generated section
6. Provide summary of generated commands

Process:

1. **Discover Test Files**: Find all test_*.py files in tests/
2. **Generate Unique Targets**: Create make targets with unique names for each test file
3. **Update Makefile**: Add/update generated targets in Makefile
4. **Report Results**: Show what commands were added/updated

The generated make targets will:
- Use the existing pytest pattern from the test runner
- Handle nested directory structures properly
- Use relative paths from the project root
- Resolve naming conflicts by adding directory context
- Allow easy execution like `make test_service_name`

Implementation:

1. First, discover all test files in the tests/ directory

2. Generate the individual test commands by reading current Makefile and creating new section

3. Create make targets for each test file, handling duplicates by adding directory context:
   - `test_service_name` → `tests/services/test_service_name.py`
   - `test_service_name_submodule` → `tests/services/submodule/test_service_name.py`

4. Update the Makefile with auto-generated section:
   ```makefile
   # Auto-generated individual test commands
   test_service_name:
   	python -m pytest tests/services/test_service_name.py

   test_utils:
   	python -m pytest tests/utils/test_utils.py

   test_integration:
   	python -m pytest tests/integration/test_integration.py
   ```

5. Generate comprehensive list covering all test files found in the repository

Generated Commands Summary:
- **Service Tests**: Individual make targets for each service test file
- **Utility Tests**: Individual make targets for utility test files
- **Integration Tests**: Individual make targets for integration test files
- **Unit Tests**: Individual make targets for unit test files

Usage Examples:
```bash
# Run specific service test
make test_service_name

# Run utility tests
make test_utils

# Run integration tests
make test_integration
```

This command is rerunnable - it will update the Makefile with any new test files discovered while preserving existing content. The auto-generated section will be replaced each time to ensure it stays current with the test file structure.