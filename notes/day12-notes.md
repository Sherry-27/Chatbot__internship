## Day 12 Notes

### Docker:
- docker compose build completed successfully.
- docker compose up -d started container.
- Second startup after docker compose down: all documents skipped (SKIP messages).
- day10/chat_history.db exists on host after container stopped — volumes working.

### CI Pipeline:
- All 9 pytest tests passed locally.
- GitHub Actions workflow triggered on push.
- All CI jobs completed with green tick.

### Reflection:
- Docker eliminates "works on my machine" problem — identical environment everywhere.
- Volumes ensure data persists even when container is replaced or restarted.
- CI catches broken code before it reaches main branch automatically.