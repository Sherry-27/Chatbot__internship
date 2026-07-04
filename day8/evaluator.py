import os
import sys
import re
import google.generativeai as genai
from dotenv import load_dotenv

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

load_dotenv()
genai.configure(api_key=os.getenv('GEMINI_API_KEY'))

JUDGE_MODEL = 'gemini-1.5-flash'

def _call_judge(prompt):
    model = genai.GenerativeModel(JUDGE_MODEL)
    response = model.generate_content(prompt)
    raw = response.text.strip()
    matches = re.findall(r'\d+\.\d+|\d+', raw)
    if not matches:
        return 0.0
    score = float(matches[0])
    return max(0.0, min(1.0, score))

def score_faithfulness(question, answer, context_chunks):
    context_text = '\n\n'.join(c['text'] for c in context_chunks)
    prompt = f'''You are an expert evaluator assessing RAG system quality.
Score the FAITHFULNESS of the answer below on a scale from 0.0 to 1.0.
FAITHFULNESS: Every factual claim in the answer must be directly supported by the provided CONTEXT.

CONTEXT:
{context_text}

QUESTION: {question}
ANSWER: {answer}

Output ONLY a single float between 0.0 and 1.0. Nothing else.
Score:'''
    return _call_judge(prompt)

def score_answer_relevance(question, answer):
    prompt = f'''You are an expert evaluator assessing RAG system quality.
Score the ANSWER RELEVANCE on a scale from 0.0 to 1.0.
ANSWER RELEVANCE: Does the answer directly address the question?

QUESTION: {question}
ANSWER: {answer}

Output ONLY a single float between 0.0 and 1.0. Nothing else.
Score:'''
    return _call_judge(prompt)

def score_context_recall(question, context_chunks, ground_truth):
    context_text = '\n\n'.join(c['text'] for c in context_chunks)
    prompt = f'''You are an expert evaluator assessing RAG system quality.
Score the CONTEXT RECALL on a scale from 0.0 to 1.0.
CONTEXT RECALL: Does the retrieved CONTEXT contain all information needed to produce the ground truth answer?

QUESTION: {question}
GROUND TRUTH ANSWER: {ground_truth}
RETRIEVED CONTEXT:
{context_text}

Output ONLY a single float between 0.0 and 1.0. Nothing else.
Score:'''
    return _call_judge(prompt)

def evaluate_single(question, answer, context_chunks, ground_truth):
    faithfulness = score_faithfulness(question, answer, context_chunks)
    answer_relevance = score_answer_relevance(question, answer)
    context_recall = score_context_recall(question, context_chunks, ground_truth)
    mean_score = round((faithfulness + answer_relevance + context_recall) / 3, 4)
    return {'faithfulness': round(faithfulness, 4), 'answer_relevance': round(answer_relevance, 4), 'context_recall': round(context_recall, 4), 'mean': mean_score}

def evaluate_dataset(chatbot_name, test_cases, retrieve_fn, generate_fn):
    print(f'\nEvaluating: {chatbot_name}')
    print(f'Test cases: {len(test_cases)}')
    print('-' * 50)
    all_scores = []
    for i, case in enumerate(test_cases, 1):
        question = case['question']
        ground_truth = case['ground_truth']
        chunks = retrieve_fn(question)
        answer = generate_fn(question, chunks)
        scores = evaluate_single(question, answer, chunks, ground_truth)
        all_scores.append(scores)
        print(f'  [{i}/{len(test_cases)}] Q: {question[:50]}')
        print(f'  faith={scores["faithfulness"]:.2f} relev={scores["answer_relevance"]:.2f} recall={scores["context_recall"]:.2f} mean={scores["mean"]:.2f}')
    avg = {
        'chatbot': chatbot_name,
        'faithfulness': round(sum(s['faithfulness'] for s in all_scores) / len(all_scores), 4),
        'answer_relevance': round(sum(s['answer_relevance'] for s in all_scores) / len(all_scores), 4),
        'context_recall': round(sum(s['context_recall'] for s in all_scores) / len(all_scores), 4),
        'mean': round(sum(s['mean'] for s in all_scores) / len(all_scores), 4),
    }
    print(f'\n  AVERAGES -> faith={avg["faithfulness"]:.4f} relev={avg["answer_relevance"]:.4f} recall={avg["context_recall"]:.4f} MEAN={avg["mean"]:.4f}')
    return avg