import pytest

from context_budget import calculate_context_budget
from sampling_demo import sample_token


def test_context_budget_fits():
    result = calculate_context_budget(8000, 500, 3000, 1000, 1000)
    assert result["used_tokens"] == 5500
    assert result["remaining_tokens"] == 2500
    assert result["fits"] is True


def test_context_budget_reports_overflow():
    result = calculate_context_budget(100, 40, 40, 30, 10)
    assert result["fits"] is False
    assert result["remaining_tokens"] == -20


def test_context_budget_rejects_negative_values():
    with pytest.raises(ValueError):
        calculate_context_budget(100, -1, 0, 0, 0)


def test_sampling_is_reproducible_with_seed():
    probabilities = {"a": 0.7, "b": 0.2, "c": 0.1}
    assert sample_token(probabilities, 0.7, seed=42) == sample_token(
        probabilities, 0.7, seed=42
    )


def test_sampling_rejects_invalid_temperature():
    with pytest.raises(ValueError):
        sample_token({"a": 1.0}, 0)


def test_sampling_rejects_invalid_probability_sum():
    with pytest.raises(ValueError):
        sample_token({"a": 0.4, "b": 0.4}, 1.0)
