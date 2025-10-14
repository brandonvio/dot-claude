---
description: Generate or update comprehensive documentation for the document classification system
argument-hint: "Optional: specific component (file|llm|xlsx) to focus documentation on"
allowed-tools: Read, Write, Glob, Grep, Bash
---

Generate or update comprehensive documentation for the document classification system in `/docs/classifier.md`. If the documentation already exists, intelligently update only relevant sections based on recent git commits.

The classifier system includes:
- `classify_file` Lambda function (rule-based classification)
- `classify_file_llm` Lambda function (AI-powered classification)
- `classify_xlsx` Lambda function (Excel file classification)
- DynamoDB classification rule tables
- Integration with document processing pipeline

Steps:
1. Check if `/docs/classifier.md` exists and get its last modification date
2. If document exists, analyze git commits since last modification to identify relevant changes
3. Analyze classifier Lambda functions in `services/functions/`
4. Examine DynamoDB table schemas for classification rules
5. Review test files to understand classification behavior and examples
6. Check integration points with other services
7. Generate or update documentation with:
   - System architecture overview
   - Classification workflow and decision tree
   - Rule-based vs LLM-based classification approaches
   - DynamoDB table structures and data flow
   - Configuration and environment variables
   - Usage examples and test cases
   - Integration with document processing pipeline
   - Troubleshooting and monitoring guidance

Usage examples:
- `/document-classifier` - Generate complete documentation
- `/document-classifier file` - Focus on file-level classification
- `/document-classifier llm` - Focus on LLM classification approach
- `/document-classifier xlsx` - Focus on Excel file classification

The command will create comprehensive documentation that serves as both technical reference and onboarding guide for the classification system.