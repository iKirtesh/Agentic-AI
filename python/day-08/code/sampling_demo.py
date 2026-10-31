import math
import random


def sample_token(
    probabilities: dict[str, float],
    temperature: float,
    seed: int | None = None,
) -> str:
    if temperature <= 0:
        raise ValueError("Temperature must be greater than zero")
    if not probabilities:
        raise ValueError("At least one token is required")
    if any(probability < 0 for probability in probabilities.values()):
        raise ValueError("Probabilities cannot be negative")
    if not math.isclose(sum(probabilities.values()), 1.0, abs_tol=1e-6):
        raise ValueError("Probabilities must sum to 1")

    tokens = list(probabilities)
    adjusted = [
        probability ** (1.0 / temperature)
        for probability in probabilities.values()
    ]
    total = sum(adjusted)
    weights = [value / total for value in adjusted]
    return random.Random(seed).choices(tokens, weights=weights, k=1)[0]


if __name__ == "__main__":
    candidates = {"Python": 0.7, "Java": 0.2, "JavaScript": 0.1}
    for temp in (0.2, 0.7, 1.5):
        print(f"temperature={temp}: {sample_token(candidates, temp)}")
