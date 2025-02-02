from diffusers import StableDiffusionPipeline
import torch
import os
import uuid

MODEL_NAME = "runwayml/stable-diffusion-v1-5"  # Change this to SDXL if needed
OUTPUT_DIR = "generated_images"
os.makedirs(OUTPUT_DIR, exist_ok=True)


# Load Stable Diffusion with GPU
pipe = StableDiffusionPipeline.from_pretrained(MODEL_NAME).to("cuda")

def generate_image(prompt):
    filename = f"{uuid.uuid4().hex}.png"
    output_path = os.path.join(OUTPUT_DIR, filename)

    # Improve image quality settings
    image = pipe(
        prompt,
        height=512,  # Adjust as needed
        width=512,
        num_inference_steps=50,  # Increase steps for better detail
        guidance_scale=8.5,  # Higher values = more accurate
    ).images[0]

    image.save(output_path)
    return output_path
