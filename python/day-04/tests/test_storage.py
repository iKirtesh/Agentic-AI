import sys
from pathlib import Path

import pytest

CODE_DIR = Path(__file__).resolve().parents[1] / "code"
sys.path.insert(0, str(CODE_DIR))

from app import add_task, complete_task  # noqa: E402
from storage import StorageError, load_tasks, save_tasks  # noqa: E402


def sample_tasks():
    return [{
        "id": 1,
        "title": "Learn JSON",
        "priority": "high",
        "completed": False,
    }]


def test_missing_file_returns_empty_list(tmp_path):
    assert load_tasks(tmp_path / "missing.json") == []


def test_save_and_load_round_trip(tmp_path):
    path = tmp_path / "nested" / "tasks.json"
    tasks = sample_tasks()
    save_tasks(path, tasks)
    assert load_tasks(path) == tasks


def test_invalid_json_raises_storage_error(tmp_path):
    path = tmp_path / "tasks.json"
    path.write_text("{not valid json", encoding="utf-8")
    with pytest.raises(StorageError, match="Could not read"):
        load_tasks(path)


def test_wrong_top_level_json_type_raises_storage_error(tmp_path):
    path = tmp_path / "tasks.json"
    path.write_text('{"task": "not a list"}', encoding="utf-8")
    with pytest.raises(StorageError, match="JSON array"):
        load_tasks(path)


def test_invalid_task_shape_raises_storage_error(tmp_path):
    path = tmp_path / "tasks.json"
    path.write_text('[{"id": 1}]', encoding="utf-8")
    with pytest.raises(StorageError, match="missing required"):
        load_tasks(path)


def test_add_task_validates_and_normalizes():
    tasks = []
    task = add_task(tasks, "  Build agent  ", " HIGH ")
    assert task["title"] == "Build agent"
    assert task["priority"] == "high"
    assert task["id"] == 1


def test_add_task_rejects_empty_title():
    with pytest.raises(ValueError, match="empty"):
        add_task([], "  ")


def test_complete_task_updates_matching_task():
    tasks = sample_tasks()
    assert complete_task(tasks, 1) is True
    assert tasks[0]["completed"] is True


def test_complete_task_returns_false_for_unknown_id():
    assert complete_task(sample_tasks(), 99) is False


def test_saved_tasks_survive_reload(tmp_path):
    path = tmp_path / "tasks.json"
    tasks = sample_tasks()
    save_tasks(path, tasks)
    restored = load_tasks(path)
    assert restored[0]["title"] == "Learn JSON"
    assert restored[0]["completed"] is False
