# Day 5 Notes — OOP, Dataclasses, Composition, and Pydantic

## 1. What is OOP?
Object-oriented programming organizes code around objects that combine data and behavior. It is useful for concepts with state, identity, and operations. It is not mandatory for every problem; ordinary functions are often simpler for small transformations.

## 2. Class and object
A class defines a kind of object. An object is an instance of that class.

```python
class Task:
    pass

first = Task()
second = Task()
print(type(first))
print(first is second)  # False
```

## 3. Constructor, attributes, and self
`__init__` initializes a newly created instance. `self` refers to that instance.

```python
class Task:
    def __init__(self, title: str, priority: str = "medium"):
        self.title = title
        self.priority = priority
        self.completed = False

    def mark_complete(self) -> None:
        self.completed = True

    def describe(self) -> str:
        status = "Done" if self.completed else "Pending"
        return f"{self.title} — {status}"

task = Task("Learn classes", "high")
task.mark_complete()
print(task.describe())
```

## 4. Instance, class, and static methods
- Instance method receives `self` and works with one object's state.
- Class method receives `cls`, often for alternate constructors or class-level behavior.
- Static method receives neither; it is a related helper.

```python
class Task:
    DEFAULT_PRIORITY = "medium"

    def __init__(self, title: str, priority: str):
        self.title = title
        self.priority = priority

    @classmethod
    def quick(cls, title: str):
        return cls(title, cls.DEFAULT_PRIORITY)

    @staticmethod
    def valid_priority(value: str) -> bool:
        return value in {"low", "medium", "high"}
```

## 5. Encapsulation and properties
Encapsulation groups state and behavior and defines how callers interact with state. Python uses conventions: `_name` means internal-use by convention; it is not a security boundary.

```python
class Task:
    def __init__(self, title: str):
        self.title = title

    @property
    def title(self) -> str:
        return self._title

    @title.setter
    def title(self, value: str) -> None:
        clean = value.strip()
        if not clean:
            raise ValueError("Title cannot be empty")
        self._title = clean
```

Use properties when controlled assignment is useful; avoid unnecessary boilerplate.

## 6. Composition
Composition models a "has-a" relationship and assembles objects from smaller objects.

```python
class User:
    def __init__(self, username: str):
        self.username = username

class TaskList:
    def __init__(self, owner: User):
        self.owner = owner
        self.tasks = []
```

A task list has an owner and contains tasks. Composition is often more flexible than deep inheritance.

## 7. Dataclasses
Dataclasses reduce boilerplate for classes primarily used to hold data.

```python
from dataclasses import dataclass, field

@dataclass
class TaskRecord:
    id: int
    title: str
    priority: str = "medium"
    completed: bool = False
    tags: list[str] = field(default_factory=list)
```

Use `field(default_factory=list)` to give each instance its own list. Do not use a shared mutable default. Dataclasses do not validate values at runtime just because annotations exist. `frozen=True` can provide a read-only value-object interface.

## 8. Pydantic v2
Pydantic parses and validates data against declared types and constraints. It is especially useful at boundaries where data arrives from users, APIs, LLMs, or tools.

```python
from typing import Literal
from pydantic import BaseModel, ConfigDict, Field

class TaskInput(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True)
    title: str = Field(min_length=1, max_length=120)
    priority: Literal["low", "medium", "high"] = "medium"
    completed: bool = False

task = TaskInput(title="Learn Pydantic", priority="high")
print(task.model_dump())
```

Useful methods:
- `model_validate(data)`: validate Python input.
- `model_dump()`: produce a Python dictionary.
- `model_dump_json()`: produce JSON text.
- `ValidationError`: raised for invalid input.

Pydantic may coerce compatible values depending on configuration. Use strict validation when coercion is not acceptable. Pydantic validation is not authorization: check permissions separately before running a tool.

## 9. Choosing a data structure
| Choice | Good fit |
|---|---|
| Dictionary | Flexible lightweight records |
| Dataclass | Internal Python data objects |
| Pydantic model | Parsing and validating external input |

You can validate external input with Pydantic and convert it to an internal dataclass, but avoid extra layers unless they provide a clear benefit.

## 10. Agentic AI connection
- Tool arguments are external data and should be validated.
- Pydantic schemas can describe accepted tool inputs.
- Dataclasses can represent internal agent state.
- Composition can connect an agent to tools, memory, and configuration.
- Model validation reduces malformed data reaching tool implementations.

## Common mistakes
1. Forgetting `self` in instance methods.
2. Confusing a class with an instance.
3. Sharing mutable defaults between dataclass instances.
4. Assuming type hints perform runtime validation.
5. Treating underscore-prefixed fields as secure secrets.
6. Using inheritance where composition is simpler.
7. Treating Pydantic as an authorization mechanism.

## Self-check
- What is the difference between a class and an object?
- Why does an instance method receive self?
- What does default_factory solve?
- When would you use a dataclass rather than Pydantic?
- Why validate tool arguments before executing a tool?
