from src.retriever import retrieve
from src.generator import generate_response

def rag_chatbot(query):
    contexts = retrieve(query)
    response = generate_response(query, contexts)
    return response, contexts
