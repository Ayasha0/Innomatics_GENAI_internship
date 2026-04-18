import PyPDF2
from io import BytesIO

def extract_text(uploaded_file) -> str:
    """Extract text from an uploaded file (PDF or TXT)."""
    if uploaded_file.name.lower().endswith(".pdf"):
        reader = PyPDF2.PdfReader(BytesIO(uploaded_file.read()))
        text = ""
        for page in reader.pages:
            extracted = page.extract_text()
            if extracted:
                text += extracted + "\n"
        return text
    elif uploaded_file.name.lower().endswith(".txt"):
        return uploaded_file.read().decode("utf-8")
    else:
        raise ValueError("Unsupported file format. Please upload a PDF or TXT file.")