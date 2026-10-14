# Day 1 Assignments

Complete these exercises independently before looking up solutions. Use only the concepts introduced in Day 1 unless an optional challenge says otherwise.

## Assignment 1 — Personal introduction (easy)

Create variables for a name, learning goal, preferred programming language, and daily study hours. Print a formatted introduction using an f-string.

**Acceptance criteria**
- Use at least four variables.
- Include an f-string.
- Output is readable and correctly formatted.

## Assignment 2 — Study-time calculator (easy)

Ask the user for daily study hours and number of days. Display the total study hours.

**Acceptance criteria**
- Convert numeric input before performing arithmetic.
- Test with 4 hours per day for 30 days; expected total: 120 hours.
- Display the result clearly.

## Assignment 3 — Token estimate (medium)

Ask for:
- Number of requests
- Estimated input tokens per request
- Estimated output tokens per request

Calculate total estimated input tokens, output tokens, and combined tokens.

**Acceptance criteria**
- Convert all numeric input.
- Use meaningful variable names.
- Explain that these are estimates, not a provider billing calculation.

## Assignment 4 — String analyzer (medium)

Ask the user for a sentence. Print:
- Original sentence
- Character count
- Uppercase sentence
- Lowercase sentence
- Whether the sentence contains the word `Python`

**Acceptance criteria**
- Use `len()`, `.upper()`, `.lower()`, and the `in` operator.
- Try sentences with and without the word.

**Optional challenge:** Make the membership check case-insensitive.

## Assignment 5 — Task summary (medium)

Extend `code/task_assistant.py`:
- Add a task description.
- Display estimated duration in minutes.
- Map priority 1, 2, and 3 to Low, Medium, and High.
- Warn when the duration exceeds four hours.

**Acceptance criteria**
- Use clear variable names and f-strings.
- Test all three priority levels.
- Test a duration below and above four hours.

## Assignment 6 — Debug these snippets (medium)

For each snippet, explain the error and correct it.

### A. Input and arithmetic

```python
age = input("Age: ")
print(age + 1)
```

### B. Equality

```python
count = 5
print(count = 5)
```

### C. Indentation

```python
if 3 > 2:
print("Correct")
```

### D. Conversion

```python
requests = int("many")
```

## Optional challenge — Add input validation

Update the task assistant so it:
- Rejects blank task titles.
- Accepts only priorities 1, 2, or 3.
- Rejects negative estimated hours.
- Shows a helpful message when a numeric value cannot be parsed.

You may need to learn `try/except` early for this challenge; the topic is formally covered on Day 4.

## Submission checklist

- [ ] Save solutions in separate Python files or clearly named functions.
- [ ] Run each program with at least two input examples.
- [ ] Test one invalid or edge-case input.
- [ ] Add a short explanation of your approach.
- [ ] Commit your work to Git with a descriptive message.
