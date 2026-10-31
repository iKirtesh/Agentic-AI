# Day 4 Assignments

Try these before checking `answers.md`.

## 1. Safe integer input
Write a function that converts text to an integer. Handle `ValueError` and return a clear message or raise a meaningful error.

## 2. Custom exception
Create `TaskNotFoundError`. Write a task lookup function that raises it when an ID does not exist.

## 3. Module practice
Create `math_utils.py` with functions for addition, subtraction, and multiplication. Import and call them from another file.

## 4. pathlib practice
Create a `data` directory if it does not exist. Build a path to `notes.txt` using pathlib, write text, and read it back.

## 5. JSON conversion
Convert a Python dictionary to JSON text and back. Explain the difference between `dumps` and `loads`.

## 6. JSON file persistence
Save a list of task dictionaries to `tasks.json`, restart your script, and load the saved tasks.

## 7. Environment variables
Read `APP_ENV` with a default of `development`. Read `OPENAI_API_KEY` without printing its value. If it is missing, display a safe configuration message.

## 8. Persistent Task Manager
Use `code/storage.py` and `code/app.py` as a reference or build your own application. It must:
- Add tasks.
- List saved tasks.
- Mark tasks completed.
- Filter pending tasks.
- Save changes to JSON.
- Load data when the application starts.
- Handle missing or malformed files without an unhandled traceback.

## Optional challenge
Implement an atomic JSON save: write to a temporary file in the same directory, then replace the destination with the temporary file. Clean up the temporary file if replacement fails.

## Tests
Write at least eight tests for missing files, round-trip persistence, invalid JSON, wrong JSON shape, adding a task, completing a task, missing task IDs, and empty data.

## Submission checklist
- [ ] I used try/except for expected failures.
- [ ] I used pathlib for paths.
- [ ] I can explain JSON serialization.
- [ ] I can load saved tasks after restarting.
- [ ] No real secrets or API keys are committed.
- [ ] I ran the test suite.
