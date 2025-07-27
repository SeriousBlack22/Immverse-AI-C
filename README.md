# Immverse-AI-C

This project is a RAG (Retrieval-Augmented Generation) application that uses Google's Gemini model to answer questions based on a provided document.

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

### Streamlit UI

To run the Streamlit user interface:

```bash
streamlit run streamlit_rag_ui.py
```

### Command-Line Interface

To run the command-line interface:

```bash
python cpu_rag_with_gemini.py
```

