"""Small JSON persistence layer for the Day 4 task manager."""
import json
from pathlib import Path
from typing import Any


class StorageError(Exception):
    """Raised when stored task data cannot be read or validated."""


def load_tasks(path: Path) -> list[dict[str, Any]]:
    """Load task dictionaries from JSON; return [] if the file is absent."""
    if not path.exists():
        return []

    try:
        raw_data = path.read_text(encoding="utf-8")
        data = json.loads(raw_data)
    except (OSError, json.JSONDecodeError) as error:
        raise StorageError(f"Could not read task data from {path}: {error}") from error

    if not isinstance(data, list):
        raise StorageError("Task data must be a JSON array.")

    for index, task in enumerate(data):
        if not isinstance(task, dict):
            raise StorageError(f"Task at position {index} must be a JSON object.")
        required = {"id", "title", "priority", "completed"}
        if not required.issubset(task):
            raise StorageError(f"Task at position {index} is missing required fields.")
        if not isinstance(task["id"], int) or isinstance(task["id"], bool):
            raise StorageError(f"Task ID at position {index} must be an integer.")
        if not isinstance(task["title"], str):
            raise StorageError(f"Task title at position {index} must be text.")
        if task["priority"] not in {"low", "medium", "high"}:
            raise StorageError(f"Task priority at position {index} is invalid.")
        if not isinstance(task["completed"], bool):
            raise StorageError(f"Task completion status at position {index} must be Boolean.")

    return data


def save_tasks(path: Path, tasks: list[dict[str, Any]]) -> None:
    """Write task dictionaries as formatted UTF-8 JSON."""
    path.parent.mkdir(parents=True, exist_ok=True)
    try:
        serialized = json.dumps(tasks, indent=2, ensure_ascii=False)
        temporary_path = path.with_suffix(path.suffix + ".tmp")
        temporary_path.write_text(serialized + "\n", encoding="utf-8")
        temporary_path.replace(path)
    except (OSError, TypeError, ValueError) as error:
        raise StorageError(f"Could not save task data to {path}: {error}") from error
