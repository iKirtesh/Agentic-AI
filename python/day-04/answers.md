# Day 4 Answer Key

These are sample approaches. Try the assignments independently first.

## 1. Safe integer conversion

```python
def parse_integer(value: str) -> int:
    try:
        return int(value)
    except ValueError as error:
        raise ValueError("Please provide a whole number.") from error
```

## 2. Custom exception

```python
class TaskNotFoundError(Exception):
    pass


def find_task(tasks: list[dict], task_id: int) -> dict:
    for task in tasks:
        if task["id"] == task_id:
            return task
    raise TaskNotFoundError(f"Task {task_id} was not found.")
```

## 3. Module practice

Define functions in `math_utils.py`, then import them using `from math_utils import add` in a script in the same importable directory.

## 4. pathlib practice

```python
from pathlib import Path

data_dir = Path("data")
data_dir.mkdir(parents=True, exist_ok=True)
notes_path = data_dir / "notes.txt"
notes_path.write_text("Day 4 practice", encoding="utf-8")
print(notes_path.read_text(encoding="utf-8"))
```

## 5. JSON conversion

```python
import json

task = {"id": 1, "title": "Practice JSON", "completed": False}
text = json.dumps(task, indent=2)
restored = json.loads(text)
assert restored == task
```

`dumps` converts a Python value to JSON text; `loads` parses JSON text into Python values.

## 6–8. Persistent Task Manager

See `code/storage.py` for JSON loading and saving, and `code/app.py` for the menu and task operations. The test file shows how to test persistence using a temporary directory.

## 7. Environment variable

```python
import os

app_env = os.getenv("APP_ENV", "development")
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    print("OPENAI_API_KEY is not configured.")
```

Never print or commit the key itself.
