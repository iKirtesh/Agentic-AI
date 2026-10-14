# Python for Agentic AI

This folder contains a structured Python curriculum for the first month of the Agentic AI roadmap.

## Daily learning format

Each day should include:

1. **Learning objectives** — what you should understand by the end.
2. **Notes** — concepts, examples, and common mistakes.
3. **Runnable code** — small examples connected to the day's topics.
4. **Assignments** — tasks to solve independently.
5. **Tests/review** — verify behavior and record what you learned.

## Month 1 — Python learning sequence

| Day | Topic | Practical outcome |
|---|---|---|
| 01 | Setup, syntax, variables, data types, operators, strings, input/output | CLI task assistant |
| 02 | Lists, tuples, sets, dictionaries, conditions, loops | Task manager with filtering |
| 03 | Functions, parameters, return values, type hints | Reusable task utilities |
| 04 | Exceptions, modules, paths, JSON and environment variables | Persistent task storage |
| 05 | Classes, dataclasses, composition and Pydantic | Validated task model |
| 06 | HTTP, JSON APIs, httpx, async/await and timeouts | Resilient API client |
| 07 | pytest, fixtures, mocking and Git | Tested Python mini-project |
| 08–14 | LLM concepts, prompting, API integration, structured output, context, reliability | AI bug-triage assistant |
| 15–21 | Tool calling, execution, search, agent loop, state and guardrails | Tool-using developer agent |
| 22–30 | FastAPI, persistence, frontend, testing, security, Docker and evaluation | Full-stack AI developer assistant |

## Setup

From the repository root:

```bash
python --version
python -m venv .venv
```

Activate the environment on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Activate on macOS/Linux:

```bash
source .venv/bin/activate
```

Day 1 uses only the Python standard library. Run the examples directly:

```bash
python python/day-01/code/hello.py
python python/day-01/code/task_assistant.py
python python/day-01/code/exercises.py
```

Run the Day 1 tests after installing pytest:

```bash
python -m pip install pytest
python -m pytest python/day-01/tests -q
```

## Learning rule

Do not mark a day complete just because you read the notes. Run the code, complete the assignments, explain the key ideas in your own words, and test at least one edge case.


## Day 2 — Collections and control flow

Open the [Day 2 lesson](day-02/README.md) for detailed notes, assignments, answers, runnable examples, and tests.

Run the examples from the repository root:

```bash
python python/day-02/code/collections_demo.py
python python/day-02/code/task_manager.py
python -m pytest python/day-02/tests -q
```


## Day 3 — Functions and reusable code

Open the [Day 3 lesson](day-03/README.md) for detailed notes, assignments, sample answers, runnable utilities, and unit tests.

Run the examples from the repository root:

```bash
python python/day-03/code/task_utils.py
python python/day-03/code/demo.py
python -m pytest python/day-03/tests -q
```
