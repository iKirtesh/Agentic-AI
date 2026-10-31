from pydantic import ValidationError

from models import TaskInput, TaskRecord
from storage import JsonTaskStorage


class TaskManager:
    def __init__(self, storage: JsonTaskStorage):
        self.storage = storage

    def list_tasks(self) -> list[TaskRecord]:
        return [TaskRecord.model_validate(item) for item in self.storage.load()]

    def create_task(self, title: str, description: str = "") -> TaskRecord:
        data = TaskInput(title=title, description=description)
        task = TaskRecord(title=data.title.strip(), description=data.description)
        tasks = self.storage.load()
        tasks.append(task.model_dump())
        self.storage.save(tasks)
        return task

    def complete_task(self, task_id: str) -> TaskRecord:
        tasks = self.storage.load()
        for index, item in enumerate(tasks):
            if item.get("id") == task_id:
                updated = TaskRecord.model_validate({**item, "completed": True})
                tasks[index] = updated.model_dump()
                self.storage.save(tasks)
                return updated
        raise KeyError(f"No task found with ID: {task_id}")
