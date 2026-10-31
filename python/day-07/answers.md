# Day 7 Answer Guide

## Part A — Expected behavior
The application should allow a user to create tasks, list saved tasks, mark a task complete, and retrieve sample remote posts. Task data is stored locally in JSON so it survives restarts.

## Part B — Example improvements

### Remove duplicates while preserving order
```python
def unique_in_order(items):
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result
```

### Word frequency
```python
def word_frequencies(text: str) -> dict[str, int]:
    counts: dict[str, int] = {}
    for word in text.lower().split():
        counts[word] = counts.get(word, 0) + 1
    return counts
```

### Safely read JSON
```python
import json
from pathlib import Path

def read_json(path: Path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        return []
    except json.JSONDecodeError as exc:
        raise ValueError("Storage file contains invalid JSON") from exc
```

## Part C — Concepts
- Separate modules make responsibilities clear and improve testability.
- Dataclasses are convenient data containers; Pydantic models validate and parse data against declared types and constraints.
- Context managers reliably close files and HTTP clients.
- `raise_for_status()` raises an HTTPX status exception for unsuccessful response codes.
- Async is useful when waiting on multiple independent I/O operations.
- Mocking HTTP keeps tests deterministic, fast and independent of internet availability.

## Self-assessment
You are ready to move on when you can build and explain the project without copying it line by line, and can diagnose a failing test using the traceback.
