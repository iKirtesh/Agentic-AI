# Day 1 Assignment Answers — Python Fundamentals

These are reference solutions. Try each assignment yourself before reading the answer. There are multiple valid ways to solve most programming problems.

## Assignment 1 — Personal introduction

**File:** `answer_01_introduction.py`

```python
name = "DODO"
learning_goal = "learn Agentic AI"
programming_language = "Python"
daily_study_hours = 4

print(
    f"My name is {name}. I want to {learning_goal}. "
    f"I am learning {programming_language} for "
    f"{daily_study_hours} hours per day."
)
```

**Why it works:** Variables store the information, and the f-string inserts their values into readable text.

## Assignment 2 — Study-time calculator

**File:** `answer_02_study_calculator.py`

```python
hours_per_day = float(input("Study hours per day: "))
number_of_days = int(input("Number of days: "))

total_hours = hours_per_day * number_of_days

print(f"Total study hours: {total_hours:.1f}")
```

Example: entering `4` hours and `30` days produces `Total study hours: 120.0`.

**Why it works:** `input()` returns strings, so the values are converted before multiplication.

## Assignment 3 — Token estimate

**File:** `answer_03_token_estimate.py`

```python
request_count = int(input("Number of requests: "))
input_tokens_per_request = int(input("Input tokens per request: "))
output_tokens_per_request = int(input("Output tokens per request: "))

total_input_tokens = request_count * input_tokens_per_request
total_output_tokens = request_count * output_tokens_per_request
total_tokens = total_input_tokens + total_output_tokens

print(f"Estimated input tokens: {total_input_tokens}")
print(f"Estimated output tokens: {total_output_tokens}")
print(f"Estimated combined tokens: {total_tokens}")
print("Note: This estimates token volume, not provider billing.")
```

Example: 3 requests, 100 input tokens, and 50 output tokens per request results in 300 input tokens, 150 output tokens, and 450 combined tokens.

## Assignment 4 — String analyzer

**File:** `answer_04_string_analyzer.py`

```python
sentence = input("Enter a sentence: ")

print(f"Original: {sentence}")
print(f"Character count: {len(sentence)}")
print(f"Uppercase: {sentence.upper()}")
print(f"Lowercase: {sentence.lower()}")
print(f"Contains Python: {'python' in sentence.lower()}")
```

**Optional case-insensitive challenge:** The final line uses `sentence.lower()`, so it matches `Python`, `PYTHON`, or `python`.

## Assignment 5 — Task summary

**File:** `answer_05_task_summary.py`

```python
owner = input("Enter your name: ").strip()
task = input("Enter task title: ").strip()
description = input("Enter task description: ").strip()
priority = int(input("Priority (1-3): "))
estimated_hours = float(input("Estimated hours: "))

priority_labels = {
    1: "Low",
    2: "Medium",
    3: "High",
}

if priority not in priority_labels:
    print("Invalid priority. Choose 1, 2, or 3.")
else:
    estimated_minutes = estimated_hours * 60

    print("\n--- Task Summary ---")
    print(f"Owner: {owner}")
    print(f"Task: {task}")
    print(f"Description: {description}")
    print(f"Priority: {priority_labels[priority]}")
    print(f"Estimated duration: {estimated_hours:.1f} hours")
    print(f"Estimated duration: {estimated_minutes:.0f} minutes")
    print("Status: Pending")

    if estimated_hours > 4:
        print("Warning: This task is estimated to take more than four hours.")
```

This reference solution checks whether priority is valid. It does not yet handle text entered where a number is expected; exception handling is covered later in the roadmap.

## Assignment 6 — Debug the snippets

### A. Input and arithmetic

Incorrect:

```python
age = input("Age: ")
print(age + 1)
```

Correct:

```python
age = int(input("Age: "))
print(age + 1)
```

**Explanation:** `input()` returns a string. Convert the input to an integer before adding a number.

### B. Equality

Incorrect:

```python
count = 5
print(count = 5)
```

Correct:

```python
count = 5
print(count == 5)
```

**Explanation:** `=` assigns a value; `==` compares values and produces a Boolean result.

### C. Indentation

Incorrect:

```python
if 3 > 2:
print("Correct")
```

Correct:

```python
if 3 > 2:
    print("Correct")
```

**Explanation:** The body of the `if` statement must be indented.

### D. Conversion

Incorrect for the intended numeric conversion:

```python
requests = int("many")
```

Safer beginner solution when the input must be numeric:

```python
requests_text = input("Number of requests: ")
requests = int(requests_text)
print(f"Requests: {requests}")
```

**Explanation:** `int("many")` raises `ValueError`. This corrected example expects a valid integer. Handling invalid entries with `try/except` is a follow-up task.

## Optional challenge — Input validation

**File:** `answer_07_validated_task.py`

```python
def read_non_empty(prompt: str) -> str:
    """Keep asking until the user enters non-empty text."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("This field cannot be empty.")


def read_priority() -> int:
    """Read a priority in the range 1 through 3."""
    while True:
        raw_value = input("Priority (1-3): ").strip()
        try:
            priority = int(raw_value)
        except ValueError:
            print("Enter a whole number: 1, 2, or 3.")
            continue

        if priority in (1, 2, 3):
            return priority
        print("Priority must be 1, 2, or 3.")


def read_non_negative_hours() -> float:
    """Read a non-negative duration."""
    while True:
        raw_value = input("Estimated hours: ").strip()
        try:
            hours = float(raw_value)
        except ValueError:
            print("Enter a valid number, such as 1 or 1.5.")
            continue

        if hours >= 0:
            return hours
        print("Estimated hours cannot be negative.")


def main() -> None:
    owner = read_non_empty("Name: ")
    task = read_non_empty("Task title: ")
    priority = read_priority()
    hours = read_non_negative_hours()

    priority_labels = {1: "Low", 2: "Medium", 3: "High"}
    print("\n--- Task Summary ---")
    print(f"Owner: {owner}")
    print(f"Task: {task}")
    print(f"Priority: {priority_labels[priority]}")
    print(f"Estimated duration: {hours:.1f} hours")


if __name__ == "__main__":
    main()
```

**Why it works:** `try/except` catches invalid numeric conversions, while loops allow the program to request a valid value again. The functions each handle one responsibility.

## Self-review checklist

- [ ] I typed the solutions rather than only copying them.
- [ ] I can explain each variable and conversion.
- [ ] I tested at least two normal inputs per program.
- [ ] I tried edge cases such as empty text, invalid numbers, and priority 4.
- [ ] I can explain why each debugging example failed.

## Run your solutions

Save each code block in its own `.py` file, then run it from the terminal:

```bash
python answer_01_introduction.py
```

Repeat with the filename for each assignment. Keep your own solutions separate from the original exercise prompts so you can revisit the work later.
