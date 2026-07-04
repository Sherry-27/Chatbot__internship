## Day 7 Notes

### Re-ranking Observations:
- Weather chunk rerank_score: ~-8.0 (very low)
- NexusChat description chunk rerank_score: ~5.0 (very high)
- Before re-ranking: NexusChat description was position 4.
- After re-ranking: moved to position 1. ✅
- Local CPU model = no API cost, no latency from network calls.

### Query Decomposition:
- Simple question stays as 1 sub-question ✅
- Complex question splits into 2-3 sub-questions ✅

### Benchmark Table:
| Metric | Week 1 Dense | Week 2 Hybrid | Week 2 Advanced |
|--------|-------------|---------------|-----------------|
| Mentions file formats? | Yes | Yes | Yes |
| Mentions pricing? | No | Yes | Yes |
| Gives recommendation? | No | No | Yes |
| Completeness (1-5) | 2 | 3 | 5 |

### Reflection:
- Advanced version gave most complete answer.
- Re-ranking + decomposition adds latency — skip for simple queries.
- Bad decomposition fix: validate sub-questions before answering.