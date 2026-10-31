# Day 7 Notes — Integration and Weekly Revision

## 1. Why integration matters
Individual Python concepts become useful when combined into a working application. Keep responsibilities separate: models validate data, storage handles persistence, managers enforce business rules, API clients handle network communication, and the CLI handles user interaction.

## 2. Separation of concerns
- Model: what valid task data looks like.
- Storage: how task data is read and written.
- Manager: what operations are allowed.
- API client: how external services are called.
- CLI: how a human interacts with the program.
- Tests: whether each behavior works as expected.

This structure makes changes easier. For example, replacing JSON storage with a database should not require rewriting the CLI.

## 3. Data validation
Validate external or user-provided data at boundaries. Pydantic can validate input fields and types. Do not assume JSON from a file or external API is trustworthy.

## 4. Persistence
JSON is suitable for a small learning project. Write files with UTF-8 encoding and use a context manager. Handle missing files separately from malformed JSON. For larger or concurrent applications, use a database and appropriate transaction/locking behavior.

## 5. API integration
Use HTTPX with a timeout, call `raise_for_status()`, and handle timeout and request errors at a meaningful boundary. Reuse clients for multiple requests. Treat API response data as untrusted input.

## 6. Async integration
Use `httpx.AsyncClient` and `await` when coordinating concurrent network I/O. Use `asyncio.gather` for independent requests. Add concurrency limits and failure policies as the workload grows. Async is not a general speed boost for CPU-heavy operations.

## 7. Testing strategy
- Unit-test business rules without external services.
- Test persistence using temporary directories.
- Test HTTP behavior using `httpx.MockTransport`.
- Test failure cases as well as success cases.
- Keep tests deterministic; do not rely on a live public API.

## 8. Week 1 knowledge checklist
You should be able to explain and use:
- Python primitive types, variables and operators.
- Lists, tuples, sets, dictionaries and control flow.
- Functions, arguments, return values, scope and type hints.
- Exceptions, modules, pathlib, files, JSON and environment variables.
- Classes, dataclasses, Pydantic and composition.
- HTTP methods, status codes, headers, query parameters and JSON bodies.
- HTTPX clients, timeouts, status errors and request errors.
- Async functions, await, gather and AsyncClient.
- pytest, fixtures or temporary paths, and mocks.

## 9. Engineering habits
- Use descriptive names and small functions.
- Keep secrets out of source control.
- Validate input at system boundaries.
- Avoid swallowing exceptions silently.
- Keep network calls out of unit tests.
- Run tests after changes.
- Write a README with setup and run instructions.
