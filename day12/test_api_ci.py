import sys
import os
import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch, MagicMock

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

def make_mock_app():
    with patch('google.generativeai.configure'), \
         patch('google.generativeai.GenerativeModel') as MockModel, \
         patch('chromadb.PersistentClient') as MockChroma, \
         patch('day10.persistent_index.smart_startup') as MockStartup, \
         patch('day10.chat_store.initialise_db'), \
         patch('day6.bm25_retriever.BM25Retriever'):
        mock_response = MagicMock()
        mock_response.text = 'NexusChat is a RAG chatbot. [Source: sample.pdf]'
        MockModel.return_value.generate_content.return_value = mock_response
        mock_collection = MagicMock()
        mock_collection.count.return_value = 42
        mock_collection.query.return_value = {
            'documents': [['NexusChat is an enterprise RAG chatbot.']],
            'metadatas': [[{'source': 'sample.pdf'}]],
            'distances': [[0.12]],
        }
        MockChroma.return_value.get_or_create_collection.return_value = mock_collection
        MockStartup.return_value = {'collection': mock_collection, 'total_chunks': 42, 'indexed_this_run': 0, 'skipped': 4}
        from day10.persistent_api import app
        return app

app = make_mock_app()
client = TestClient(app)

class TestHealthEndpoint:
    def test_health_returns_ok(self):
        r = client.get('/health')
        assert r.status_code == 200
        assert r.json()['status'] == 'ok'

    def test_health_contains_chunks_indexed(self):
        r = client.get('/health')
        assert 'chunks_indexed' in r.json()

class TestChatEndpoint:
    def test_chat_requires_question(self):
        r = client.post('/chat', json={})
        assert r.status_code == 422

    def test_chat_returns_answer_and_session(self):
        r = client.post('/chat', json={'question': 'What is NexusChat?'})
        assert r.status_code == 200
        data = r.json()
        assert 'answer' in data
        assert 'session_id' in data
        assert 'sources' in data

    def test_chat_session_id_persists(self):
        r1 = client.post('/chat', json={'question': 'Hello'})
        sid = r1.json()['session_id']
        r2 = client.post('/chat', json={'question': 'Follow up', 'session_id': sid})
        assert r2.status_code == 200
        assert r2.json()['session_id'] == sid

    def test_chat_empty_question_rejected(self):
        r = client.post('/chat', json={'question': ''})
        assert r.status_code in (400, 422)

class TestIngestEndpoint:
    def test_ingest_requires_fields(self):
        r = client.post('/ingest', json={'filename': 'test.txt'})
        assert r.status_code == 422

    def test_ingest_returns_chunk_count(self):
        r = client.post('/ingest', json={'filename': 'test.txt', 'content': 'This is test content. ' * 20})
        assert r.status_code == 200
        assert 'chunks_added' in r.json()

class TestSessionEndpoint:
    def test_missing_session_returns_404(self):
        r = client.get('/session/nonexistent-session-id')
        assert r.status_code == 404

    def test_existing_session_returns_history(self):
        r1 = client.post('/chat', json={'question': 'CI test question'})
        sid = r1.json()['session_id']
        r2 = client.get(f'/session/{sid}')
        assert r2.status_code == 200
        assert r2.json()['turn_count'] >= 1