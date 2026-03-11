# AI Tech-Scribe Solutions: Intelligence Pipeline v1.2

## 🚀 Overview
This is a production-ready **AI Transcription & Intelligence Pipeline**. It transforms raw audio into structured, professional executive reports using state-of-the-art Neural Networks and Natural Language Processing (NLP).

## 🛠️ The Technology Stack
- **Speech-to-Text:** OpenAI Whisper (Transformer-based Encoder-Decoder)
- **NLP Engine:** Custom Python post-processing for "Clean Verbatim" scrubbing.
- **Inference Mode:** Optimized for CPU (FP32) for maximum accessibility.
- **Reporting:** Automated PDF generation via FPDF.

## 📦 Key Features
- **High-Accuracy Transcription:** Leverages the 'Small' Whisper model for 90%+ accuracy.
- **Clean Verbatim Filtering:** Automated removal of linguistic fillers (um, uh, like, you know).
- **Extractive Summarization:** Algorithm-based intelligence layer that identifies key takeaways.
- **Branded PDF Export:** Generates a ready-to-deliver business document with professional formatting.

## 📂 Project Structure
- `engine.py`: The core pipeline (Load -> Transcribe -> Clean -> Summarize -> Export).
- `Professional_Report.pdf`: The final branded deliverable for the client.
- `venv/`: Isolated virtual environment for stability.

## 🚦 Getting Started
1. Activate environment: `.\venv\Scripts\Activate.ps1`
2. Run pipeline: `python engine.py`
3. View results in `Professional_Report.pdf`