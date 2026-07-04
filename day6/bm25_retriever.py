import os
import sys
import numpy as np
from rank_bm25 import BM25Okapi

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

from day2.ingestion import load_document
from day2.chunking import chunk_recursive

class BM25Retriever:
    def __init__(self):
        self.bm25 = None
        self.chunks = []
        self.sources = []

    def _tokenise(self, text):
        return text.lower().split()

    def index(self, chunks, sources):
        self.chunks = chunks
        self.sources = sources
        tokenised = [self._tokenise(chunk) for chunk in chunks]
        self.bm25 = BM25Okapi(tokenised)
        print(f'BM25 index built over {len(chunks)} chunks.')

    def search(self, query, top_k=3):
        if self.bm25 is None:
            raise RuntimeError('Call index() before search()')
        query_tokens = self._tokenise(query)
        scores = self.bm25.get_scores(query_tokens)
        top_indices = np.argsort(scores)[::-1][:top_k]
        results = []
        for idx in top_indices:
            results.append({'text': self.chunks[idx], 'source': self.sources[idx], 'score': float(scores[idx]), 'rank_idx': int(idx)})
        return results

def build_bm25_index(doc_paths):
    all_chunks, all_sources = [], []
    for path in doc_paths:
        text = load_document(path)
        chunks = chunk_recursive(text, size=400, overlap=80)
        for chunk in chunks:
            all_chunks.append(chunk)
            all_sources.append(os.path.basename(path))
    retriever = BM25Retriever()
    retriever.index(all_chunks, all_sources)
    return retriever