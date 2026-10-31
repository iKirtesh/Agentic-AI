"""Command-line task manager with JSON persistence."""
from pathlib import Path

from config import load_settings
from storage import StorageError, load_tasks, save_tasks


VALID_PRIORITIES = {"low", "medium", "high"}


def add_task(tasks: list[dict], title: str, priority: str = "medium") -> dict:
    """Validate and append a new task."""
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
    """Mark a task completed; return False if it does not exist."""
    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = True
            return True
    return False


def display_tasks(tasks: list[dict]) -> None:
    if not tasks:
        print("No tasks to display.")
        return
    for task in tasks:
        status = "Done" if task["completed"] else "Pending"
        print(f'#{task["id"]} | {task["title"]} | {task["priority"]} | {status}')


def main() -> None:
    settings = load_settings()
    data_path = Path(settings.data_file)

    try:
        tasks = load_tasks(data_path)
    except StorageError as error:
        print(f"Storage error: {error}")
        print("Fix the data file before continuing; no data was overwritten.")
        return

    print(f"Task Manager ({settings.app_env})")
    while True:
        print("\n1. Add task\n2. List tasks\n3. Complete task\n4. Pending tasks\n0. Quit")
        choice = input("Choose: ").strip()

        if choice == "1":
            title = input("Title: ")
            priority = input("Priority (low/medium/high, default medium): ").strip() or "medium"
            try:
                task = add_task(tasks, title, priority)
                save_tasks(data_path, tasks)
            except (ValueError, StorageError) as error:
                print(f"Could not add task: {error}")
            else:
                print(f'Added task #{task["id"]}.')

        elif choice == "2":
            display_tasks(tasks)

        elif choice == "3":
            try:
                task_id = int(input("Task ID: ").strip())
            except ValueError:
                print("Enter a valid whole-number ID.")
                continue
            if complete_task(tasks, task_id):
                try:
                    save_tasks(data_path, tasks)
                except StorageError as error:
                    print(f"Could not save completion: {error}")
                else:
                    print("Task completed and saved.")
            else:
                print("Task ID not found.")

        elif choice == "4":
            display_tasks([task for task in tasks if not task["completed"]])

        elif choice == "0":
            print("Goodbye.")
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
