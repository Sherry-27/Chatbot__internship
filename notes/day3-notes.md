## Day 3 Notes

### Observation Questions:
- Gemini embedding vector has 768 dimensions. Each number captures 
  a different aspect of meaning in the text.
- "A feline rested on a rug" had high similarity to cat sentence 
  despite sharing no words — surprising but correct.
- RETRIEVAL_QUERY used for questions because model optimizes 
  query vectors differently for better matching against documents.
- Cosine similarity 0.95 means two chunks discuss almost identical content.

### Reflection Questions:
- Off-topic query still returns results but with high distance scores — 
  shows importance of having relevant documents in the index.
- Same embedding model must be used for index and query — 
  different models produce incompatible vector spaces.
- For persistence: use chromadb.PersistentClient(path="./chroma_db") 
  instead of chromadb.Client().
- Missing piece: feeding retrieved chunks + question to Gemini 
  to generate final answer. This is Day 4.

## RAG Pipeline Diagram


                ┌─────────────────────────────┐
                │ Raw Document                │
                │ (.txt / .pdf / .docx)       │
                └─────────────┬───────────────┘
                              │
                              ▼
                   load_document()
                              │
                              ▼
                     Raw Text String
                              │
                              ▼
                  chunk_recursive()
                              │
                              ▼
                  Text Chunks (List)
                              │
                              ▼
                     embed_text()
                              │
                              ▼
               Embedding Vectors (768-D)
                              │
                              ▼
                 ChromaDB collection.add()
                              │
                              ▼
                  Vector Database Storage


User Question ──► embed_query() ──► Query Vector
                                     │
                                     ▼
                          ChromaDB collection.query()
                                     │
                                     ▼
                        Top-K Relevant Chunks
                                     │
                                     ▼
                  Gemini + Retrieved Context
                                     │
                                     ▼
                           Final Answer
```
