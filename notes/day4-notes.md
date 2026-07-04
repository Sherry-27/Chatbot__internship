## Day 4 Notes

### Observation Questions:
- Q2 (pricing): Gemini correctly refused — "I could not find that information in the provided documents." No hallucination.
- Q1 SOURCES: Correctly named sample.pdf. Without source labels, model cannot cite documents.
- Testing with fake chunks first catches generation bugs before connecting ChromaDB.

### Experiment A: Removed grounding instruction
- Gemini hallucinated a refund policy when grounding instruction removed.
- Restored instruction after testing.

### Experiment B: top_k values
- top_k=1: Answer shorter, less complete.
- top_k=6: Repetitive answers. Best value = top_k=3.

### Experiment C: sample2.txt added
- Chatbot correctly cited sample2.txt for pricing question.
- Easy to expand knowledge base — just add a file.

### Reflection:
- Hardest layer: chunking — wrong chunk size loses context or wastes tokens.
- Production needs: multi-turn memory, faster response, UI, 10k+ document support.