import streamlit as st
from cpu_rag_with_gemini import rag_pipeline

st.title("💬 RAG Assistant (Gemini + FAISS)")
query = st.text_input("Ask a question:")

if query:
    answer = rag_pipeline(query)
    st.write("**Answer:**")
    st.write(answer)
