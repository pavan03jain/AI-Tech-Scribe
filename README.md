# 🎙️ AI Tech-Scribe Intelligence (v5.0)

**Turn messy meeting audio into executive-grade business intelligence in seconds.**

## 🚀 The Value Proposition
Manual transcription is slow and summaries are often biased. **AI Tech-Scribe** uses a hybrid architecture to provide fast, private, and high-intelligence reports.
- **Privacy First:** Transcription happens locally on your hardware.
- **Executive Grade:** Powered by Gemini 2.0 for human-level summaries.
- **Action Oriented:** Automatically extracts tasks and deadlines.

## 🛠️ Tech Stack
- **Transcription:** OpenAI Whisper (via Faster-Whisper)
- **Intelligence:** Google Gemini 1.5/2.0 Flash
- **Output:** FPDF (Automated PDF Reporting)
- **Language:** Python 3.11+

## 📄 Sample Output
The engine generates a `Professional_Report.pdf` containing:
1. **Executive Summary:** A 3-sentence high-level brief.
2. **Action Items:** 5 critical tasks identified from the conversation.
3. **Verified Transcript:** Cleaned, timestamped verbatim text.

## ⚙️ Quick Start
1. Clone the repo: `git clone https://github.com/pavan03jain/AI-Tech-Scribe.git`
2. Install dependencies: `pip install -r requirements.txt`
3. Add your Gemini API Key to `engine.py`.
4. Run: `python engine.py`