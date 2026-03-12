import time
import os
import datetime
from groq import Groq # Modern 2026 Standard for fast, free AI
from faster_whisper import WhisperModel
from fpdf import FPDF

# --- 1. THE BRAIN: Groq Llama 3 Intelligence ---
def get_intelligence(full_transcript):
    api_key = os.environ.get("GROQ_API_KEY")
    
    if not api_key:
        print("❌ Error: GROQ_API_KEY not found in environment.")
        return "Manual Review Required: API Key Missing.", ["Set environment variable GROQ_API_KEY"]

    client = Groq(api_key=api_key)
    
    # We use Llama 3.3 70B - it's highly intelligent and free on Groq
    prompt = f"""
    Analyze the following transcript and provide a professional executive briefing.
    
    FORMAT YOUR RESPONSE EXACTLY LIKE THIS:
    SUMMARY: [A sophisticated 3-sentence summary of the core message and outcome]
    ACTIONS:
    - [Verb-led action item 1]
    - [Verb-led action item 2]
    - [Verb-led action item 3]
    - [Verb-led action item 4]
    - [Verb-led action item 5]

    TRANSCRIPT:
    {full_transcript}
    """

    try:
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.5,
            max_tokens=1024
        )
        
        res_text = completion.choices[0].message.content
        
        # Parsing Logic
        if "SUMMARY:" in res_text and "ACTIONS:" in res_text:
            summary = res_text.split("SUMMARY:")[1].split("ACTIONS:")[0].strip()
            actions_block = res_text.split("ACTIONS:")[1].strip()
            actions = [a.strip().lstrip('- •*') for a in actions_block.split('\n') if a.strip()]
            
            return summary.encode('latin-1', 'ignore').decode('latin-1'), actions[:5]
        else:
            return "Summary synthesis complete. See transcript for details.", ["Review transcript manually."]

    except Exception as e:
        print(f"⚠️ Intelligence Error: {e}")
        return "Local processing only. AI layer bypassed.", ["Verify Groq API Key and Quota."]

# --- 2. THE FORMATTER: Professional PDF Engine ---
def format_time(seconds):
    return f"{int(seconds // 60):02d}:{int(seconds % 60):02d}"

def clean_text(text):
    return " ".join(text.encode('latin-1', 'ignore').decode('latin-1').split())

def create_pro_report(summary, segments, actions, original_filename):
    pdf = FPDF()
    pdf.add_page()
    
    # Header Banner (Navy Blue)
    pdf.set_fill_color(20, 40, 60) 
    pdf.rect(0, 0, 210, 40, 'F')
    pdf.set_text_color(255, 255, 255)
    pdf.set_font("Arial", 'B', 22)
    pdf.cell(190, 20, txt="AI TECH-SCRIBE INTELLIGENCE", ln=True, align='C')
    pdf.set_font("Arial", 'I', 10)
    pdf.cell(190, 5, txt=f"REPORT GEN: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}", ln=True, align='C')
    pdf.ln(25)

    # Summary Section
    pdf.set_text_color(20, 40, 60)
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(190, 10, txt="EXECUTIVE BRIEFING", ln=True)
    pdf.set_draw_color(20, 40, 60)
    pdf.line(10, pdf.get_y(), 200, pdf.get_y())
    pdf.ln(4)
    pdf.set_text_color(0, 0, 0)
    pdf.set_font("Arial", '', 11)
    pdf.multi_cell(0, 7, txt=summary)
    pdf.ln(8)

    # Action Items Section
    pdf.set_fill_color(240, 245, 250)
    pdf.set_font("Arial", 'B', 12)
    pdf.set_text_color(20, 40, 60)
    pdf.cell(190, 10, txt=">>> CRITICAL TAKEAWAYS", ln=True, fill=True)
    pdf.set_font("Arial", '', 10)
    pdf.set_text_color(0, 0, 0)
    for item in actions:
        pdf.multi_cell(0, 7, txt=f"- {clean_text(item)}")
    pdf.ln(8)

    # Transcript Section
    pdf.set_font("Arial", 'B', 14)
    pdf.set_text_color(20, 40, 60)
    pdf.cell(190, 10, txt="VERIFIED TRANSCRIPT", ln=True)
    pdf.line(10, pdf.get_y(), 200, pdf.get_y())
    pdf.ln(4)
    
    for seg in segments:
        pdf.set_font("Arial", 'B', 9)
        pdf.set_text_color(120, 120, 120)
        pdf.write(7, f"[{format_time(seg.start)}] ")
        pdf.set_font("Arial", '', 10)
        pdf.set_text_color(0, 0, 0)
        pdf.write(7, f"{clean_text(seg.text)}\n")
        pdf.ln(1)

    report_name = f"Report_{original_filename.split('.')[0]}.pdf"
    pdf.output(report_name)
    return report_name

# --- 3. MAIN PIPELINE ---
def main():
    file_path = "meeting.mp3" # CHANGE TO "cricket.mp3" as needed
    
    if not os.path.exists(file_path):
        print(f"❌ File not found: {file_path}")
        return

    print(f"⏳ STAGE 1: Local Transcription ({file_path})...")
    start_time = time.time()
    
    model = WhisperModel("small", device="cpu", compute_type="int8")
    segments_gen, _ = model.transcribe(file_path, beam_size=5)
    segments = list(segments_gen)
    full_text = " ".join([s.text for s in segments])
    
    print("🧠 STAGE 2: Groq Cloud Intelligence (Llama 3)...")
    summary, actions = get_intelligence(full_text)
    
    print("📄 STAGE 3: Finalizing Report...")
    report_file = create_pro_report(summary, segments, actions, file_path)
    
    print(f"\n✅ SUCCESS! saved as: {report_file}")
    print(f"⏱️ Total processing time: {time.time() - start_time:.1f}s")

if __name__ == "__main__":
    main()