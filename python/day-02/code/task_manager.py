"""A small in-memory command-line task manager."""


VALID_PRIORITIES = {"low", "medium", "high"}


def add_task(tasks: list[dict], title: str, priority: str = "medium") -> dict:
    """Validate and add a task. Returns the created task."""
    clean_title = title.strip()
    clean_priority = priority.strip().lower()

    if not clean_title:
        raise ValueError("Task title cannot be empty.")
    if clean_priority not in VALID_PRIORITIES:
        raise ValueError("Priority must be low, medium, or high.")

    task = {
        "id": max((item["id"] for item in tasks), default=0) + 1,
        "title": clean_title,
        "priority": clean_priority,
        "completed": False,
    }
    tasks.append(task)
    return task


def complete_task(tasks: list[dict], task_id: int) -> bool:
    """Mark a task complete. Returns False if the ID does not exist."""
    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = True
            return True
    return False


def pending_tasks(tasks: list[dict]) -> list[dict]:
    """Return a new list of incomplete tasks."""
    return [task for task in tasks if not task["completed"]]


def display_tasks(tasks: list[dict]) -> None:
    if not tasks:
        print("No tasks to display.")
        return

    for task in tasks:
        status = "Done" if task["completed"] else "Pending"
        print(
            f'#{task["id"]} | {task["title"]} | '
            f'{task["priority"].title()} | {status}'
        )


def show_summary(tasks: list[dict]) -> None:
    total = len(tasks)
    completed = sum(1 for task in tasks if task["completed"])
    pending = total - completed
    percentage = completed / total * 100 if total else 0.0
    print(
        f"Total: {total} | Completed: {completed} | "
        f"Pending: {pending} | Completion: {percentage:.1f}%"
    )


def main() -> None:
    tasks: list[dict] = []
    menu = (
        "\n--- Task Manager ---\n"
        "1. Add task\n"
        "2. List all tasks\n"
        "3. Complete task\n"
        "4. List pending tasks\n"
        "5. Show summary\n"
        "0. Quit"
    )

    while True:
        print(menu)
        choice = input("Choose an option: ").strip()

        if choice == "1":
            title = input("Task title: ")
            priority = input("Priority (low/medium/high, default medium): ")
            priority = priority.strip() or "medium"
            try:
                task = add_task(tasks, title, priority)
            except ValueError as error:
                print("Could not add task:", error)
            else:
                print(f'Added task #{task["id"]}: {task["title"]}')

        elif choice == "2":
            display_tasks(tasks)

        elif choice == "3":
            raw_id = input("Task ID to complete: ").strip()
            try:
                task_id = int(raw_id)
            except ValueError:
                print("Please enter a whole-number task ID.")
                continue
            if complete_task(tasks, task_id):
                print(f"Task #{task_id} completed.")
            else:
                print(f"No task found with ID {task_id}.")

        elif choice == "4":
            display_tasks(pending_tasks(tasks))

        elif choice == "5":
            show_summary(tasks)

        elif choice == "0":
            print("Good work. Keep practicing!")
            break

        else:
            print("Invalid option. Choose 0, 1, 2, 3, 4, or 5.")


if __name__ == "__main__":
    main()
