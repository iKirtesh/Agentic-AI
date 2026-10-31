# Day 7 Assignments — Agent Task Hub

## Part A: Build and understand
1. Run the application and inspect each module.
2. Create a task with a title and description.
3. List all tasks.
4. Mark a task completed.
5. Confirm the task survives an application restart.
6. Fetch one remote post.
7. Fetch three remote posts concurrently.

## Part B: Improve the project
1. Add task priorities: low, medium and high.
2. Add a due date and validate its format.
3. Add a command to delete a task.
4. Add filtering by completion status.
5. Add a maximum length for task titles.
6. Add a user-friendly message for invalid menu input.
7. Add a test for malformed JSON storage.

## Part C: Weekly coding assessment
1. Write a function that counts word frequencies in a string.
2. Write a function that removes duplicate values while preserving order.
3. Create a dataclass representing a user.
4. Read a JSON file safely, handling a missing file.
5. Use HTTPX to retrieve a resource with a timeout.
6. Use asyncio.gather to fetch independent resources concurrently.
7. Write a pytest test for a function that raises an exception.

## Part D: Explain without notes
- Why should business logic not live entirely inside the CLI?
- What is the difference between a dataclass and a Pydantic model?
- Why use a context manager for a file or HTTP client?
- What does raise_for_status() do?
- When should you use async/await?
- Why should tests mock external HTTP calls?

## Completion checklist
- [ ] Application starts successfully.
- [ ] Task creation and listing work.
- [ ] Completion status is persisted.
- [ ] Invalid input is rejected.
- [ ] API request works when internet is available.
- [ ] Async example works.
- [ ] Unit tests pass.
- [ ] I can explain the architecture.
