"""Demonstrate Pydantic validation, dataclasses, and composition."""
from pydantic import ValidationError
from models import TaskInput, TaskManager


def main() -> None:
    manager = TaskManager()
    incoming = [
        {"title": "Learn classes", "priority": "high"},
        {"title": "Practice dataclasses"},
        {"title": "Validate tool arguments", "priority": "medium"},
    ]

    for item in incoming:
        task = manager.add(TaskInput.model_validate(item))
        print("Created:", task.describe())

    manager.complete(2)
    print("\nPending tasks:")
    for task in manager.pending():
        print(task.describe())

    print("\nModel as dictionary:", TaskInput(title="Review models").model_dump())

    try:
        TaskInput(title="   ", priority="urgent")
    except ValidationError as error:
        print("\nInvalid input rejected:")
        print(error)


if __name__ == "__main__":
    main()
