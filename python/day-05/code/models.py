"""Task models demonstrating Pydantic v2 and dataclasses."""
from dataclasses import dataclass, field
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field

Priority = Literal["low", "medium", "high"]


class TaskInput(BaseModel):
    """Validated task data received from an external boundary."""
    model_config = ConfigDict(str_strip_whitespace=True)

    title: str = Field(min_length=1, max_length=120)
    priority: Priority = "medium"
    completed: bool = False


@dataclass
class TaskRecord:
    """Internal task record with simple domain behavior."""
    id: int
    title: str
    priority: Priority = "medium"
    completed: bool = False
    tags: list[str] = field(default_factory=list)

    def mark_complete(self) -> None:
        self.completed = True

    def describe(self) -> str:
        status = "Done" if self.completed else "Pending"
        return f"#{self.id} {self.title} [{self.priority}] — {status}"


class TaskManager:
    """Manage task records using composition."""
    def __init__(self) -> None:
        self._tasks: list[TaskRecord] = []

    def add(self, task_input: TaskInput) -> TaskRecord:
        next_id = max((task.id for task in self._tasks), default=0) + 1
        task = TaskRecord(
            id=next_id,
            title=task_input.title,
            priority=task_input.priority,
            completed=task_input.completed,
        )
        self._tasks.append(task)
        return task

    def find(self, task_id: int) -> TaskRecord | None:
        return next((task for task in self._tasks if task.id == task_id), None)

    def complete(self, task_id: int) -> bool:
        task = self.find(task_id)
        if task is None:
            return False
        task.mark_complete()
        return True

    def pending(self) -> list[TaskRecord]:
        return [task for task in self._tasks if not task.completed]

    def all(self) -> list[TaskRecord]:
        return list(self._tasks)
