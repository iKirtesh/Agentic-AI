# Day 2 Assignments

**Rule:** Attempt the exercises before opening `answers.md`. Type your own solution rather than copying it.

## Assignment 1 — List operations
Create a list of five skills. Print the first and last skills, print the first three skills, add one skill, and remove one skill.

**Expected skills:** indexing, slicing, `append()`, `remove()`.

## Assignment 2 — Remove duplicates
Given `tools = ["search", "python", "search", "calculator", "python"]`, create a collection of unique tools. Explain whether your chosen collection preserves the original order.

## Assignment 3 — Task dictionary
Create a dictionary for a task with `id`, `title`, `priority`, and `completed`. Print the title and safely read an optional `due_date`.

## Assignment 4 — Priority decision
Given a priority string, print:
- `Do this soon` for `high`
- `Schedule this` for `medium`
- `Low urgency` for `low`
- `Unknown priority` for any other value

## Assignment 5 — Loop and enumerate
Print each task from a list with a user-facing number starting at 1. The first list item is still at index 0.

## Assignment 6 — Filter pending tasks
Given a list of task dictionaries, use a list comprehension to create a list containing only tasks where `completed` is `False`.

## Assignment 7 — zip two lists
Combine a list of three task names and a list of three durations. Print each task with its duration. Then remove one duration and observe how `zip()` behaves.

## Assignment 8 — Build the CLI Task Manager
Use `code/task_manager.py` as a starting point or write your own version. It must:
1. Add a task.
2. List tasks with IDs, priorities, and completion status.
3. Mark a task completed.
4. Filter and display pending tasks.
5. Quit without an infinite loop.
6. Handle invalid menu choices and invalid task IDs without crashing.

## Optional challenge — Summary report
Display the total number of tasks, number completed, number pending, and completion percentage. Avoid division by zero when the task list is empty.

## Submission checklist
- [ ] I wrote the code myself.
- [ ] I tested empty input and an invalid task ID.
- [ ] I can explain each collection used.
- [ ] I ran `python -m pytest -q`.
- [ ] I can explain my solution without reading it line by line.
