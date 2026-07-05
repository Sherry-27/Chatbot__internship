## Day 9 Notes

### Observation Questions:
- FastAPI generates full Swagger UI from Pydantic models automatically. Zero manual docs needed.
- Missing required field returns 422 Unprocessable Entity — FastAPI handles this automatically via Pydantic.
- GET is for reading data (no body). POST is for sending data. /health just reads status so GET. /echo sends data so POST.

### Error Handling Tests:
- Empty question: 422 Unprocessable Entity
- Missing question field: 422 Unprocessable Entity
- Empty ingest content: 400 Bad Request
- Invalid endpoint: 404 Not Found

### Reflection:
- 400 = client sent bad data. 422 = request structure invalid (Pydantic validation).
- Problems with in-memory index: crashes lose everything, can't scale to multiple servers. Fix: PersistentClient + database.
- File uploads need multipart/form-data handling with FastAPI's UploadFile instead of raw text.
- chat_sessions resets on crash. Fix: store sessions in SQLite or Redis.
- Next needed: a web UI so users can chat without terminal.