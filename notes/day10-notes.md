## Day 10 Notes

### Observation Questions:
- check_same_thread=False allows SQLite connection from multiple FastAPI threads. Without it, crashes on concurrent requests.
- ? placeholders prevent SQL injection — never use f-strings with user input in SQL.
- Running twice without deleting: data from run 1 still exists, new data adds on top.

### Restart Test Results:
- Run 1: All documents indexed (slow — Gemini API calls made).
- Run 2: All documents skipped (fast — under 2 seconds, 0 API calls).
- Run 3 after modifying sample2.txt: Only sample2.txt re-indexed.

### Reflection:
- BM25 doesn't need disk persistence — it rebuilds from text in seconds, no API calls needed.
- Ingested documents lost on restart — fix by saving content to disk before indexing.
- Lost on restart: BM25 index and any documents ingested via /ingest endpoint.
- To diagnose missing conversation: check day10/chat_history.db with sqlite3 command.