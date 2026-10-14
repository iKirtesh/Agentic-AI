"""Day 2 examples: collections and control flow."""


def main() -> None:
    # List: ordered, mutable, duplicates allowed.
    skills = ["Python", "Java", "SQL", "Python"]
    print("First skill:", skills[0])
    print("First two:", skills[:2])
    skills.append("Git")
    print("Updated skills:", skills)

    # Tuple: ordered, immutable.
    location = (18.52, 73.86)
    print("Coordinates:", location)

    # Set: unique values.
    unique_skills = set(skills)
    print("Unique skills:", unique_skills)
    print("Knows Python:", "Python" in unique_skills)

    # Dictionary: named fields.
    task = {
        "id": 1,
        "title": "Learn collections",
        "priority": "high",
        "completed": False,
    }
    print("Task title:", task["title"])
    print("Due date:", task.get("due_date", "Not set"))

    # Conditional logic.
    if task["priority"] == "high":
        print("Priority: do this soon")
    elif task["priority"] == "medium":
        print("Priority: schedule it")
    else:
        print("Priority: low")

    # Enumerate gives a counter and an item.
    for number, skill in enumerate(skills, start=1):
        print(f"{number}. {skill}")

    # Zip combines values pairwise.
    names = ["Read", "Code", "Test"]
    minutes = [20, 45, 30]
    for name, duration in zip(names, minutes):
        print(f"{name}: {duration} minutes")

    # Comprehension filters pending tasks.
    tasks = [
        {"title": "Read", "completed": True},
        {"title": "Code", "completed": False},
        {"title": "Test", "completed": False},
    ]
    pending = [item["title"] for item in tasks if not item["completed"]]
    print("Pending tasks:", pending)


if __name__ == "__main__":
    main()
