import pdfplumber
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load API Key
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)

def extract_text_from_pdf(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n\n"
    return text

def summarize_text(text):
    model = genai.GenerativeModel("gemini-1.5-flash-001")
    response = model.generate_content(
        f"Summarize this financial document, focusing on future growth, business changes, and key triggers:\n\n{text}"
    )
    return response.text

if __name__ == "__main__":
    pdf_path = "D:\Aakash\SDE\Projects\Job Assignments\InvestorReportAnalyzer\SJS Transcript Call.pdf"  ##### pdf path in local
    extracted_text = extract_text_from_pdf(pdf_path)

    if extracted_text.strip():
        summary = summarize_text(extracted_text)
        print("\n*** Summary of the PDF ***\n")
        print(summary)

        ####### Save summary
        with open("summary.txt", "w", encoding="utf-8") as f:
            f.write(summary)
    else:
        print("No text extracted from the PDF. Check the file.")
