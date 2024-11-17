from PyPDF2 import PdfReader

def extract_text_from_pdf(file_path, query=None):
    reader = PdfReader(file_path)
    text = "".join(page.extract_text() for page in reader.pages)
    if query:
        return f"Query: '{query}' - Relevant text: {text[:500]}"  # Simplified query logic
    return text
