# Immverse-AI-C

# 🧠 CPU-Based RAG LLM Inference Pipeline (Gemini + FAISS + MiniLM)

This project implements a **Retrieval-Augmented Generation (RAG)** pipeline optimized to run on **CPU-only environments** using:

- 🔍 FAISS for document similarity search
- 🧠 SentenceTransformers (MiniLM) for vector embeddings
- 🤖 Google Gemini API for generating final answers
- 💻 Streamlit Web UI and Command-Line Interface
- 📊 Benchmarking support for latency measurement

---

## 🚀 Features

- ✅ CPU-only execution — no GPU required
- ⚡ Lightweight and fast (MiniLM + FAISS)
- 🔌 Easily pluggable knowledge base (`documents.txt`)
- 🤖 Gemini-powered natural language responses
- 🧪 Benchmarks latency in `benchmark_results.txt`
- 🌐 Simple Streamlit-based Web UI

---

## 📂 Project Structure

| File                       | Purpose                                                       |
|----------------------------|---------------------------------------------------------------|
| `cpu_rag_with_gemini.py`   | Main CLI pipeline for retrieval + Gemini answer               |
| `streamlit_rag_ui.py`      | Streamlit app for interactive querying                        |
| `document_loader.py`       | Utility to load `.txt` or `.pdf` documents                    |
| `documents.txt`            | The document knowledge base (1 line = 1 document)             |
| `benchmark_results.txt`    | Logs of time taken per query                                  |
| `requirements.txt`         | Python package requirements                                   |
| `README.md`                | Project documentation                                         |

---

## 🛠️ Technologies Used

| Component              | Tool / Library                        |
|------------------------|----------------------------------------|
| Text Embedding         | `sentence-transformers` (MiniLM)       |
| Vector Similarity      | `faiss-cpu`                            |
| Language Model (LLM)   | Google Gemini API (`generativeai`)     |
| Web Interface (UI)     | `streamlit` (optional)                 |
| Benchmarking           | Python `time`, stored in `.txt` file   |

---

## Setup

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/Immverse-AI-C.git
    cd Immverse-AI-C
    ```

2.  **Create a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Create a `.env` file:**
    Create a file named `.env` in the root of the project and add your Google API key:
    ```
    GOOGLE_API_KEY="YOUR_API_KEY_HERE"
    ```

## Usage


### Command-Line Interface

To run the command-line interface:

```bash
python cpu_rag_with_gemini.py
```

### Streamlit UI

To run the Streamlit user interface:

```bash
streamlit run streamlit_rag_ui.py
```