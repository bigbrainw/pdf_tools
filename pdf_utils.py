import fitz  # PyMuPDF
import anthropic
import os
from dotenv import load_dotenv

load_dotenv()
client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

def extract_paragraphs(pdf_path):
    doc = fitz.open(pdf_path)
    paragraphs = []
    for page_num, page in enumerate(doc):
        blocks = page.get_text("blocks")
        for block in blocks:
            text = block[4].strip()
            if text:
                paragraphs.append({
                    'page_num': page_num,
                    'text': text,
                    'bbox': block[:4]
                })
    return paragraphs

def find_relevant_paragraphs(paragraphs, user_query):
    prompt = (
        "Here are some paragraphs from a PDF document:\n\n" +
        "\n\n".join(f"Paragraph {i+1}: {para['text']}" for i, para in enumerate(paragraphs[:50])) +
        f"\n\nBased on the question: '{user_query}', return a comma-separated list of paragraph numbers that are most relevant."
    )

    response = client.messages.create(
        model="claude-3-7-sonnet-20250219",
        max_tokens=100,
        messages=[{"role": "user", "content": prompt}]
    )

    indices = [int(x.strip()) - 1 for x in response.content[0].text.split(',') if x.strip().isdigit()]
    return [paragraphs[i] for i in indices if 0 <= i < len(paragraphs)]

def highlight_paragraphs(pdf_path, output_path, paragraphs_to_highlight):
    doc = fitz.open(pdf_path)
    for para in paragraphs_to_highlight:
        page = doc[para['page_num']]
        rect = fitz.Rect(para['bbox'])
        page.add_highlight_annot(rect)
    doc.save(output_path, garbage=4, deflate=True)
