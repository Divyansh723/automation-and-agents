# main.py
from scripts.transcribe import transcribe_dream_audio
from scripts.interpret_dream import interpret_dream 
from scripts.generate_art import generate_dream_image
from scripts.journal_entry import save_to_notion

def run_dream_pipeline():
    print("\n🎤 STEP 1: Transcribing audio...")
    dream_text = transcribe_dream_audio(
        audio_path="whisper_input/dream.wav",
        output_path="transcripts/dream_text.txt"
    )

    print("\n🧠 STEP 2: Interpreting the dream with Gemini...")
    interpretation_path = interpret_dream(
        transcript_path="transcripts/dream_text.txt",
        output_path="analysis_outputs/dream_analysis.txt"
    )

    print("\n🎨 STEP 3: Generating dream image using Stable Diffusion...")
    image_path = generate_dream_image(
        analysis_path="analysis_outputs/dream_analysis.txt",
        output_path="art_outputs/dream_image.png"
    )

    print("\n📒 STEP 4: Uploading to Notion...")
    save_to_notion(
        dream_text_path="transcripts/dream_text.txt",
        analysis_path="analysis_outputs/dream_analysis.txt",
        image_url="https://your-image-url.com/dream_image.png"  # update this if auto-uploaded
    )

    print("\n✅ DreamWeaver.AI pipeline complete!")

if __name__ == "__main__":
    run_dream_pipeline()