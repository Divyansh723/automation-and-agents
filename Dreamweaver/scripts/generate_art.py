import os
import torch
from diffusers import AutoPipelineForText2Image
from dotenv import load_dotenv

load_dotenv()

USE_GPU = torch.cuda.is_available()

def extract_visual_prompt(content: str) -> str:
    content = content.replace("  ", " ")
    start_tags = ["5. **Visual Art Prompt:**", "5. Visual Art Prompt:"]
    end_tags   = ["6. **Journal Entry Summary", "6. Journal Entry Summary"]

    start_idx = end_idx = -1
    for tag in start_tags:
        if tag in content:
            start_idx = content.index(tag) + len(tag)
            break
    for tag in end_tags:
        if tag in content:
            end_idx = content.index(tag, start_idx)
            break

    if start_idx < 0 or end_idx < 0:
        raise ValueError("⚠️ Visual Art Prompt section not found.")

    prompt = content[start_idx:end_idx].strip()
    if not prompt:
        raise ValueError("⚠️ Extracted prompt is empty.")

    return f"Anime style: {prompt}"

def generate_dream_image(
    analysis_path="../analysis_outputs/dream_analysis.txt",
    output_path="../art_outputs/dream_image.png",
    height=768, width=768
):
    with open(analysis_path, "r", encoding="utf-8") as f:
        content = f.read()

    prompt = extract_visual_prompt(content)
    print("🎨 Kandinsky prompt:\n", prompt)

    pipe = AutoPipelineForText2Image.from_pretrained(
        "kandinsky-community/kandinsky-2-2-decoder",
        torch_dtype=torch.float16 if USE_GPU else torch.float32
    )

    if USE_GPU:
        pipe = pipe.to("cuda")
    else:
        pipe.enable_model_cpu_offload()

    image = pipe(
        prompt=prompt,
        negative_prompt="low quality, bad quality",
        prior_guidance_scale=1.0,
        guidance_scale=7.5,
        num_inference_steps=50,
        height=height,
        width=width
    ).images[0]

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    image.save(output_path)
    print("✅ Dream image saved to:", output_path)
    return output_path
