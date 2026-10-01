---
name: rag-debugger
description: Diagnose why a retrieval-augmented generation app returns wrong, missing or ungrounded answers. Use when the user reports bad RAG quality, hallucinations with context, or low retrieval recall, and wants a ranked debugging plan.
---

# RAG Debugger

Debug in pipeline order. Do not tune the generator until retrieval is proven good.

## Procedure

1. **Collect** 5-10 failing questions with the expected answer and the document that contains it.
2. **Check retrieval first.** For each failure: is the right chunk in the top-k? Classify:
   - *Not indexed*: document missing or parsing dropped the text (tables, PDFs, headings)
   - *Chunked badly*: answer split across chunks, or chunk lacks context (title, section)
   - *Ranked low*: right chunk exists at rank > k (try hybrid BM25 + embeddings, reranker, larger k)
   - *Query mismatch*: question wording differs from the doc (try query rewriting)
3. **Only if the right chunk is retrieved**, check generation:
   - Prompt tells the model to use only the sources and to say "I don't know"
   - Context order and size (important chunks first, trim noise)
   - Citations required, and verified against sources
4. **Measure**: report recall@k before and after each change on the failing set plus a held-out set, so fixes don't overfit.

## Output format

A table: question | failure class | evidence | proposed fix | expected metric change.
End with the single change to try first and why.

