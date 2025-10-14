---
description: Generate individual test commands in services/Makefile for all test files
allowed-tools: Glob, Read, Write
---

Generate individual test commands in the services/Makefile for all test_*.py files found in the services/tests/ directory. This allows engineers to run specific tests using make targets like `make test_metadata_service` instead of remembering full pytest paths.

Steps:
1. Scan the services/tests/ directory recursively for all test_*.py files
2. Read the current services/Makefile to preserve existing content
3. Generate make targets for each test file using the pattern `test_{filename}`
4. Handle duplicate filenames by adding directory context (e.g., `test_metadata_service_metadata`)
5. Update the Makefile with the new individual test targets in an auto-generated section
6. Provide summary of generated commands

Process:

1. **Discover Test Files**: Find all test_*.py files in services/tests/
2. **Generate Unique Targets**: Create make targets with unique names for each test file
3. **Update Makefile**: Add/update generated targets in services/Makefile
4. **Report Results**: Show what commands were added/updated

The generated make targets will:
- Use the existing pytest pattern from run-unit-tests
- Handle nested directory structures properly
- Use relative paths from the services directory context
- Resolve naming conflicts by adding directory context
- Allow easy execution like `make test_metadata_service`

Implementation:

1. First, discover all test files:

2. Generate the individual test commands by reading current Makefile and creating new section:

3. Create make targets for each test file, handling duplicates by adding directory context:
   - `test_metadata_service` → `tests/shared/services/test_metadata_service.py`
   - `test_metadata_service_metadata` → `tests/shared/services/metadata/test_metadata_service.py`

4. Update the services/Makefile with auto-generated section:
   ```makefile
   # Auto-generated individual test commands
   test_combine_textract_files:
   	python -m pytest tests/combine_textract_files/test_combine_textract_files.py

   test_metadata_service:
   	python -m pytest tests/shared/services/test_metadata_service.py

   test_metadata_service_metadata:
   	python -m pytest tests/shared/services/metadata/test_metadata_service.py
   ```

5. Generate comprehensive list covering all 36+ test files found in the repository

Generated Commands Summary:
- **Lambda Function Tests**: `test_classify_file`, `test_get_gbd_document`, `test_preprocess_document`, etc.
- **Shared Service Tests**: `test_s3_service`, `test_kafka_service`, `test_filenet_service`, etc.
- **DynamoDB Tests**: `test_db_service`, `test_gbd_ingestion_client`, `test_doc_ingestion_client`, etc.
- **Model Tests**: `test_core`, `test_document`
- **Integration Tests**: `test_extraction_service_contract`, `test_document_service_contract`

Usage Examples:
```bash
# Run specific lambda function test
make test_classify_file

# Run shared service tests
make test_metadata_service
make test_s3_service

# Run database tests
make test_db_service
make test_gbd_ingestion_client

# Run model tests
make test_document
make test_core
```

This command is rerunnable - it will update the Makefile with any new test files discovered while preserving existing content. The auto-generated section will be replaced each time to ensure it stays current with the test file structure.

**Total Generated**: 36 individual test commands covering all test_*.py files in the services/tests/ directory structure.