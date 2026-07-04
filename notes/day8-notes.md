## Day 8 Notes

### Evaluator Test:
- Faithful answer faithfulness score: ~0.95
- Hallucinated answer faithfulness score: ~0.40
- Evaluator correctly penalised hallucinated answer 
- Both scored similarly on relevance — both answered the question, just one added extra wrong info.
- Risk of Gemini judging itself: bias toward its own outputs. Mitigation: use different model as judge.

### Report Card:
| Chatbot Version | Faithfulness | Relevance | Context Recall | Mean |
|----------------|-------------|-----------|----------------|------|
| Week 1 Dense | 0.75 | 0.80 | 0.70 | 0.75 |
| Week 2 Hybrid | 0.85 | 0.85 | 0.82 | 0.84 |
| Week 2 Advanced | 0.92 | 0.90 | 0.88 | 0.90 |

### Reflection:
- Context recall improved most — hybrid search found right chunks.
- High recall + low faithfulness = model hallucinating despite good retrieval.
- High faithfulness + low recall = model staying grounded but missing info.
- Stronger judge model = stricter, more accurate scores.
- Re-run evaluation after every major pipeline change.