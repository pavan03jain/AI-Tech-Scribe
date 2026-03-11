# How the AI Intelligence Pipeline Works

### 1. Audio Processing (The Hearing)
The system uses the **Faster-Whisper** engine. It converts sound waves into a visual "spectrogram" that the AI can read. We use **int8 quantization**, which makes the math simpler and the processing 4x faster.

### 2. Natural Language Processing (The Cleaning)
After the AI writes the text, a Python filter scans for "filler words" (um, uh, like). It removes them to create a **Clean Verbatim** transcript.

### 3. Summarization (The Intelligence)
The script analyzes the transcript and extracts the most important sentences (Intro, Middle, and Conclusion) to create a quick **Executive Summary**.
