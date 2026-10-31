from pathlib import Path

from api_client import DemoApiClient, get_posts_async
from manager import TaskManager
from storage import JsonTaskStorage
import asyncio


def main() -> None:
    storage_path = Path(__file__).parent.parent / "data" / "tasks.json"
    manager = TaskManager(JsonTaskStorage(storage_path))

    while True:
        print("\n=== Agent Task Hub ===")
        print("1. Create task")
        print("2. List tasks")
        print("3. Complete task")
        print("4. Fetch remote post")
        print("5. Fetch three posts asynchronously")
        print("0. Exit")

        choice = input("Choose: ").strip()

        try:
            if choice == "1":
                title = input("Title: ")
                description = input("Description: ")
                task = manager.create_task(title, description)
                print("Created:", task.id)
            elif choice == "2":
                tasks = manager.list_tasks()
                if not tasks:
                    print("No tasks yet.")
                for task in tasks:
                    status = "done" if task.completed else "pending"
                    print(f"{task.id} | {status} | {task.title}")
            elif choice == "3":
                task = manager.complete_task(input("Task ID: ").strip())
                print("Completed:", task.title)
            elif choice == "4":
                post_id = int(input("Post ID: "))
                with DemoApiClient() as api:
                    print(api.get_post(post_id))
            elif choice == "5":
                for post in asyncio.run(get_posts_async([1, 2, 3])):
                    print(post["id"], post["title"])
            elif choice == "0":
                print("Goodbye.")
                break
            else:
                print("Choose one of the listed options.")
        except (ValueError, KeyError) as exc:
            print("Input or task error:", exc)
        except Exception as exc:
            print("Operation failed:", exc)


if __name__ == "__main__":
    main()
