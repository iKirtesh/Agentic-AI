import pytest

from storage import JsonTaskStorage


def test_missing_file_returns_empty_list(tmp_path):
    assert JsonTaskStorage(tmp_path / "missing.json").load() == []


def test_invalid_json_raises_value_error(tmp_path):
    path = tmp_path / "tasks.json"
    path.write_text("{not-json", encoding="utf-8")
    with pytest.raises(ValueError, match="Invalid JSON"):
        JsonTaskStorage(path).load()


def test_storage_round_trip(tmp_path):
    storage = JsonTaskStorage(tmp_path / "nested" / "tasks.json")
    storage.save([{"id": "1", "title": "hello"}])
    assert storage.load() == [{"id": "1", "title": "hello"}]
