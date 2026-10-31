# Day 8 Assignments

## A. Conceptual questions
1. What is an LLM?
2. Why do models use token IDs?
3. What is an embedding?
4. What does self-attention help a Transformer do?
5. Explain Query, Key and Value in attention.
6. What is the context window?
7. Explain next-token prediction.
8. What is the difference between training and inference?
9. What does temperature change?
10. Why can an LLM hallucinate?
11. Is an LLM automatically an AI agent? Explain.
12. Why is one word not necessarily one token?

## B. Coding tasks
1. Install tiktoken and count tokens in five different sentences.
2. Display the decoded token pieces for a sentence.
3. Compare token counts for English text, code and a long uncommon word.
4. Build a context-budget calculator.
5. Make the calculator reject negative values.
6. Make it report when the total exceeds the context limit.
7. Implement a weighted next-token sampling simulation.
8. Compare output distributions at low, medium and high temperature.
9. Add input validation for empty probability dictionaries and probabilities that do not sum to one.

## C. Mini-project
Complete the LLM Playground:
- Token counter.
- Token-piece inspector.
- Context-budget calculator.
- Sampling demonstration.
- CLI interface.
- Unit tests.

## D. Reflection
Write a short explanation of how these concepts will matter when building an agent that calls tools and maintains conversation history.

## Completion checklist
- [ ] Explain LLM generation in your own words.
- [ ] Explain tokenization and embeddings.
- [ ] Explain attention conceptually.
- [ ] Calculate a context budget.
- [ ] Explain temperature and sampling.
- [ ] Distinguish training from inference.
- [ ] Identify hallucinations and mitigations.
- [ ] Run the playground and its tests.
