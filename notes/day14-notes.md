## Day 14 Notes

### Auth Test Results:
- Key 1 validated correctly.
- Fake key returned None.
- After revoking key 2, exactly 1 key remained.

### Rate Limiter Test:
- Requests 1-20: ALLOWED
- Requests 21-25: BLOCKED
- 20 allowed, 5 blocked — assertion passed.

### Security Test Suite Results:
- PASS No key → 401
- PASS No key error message correct
- PASS Wrong key → 401
- PASS Wrong key error message correct
- PASS Valid key → 200
- PASS Valid key response has answer
- PASS /health public → 200
- PASS 20 requests allowed
- PASS Excess requests blocked 429
- PASS Retry-After header present
- PASS retry_after in body
=== Results: 11 passed, 0 failed ===

### Reflection:
- SHA-256 hashes: attacker cannot reverse hashes to get raw keys. Hashes are one-way — useless for making API calls.
- Rate limit counters lost on restart — acceptable behavior since restarting naturally resets abuse windows.
- ADMIN_SECRET in env var better than hardcoded — not visible in source code or git history. Next step: rotate secret regularly.
- For friendly 429 UI: catch status 429 in sendQuestion() and show "Too many messages. Please wait X seconds." in chat bubble.