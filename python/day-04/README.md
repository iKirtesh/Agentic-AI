# Day 4 — Exceptions, Modules, Files, JSON, and Environment Variables

**Duration:** 4 hours  
**Project:** Persistent Task Manager

## Learning objectives
- Handle expected errors with try/except/else/finally.
- Raise meaningful exceptions and define a custom exception.
- Organize code into importable modules.
- Build safe, portable paths with pathlib.
- Read and write files using context managers.
- Serialize Python data to JSON and load it back.
- Read configuration from environment variables and optional .env files.
- Keep secrets out of Git.

## Study plan
1. **Hour 1:** Read exception handling notes and run the examples.
2. **Hour 2:** Practice modules, pathlib, and file operations.
3. **Hour 3:** Learn JSON serialization and environment configuration.
4. **Hour 4:** Run the persistent task manager, complete assignments, and execute tests.

## Run from the repository root

```bash
python -m pip install -r python/day-04/requirements.txt
python python/day-04/code/app.py
python -m pytest python/day-04/tests -q
```

Optional: copy `.env.example` to `.env` and change the non-secret app settings. Never commit real API keys.

## Files
- [Detailed notes](notes.md)
- [Assignments](assignments.md)
- [Sample answers](answers.md)
- `code/storage.py` — JSON persistence
- `code/config.py` — environment configuration
- `code/app.py` — command-line application
- `tests/test_storage.py` — storage and validation tests

## Done when
- [ ] I can handle invalid user input without crashing.
- [ ] I can explain why context managers are useful.
- [ ] I can save Python data as JSON and load it back.
- [ ] I can import code from another module.
- [ ] I can configure an app without hardcoding secrets.
- [ ] My tasks remain available after restarting the application.
