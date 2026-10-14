"""Demonstrate importing and reusing task utility functions."""
from task_utils import (
    complete_task,
    create_task,
    filter_pending,
    summarize_tasks,
)


def main() -> None:
    tasks = [
        create_task(1, "Learn function parameters", "high"),
        create_task(2, "Practice return values", "medium"),
        create_task(3, "Write unit tests", "low"),
    ]

    complete_task(tasks, 2)

    print("Pending tasks:")
    for task in filter_pending(tasks):
        print(f'#{task["id"]}: {task["title"]} ({task["priority"]})')

    print("Summary:")
    for key, value in summarize_tasks(tasks).items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()
