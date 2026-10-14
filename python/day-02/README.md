# Day 2 — Python Collections and Control Flow

**Duration:** 4 hours  
**Project:** Command-line Task Manager

## Learning objectives
- Use lists, tuples, sets, and dictionaries.
- Read and modify collection elements with indexing, slicing, and methods.
- Make decisions with `if`, `elif`, and `else`.
- Repeat work with `for` and `while`.
- Use `enumerate()`, `zip()`, membership tests, and list comprehensions.
- Build and test a small task manager.

## Suggested schedule
1. **60 min — Concepts:** Read [notes](notes.md) and type every example yourself.
2. **90 min — Build:** Run the code in `code/` and modify it.
3. **45 min — Assignments:** Complete [assignments](assignments.md) without looking at answers.
4. **30 min — Tests/review:** Run the tests and test edge cases.
5. **15 min — Notes:** Explain each collection and loop in your own words.

## Run the examples
From this directory:

```bash
python code/collections_demo.py
python code/task_manager.py
```

Run tests from this directory (install pytest first if needed):

```bash
python -m pip install pytest
python -m pytest -q
```

## Files
- [Detailed notes](notes.md)
- [Assignments](assignments.md)
- [Answer key](answers.md)
- `code/collections_demo.py` — examples of collections and control flow
- `code/task_manager.py` — runnable command-line task manager
- `tests/test_task_manager.py` — automated tests

## Done when
- [ ] You can explain when to use a list, tuple, set, and dictionary.
- [ ] You can loop through a list and a dictionary.
- [ ] You can filter tasks with a list comprehension.
- [ ] You can add, list, and complete tasks in the CLI.
- [ ] You can explain why a task ID/index must be validated before use.
