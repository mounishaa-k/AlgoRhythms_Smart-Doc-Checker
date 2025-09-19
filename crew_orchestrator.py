import google.generativeai as genai
import json
from billing import charge_flexprice

API_KEY = "give ur api key"
genai.configure(api_key=API_KEY)

class SmartDocChecker:
    def __init__(self, documents):
        self.documents = documents

    def run(self):
        docs_context = "\n\n".join(
            [f"Filename: {doc['filename']}\nContent:\n{doc['text']}" for doc in self.documents]
        )

        prompt = f"""
        You are a document analysis agent. Compare the following documents and detect:
        - Contradictions (different rules, deadlines, policies)
        - Ambiguities
        - Overlaps

        Return the output STRICTLY in JSON with this format:
        {{
          "conflicts": [
            {{"type": "string", "description": "string"}}
          ],
          "suggestions": ["string", "string"],
          "usage_docs": {len(self.documents)},
          "usage_reports": 1
        }}

        Documents to analyze:
        {docs_context}
        """

        try:
            model = genai.GenerativeModel("gemini-1.5-flash")
            response = model.generate_content([prompt])
            text = response.text.strip()

            # Try JSON parsing
            try:
                result_json = json.loads(text)
            except Exception:
                # Sometimes Gemini wraps in code fences ```json ... ```
                if text.startswith("```"):
                    text = text.strip("` \n").replace("json", "", 1).strip()
                result_json = json.loads(text)

            conflicts = result_json.get("conflicts", [])
            suggestions = result_json.get("suggestions", [])

            if isinstance(suggestions, str):
                suggestions = [suggestions]

            result_json = {
                "conflicts": conflicts,
                "suggestions": suggestions,
                "usage_docs": len(self.documents),
                "usage_reports": 1
            }

        except Exception as e:
            result_json = {
                "conflicts": [],
                "suggestions": [f"Parsing error: {str(e)}"],
                "usage_docs": len(self.documents),
                "usage_reports": 1
            }

        # Billing
        charge_flexprice("docs", len(self.documents))
        charge_flexprice("reports", 1)

        return result_json


def run_check(documents):
    checker = SmartDocChecker(documents)
    return checker.run()
