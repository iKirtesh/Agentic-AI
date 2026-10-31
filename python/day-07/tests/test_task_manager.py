import pytest

from manager import TaskManager
from storage import JsonTaskStorage


def test_create_and_list_task(tmp_path):
    manager = TaskManager(JsonTaskStorage(tmp_path / "tasks.json"))
    created = manager.create_task("Learn Python", "Week one project")
    tasks = manager.list_tasks()
    assert len(tasks) == 1
    assert tasks[0].id == created.id
    assert tasks[0].title == "Learn Python"
    assert tasks[0].completed is False


def test_complete_task_persists(tmp_path):
    manager = TaskManager(JsonTaskStorage(tmp_path / "tasks.json"))
    task = manager.create_task("Write tests")
    completed = manager.complete_task(task.id)
    assert completed.completed is True
    assert manager.list_tasks()[0].completed is True


def test_missing_task_raises_key_error(tmp_path):
    manager = TaskManager(JsonTaskStorage(tmp_path / "tasks.json"))
    with pytest.raises(KeyError):
        manager.complete_task("missing-id")


def test_empty_title_is_rejected(tmp_path):
    manager = TaskManager(JsonTaskStorage(tmp_path / "tasks.json"))
    with pytest.raises(ValueError):
        manager.create_task("")
