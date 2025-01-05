import PyPDF2
from typing import List, Dict
import re
from collections import deque
import json
import os
from datetime import datetime


def extract_text_from_pdf(pdf_path: str) -> str:
    """Extract text from PDF file."""
    text = ""
    with open(pdf_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        for page in pdf_reader.pages:
            text += page.extract_text() + "\n"
    return text


def preprocess_text(text: str) -> str:
    """Clean and preprocess the extracted text."""
    # Remove excessive newlines and whitespace
    text = re.sub(r'\n+', '\n', text)
    text = re.sub(r'\s+', ' ', text)
    # Remove footer/header patterns (customize based on your PDF)
    text = re.sub(r'\d+\s*of\s*\d+', '', text)
    return text.strip()


def split_into_sentences(text: str) -> List[str]:
    """Split text into sentences using basic rules."""
    # Simple sentence splitting - can be improved with nltk or spacy
    sentences = re.split(r'(?<=[.!?])\s+', text)
    return [s.strip() for s in sentences if s.strip()]


def create_semantic_chunks(sentences: List[str],
                           max_chunk_size: int = 1000,
                           overlap: int = 100) -> List[Dict]:
    """
    Create overlapping chunks of text that preserve semantic meaning.
    Returns list of dictionaries with chunk text and metadata.
    """
    chunks = []
    current_chunk = []
    current_size = 0

    # Use deque for sliding window of previous sentences
    previous_sentences = deque(maxlen=3)

    for sentence in sentences:
        sentence_size = len(sentence)

        # If adding this sentence would exceed max size, create new chunk
        if current_size + sentence_size > max_chunk_size and current_chunk:
            # Create chunk with metadata
            chunk_text = ' '.join(current_chunk)
            chunks.append({
                'text': chunk_text,
                'size': len(chunk_text),
                'sentences': len(current_chunk),
                'overlap_previous': ' '.join(list(previous_sentences))
            })

            # Start new chunk with overlap
            overlap_size = 0
            overlap_sentences = []

            # Add sentences from end of previous chunk until overlap size is reached
            for prev_sentence in reversed(current_chunk):
                if overlap_size + len(prev_sentence) > overlap:
                    break
                overlap_sentences.insert(0, prev_sentence)
                overlap_size += len(prev_sentence)

            current_chunk = overlap_sentences
            current_size = overlap_size

        current_chunk.append(sentence)
        current_size += sentence_size
        previous_sentences.append(sentence)

    # Add final chunk
    if current_chunk:
        chunk_text = ' '.join(current_chunk)
        chunks.append({
            'text': chunk_text,
            'size': len(chunk_text),
            'sentences': len(current_chunk),
            'overlap_previous': ' '.join(list(previous_sentences))
        })

    return chunks


def chunk_pdf(pdf_path: str,
              max_chunk_size: int = 1000,
              overlap: int = 100) -> List[Dict]:
    """
    Main function to process PDF and create semantic chunks.
    Returns list of chunks with metadata.
    """
    # Extract and preprocess text
    raw_text = extract_text_from_pdf(pdf_path)
    clean_text = preprocess_text(raw_text)

    # Split into sentences
    sentences = split_into_sentences(clean_text)

    # Create chunks
    chunks = create_semantic_chunks(sentences, max_chunk_size, overlap)

    return chunks


def export_chunks(chunks: List[Dict],
                  output_format: str = 'markdown',
                  output_dir: str = 'chunks',
                  pdf_name: str = 'document') -> str:
    """
    Export chunks to readable format.
    Supports 'markdown' and 'json' formats.
    Returns the path to the output directory.
    """
    # Create output directory if it doesn't exist
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_dir = f"./chunking/{output_dir}_{pdf_name}_{timestamp}"
    os.makedirs(output_dir, exist_ok=True)

    if output_format == 'markdown':
        # Create a single markdown file with all chunks
        output_path = os.path.join(output_dir, f"{pdf_name}_chunks.md")
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(f"# Chunks from {pdf_name}\n\n")
            f.write(
                f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")

            for i, chunk in enumerate(chunks, 1):
                f.write(f"## Chunk {i}\n\n")
                f.write(f"- Size: {chunk['size']} characters\n")
                f.write(f"- Sentences: {chunk['sentences']}\n\n")
                f.write("### Content:\n\n")
                f.write(f"{chunk['text']}\n\n")
                f.write("### Overlap with Previous Chunk:\n\n")
                f.write(f"{chunk['overlap_previous']}\n\n")
                f.write("---\n\n")

    elif output_format == 'json':
        # Export as JSON with pretty formatting
        output_path = os.path.join(output_dir, f"{pdf_name}_chunks.json")
        export_data = {
            'document_name': pdf_name,
            'generation_time': datetime.now().isoformat(),
            'chunks': chunks
        }
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(export_data, f, indent=2, ensure_ascii=False)

    else:
        raise ValueError(f"Unsupported output format: {output_format}")

    return output_dir


# Example usage
if __name__ == "__main__":
    pdf_path = "./pdfs/SWEBOK.pdf"
    pdf_name = os.path.splitext(os.path.basename(pdf_path))[0]

    # Generate chunks
    chunks = chunk_pdf(
        pdf_path,
        max_chunk_size=1000,
        overlap=100
    )

    # Export in both formats
    markdown_dir = export_chunks(chunks, 'markdown', pdf_name=pdf_name)
    json_dir = export_chunks(chunks, 'json', pdf_name=pdf_name)

    print(f"Chunks exported to:")
    print(f"Markdown: {markdown_dir}")
    print(f"JSON: {json_dir}")
