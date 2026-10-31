from context_budget import calculate_context_budget
from sampling_demo import sample_token
from tokenizer import count_tokens, inspect_tokens


def main() -> None:
    print("=== LLM Playground ===")
    text = input("Enter a sentence: ")
    print("Token count:", count_tokens(text))
    print("Token pieces:", inspect_tokens(text))

    budget = calculate_context_budget(
        context_limit=8000,
        instruction_tokens=500,
        history_tokens=3000,
        retrieved_tokens=1000,
        output_tokens=1000,
    )
    print("\nContext budget:", budget)

    candidates = {"Python": 0.7, "Java": 0.2, "JavaScript": 0.1}
    print("\nSampling simulation:")
    for temperature in (0.2, 0.7, 1.5):
        print(temperature, "->", sample_token(candidates, temperature))


if __name__ == "__main__":
    main()
