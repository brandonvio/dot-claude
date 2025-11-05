

review:
.claude/commands/execute-tasks.md
.claude/agents/constitution-spec-generator.md
.claude/agents/constitution-task-generator.md
.claude/agents/constitution-task-executor.md

goal:
create a constitution code reviewer agent that reviews code based on a given constitution specification. the agent should review the implementation by the constitution task executor. it should compare the implementation to the spec and tasks file and the constituion. if the code review agent finds any issues or deviations from the constitution specification, it should generate a `{filename}-r1-tasks.md` file detailing the issues found and suggesting improvements. if no issues are found, it should generate a `{filename}-r1-approval.md` file indicating that the code meets the constitution specification or otherwise intentional and documented deviations.

if issues are found:
- create a `{filename}-r1-review.md` file indicating the issues found and suggesting improvements.

update the .claude/commands/execute-tasks.md command.
In addition to running the constitution task executor, it should also run the constitution code reviewer after the task executor completes its work. 

If the the constitution code reviewer generates a `{filename}-r1-tasks.md` file, the execute-tasks command should... execute the constitution task executor again using the new tasks file... and continue this loop until the constitution code reviewer generates a `{filename}-r1-approval.md` file indicating that the code meets the constitution specification.