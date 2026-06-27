import os
import fitz
from docx import Document

def load_txt(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

def load_pdf(path):
    doc = fitz.open(path)
    pages = []
    for page in doc:
        pages.append(page.get_text())
    return ' '.join(pages)

def load_docx(path):
    doc = Document(path)
    paragraphs = []
    for p in doc.paragraphs:
        if p.text.strip():
            paragraphs.append(p.text)
    return ' '.join(paragraphs)

def load_document(path):
    ext = os.path.splitext(path)[1].lower()
    if ext == '.txt':
        return load_txt(path)
    elif ext == '.pdf':
        return load_pdf(path)
    elif ext == '.docx':
        return load_docx(path)
    else:
        raise ValueError(f'Unsupported file type: {ext}')

if __name__ == '__main__':
    for filename in ['day2/sample.txt', 'day2/sample.pdf', 'day2/sample.docx']:
        print(f'\n--- Loading {filename} ---')
        text = load_document(filename)
        print(f'Characters loaded: {len(text)}')
        print(f'Preview: {text[:150]}...')