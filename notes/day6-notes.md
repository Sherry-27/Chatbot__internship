## Day 6 Notes

### Chunking Comparison:
| Query | BM25 Top Source | Dense Top Source | Better Method |
|-------|----------------|-----------------|---------------|
| What is NexusChat? | sample.pdf | sample.pdf | Dense |
| Professional plan 200 USD | sample2.txt | sample.pdf | BM25 |
| confidential data AI services | sample.docx | sample.docx | Tie |

### Observation Questions:
- Query 2: BM25 found sample2.txt first — exact keyword match wins.
- Query 1: Dense performed better — semantic understanding of "NexusChat".
- "What does the product do?" — BM25 would miss it, no exact keyword match.

### Benchmark:
| Metric | Week 1 Dense | Week 2 Hybrid |
|--------|-------------|---------------|
| Top source (keyword query) | sample.pdf | sample2.txt |
| Finds sample2.txt? | No | Yes |
| Answer quality (1-5) | 3 | 5 |

### Reflection:
- k=1: Top ranked results get boosted much more aggressively.
- At scale: pre-compute BM25 index, cache dense embeddings, use async processing.
- Dense: semantic queries. BM25: exact keywords. Hybrid: both.