# Day 2 Answer Key

Try the assignments first. These are sample solutions; your implementation may differ.

## 1. List operations

```python
skills = ["Python", "Java", "SQL", "Git", "React"]
print(skills[0])
print(skills[-1])
print(skills[:3])
skills.append("FastAPI")
skills.remove("Git")
print(skills)
```

## 2. Remove duplicates

```python
tools = ["search", "python", "search", "calculator", "python"]
unique_tools = set(tools)
print(unique_tools)
```

A set removes duplicates but does not guarantee display order. To preserve first-seen order:

```python
unique_in_order = list(dict.fromkeys(tools))
print(unique_in_order)
```

## 3. Task dictionary

```python
task = {
    "id": 1,
    "title": "Practice dictionaries",
    "priority": "high",
    "completed": False,
}
print(task["title"])
print(task.get("due_date", "No due date"))
```

## 4. Priority decision

```python
priority = "medium"
if priority == "high":
    print("Do this soon")
elif priority == "medium":
    print("Schedule this")
elif priority == "low":
    print("Low urgency")
else:
    print("Unknown priority")
```

## 5. Loop and enumerate

```python
tasks = ["Read notes", "Write code", "Run tests"]
for number, task in enumerate(tasks, start=1):
    print(f"{number}. {task}")
```

## 6. Filter pending tasks

```python
tasks = [
    {"id": 1, "title": "Read", "completed": True},
    {"id": 2, "title": "Code", "completed": False},
    {"id": 3, "title": "Test", "completed": False},
]
pending = [task for task in tasks if not task["completed"]]
print(pending)
```

## 7. zip

```python
names = ["Read", "Code", "Test"]
minutes = [20, 45, 30]
for name, duration in zip(names, minutes):
    print(f"{name}: {duration} minutes")
```

If one list is shorter, `zip()` stops when the shortest iterable ends.

## 8. CLI Task Manager

See `code/task_manager.py`. It stores tasks as dictionaries inside a list, uses a loop for the menu, conditions for menu decisions, and validates task IDs.

## 9. Optional summary report

```python
total = len(tasks)
completed = sum(1 for task in tasks if task["completed"])
pending_count = total - completed
percentage = (completed / total * 100) if total else 0.0

print(f"Total: {total}")
print(f"Completed: {completed}")
print(f"Pending: {pending_count}")
print(f"Completion: {percentage:.1f}%")
```

The conditional expression avoids dividing by zero when there are no tasks.
