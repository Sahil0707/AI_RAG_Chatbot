import streamlit as st
from src.rag_pipeline import rag_chatbot
from src.generator import MODEL_NAME
from pathlib import Path

# App config
st.set_page_config(page_title="AI RAG Chatbot", page_icon="🤖", layout="wide")
st.title("📖 AI-RAG Chatbot")

# Sidebar info
with st.sidebar:
    st.header("📊 Chatbot Info")
    st.write(f"**Model in use:** `{MODEL_NAME}`")

    chunk_count = len(list(Path("chunks").glob("*.txt")))
    st.write(f"**Number of document chunks:** `{chunk_count}`")

    st.markdown("---")
    st.caption("Built by Sahil")

# User input field
user_query = st.text_input("💬 Ask a question:")

if st.button("🔍 Ask"):
    if not user_query:
        st.warning("Please enter a question.")
    else:
        with st.spinner("Generating answer..."):
            response, contexts = rag_chatbot(user_query)

        st.success("✅ Answer generated:")
        st.markdown(f"**Answer:** {response}")

        st.markdown("---")
        st.subheader("📄 Source Passages")
        for i, c in enumerate(contexts, start=1):
            with st.expander(f"Source {i}"):
                st.write(c)
