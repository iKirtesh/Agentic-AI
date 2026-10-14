# Day 2 Notes — Collections and Control Flow

## 1. Why collections matter

A variable stores one reference/value; a collection groups related values. An AI application might store a conversation as a list of messages, represent one message as a dictionary, and track unique tool names with a set.

## 2. Lists

A list is ordered, mutable, and allows duplicates.

```python
tasks = ["Study Python", "Build an agent", "Study Python"]
print(tasks[0])       # Study Python
print(tasks[-1])      # Study Python
print(tasks[0:2])     # ['Study Python', 'Build an agent']
tasks.append("Write tests")
tasks[1] = "Build a task manager"
tasks.remove("Study Python")  # removes the first matching item
last_task = tasks.pop()       # removes and returns the last item
```

Important:
- Indexing starts at `0`; negative indices count from the end.
- Slices use `sequence[start:stop]`; the stop position is excluded.
- `append(x)` adds one item; `extend(items)` adds multiple items.
- `sort()` modifies a list in place. `sorted(items)` returns a new sorted list.
- Accessing an invalid index raises `IndexError`.

## 3. Tuples

A tuple is ordered and immutable. Use it for a fixed group of values.

```python
coordinates = (18.52, 73.86)
print(coordinates[0])
# coordinates[0] = 20.0  # TypeError: tuples cannot be changed
```

A one-item tuple needs a comma: `single = ("Python",)`. Parentheses alone do not make a tuple.

## 4. Sets

A set stores unique hashable values and is useful for membership checks and removing duplicates. Sets are not indexed and should not be relied on for display order.

```python
tools = {"search", "calculator", "search"}
tools.add("calendar")
tools.discard("search")  # safe if the item is absent
print("calculator" in tools)
```

Set operations:
```python
a = {"python", "sql"}
b = {"python", "api"}
print(a | b)  # union
print(a & b)  # intersection
print(a - b)  # items only in a
```

## 5. Dictionaries

A dictionary maps unique keys to values. It is ideal for structured records.

```python
task = {
    "id": 1,
    "title": "Practice loops",
    "priority": "high",
    "completed": False,
}
print(task["title"])
print(task.get("due_date", "No due date"))
task["completed"] = True
task["category"] = "Python"
```

- `task["title"]` raises `KeyError` if the key is absent.
- `task.get("due_date", default)` safely provides a default.
- `task.keys()`, `task.values()`, and `task.items()` expose keys, values, and key-value pairs.
- Dictionary keys must be hashable; strings and numbers are common choices.

## 6. Choosing the right collection

| Need | Use |
|---|---|
| Ordered items that may change | List |
| Fixed ordered group | Tuple |
| Unique items / membership checks | Set |
| Named fields or key-value lookup | Dictionary |

A task manager commonly uses a **list of dictionaries**: the list holds tasks, and each dictionary describes one task.

## 7. Membership and conditions

```python
languages = ["Python", "Java"]
print("Python" in languages)      # True
print("Ruby" not in languages)    # True

priority = "high"
if priority == "high":
    print("Do this soon")
elif priority == "medium":
    print("Schedule this")
else:
    print("Low urgency")
```

Use `==` to compare values and `=` to assign values. Conditions evaluate to truthy or falsy values. Prefer explicit comparisons when they make intent clearer.

## 8. for loops and enumerate

```python
for language in ["Python", "Java", "SQL"]:
    print(language)

tasks = ["Read", "Code", "Test"]
for index, task in enumerate(tasks, start=1):
    print(f"{index}. {task}")
```

Use `for` when iterating over a collection. `enumerate()` supplies both an index/counter and an item. The `start=1` argument changes the displayed counter, not the list's actual indexing.

## 9. while loops

A `while` loop repeats while its condition is true.

```python
remaining = 3
while remaining > 0:
    print(f"{remaining} attempts left")
    remaining -= 1
```

Always make sure the loop can terminate. A condition that never becomes false can create an infinite loop. In menu-driven programs, `break` can exit when the user chooses Quit.

## 10. zip

`zip()` combines corresponding elements from iterables and stops when the shortest iterable ends.

```python
names = ["Asha", "Ravi"]
scores = [85, 91]
for name, score in zip(names, scores):
    print(f"{name}: {score}")
```

## 11. List comprehensions

A list comprehension builds a list from an iterable, optionally filtering items.

```python
numbers = [1, 2, 3, 4, 5, 6]
squares = [number ** 2 for number in numbers]
evens = [number for number in numbers if number % 2 == 0]
```

Equivalent filtering with a regular loop is often easier to debug for beginners. Keep comprehensions simple and readable.

## 12. Practical task data model

```python
task = {
    "id": 1,
    "title": "Learn dictionaries",
    "priority": "high",
    "completed": False,
}
tasks = [task]
pending = [item for item in tasks if not item["completed"]]
```

The list stores many tasks. Each dictionary provides predictable fields. The boolean `completed` supports filtering.

## 13. Common mistakes

1. Using `=` instead of `==` in a comparison.
2. Forgetting that list indexes start at zero.
3. Assuming a slice includes its stop index.
4. Using a set when order or duplicates matter.
5. Using `task["missing"]` when the key may not exist; use `.get()` if a default is appropriate.
6. Removing a list item while looping over the same list, which can skip items. Build a filtered list instead.
7. Writing an infinite `while` loop.
8. Assuming `zip()` checks that both lists have equal length; it silently stops at the shorter one.

## 14. Connection to agentic AI

- **Conversation history:** list of message dictionaries.
- **Tool registry:** dictionary mapping tool names to handlers.
- **Allowed tools:** set for quick membership checks.
- **Agent decisions:** `if/elif/else` based on tool results or task state.
- **Batch processing:** loops over tasks, messages, and tool outputs.
- **Filtering:** comprehensions to select pending tasks or relevant results.

## Day 2 self-check

Explain aloud:
- Why would a task be a dictionary and the task collection a list?
- When is a set better than a list?
- What does `enumerate(tasks, start=1)` return on each iteration?
- Why can modifying a list during iteration be risky?
- How would you select only incomplete tasks?
