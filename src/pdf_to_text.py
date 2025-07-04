import pdfplumber
from pathlib import Path

pdf_path = "data/AI Training Document.pdf"
output_path = "data/AI_Training_Document.txt"

with pdfplumber.open(pdf_path) as pdf:
    full_text = ""
    for page in pdf.pages:
        text = page.extract_text()
        if text:
            full_text += text + "\n"

Path(output_path).write_text(full_text, encoding="utf-8")
print(f"✅ PDF converted to: {output_path}")
