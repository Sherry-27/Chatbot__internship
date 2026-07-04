# NexusChat — RAG Chatbot (Week 1 & 2 Build)

A Retrieval-Augmented Generation chatbot built from scratch using
Google Gemini and ChromaDB. Answers questions from documents with
cited sources and supports multi-turn conversation.

## What It Does
- Loads documents in TXT, PDF, and DOCX format
- Splits documents into searchable chunks
- Embeds chunks using Gemini embedding model
- Stores and searches vectors using ChromaDB
- Generates grounded, cited answers using gemini-1.5-flash
- Remembers conversation history and resolves follow-up questions
- Hybrid search (BM25 + Dense) with Reciprocal Rank Fusion
- Cross-encoder re-ranking for better result ordering
- Query decomposition for complex multi-part questions
- Evaluation harness with faithfulness, relevance, and recall metrics

## How to Run
1. Clone this repo and create a virtual environment
2. pip install -r requirements.txt
3. Add your GEMINI_API_KEY to .env file
4. Run: python day5/memory_chatbot.py

## Project Structure
- day2/ - document ingestion and chunking
- day3/ - embeddings and vector store
- day4/ - generation and first complete pipeline
- day5/ - conversation memory and polished chatbot
- day6/ - hybrid search with BM25 and RRF
- day7/ - re-ranking and query decomposition
- day8/ - evaluation harness and report card
- notes/ - daily learning notes and reflections

## What I Learned
Building a RAG system from scratch taught me that retrieval quality
is the foundation of everything — bad chunks mean bad answers regardless
of how good the LLM is. Hybrid search and re-ranking meaningfully improve
results, and evaluation metrics are essential to prove improvements
rather than just feeling like things got better.