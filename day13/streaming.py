import json
import os
import sys
import google.generativeai as genai

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

from day4.generator import build_prompt

GENERATION_MODEL = 'gemini-1.5-flash'

def stream_answer(question: str, retrieved_chunks: list):
    prompt = build_prompt(question, retrieved_chunks)
    model = genai.GenerativeModel(GENERATION_MODEL)
    response = model.generate_content(prompt, stream=True)
    for chunk in response:
        if chunk.text:
            event = json.dumps({'token': chunk.text})
            yield f'data: {event}\n\n'
    sources = [{'source': c['source'], 'preview': c['text'][:150]} for c in retrieved_chunks]
    yield f'data: {json.dumps({"sources": sources})}\n\n'
    yield f'data: {json.dumps({"done": True})}\n\n'