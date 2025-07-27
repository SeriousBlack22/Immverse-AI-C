import os
import time
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# --- Configuration ---
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
GENAI_MODEL = "models/gemini-1.5-flash-latest"
DOCUMENT_FILE = "documents.txt"
TOP_K = 2

# --- Initialize Gemini ---
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel(GENAI_MODEL)

# --- Load Documents ---
with open(DOCUMENT_FILE, "r", encoding="utf-8") as f:
    docs = [line.strip() for line in f.readlines() if line.strip()]

# --- Create Embeddings and FAISS index ---
print("Loading embedding model...")
embed_model = SentenceTransformer("all-MiniLM-L6-v2")
embeddings = embed_model.encode(docs)
index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(np.array(embeddings))

# --- RAG Pipeline ---
def rag_pipeline(user_query):
    print(f"\n [Query]: {user_query}")
    
    query_vec = embed_model.encode([user_query])
    top_k_scores, top_k_indices = index.search(np.array(query_vec), TOP_K)
    top_docs = [docs[i] for i in top_k_indices[0]]

    print("[Top Docs]:", top_docs)

    # Start benchmarking
    start = time.time()

    prompt = f"Use the following docs to answer the question:\n{top_docs}\n\nQuestion: {user_query}"
    response = model.generate_content([{"role": "user", "parts": [prompt]}])
    end = time.time()

    # Print and save
    print("\n[Gemini Answer]:", response.text)
    elapsed_time = end - start
    print(f"Total time: {elapsed_time:.2f} seconds")

    with open("benchmark_results.txt", "a") as f:
        f.write(f"Query: {user_query}\n")
        f.write(f"Time Taken: {elapsed_time:.2f} seconds\n")
        f.write("-" * 40 + "\n")

# --- Main ---
if __name__ == "__main__":
    print("\nGemini RAG Assistant Ready (CPU Only)")
    while True:
        user_input = input("\nAsk: ")
        if user_input.lower() in ["exit", "quit"]:
            break
        rag_pipeline(user_input)
