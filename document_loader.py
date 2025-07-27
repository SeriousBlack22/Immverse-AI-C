from PyPDF2 import PdfReader

def load_pdf(file_path):
    reader = PdfReader(file_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

def load_txt(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()
