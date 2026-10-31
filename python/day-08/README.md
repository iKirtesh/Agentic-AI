# Day 8 — LLM Fundamentals

## Objectives
Understand LLMs, Transformers, tokens, embeddings, attention, context windows, next-token prediction, sampling, training vs inference, and hallucinations.

## Four-hour plan
1. LLM overview and generation (40 min)
2. Transformer concepts (40 min)
3. Tokenization and context windows (40 min)
4. Next-token prediction and temperature (40 min)
5. Training, inference and limitations (40 min)
6. Python playground and review (40 min)

## Setup
```bash
python -m pip install -r python/day-08/requirements.txt
```

## Run
```bash
python python/day-08/code/app.py
```

## Tests
```bash
python -m pytest python/day-08/tests -q
```

## Project
The LLM Playground demonstrates token counting with tiktoken, context-budget arithmetic and a simplified temperature sampling simulation. It does not call a real LLM or reproduce a production model's decoding pipeline.

## Learning resources
- https://platform.openai.com/tokenizer
- https://platform.openai.com/docs/guides/text-generation
- https://arxiv.org/abs/1706.03762
- https://github.com/openai/tiktoken
