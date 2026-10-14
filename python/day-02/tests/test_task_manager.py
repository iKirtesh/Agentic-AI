import sys
from pathlib import Path

import pytest

CODE_DIR = Path(__file__).resolve().parents[1] / "code"
sys.path.insert(0, str(CODE_DIR))

from task_manager import add_task, complete_task, pending_tasks  # noqa: E402


def test_add_task_trims_title_and_normalizes_priority():
    tasks = []
    task = add_task(tasks, "  Learn Python  ", " HIGH ")

    assert task["title"] == "Learn Python"
    assert task["priority"] == "high"
    assert task["completed"] is False
    assert task["id"] == 1


def test_add_task_rejects_empty_title():
    with pytest.raises(ValueError, match="title"):
        add_task([], "   ")


def test_add_task_rejects_invalid_priority():
    with pytest.raises(ValueError, match="Priority"):
        add_task([], "Learn", "urgent")


def test_task_ids_increase():
    tasks = []
    first = add_task(tasks, "First")
    second = add_task(tasks, "Second")

    assert first["id"] == 1
    assert second["id"] == 2


def test_complete_task_returns_false_for_unknown_id():
    assert complete_task([], 99) is False


def test_complete_task_marks_matching_task():
    tasks = []
    task = add_task(tasks, "Write tests")

    assert complete_task(tasks, task["id"]) is True
    assert task["completed"] is True


def test_pending_tasks_only_returns_incomplete_tasks():
    tasks = []
    first = add_task(tasks, "Read notes")
    add_task(tasks, "Write code")
    complete_task(tasks, first["id"])

    assert [task["title"] for task in pending_tasks(tasks)] == ["Write code"]
