from langchain_core.messages import SystemMessage, HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

def interpret_dream(
    transcript_path="../transcripts/dream_text.txt",
    output_path="../analysis_outputs/dream_analysis.txt",
    model_name="gemini-2.0-flash"
):
    # ✅ Load environment variables
    load_dotenv()
    # GOOGLE_API_KEY is picked up automatically by LangChain if set

    # ✅ Load dream transcript
    with open(transcript_path, "r", encoding="utf-8") as file:
        dream_text = file.read()

    # ✅ Define the system and user prompts
    system_prompt = SystemMessage(content=(
        "You are a professional dream analyst with deep knowledge of psychology, mythology, and emotional intelligence."
    ))

    user_prompt = f"""
Interpret the following dream:
\"\"\"{dream_text}\"\"\"

Return your response structured like this:

1. Dream Theme:
2. Key Symbols & Meanings:
3. Emotional Tone (scale 0-10 for each):
   - Fear:
   - Joy:
   - Confusion:
   - Curiosity:
4. Interpretation (2-3 paragraphs):
5. Visual Art Prompt (describe what should be illustrated):
6. Journal Entry Summary (1st person, poetic tone):
"""

    # ✅ Load Gemini LLM
    llm = ChatGoogleGenerativeAI(
        model=model_name,
        temperature=0.5,
        max_output_tokens=1000,
    )

    # ✅ Generate response
    response = llm.invoke([
        system_prompt,
        HumanMessage(content=user_prompt)
    ])

    # ✅ Save interpretation
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(response.content)

    print("✅ Dream interpretation saved to:", output_path)
    return output_path
