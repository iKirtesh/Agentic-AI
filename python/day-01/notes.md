# Day 1 Notes — Python Fundamentals

## 1. Python and the interpreter

Python is a general-purpose programming language used for scripting, backend APIs, automation, data work, and AI applications. Python code is commonly executed by the Python interpreter.

Check the installation:

```bash
python --version
```

Create and activate a virtual environment to isolate project dependencies.

Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

macOS/Linux:

```bash
python -m venv .venv
source .venv/bin/activate
```

## 2. First program

```python
print("Hello, Agentic AI!")
print(10 + 20)
```

`print()` displays values. Python executes statements in order.

## 3. Indentation and comments

Python uses indentation to define code blocks. Four spaces per indentation level is the usual convention.

```python
if 10 > 5:
    print("The condition is true")
```

A comment begins with `#`:

```python
# This is a comment
language = "Python"
```

Unlike Java, Python usually does not use braces to define blocks.

## 4. Variables and naming

A variable is a name bound to a value.

```python
task_name = "Learn Python"
retry_count = 3
estimated_hours = 1.5
is_completed = False
```

Python is dynamically typed: you do not declare a variable's type before assigning it. Names are case-sensitive. Use descriptive `snake_case` names for variables and functions.

Prefer:

```python
model_name = "example-model"
request_count = 5
```

over unclear names such as `x` or `a` when the meaning matters.

## 5. Common built-in types

| Type | Example | Meaning |
|---|---|---|
| `str` | `"hello"` | Text |
| `int` | `42` | Whole number |
| `float` | `3.14` | Floating-point number |
| `bool` | `True` | Boolean value |
| `NoneType` | `None` | Absence of a value |

Inspect a value with `type(value)`. Python Boolean literals are `True` and `False`, with capital first letters.

## 6. Operators

Arithmetic:

| Operator | Meaning | Example |
|---|---|---|
| `+` | Addition | `2 + 3 == 5` |
| `-` | Subtraction | `5 - 2 == 3` |
| `*` | Multiplication | `3 * 4 == 12` |
| `/` | Division | `7 / 2 == 3.5` |
| `//` | Floor division | `7 // 2 == 3` |
| `%` | Remainder | `7 % 2 == 1` |
| `**` | Exponentiation | `2 ** 3 == 8` |

Comparisons include `==`, `!=`, `>`, `<`, `>=`, and `<=`. They return Boolean values.

Logical operators are `and`, `or`, and `not`.

**Remember:** `=` assigns a value; `==` compares values.

## 7. Type conversion and user input

`input()` always returns a string.

```python
age_text = input("Age: ")
age = int(age_text)
```

Use `float()` for decimal values and `str()` to convert a value to text. Conversion can fail: `int("hello")` raises `ValueError`. Handle invalid input when building robust applications.

A subtle truth-value rule:

```python
bool("")       # False
bool("False")  # True, because the string is nonempty
```

Do not use `bool(user_input)` to parse textual yes/no values.

## 8. Strings

Strings represent text. Both single and double quotes are valid.

```python
name = "Agent"
message = 'Hello'
```

Useful operations:

```python
text = "  Learn Python  "
text.strip()       # "Learn Python"
text.lower()       # "  learn python  "
text.upper()       # "  LEARN PYTHON  "
text.replace("Python", "AI")
len(text)          # Number of characters
"Python" in text   # Membership test
```

Strings are immutable: methods such as `strip()` return a new string rather than modifying the original string.

Indexing begins at zero. For `language = "Python"`, `language[0]` is `"P"`, and `language[-1]` is `"n"`. Slicing `language[0:3]` returns `"Pyt"`; the end index is excluded.

## 9. F-strings

F-strings insert values and expressions into text.

```python
name = "Learner"
hours = 4
print(f"{name} will study for {hours} hours.")
print(f"Total for 30 days: {hours * 30} hours")
```

Format a floating-point value to two decimal places with `f"{value:.2f}"`.

## 10. Mini-project design

The Day 1 task assistant collects a task owner, title, priority, and estimated duration, then prints a summary.

Current scope:
- Basic interactive input and output.
- Variables, numeric conversion, and f-strings.
- No database, network, or LLM integration yet.

Known limitation: invalid numeric input can raise an exception. Later lessons will cover validation and exception handling.

## 11. Connection to Agentic AI

These basics support later agent engineering:

- Strings represent user messages and prompts.
- Dictionaries and lists will represent structured data and message histories.
- Booleans support conditions and permission checks.
- Numeric types support counters, limits, timing, and cost calculations.
- Functions and modules will help organize tools and agent logic.
- Input validation prevents malformed data from entering a workflow.

## 12. Review questions

1. Why does `input()` return a string?
2. What is the difference between `=` and `==`?
3. What is the result of `10 // 3` and `10 % 3`?
4. Why is `bool("False")` true?
5. What does `.strip()` do?
6. What does the format specifier `:.2f` mean?
7. Why should code avoid hard-coded API secrets?

## 13. End-of-day reflection

Record your own answers before moving on:

- Concepts I can explain:
- Exercises completed:
- Errors I encountered and how I fixed them:
- One concept I need to revisit:
- Git commit hash:
