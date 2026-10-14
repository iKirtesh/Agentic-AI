"""A beginner-friendly command-line task summary.

This Day 1 version demonstrates input/output, variables, numeric conversion,
and f-strings. Robust input validation is an assignment for a later day.
"""


def summarize_task(
    owner: str,
    task: str,
    priority: int,
    estimated_hours: float,
) -> str:
    """Return a formatted task summary.

    Args:
        owner: Person responsible for the task.
        task: Short task title.
        priority: Priority from 1 (low) to 3 (high).
        estimated_hours: Non-negative estimated duration in hours.

    Returns:
        A readable task summary.
    """
    status = "Pending"
    return (
        "\n--- Task Summary ---\n"
        f"Owner: {owner}\n"
        f"Task: {task}\n"
        f"Priority: {priority}\n"
        f"Estimated duration: {estimated_hours:.1f} hours\n"
        f"Status: {status}"
    )


def main() -> None:
    """Collect task details and print the summary."""
    print("=== AI Task Assistant ===")

    owner = input("Enter your name: ").strip()
    task = input("Enter your task: ").strip()
    priority = int(input("Enter priority (1-3): "))
    estimated_hours = float(input("Estimated hours: "))

    print(summarize_task(owner, task, priority, estimated_hours))
    print("Task created successfully!")


if __name__ == "__main__":
    main()
