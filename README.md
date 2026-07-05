# NexusChat — Enterprise RAG Chatbot

Built from scratch over 2 weeks using Google Gemini and ChromaDB.

## Stack
- Embeddings: Google Gemini (gemini-embedding-001)
- Vector Store: ChromaDB
- Generation: Gemini 1.5 Flash
- Retrieval: Hybrid Search (BM25 + Dense) + RRF
- Re-ranking: Cross-Encoder (ms-marco-MiniLM-L-6-v2)
- Backend: FastAPI
- Memory: Conversation history with query rewriting

## Features
- TXT, PDF, DOCX document ingestion
- Hybrid retrieval with Reciprocal Rank Fusion
- Cross-encoder re-ranking
- Query decomposition for complex questions
- Conversation memory with follow-up resolution
- Evaluation harness (faithfulness, relevance, recall)
- REST API with /chat /ingest /health /session endpoints

## Setup
```bash
pip install -r requirements.txt
# Add GEMINI_API_KEY to .env
python day5/memory_chatbot.py
```

## Project Structure
- day2/ — ingestion + chunking
- day3/ — embeddings + vector store
- day4/ — generation + RAG pipeline
- day5/ — conversation memory
- day6/ — hybrid search + RRF
- day7/ — re-ranking + query decomposition
- day8/ — evaluation metrics
- day9/ — FastAPI backend
