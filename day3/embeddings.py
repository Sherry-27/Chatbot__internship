import os
import math
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
genai.configure(api_key=os.getenv('GEMINI_API_KEY'))

EMBED_MODEL = 'models/gemini-embedding-001'

def embed_text(text):
    result = genai.embed_content(
        model=EMBED_MODEL,
        content=text,
        task_type='RETRIEVAL_DOCUMENT',
    )
    return result['embedding']

def embed_query(text):
    result = genai.embed_content(
        model=EMBED_MODEL,
        content=text,
        task_type='RETRIEVAL_QUERY',
    )
    return result['embedding']

if __name__ == '__main__':
    print("Testing embeddings...")
    sentence = 'Retrieval-Augmented Generation improves LLM accuracy.'
    vector = embed_text(sentence)
    print(f'Text: {sentence}')
    print(f'Vector dimensions: {len(vector)}')
    print(f'First 10 values: {[round(v, 4) for v in vector[:10]]}')
    print(f'Min value: {min(vector):.4f} Max value: {max(vector):.4f}')
    print()

    def cosine_similarity(v1, v2):
        dot = sum(a * b for a, b in zip(v1, v2))
        norm1 = math.sqrt(sum(a * a for a in v1))
        norm2 = math.sqrt(sum(b * b for b in v2))
        return dot / (norm1 * norm2) if (norm1 * norm2) != 0 else 0

    texts = [
        'The cat sat on the mat.',
        'A feline rested on a rug.',
        'Machine learning models process data.',
        'Deep neural networks learn representations.',
        'The weather in London is often rainy.',
    ]
    print('Cosine similarity to: "The cat sat on the mat."')
    print('-' * 50)
    base_vec = embed_text(texts[0])
    for t in texts:
        vec = embed_text(t)
        sim = cosine_similarity(base_vec, vec)
        print(f' {sim:.4f} | {t}')

#Testing embeddings...
#Text: Retrieval-Augmented Generation improves LLM accuracy.
#Vector dimensions: 3072
#Min value: -0.2150 Max value: 0.2498

#Cosine similarity to: "The cat sat on the mat."
#--------------------------------------------------
# 1.0000 | The cat sat on the mat.
# 0.8875 | A feline rested on a rug.
# 0.7726 | Machine learning models process data.
# 0.7604 | Deep neural networks learn representations.
# 0.7591 | The weather in London is often rainy.
