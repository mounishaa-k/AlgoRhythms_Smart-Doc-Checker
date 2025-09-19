import google.generativeai as genai
import os

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def analyze_document_text(text, filename):
    """Call Gemini API to analyze document text."""
    model = genai.GenerativeModel("gemini-pro")
    prompt = f"""
    Extract key rules, policies, or constraints from the document '{filename}'.
    Return them as a JSON list of items like:
    [
      {{"rule": "Submit before 10 PM", "category": "deadline"}},
      {{"rule": "Attendance minimum 75%", "category": "policy"}}
    ]
    """
    response = model.generate_content(prompt + "\n\nDocument:\n" + text)
    return {"filename": filename, "rules": response.text}
