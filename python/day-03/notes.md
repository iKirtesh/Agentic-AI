# Day 3 Notes — Functions and Reusable Code

## 1. Why functions?

A function packages a task behind a name. Instead of repeating validation logic in several places, write it once and call it whenever needed.

```python
def greet(name):
    return f"Hello, {name}!"

message = greet("Kirtesh")
print(message)
```

- `def` starts a function definition.
- `name` is a parameter.
- `"Kirtesh"` is an argument passed to the function.
- `return` sends a result back to the caller.

## 2. Parameters and arguments

### Positional arguments
Values are matched to parameters by their position.

```python
def subtract(a, b):
    return a - b

print(subtract(10, 3))  # 7
```

### Keyword arguments
Values are matched by parameter name.

```python
print(subtract(a=10, b=3))
```

Keyword arguments can improve readability, especially when a function has several parameters.

### Default parameters
A default value is used when the caller omits that argument.

```python
def create_greeting(name: str, prefix: str = "Hello") -> str:
    return f"{prefix}, {name}!"

print(create_greeting("Asha"))
print(create_greeting("Asha", prefix="Welcome"))
```

Use immutable defaults such as strings, numbers, or `None`. Avoid mutable defaults such as `tasks=[]`; that list would be shared between calls.

## 3. Return versus print

`print()` displays information. `return` makes a value available to the caller.

```python
def add_for_display(a: int, b: int) -> None:
    print(a + b)

def add(a: int, b: int) -> int:
    return a + b

result = add(2, 3)  # result is 5
```

A function that reaches the end without a return statement returns `None`. A function can print and return, but reusable business logic should generally return results rather than printing them directly.

## 4. Type hints

Type hints communicate intended input and output types. Python does not automatically enforce them at runtime.

```python
def calculate_total(prices: list[float]) -> float:
    """Return the sum of the provided prices."""
    return sum(prices)
```

Useful annotations:
- `str`: string
- `int`: integer
- `float`: floating-point number
- `bool`: Boolean
- `None`: no meaningful return value
- `list[str]`: list of strings
- `dict[str, object]`: dictionary with string keys and mixed values
- `str | None`: either a string or `None` (Python 3.10+)

Type hints are documentation and tooling support, not a substitute for validating untrusted user input.

## 5. Docstrings

A docstring describes a function's purpose, arguments, and return behavior.

```python
def is_even(number: int) -> bool:
    """Return True if number is divisible by two."""
    return number % 2 == 0
```

Prefer clear names and short docstrings that explain behavior. Document important exceptions and assumptions where appropriate.

## 6. Local scope

Variables created inside a function are local to that call.

```python
def calculate_area(width: float, height: float) -> float:
    area = width * height
    return area

print(calculate_area(3, 4))
# print(area)  # NameError: area is local to the function
```

Pass dependencies as arguments and return results rather than relying on hidden global state.

## 7. Pure functions and side effects

A pure function:
1. Returns the same result for the same inputs.
2. Does not change state outside itself.

```python
def normalize_title(title: str) -> str:
    return title.strip()
```

A function that modifies a task dictionary, writes a file, sends a network request, or prints output has a side effect. Side effects are sometimes necessary, but isolating them makes code easier to test.

## 8. Validation and exceptions

A function should clearly define what happens for invalid input. It may return a failure value or raise an exception, depending on its contract.

```python
def percentage(part: float, total: float) -> float:
    if total <= 0:
        raise ValueError("total must be greater than zero")
    return part / total * 100
```

Raise a meaningful exception when the caller supplied an invalid argument. Catch exceptions at a boundary where you can respond usefully; do not hide errors with a broad empty `except`.

## 9. Functions over task data

```python
def find_task(tasks: list[dict], task_id: int) -> dict | None:
    """Return the task with the requested ID, or None."""
    for task in tasks:
        if task.get("id") == task_id:
            return task
    return None
```

This function separates the search operation from the menu or user interface. A caller can decide whether to print an error, ask again, or record a result.

## 10. Keep functions focused

Prefer functions that do one understandable job:
- `normalize_title()`: clean a title.
- `validate_priority()`: validate a priority.
- `create_task()`: construct a new task record.
- `find_task_by_id()`: search for a task.
- `complete_task()`: update completion status.
- `summarize_tasks()`: calculate counts and percentage.

Avoid a single giant function that validates input, updates data, prints output, and handles every menu option.

## 11. Connection to agentic AI

Agent systems are easier to reason about when they are composed of small functions:
- An input-validation function checks tool arguments.
- A tool function performs one action.
- A parser function converts an API response into useful data.
- A decision function returns which action should happen next.
- Tests verify each unit without requiring a live LLM call.

Do not confuse a regular Python function with an AI agent. A function executes its defined logic; an agent typically combines model-driven decisions, state, and tool execution in a controlled loop.

## 12. Common mistakes
1. Forgetting to call a function after defining it.
2. Printing a value when the caller needs to use it.
3. Forgetting that a function without an explicit return yields `None`.
4. Using a mutable default such as `items=[]`.
5. Assuming type hints validate input at runtime.
6. Making one function responsible for too many tasks.
7. Catching every exception and silently ignoring it.
8. Testing only the happy path.

## Self-review
- Can I explain the difference between a parameter and an argument?
- Can I write a function that returns a value and test it?
- Can I explain why `tasks=[]` is a risky default argument?
- Can I separate business logic from printing?
- Can I test empty collections and unknown IDs?
