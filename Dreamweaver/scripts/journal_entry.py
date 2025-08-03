from notion_client import Client
from datetime import datetime
import os
from dotenv import load_dotenv

def extract_section(content, start_tags, end_tags=None):
    """
    Extract a section from content using multiple possible start and end tag styles.
    """
    content = content.replace("  ", " ").replace("*", "") 
    start_idx = end_idx = -1

    for tag in start_tags:
        if tag in content:
            start_idx = content.find(tag) + len(tag)
            break

    if start_idx == -1:
        return ""

    if end_tags:
        for tag in end_tags:
            if tag in content[start_idx:]:
                end_idx = content.find(tag, start_idx)
                break
    else:
        end_idx = len(content)

    return content[start_idx:end_idx].strip() if end_idx != -1 else content[start_idx:].strip()

def save_to_notion(
    dream_text_path="../transcripts/dream_text.txt",
    analysis_path="../analysis_outputs/dream_analysis.txt",
    image_url="https://your-image-url.com/dream_image.png"
):
    # 🔐 Load environment variables
    load_dotenv()
    NOTION_TOKEN = os.getenv("NOTION_TOKEN")
    DATABASE_ID = os.getenv("NOTION_DB_ID")

    # 🧠 Initialize Notion client
    notion = Client(auth=NOTION_TOKEN)

    # 📄 Load dream text and analysis
    with open(dream_text_path, "r", encoding="utf-8") as f:
        dream_text = f.read().strip()

    with open(analysis_path, "r", encoding="utf-8") as f:
        analysis = f.read()

    # ✨ Extract sections with tag flexibility
    theme = extract_section(
        analysis,
        ["1. **Dream Theme:**", "1. Dream Theme:"],
        ["2. **Key Symbols", "2. Key Symbols"]
    )

    mood_scores = extract_section(
        analysis,
        ["3. **Emotional Tone", "3. Emotional Tone"],
        ["4. **Interpretation", "4. Interpretation"]
    )

    interpretation = extract_section(
        analysis,
        ["4. **Interpretation:**", "4. Interpretation:"],
        ["5. **Visual Art Prompt", "5. Visual Art Prompt"]
    )

    visual_prompt = extract_section(
        analysis,
        ["5. **Visual Art Prompt:**", "5. Visual Art Prompt:"],
        ["6. **Journal Entry Summary", "6. Journal Entry Summary"]
    )

    journal_summary = extract_section(
        analysis,
        ["6. **Journal Entry Summary (1st person, poetic tone):**", "6. Journal Entry Summary:","6. Journal Entry Summary (1st person, poetic tone):"]
    )

    # 📝 Push to Notion
    response = notion.pages.create(
        parent={"database_id": DATABASE_ID},
        properties={
            "Dream Title": {
                "title": [{
                    "text": {
                        "content": "Dream on " + datetime.now().strftime("%B %d, %Y")
                    }
                }]
            },
            "Date": {
                "date": {
                    "start": datetime.now().isoformat()
                }
            },
            "Dream Text": {
                "rich_text": [{"text": {"content": dream_text[:2000]}}]
            },
            "Theme": {
                "rich_text": [{"text": {"content": theme[:2000]}}]
            },
            "Mood Scores": {
                "rich_text": [{"text": {"content": mood_scores[:2000]}}]
            },
            "Interpretation": {
                "rich_text": [{"text": {"content": interpretation[:2000]}}]
            },
            "Visual Prompt": {
                "rich_text": [{"text": {"content": visual_prompt[:2000]}}]
            },
            "Journal Summary": {
                "rich_text": [{"text": {"content": journal_summary[:2000]}}]
            },
            "Image URL": {
                "url": image_url
            }
        }
    )

    print("✅ Dream successfully saved to Notion!")
    return response
