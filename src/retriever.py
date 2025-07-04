import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
import pickle

model = SentenceTransformer('all-MiniLM-L6-v2')
index = faiss.read_index("vectordb/document_index.faiss")
with open("vectordb/chunks.pkl", "rb") as f:
    texts = pickle.load(f)

def retrieve(query, top_k=3):
    query_vec = model.encode([query]).astype("float32")
    distances, indices = index.search(query_vec, top_k)
    return [texts[i] for i in indices[0]]

if __name__ == "__main__":
    print(retrieve("What is eBay's refund policy?"))
