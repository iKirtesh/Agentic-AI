"""Tests for the Day 1 task assistant and practice exercises."""

from python.day_01.code.exercises import analyze_text, calculate_study_hours, estimate_tokens
from python.day_01.code.task_assistant import summarize_task


def test_summarize_task_includes_details() -> None:
    summary = summarize_task("DODO", "Learn Python", 2, 2.0)

    assert "Owner: DODO" in summary
    assert "Task: Learn Python" in summary
    assert "Priority: 2" in summary
    assert "Estimated duration: 2.0 hours" in summary
    assert "Status: Pending" in summary


def test_calculate_study_hours() -> None:
    assert calculate_study_hours(4, 30) == 120


def test_estimate_tokens() -> None:
    assert estimate_tokens(3, 100, 50) == {
        "input_tokens": 300,
        "output_tokens": 150,
        "total_tokens": 450,
    }


def test_analyze_text_is_case_insensitive_for_python() -> None:
    result = analyze_text("I am learning PYTHON")

    assert result["contains_python"] is True
    assert result["character_count"] == len("I am learning PYTHON")


def test_analyze_text_without_python() -> None:
    result = analyze_text("Learning programming")

    assert result["contains_python"] is False
