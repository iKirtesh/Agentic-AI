# Day 3 Answer Key

These are example solutions. Understand the behavior and try implementing each one yourself.

## 1. Greeting

```python
def greet(name: str) -> str:
    """Return a greeting for the provided name."""
    clean_name = name.strip()
    if not clean_name:
        raise ValueError("name cannot be empty")
    return f"Hello, {clean_name}!"
```

## 2. Safe division

```python
def divide(a: float, b: float) -> float:
    """Divide a by b; reject a zero denominator."""
    if b == 0:
        raise ValueError("denominator cannot be zero")
    return a / b
```

## 3–7. Task functions

See `code/task_utils.py` for the full implementations and type hints.

## 8. Refactor principle

Call pure utility functions from your application code. Keep `input()` and `print()` near the command-line interface, not inside functions that should be reusable by a web API or AI agent.

## Optional challenge

```python
def filter_pending(tasks: list[dict]) -> list[dict]:
    """Return a new list containing incomplete tasks."""
    return [task for task in tasks if not task.get("completed", False)]
```

This creates a new list and does not remove items from the original collection.
