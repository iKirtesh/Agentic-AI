# Day 4 Notes — Exceptions, Modules, Files, JSON, and Environment Variables

## 1. What is an exception?

An exception is an event that interrupts normal program execution. Examples include converting invalid text to an integer, opening a missing file, or parsing malformed JSON.

```python
number = int("hello")  # ValueError
```

If an exception is not handled, the program stops and Python displays a traceback.

## 2. try and except

Put code that may fail inside `try`, and handle the specific expected error in `except`.

```python
try:
    age = int(input("Enter age: "))
except ValueError:
    print("Please enter a whole number.")
else:
    print(f"Age: {age}")
```

- `try`: code that may raise an exception.
- `except`: handles a matching exception.
- `else`: runs only when the try block completes without an exception.
- `finally`: runs whether or not an exception occurred, commonly for cleanup.

```python
try:
    file = open("notes.txt", encoding="utf-8")
except FileNotFoundError:
    print("File does not exist.")
else:
    print(file.read())
    file.close()
finally:
    print("File operation finished.")
```

Prefer a context manager with `with open(...)` for files; it closes the file automatically.

## 3. Catch specific errors

Good:

```python
try:
    value = int("abc")
except ValueError as error:
    print(f"Invalid integer: {error}")
```

Avoid catching every exception with a bare `except:` or silently ignoring errors. Broad handling can hide programming bugs. Catch the errors you expect and can handle meaningfully.

## 4. Raise exceptions

Use `raise` when a function detects invalid input.

```python
def percentage(part: float, total: float) -> float:
    if total <= 0:
        raise ValueError("total must be greater than zero")
    return part / total * 100
```

Useful built-in exceptions:
- `ValueError`: correct type, invalid value.
- `TypeError`: operation receives an inappropriate type.
- `FileNotFoundError`: requested file does not exist.
- `PermissionError`: process lacks permission.
- `KeyError`: dictionary key does not exist.
- `JSONDecodeError`: input is not valid JSON.

You can create a custom exception for a domain-specific error:

```python
class TaskNotFoundError(Exception):
    """Raised when a task ID cannot be found."""
```

## 5. Modules and imports

A module is a Python file that contains reusable code.

Example structure:

```text
project/
  app.py
  storage.py
  config.py
```

In `storage.py`:

```python
def load_tasks():
    return []
```

In `app.py`:

```python
from storage import load_tasks

tasks = load_tasks()
```

Other import styles:

```python
import json
from pathlib import Path
from datetime import datetime, timezone
```

Prefer explicit imports. Avoid `from module import *`, which makes it harder to know where names came from.

The check `if __name__ == "__main__":` runs a module's demo/application code only when that file is executed directly, not when imported.

## 6. File paths with pathlib

Hardcoded paths can behave differently on Windows, macOS, and Linux. `pathlib.Path` provides portable path operations.

```python
from pathlib import Path

project_dir = Path(__file__).resolve().parent
data_dir = project_dir / "data"
data_dir.mkdir(parents=True, exist_ok=True)

data_file = data_dir / "tasks.json"
print(data_file.exists())
```

Useful methods:
- `Path(__file__)`: path of the current source file.
- `.resolve()`: produce an absolute resolved path.
- `/ "filename"`: join path components.
- `.parent`: parent directory.
- `.mkdir(parents=True, exist_ok=True)`: create directories safely.
- `.exists()`: check whether a path exists.
- `.is_file()`: check whether it is a file.

## 7. Read and write text files

Use `with` so Python closes the file even if an error occurs.

```python
from pathlib import Path

path = Path("notes.txt")

path.write_text("Hello Python\n", encoding="utf-8")
content = path.read_text(encoding="utf-8")
print(content)
```

For larger files or streaming, use:

```python
with path.open("r", encoding="utf-8") as file:
    for line in file:
        print(line.rstrip())
```

Common modes:
- `"r"`: read.
- `"w"`: write, replacing existing contents.
- `"a"`: append.
- `"x"`: create a new file, failing if it exists.

Always choose an encoding such as UTF-8 when handling text.

## 8. JSON

JSON (JavaScript Object Notation) is a text format used to exchange structured data. It is widely used in APIs and configuration files.

Python values map to JSON values:

| Python | JSON |
|---|---|
| dict | object |
| list | array |
| str | string |
| int / float | number |
| True / False | true / false |
| None | null |

Write JSON:

```python
import json

task = {"id": 1, "title": "Learn JSON", "completed": False}
json_text = json.dumps(task, indent=2)
print(json_text)
```

Read JSON text:

```python
loaded_task = json.loads(json_text)
print(loaded_task["title"])
```

Write/read JSON files:

```python
from pathlib import Path
import json

path = Path("tasks.json")
tasks = [{"id": 1, "title": "Learn JSON", "completed": False}]

path.write_text(json.dumps(tasks, indent=2), encoding="utf-8")
loaded_tasks = json.loads(path.read_text(encoding="utf-8"))
```

- `json.dumps(value)`: Python object to JSON string.
- `json.loads(text)`: JSON string to Python object.
- `json.dump(value, file)`: write JSON to file.
- `json.load(file)`: read JSON from file.

JSON supports basic data types, not every Python object. For example, a datetime must be converted to a string or another supported representation before serialization.

Validate loaded data. A syntactically valid JSON file might still have the wrong structure or missing fields. Treat files as untrusted input.

## 9. Safe JSON persistence

A robust storage layer should:
1. Create its data directory when necessary.
2. Return an empty collection when the file does not exist.
3. Handle malformed JSON clearly.
4. Check that the decoded top-level value is the expected type.
5. Write using UTF-8 and readable indentation.

For important data, consider writing to a temporary file and then replacing the original file. This reduces the risk of leaving a partially written file if a process stops during a write. JSON files are suitable for small local exercises, not concurrent multi-user databases.

## 10. Environment variables

Environment variables hold configuration outside your source code.

```python
import os

app_env = os.getenv("APP_ENV", "development")
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    print("API key is not configured.")
```

Never write real API keys or passwords directly into source files or Git commits.

On Windows PowerShell, set a variable for the current terminal session:

```powershell
$env:APP_ENV = "development"
```

On macOS/Linux:

```bash
export APP_ENV=development
```

## 11. .env files

A local `.env` file stores development configuration as KEY=VALUE lines. It is not loaded automatically by Python. A common library is `python-dotenv`.

Install it:

```bash
python -m pip install python-dotenv
```

Load it near application startup:

```python
from dotenv import load_dotenv
import os

load_dotenv()
app_env = os.getenv("APP_ENV", "development")
```

Commit a safe `.env.example` with placeholder values, but add the actual `.env` to `.gitignore`. If a secret is accidentally committed, deleting it in a later commit is not sufficient; rotate/revoke the exposed credential.

## 12. Connection to agentic AI

- Conversation history can be saved as JSON during early prototypes.
- Tool configuration can be read from environment variables.
- Exceptions allow an agent application to handle tool failures and invalid inputs.
- Modules separate tool implementations, storage, configuration, and application logic.
- File persistence lets a local prototype recover state after a restart.

For production agent systems, use an appropriate database for concurrent access, stronger validation, backups, and access control rather than treating a JSON file as a complete memory system.

## 13. Common mistakes
1. Using a bare `except` and hiding errors.
2. Forgetting that `"w"` replaces file contents.
3. Building paths by concatenating strings instead of using pathlib.
4. Forgetting UTF-8 encoding.
5. Confusing `json.dumps` with `json.dump`.
6. Assuming valid JSON is automatically valid application data.
7. Assuming Python loads `.env` automatically.
8. Committing a real API key.
9. Using a local JSON file for concurrent multi-user writes.

## Day 4 self-check
- Why should you catch a specific exception?
- What does a context manager do?
- What is the difference between `json.load` and `json.loads`?
- Why is pathlib preferable to manually concatenating paths?
- Why should API keys be stored outside source code?
- What happens if a JSON file is missing or malformed?
