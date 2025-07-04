from pathlib import Path
from nltk import sent_tokenize
import re

def clean_text(text):
    text = re.sub(r'\s+', ' ', text)
    return text

def chunk_text(text, max_words=300):
    sentences = sent_tokenize(text)
    chunks, chunk = [], []
    word_count = 0
    for sentence in sentences:
        words = sentence.split()
        if word_count + len(words) <= max_words:
            chunk.append(sentence)
            word_count += len(words)
        else:
            chunks.append(" ".join(chunk))
            chunk, word_count = [sentence], len(words)
    if chunk:
        chunks.append(" ".join(chunk))
    return chunks

if __name__ == "__main__":
    raw_text = Path("data/AI_Training_Document.txt").read_text(encoding="utf-8")
    clean = clean_text(raw_text)
    chunks = chunk_text(clean)
    Path("chunks").mkdir(exist_ok=True)
    for i, c in enumerate(chunks):
        Path(f"chunks/chunk_{i}.txt").write_text(c, encoding="utf-8")
