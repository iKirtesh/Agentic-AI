import sys
from pathlib import Path

import pytest

CODE_DIR = Path(__file__).resolve().parents[1] / "code"
sys.path.insert(0, str(CODE_DIR))

from task_utils import (  # noqa: E402
    complete_task,
    create_task,
    filter_pending,
    find_task_by_id,
    normalize_title,
    summarize_tasks,
    validate_priority,
)


def test_normalize_title_trims_whitespace():
    assert normalize_title("  Learn Python  ") == "Learn Python"


def test_normalize_title_rejects_empty_string():
    with pytest.raises(ValueError, match="cannot be empty"):
        normalize_title("   ")


def test_validate_priority_normalizes_case():
    assert validate_priority(" HIGH ") == "high"


def test_validate_priority_rejects_unknown_value():
    with pytest.raises(ValueError, match="Priority"):
        validate_priority("urgent")


def test_create_task_has_expected_fields():
    task = create_task(1, "Write tests", "medium")
    assert task == {
        "id": 1,
        "title": "Write tests",
        "priority": "medium",
        "completed": False,
    }


def test_create_task_rejects_nonpositive_id():
    with pytest.raises(ValueError, match="positive"):
        create_task(0, "Task")


def test_find_task_by_id_returns_task():
    task = create_task(1, "Read notes")
    assert find_task_by_id([task], 1) is task


def test_find_task_by_id_returns_none_for_missing_id():
    assert find_task_by_id([], 123) is None


def test_complete_task_updates_existing_task():
    task = create_task(1, "Finish lesson")
    assert complete_task([task], 1) is True
    assert task["completed"] is True


def test_complete_task_returns_false_for_missing_id():
    assert complete_task([], 10) is False


def test_filter_pending_returns_only_incomplete_tasks():
    done = create_task(1, "Done")
    pending = create_task(2, "Pending")
    done["completed"] = True

    result = filter_pending([done, pending])

    assert result == [pending]
    assert len([done, pending]) == 2


def test_summary_for_empty_list_avoids_division_by_zero():
    assert summarize_tasks([]) == {
        "total": 0,
        "completed": 0,
        "pending": 0,
        "completion_percentage": 0.0,
    }


def test_summary_for_all_completed_tasks():
    first = create_task(1, "First")
    second = create_task(2, "Second")
    first["completed"] = True
    second["completed"] = True

    summary = summarize_tasks([first, second])

    assert summary["total"] == 2
    assert summary["completed"] == 2
    assert summary["pending"] == 0
    assert summary["completion_percentage"] == 100.0
