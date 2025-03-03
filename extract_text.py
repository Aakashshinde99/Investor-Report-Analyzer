import pdfplumber

def extract_text_from_pdf(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n\n"
    return text

if __name__ == "__main__":
    pdf_path = "D:\Aakash\SDE\Projects\Job Assignments\InvestorReportAnalyzer\SJS Transcript Call.pdf"
    extracted_text = extract_text_from_pdf(pdf_path)
    print(extracted_text[:1000])  