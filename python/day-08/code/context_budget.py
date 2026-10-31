def calculate_context_budget(
    context_limit: int,
    instruction_tokens: int,
    history_tokens: int,
    retrieved_tokens: int,
    output_tokens: int,
) -> dict[str, int | bool]:
    values = [
        context_limit,
        instruction_tokens,
        history_tokens,
        retrieved_tokens,
        output_tokens,
    ]
    if any(value < 0 for value in values):
        raise ValueError("Token values cannot be negative")

    used = sum(values[1:])
    return {
        "context_limit": context_limit,
        "used_tokens": used,
        "remaining_tokens": context_limit - used,
        "fits": used <= context_limit,
    }
