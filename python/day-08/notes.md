# Day 8 — Detailed LLM Fundamentals Notes

## 1. What is an LLM?
A Large Language Model is a neural network trained on large datasets to model sequences of tokens. Many modern LLMs are autoregressive: they generate the next token conditioned on previous context. Some models also support images, audio, video or other modalities.

## 2. Transformer architecture
The 2017 paper *Attention Is All You Need* introduced the Transformer architecture. Important concepts:
- Token embeddings map token IDs to learned vectors.
- Positional information represents sequence order.
- Self-attention lets a position incorporate information from other positions.
- Feed-forward layers transform representations.
- Residual connections and normalization help deep networks train.
- Stacked layers build contextual representations.

Many modern generative LLMs use decoder-only Transformer architectures, though model architectures vary.

## 3. Query, Key and Value
Attention computes relationships between query and key vectors, then uses the resulting weights to combine value vectors. Intuitively, a query represents what a position is looking for, keys represent what other positions offer, and values carry the information to combine. This is an analogy, not literal human-like searching.

## 4. Tokenization
A tokenizer maps text into token IDs. Tokens can be whole words, subwords, punctuation or whitespace-bearing units. Token boundaries vary by tokenizer and model. Do not assume one word equals one token. Special tokens may mark message boundaries or other control information.

## 5. Embeddings
An embedding is a learned vector representation. Token embeddings provide numerical input to the network. Hidden representations become contextual as they pass through model layers. Similarity in embedding space can be useful, but it is not a guarantee that two words mean the same thing.

## 6. Context window
The context window is the token budget a model can process for a request. Depending on the model/API, it can include instructions, conversation history, tool outputs, retrieved content and generated output. Context limit and maximum output limit are separate constraints. Exact limits depend on the model and API.

If context is too large, applications can:
- Remove irrelevant old turns.
- Summarize history.
- Retrieve only relevant document chunks.
- Reduce tool output.
- Reserve space for the answer.

## 7. Next-token prediction
For an autoregressive model, the network produces logits for possible next tokens. A decoding strategy transforms these scores into a selection. The selected token is appended to context and generation repeats until a stop condition or output limit is reached.

## 8. Sampling and temperature
Temperature scales logits before probability normalization. Lower values generally make high-scoring tokens more dominant; higher values generally flatten the distribution. Temperature does not guarantee creativity or correctness. Some models/endpoints do not expose temperature or may constrain its values. Top-p and other decoding controls may also be available.

## 9. Training and inference
Training adjusts model parameters using examples and an optimization objective. Inference uses the trained parameters to produce outputs for a supplied context. Fine-tuning is additional training to adapt a model. Prompting, retrieval and tools are alternative ways to adapt an application without necessarily changing model weights.

## 10. Hallucinations and limitations
A hallucination is plausible-sounding but incorrect or unsupported output. Causes include incomplete training information, ambiguity, weak context, conflicting sources and probabilistic generation. Mitigations include grounding in trusted sources, retrieval, tool verification, output validation, evaluation and human review where appropriate.

## 11. LLM vs traditional ML
Traditional ML systems are often built for narrower prediction tasks, such as classification or regression. LLMs provide broad language interfaces and generation capabilities. They can complement rather than replace traditional models.

## 12. Important distinction
An LLM is not automatically an agent. A model generates outputs; an agentic application adds orchestration, tools, state, permissions, validation and feedback loops around a model.

## 13. Key vocabulary
LLM, Transformer, token, tokenizer, token ID, embedding, attention, context window, inference, training, fine-tuning, logits, sampling, temperature, hallucination.

## 14. Safety and reliability
Treat generated content as untrusted. Validate structured data, verify important claims, protect secrets, and do not allow model text alone to authorize sensitive actions.
