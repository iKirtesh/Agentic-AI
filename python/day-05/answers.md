# Day 5 Answer Key

Attempt the exercises first. These are reference solutions.

## Task class
```python
class Task:
    def __init__(self, title: str, priority: str = "medium"):
        clean = title.strip()
        if not clean:
            raise ValueError("Title cannot be empty")
        self.title = clean
        self.priority = priority
        self.completed = False

    def mark_complete(self) -> None:
        self.completed = True

    def describe(self) -> str:
        status = "Done" if self.completed else "Pending"
        return f"{self.title} — {status}"
```

## Composition
```python
class User:
    def __init__(self, username: str):
        self.username = username

class TaskList:
    def __init__(self, owner: User):
        self.owner = owner
        self.tasks = []
```

## Dataclass
```python
from dataclasses import dataclass, field

@dataclass
class TaskRecord:
    id: int
    title: str
    tags: list[str] = field(default_factory=list)
```

Each instance receives a separate tags list.

## Pydantic
See code/models.py for a Pydantic v2 input model with title constraints and a Literal priority. Use model_dump() to produce a Python dictionary.

## Design advice
Validate untrusted input at the boundary, then use an internal model for domain behavior. Keep authorization checks separate from schema validation.
