# Day 7 — Integration Project & Week 1 Revision

## Project: Agent Task Hub
Combine Python foundations, collections, functions, exceptions, JSON persistence, data models, HTTPX and async/await in a small command-line application.

## Setup
```bash
python -m pip install -r python/day-07/requirements.txt
```

## Run
From the repository root:
```bash
python python/day-07/code/app.py
```

## Test
```bash
python -m pytest python/day-07/tests -q
```

## Structure
- `code/models.py`: Pydantic task input validation and task record.
- `code/storage.py`: JSON persistence.
- `code/manager.py`: task business logic.
- `code/api_client.py`: synchronous and asynchronous public API calls.
- `code/app.py`: CLI entry point.
- `tests/`: automated tests, including mocked HTTP requests.

## Weekly outcomes
You should be able to create reusable Python modules, validate data, persist state, call an external API safely, use async for concurrent I/O, and test behavior.

## Important
The API integration uses JSONPlaceholder for practice. Its write endpoints simulate writes and do not permanently store data. Tests use mock transports and do not require internet access.
