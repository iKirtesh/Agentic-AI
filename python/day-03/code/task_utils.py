"""Reusable task utilities for Day 3 Python practice.

The functions in this module can be imported by a CLI, API, or agent tool.
"""
from typing import TypedDict


Priority = str


class Task(TypedDict):
    id: int
    title: str
    priority: str
    completed: bool


VALID_PRIORITIES = {"low", "medium", "high"}


def normalize_title(title: str) -> str:
    """Trim a task title and reject an empty result."""
    clean_title = title.strip()
    if not clean_title:
        raise ValueError("Task title cannot be empty.")
    return clean_title


def validate_priority(priority: str = "medium") -> Priority:
    """Return a lowercase valid priority or raise ValueError."""
    clean_priority = priority.strip().lower()
    if clean_priority not in VALID_PRIORITIES:
        raise ValueError("Priority must be low, medium, or high.")
    return clean_priority


def create_task(
    task_id: int,
    title: str,
    priority: str = "medium",
) -> Task:
    """Create a validated task record with an incomplete status."""
    if task_id < 1:
        raise ValueError("Task ID must be a positive integer.")

    return {
        "id": task_id,
        "title": normalize_title(title),
        "priority": validate_priority(priority),
        "completed": False,
    }


def find_task_by_id(tasks: list[Task], task_id: int) -> Task | None:
    """Return a matching task, or None when the ID is not present."""
    for task in tasks:
        if task["id"] == task_id:
            return task
    return None


def complete_task(tasks: list[Task], task_id: int) -> bool:
    """Mark a matching task complete; return False for an unknown ID."""
    task = find_task_by_id(tasks, task_id)
    if task is None:
        return False
    task["completed"] = True
    return True


def filter_pending(tasks: list[Task]) -> list[Task]:
    """Return a new list containing only incomplete tasks."""
    return [task for task in tasks if not task["completed"]]


def summarize_tasks(tasks: list[Task]) -> dict[str, int | float]:
    """Return task counts and completion percentage."""
    total = len(tasks)
    completed = sum(1 for task in tasks if task["completed"])
    pending = total - completed
    percentage = completed / total * 100 if total else 0.0

    return {
        "total": total,
        "completed": completed,
        "pending": pending,
        "completion_percentage": round(percentage, 1),
    }


def main() -> None:
    """Run a small demonstration of the utility functions."""
    tasks = [
        create_task(1, "  Learn functions  ", "HIGH"),
        create_task(2, "Write unit tests"),
    ]
    complete_task(tasks, 1)

    print("Pending tasks:")
    for task in filter_pending(tasks):
        print(f'#{task["id"]}: {task["title"]}')

    print("Summary:", summarize_tasks(tasks))


if __name__ == "__main__":
    main()
