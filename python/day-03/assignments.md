# Day 3 Assignments

Try each task before reading `answers.md`.

## 1. Greeting function
Write `greet(name: str) -> str` that returns a greeting. It should not print inside the function.

## 2. Safe division
Write `divide(a: float, b: float) -> float`. Raise `ValueError` when the denominator is zero.

## 3. Normalize a title
Write `normalize_title(title: str) -> str` that trims surrounding whitespace and rejects an empty title.

## 4. Priority validation
Write `validate_priority(priority: str) -> str` that accepts `low`, `medium`, or `high`, case-insensitively, and returns a lowercase value. Raise `ValueError` for anything else.

## 5. Create a task
Write a typed function that takes an ID, title, and optional priority (default `medium`) and returns a dictionary with `id`, `title`, `priority`, and `completed=False`.

## 6. Find and complete a task
Write `find_task_by_id(tasks, task_id)` that returns the matching dictionary or `None`. Then write `complete_task(tasks, task_id) -> bool` that returns whether a task was found and completed.

## 7. Summarize tasks
Return a dictionary containing total, completed, pending, and completion percentage. Empty input must return a percentage of `0.0` without division by zero.

## 8. Refactor
Use your functions in a small script instead of repeating validation or task-search logic. Keep input/output separate from business logic.

## Optional challenge
Write a function that accepts a list of task dictionaries and returns a new list of incomplete tasks without changing the original list.

## Required tests
Write at least eight unit tests, including:
- normal valid input
- whitespace around a title
- empty title
- valid and invalid priorities
- an unknown task ID
- completing an existing task
- empty task summary
- all tasks completed

## Submission checklist
- [ ] Functions have clear names.
- [ ] Public functions have type hints and docstrings.
- [ ] Invalid input has defined behavior.
- [ ] Tests cover normal and edge cases.
- [ ] No secrets or API keys are committed.
