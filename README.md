# AlgoRhythms_Smart-Doc-Checker
Smart Doc Checker Agent — A Streamlit-based AI tool that scans multiple documents, detects contradictions, overlaps, and ambiguities, and generates clean human-readable reports (TXT/DOCX) with visual insights. Includes billing counters and external policy monitoring.
# 📄 Smart Doc Checker Agent

Smart Doc Checker Agent is an **AI-powered document analyzer** built with **Streamlit** and **Gemini API**.  
It helps organizations quickly detect **contradictions, overlaps, and ambiguities** across multiple documents such as guidelines, policies, contracts, or circulars — and generates **human-friendly reports** in both `.txt` and `.docx` formats with **visual insights**.

---

## 🚀 Features

- 📂 Upload multiple documents (`.txt` / `.md`)  
- 🤖 **AI-powered analysis** of contradictions, ambiguities, and overlaps  
- 💡 Human-readable **suggestions** for resolving conflicts  
- 📊 Interactive **conflict distribution charts** (horizontal bar graphs)  
- 📥 Downloadable reports in **TXT** and **DOCX** formats  
- 📈 **Usage tracking** (documents analyzed & reports generated)  
- 💰 **Flexprice billing integration** (bill per doc/report)  
- 🌐 **External policy monitoring** (mock updates via Pathway integration)  

---

## 📂 Project Structure

smart-doc-checker/
│
├── app.py # Streamlit UI entry point
├── crew_orchestrator.py # Orchestrates Gemini calls & handles parsing
├── gemini_client.py # Gemini API wrapper (rule extraction)
├── conflict_detector.py # Rule-based conflict detection (basic checks)
├── report_generator.py # Generates suggestions based on conflicts
├── pathway_monitor.py # Mock monitor for external policy updates
├── billing.py # Flexprice billing logic
├── requirements.txt # Project dependencies
└── venv/ # Virtual environment (not committed)

---

## 🛠️ Tech Stack

**Core Frameworks & Libraries**
- [Streamlit](https://streamlit.io/) → Interactive UI  
- [Matplotlib](https://matplotlib.org/) → Conflict distribution graphs  
- [python-docx](https://python-docx.readthedocs.io/) → Generate `.docx` reports  

**AI / NLP**
- [Google Gemini API](https://ai.google.dev/) → Document comparison & contradiction detection  

**Billing & Monitoring**
- Custom **Flexprice Billing** → Tracks docs analyzed & reports generated  
- Mock **Pathway Monitor** → Simulates external updates (like rule page changes)  

**Language**
- Python 3.9+  

---

## ⚙️ Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/smart-doc-checker.git
   cd smart-doc-checker
Create and activate a virtual environment:

python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
Install dependencies:

pip install -r requirements.txt
Set up your Gemini API Key:

export GEMINI_API_KEY="your_api_key_here"   # macOS/Linux
set GEMINI_API_KEY=your_api_key_here        # Windows
▶️ Usage
Run the Streamlit app:

bash
Copy code
streamlit run app.py
Upload 2–3 documents (.txt / .md).

Click Run Check:

📊 Contradictions displayed clearly

💡 Suggestions shown in bullet format

📈 Conflict distribution chart (bar graph) displayed

📥 Download clean report as .txt or .docx

Try External Policy Monitor to see simulated updates.

📊 Workflow
Upload Documents → Files sent to crew_orchestrator.py.

Gemini API Analysis → Detects contradictions, ambiguities, overlaps.

Results Parsing → Extracts into conflicts & suggestions.

Streamlit Display → Shows contradictions, suggestions, and chart.

Report Generation → Downloadable in .txt and .docx.

Billing → Tracks docs analyzed & reports generated.

Policy Monitor → Simulates rule/policy updates.

📜 Example Report
TXT / DOCX Output:
Smart Doc Checker Report
==============================

CONTRADICTIONS:
1. [Timing] Devnovate-poster.txt states 10:00 AM start; Guidelines require reporting before 8:30 AM.
2. [Food] Poster mentions "Free meals"; Guidelines state no meals will be provided.
3. [Location] Poster lists KLH Bowrampet; Guidelines list KLH Bachupally.

SUGGESTIONS:
- Harmonize the reporting times across documents.
- Clarify the policy on meals & swag.
- Resolve ambiguity in the venue.
📸 Screenshots
<img width="1920" height="1020" alt="image" src="https://github.com/user-attachments/assets/1ebddf95-ab92-41a8-8621-7758a33d0dbb" />
<img width="1920" height="1020" alt="image" src="https://github.com/user-attachments/assets/88bcfcda-de55-41ff-b599-fad689fc8d95" />
<img width="1920" height="1020" alt="image" src="https://github.com/user-attachments/assets/48a44e0f-1e58-479b-9c79-dad4e896ec0c" />
<img width="1920" height="1020" alt="image" src="https://github.com/user-attachments/assets/51be60cf-d1cc-4029-a3fd-2748dcf1790a" />
<img width="1920" height="1020" alt="image" src="https://github.com/user-attachments/assets/86617d58-da3a-4a15-a278-5f0fd1ef81bd" />

💰 Billing Logic (Flexprice)
Per Document analyzed → increments doc usage counter

Per Report generated → increments report usage counter

Usage stats are displayed in the app.

🌐 External Policy Monitor
Simulates detection of updates like:

"New circular: attendance now 70%"

"Policy updated: notice period changed to 3 weeks"

Triggers re-checking of conflicts.

🔮 Future Improvements
📄 Support for PDF/Word uploads

🧠 Advanced contradiction detection with embeddings/LLMs

⏱️ Real-time monitoring via Pathway API

🎨 Richer visualizations (timelines, word clouds)

🌍 Multi-language document support
