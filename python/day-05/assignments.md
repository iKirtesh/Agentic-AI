# Day 5 Assignments

Try these before opening answers.md.

1. **Book class:** Create a Book class with title, author, and year. Create two objects.
2. **Task methods:** Create a Task class with mark_complete() and describe().
3. **Property:** Reject an empty task title using a property setter.
4. **Class and static methods:** Add a class method that creates a default-priority task and a static method that checks allowed priorities.
5. **Composition:** Create User and TaskList classes. A TaskList has an owner and contains tasks.
6. **Dataclass:** Create a task dataclass with tags using field(default_factory=list). Prove two instances do not share a list.
7. **Pydantic:** Create a v2 model with title (1–120 chars), priority (low/medium/high), and completed (default False). Test valid and invalid inputs.
8. **Conversion:** Use model_dump() and explain how it differs from dataclasses.asdict().
9. **Optional challenge:** Build a task manager using Pydantic for incoming input and a dataclass for internal task records.

## Required tests
Write at least eight tests covering valid input, blank title, too-long title, invalid priority, default values, task completion, independent default lists, and unknown IDs.

## Checklist
- [ ] Understand class vs object.
- [ ] Write instance methods.
- [ ] Explain composition.
- [ ] Use a safe dataclass mutable default.
- [ ] Validate input with Pydantic.
- [ ] Run the test suite.
