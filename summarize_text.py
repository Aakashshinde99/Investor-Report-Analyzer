import google.generativeai as genai
import os
from dotenv import load_dotenv

############# load api ###########
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=GEMINI_API_KEY)

def summarize_text(text):
    model = genai.GenerativeModel("gemini-1.5-flash-001")
    response = model.generate_content(
        f"Summarize this financial document, focusing on growth, key changes, and future prospects:\n\n{text}"
    )
    return response.text

if __name__ == "__main__":
    sample_text = "Company XYZ reported strong earnings this quarter with projected growth in the technology sector..."
    summary = summarize_text(sample_text)
    print(summary)
