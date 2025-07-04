from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
from pathlib import Path
import pickle

model = SentenceTransformer('all-MiniLM-L6-v2')
chunk_files = sorted(Path("chunks").glob("*.txt"))
texts = [f.read_text(encoding="utf-8") for f in chunk_files]
embeddings = model.encode(texts, show_progress_bar=True)

index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(np.array(embeddings).astype("float32"))
faiss.write_index(index, "vectordb/document_index.faiss")

with open("vectordb/chunks.pkl", "wb") as f:
    pickle.dump(texts, f)
