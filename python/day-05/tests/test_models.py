import sys
from pathlib import Path

import pytest
from pydantic import ValidationError

CODE_DIR = Path(__file__).resolve().parents[1] / "code"
sys.path.insert(0, str(CODE_DIR))

from models import TaskInput, TaskManager, TaskRecord  # noqa: E402


def test_valid_task_input_and_defaults():
    task = TaskInput(title="Learn Pydantic", priority="high")
    assert task.title == "Learn Pydantic"
    assert task.priority == "high"
    assert task.completed is False


def test_title_whitespace_is_stripped():
    assert TaskInput(title="  Learn classes ").title == "Learn classes"


def test_blank_title_is_rejected():
    with pytest.raises(ValidationError):
        TaskInput(title="   ")


def test_too_long_title_is_rejected():
    with pytest.raises(ValidationError):
        TaskInput(title="x" * 121)


def test_invalid_priority_is_rejected():
    with pytest.raises(ValidationError):
        TaskInput(title="Task", priority="urgent")


def test_model_dump_returns_python_dict():
    assert TaskInput(title="Review").model_dump() == {
        "title": "Review", "priority": "medium", "completed": False
    }


def test_dataclass_instances_have_separate_tag_lists():
    first = TaskRecord(id=1, title="First")
    second = TaskRecord(id=2, title="Second")
    first.tags.append("python")
    assert first.tags == ["python"]
    assert second.tags == []


def test_manager_add_and_complete():
    manager = TaskManager()
    task = manager.add(TaskInput(title="Build tool"))
    assert task.id == 1
    assert manager.complete(task.id) is True
    assert task.completed is True


def test_manager_unknown_id_returns_false():
    assert TaskManager().complete(999) is False


def test_manager_pending_excludes_completed_tasks():
    manager = TaskManager()
    manager.add(TaskInput(title="Pending"))
    completed = manager.add(TaskInput(title="Done"))
    manager.complete(completed.id)
    assert [task.title for task in manager.pending()] == ["Pending"]


def test_manager_all_returns_new_list():
    manager = TaskManager()
    manager.add(TaskInput(title="Keep"))
    returned = manager.all()
    returned.clear()
    assert len(manager.all()) == 1
