## Day 2 Observations

### Ingestion Questions:
- PDF text has extra whitespace and newline characters between words.
- Blank paragraphs removed from DOCX to avoid empty/useless chunks in retrieval.
- For HTML: would use BeautifulSoup4 library.

### Chunking Comparison Table:
| Strategy   | Chunks | Avg Length | Reads Naturally? |
|------------|--------|------------|-----------------|
| Fixed-Size | 3      | 300 chars  | Partially        |
| Sentence   | 3      | 130 chars  | Yes              |
| Recursive  | 4      | 220 chars  | Yes              |

### Experiments:
- overlap=0: Chunks share no words, context lost at boundaries.
- sentences_per_chunk=1: Too many small chunks, not enough context.
- size=100: More chunks produced, each smaller.

### Reflection:
- Fixed-Size cut sentences in half — bad for retrieval, loses meaning.
- For "What formats does NexusChat support?" — Recursive chunk best.
- Overlap prevents losing key facts that fall at chunk boundaries.

### RAG Pipeline Questions:
Q1: Demo used fixed-size chunking. I would use recursive chunking 
to preserve sentence structure and improve retrieval accuracy.

Q2: Raw DOCX → load_docx() → load_document() → chunk_recursive() 
→ embed each chunk → store in vector DB → user query embedded 
→ semantic search → top chunks passed to Gemini → final answer.