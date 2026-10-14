# Day 3 — Functions, Return Values, and Type Hints

**Duration:** 4 hours  
**Deliverable:** A reusable, tested Task Utilities module.

## Learning objectives
- Define and call functions.
- Use positional, keyword, and default arguments.
- Understand return values, local scope, and side effects.
- Add type hints and useful docstrings.
- Write small functions that are easy to test.
- Use pytest to test normal and edge cases.

## Study plan
1. **Hour 1:** Read [notes](notes.md), type the examples, and predict outputs.
2. **Hour 2:** Implement each utility function without copying the completed code.
3. **Hour 3:** Run the demo and complete [assignments](assignments.md).
4. **Hour 4:** Run tests, add at least two tests of your own, and explain your design.

## Run from the repository root

```bash
python python/day-03/code/task_utils.py
python python/day-03/code/demo.py
python -m pip install pytest
python -m pytest python/day-03/tests -q
```

## Files
- [Detailed notes](notes.md)
- [Assignments](assignments.md)
- [Sample answers](answers.md)
- `code/task_utils.py` — reusable task functions
- `code/demo.py` — demonstrates the utilities
- `tests/test_task_utils.py` — unit tests

## Done when
- [ ] I can explain parameters versus arguments.
- [ ] I can explain the difference between `return` and `print`.
- [ ] I can write a function with type hints and a docstring.
- [ ] I can test valid, invalid, and empty inputs.
- [ ] I can reuse the same function from multiple parts of a program.
