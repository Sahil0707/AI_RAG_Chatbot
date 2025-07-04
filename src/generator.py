from transformers import pipeline

# Define model name globally
MODEL_NAME = "EleutherAI/gpt-neo-125M"

# Load generator pipeline
print(f"🔄 Loading {MODEL_NAME} model on CPU...")
generator = pipeline("text-generation", model=MODEL_NAME, device=-1)
print(f"✅ {MODEL_NAME} model loaded.")

# Response generation function
def generate_response(query, contexts):
    # Use only top 3 contexts to control token length
    context_text = "\n".join(contexts[:3])

    prompt = f"""You are a helpful assistant. Answer the question based on the context below:
Context:
{context_text}
Question: {query}
Answer:"""

    # Generate response safely — no need to set max_length
    response = generator(prompt,
                         max_new_tokens=128,
                         do_sample=True,
                         pad_token_id=50256)[0]['generated_text']

    final_answer = response.split("Answer:")[-1].strip()
    return final_answer
