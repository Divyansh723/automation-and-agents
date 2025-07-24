from diffusers import StableDiffusionPipeline
import torch
import os

def extract_visual_prompt(content: str) -> str:
    """
    Extracts the Visual Art Prompt from the dream analysis text,
    whether it's in markdown-style or plain-text formatting.
    """
    start_tags = [
        "5. **Visual Art Prompt:**",
        "5. Visual Art Prompt:",
    ]
    end_tags = [
        "6. **Journal Entry Summary",
        "6. Journal Entry Summary",
    ]

    start_index = end_index = -1

    # Try all possible tag styles
    for start_tag in start_tags:
        if start_tag in content:
            start_index = content.find(start_tag) + len(start_tag)
            break

    for end_tag in end_tags:
        if end_tag in content:
            end_index = content.find(end_tag, start_index)
            break

    # Safety check
    if start_index == -1 or end_index == -1:
        raise ValueError("⚠️ Visual Art Prompt section not found properly.")

    prompt = content[start_index:end_index].strip()

    if not prompt:
        raise ValueError("⚠️ Extracted prompt is empty.")

    # Add anime-style modifier
    anime_enhanced_prompt = f"Anime style: {prompt}"
    return anime_enhanced_prompt


def generate_dream_image(
    analysis_path="../analysis_outputs/dream_analysis.txt",
    output_path="../art_outputs/dream_image.png"
):
    # 🔍 Step 1: Load dream analysis file
    with open(analysis_path, "r", encoding="utf-8") as f:
        content = f.read()

    # 🧠 Step 2: Extract the visual art prompt
    prompt = extract_visual_prompt(content)

    # 🎨 Step 3: Load Stable Diffusion model
    pipe = StableDiffusionPipeline.from_pretrained(
        "runwayml/stable-diffusion-v1-5",
        torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32,
    )
    pipe = pipe.to("cuda" if torch.cuda.is_available() else "cpu")

    # 🖼️ Step 4: Generate the image
    print(f"🎨 Generating dream image from prompt:\n\n{prompt}\n")
    image = pipe(prompt).images[0]

    # 💾 Step 5: Save image
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    image.save(output_path)

    print("✅ Dream image saved to:", output_path)
    return output_path
