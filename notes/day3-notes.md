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

### Pipeline Diagram:
RAW FILE (.txt / .pdf / .docx)
|
v
[Day 2 Task 1] load_document() --> raw text string
|
v
[Day 2 Task 2] chunk_recursive() --> list of chunk strings
|
v
[Day 3 Task 1] embed_text() --> list of 768-dim vectors
|
v
[Day 3 Task 2] collection.add() --> stored in ChromaDB

USER QUESTION --> embed_query() --> query vector
|
v
collection.query() --> top-K most similar chunks
|
v
[Day 4] Feed chunks + question to Gemini --> Final Answer