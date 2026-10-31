# Day 6 — HTTP, REST APIs, HTTPX & Async/Await

## Goals
- Understand HTTP requests, responses, methods, status codes, headers, query parameters and JSON.
- Call REST APIs with HTTPX.
- Handle HTTP, network and timeout errors.
- Use async HTTP requests concurrently.
- Test API clients without depending on the live internet.

## Setup
```bash
python -m pip install -r python/day-06/requirements.txt
```

## Run the examples
```bash
python python/day-06/code/sync_demo.py
python python/day-06/code/async_demo.py
```

## Run tests
```bash
python -m pytest python/day-06/tests -q
```

## Project
Build a reusable client for JSONPlaceholder. The implementation in `code/api_client.py` demonstrates synchronous and asynchronous fetching, query parameters, status validation, and timeouts.

## Learning order
1. Read [notes](notes.md).
2. Run both demos.
3. Complete [assignments](assignments.md).
4. Attempt the quiz before checking [answers](answers.md).
5. Run the test suite and explain each test.

## Important
JSONPlaceholder is a practice API. Its write endpoints simulate creation and updates; they do not permanently store your changes. Never put real API keys or passwords in source code.
