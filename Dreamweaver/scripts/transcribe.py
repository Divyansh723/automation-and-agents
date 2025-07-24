import whisper
import os

def transcribe_dream_audio(
    audio_path="../whisper_input/dream.wav",
    output_path="../transcripts/dream_text.txt",
    model_size="base"
):
    # 🎙️ Load Whisper model
    print(f"🔍 Loading Whisper model: {model_size}")
    model = whisper.load_model(model_size)

    # 🎧 Transcribe audio
    print(f"🎤 Transcribing: {audio_path}")
    result = model.transcribe(audio_path)

    # 💾 Save transcript
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(result["text"])

    print("✅ Transcription complete!")
    print("📝 Dream Text:", result["text"])
    return result["text"]
