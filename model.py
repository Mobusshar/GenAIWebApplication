from diffusers import StableDiffusionXLPipeline
import torch
import os
import uuid

# Use the latest Stable Diffusion XL model
MODEL_NAME = "stabilityai/stable-diffusion-xl-base-1.0"
OUTPUT_DIR = "generated_images"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Load the SDXL model with GPU (if available)
device = "cuda" if torch.cuda.is_available() else "cpu"
pipe = StableDiffusionXLPipeline.from_pretrained(MODEL_NAME, torch_dtype=torch.float16)
pipe = pipe.to(device)

def generate_image(prompt):
    filename = f"{uuid.uuid4().hex}.png"
    output_path = os.path.join(OUTPUT_DIR, filename)

    # Generate image with SDXL
    image = pipe(
        prompt,
        height=1024,  # SDXL supports higher resolution
        width=1024,
        num_inference_steps=50,  # More steps for better quality
        guidance_scale=7.5,  # Trade-off between fidelity & creativity
    ).images[0]

    image.save(output_path)
    return output_path
