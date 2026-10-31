# Day 8 Answer Guide

## A. Concepts
1. An LLM is a neural network trained to model token sequences and generate or process language.
2. Neural networks operate on numerical representations; token IDs map discrete tokenizer units to numbers.
3. An embedding is a learned numerical vector representation.
4. Self-attention lets a token representation incorporate information from other positions in its context.
5. Query is what a position seeks, key is what another position makes matchable, and value is the information combined.
6. The context window is the token budget available to a model request, including applicable input and output content.
7. Next-token prediction estimates a distribution over possible next tokens conditioned on prior context.
8. Training adjusts parameters; inference uses trained parameters to produce outputs.
9. Temperature changes the sharpness of the sampling distribution; lower generally makes high-probability tokens more dominant.
10. A model can produce plausible continuations without guaranteeing factual correctness or source verification.
11. No. An agentic application adds tools, orchestration, state, permissions and feedback around a model.
12. Tokenizers split text into units that may be words, subwords, punctuation or whitespace-bearing pieces.

## B. Example context budget
```python
def calculate_context_budget(limit, instructions, history, retrieved, output):
    values = [limit, instructions, history, retrieved, output]
    if any(value < 0 for value in values):
        raise ValueError("Token values cannot be negative")
    used = instructions + history + retrieved + output
    return {
        "used_tokens": used,
        "remaining_tokens": limit - used,
        "fits": used <= limit,
    }
```

## C. Temperature intuition
Temperature scales logits before softmax. A low value sharpens the distribution; a higher value flattens it. This is probabilistic behavior, not a guarantee that a response will be more accurate or creative.

## D. Hallucination mitigation
Ground answers in trusted information, retrieve relevant sources, verify tool results, validate structured outputs, evaluate representative examples and require human review for high-impact actions.
