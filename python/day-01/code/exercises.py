"""Small Day 1 practice exercises using Python built-ins."""


def calculate_study_hours(hours_per_day: float, number_of_days: int) -> float:
    """Calculate total study time."""
    return hours_per_day * number_of_days


def estimate_tokens(
    request_count: int,
    input_tokens_per_request: int,
    output_tokens_per_request: int,
) -> dict[str, int]:
    """Estimate token volume; this does not estimate provider billing."""
    total_input = request_count * input_tokens_per_request
    total_output = request_count * output_tokens_per_request
    return {
        "input_tokens": total_input,
        "output_tokens": total_output,
        "total_tokens": total_input + total_output,
    }


def analyze_text(text: str) -> dict[str, object]:
    """Return basic information about a sentence."""
    return {
        "character_count": len(text),
        "uppercase": text.upper(),
        "lowercase": text.lower(),
        "contains_python": "python" in text.lower(),
    }


def main() -> None:
    """Run interactive examples."""
    print("=== Study-Time Calculator ===")
    hours = float(input("Study hours per day: "))
    days = int(input("Number of days: "))
    print(f"Total study hours: {calculate_study_hours(hours, days):.1f}")

    print("\n=== String Analyzer ===")
    sentence = input("Enter a sentence: ")
    result = analyze_text(sentence)
    print(f"Characters: {result['character_count']}")
    print(f"Uppercase: {result['uppercase']}")
    print(f"Lowercase: {result['lowercase']}")
    print(f"Contains Python: {result['contains_python']}")


if __name__ == "__main__":
    main()
