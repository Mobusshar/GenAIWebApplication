import torch
from diffusers import StableDiffusionPipeline
import uuid
import os

# Ensure output directory exists
OUTPUT_DIR = "generated_images"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Check if GPU is available, otherwise use CPU
device = "cuda" if torch.cuda.is_available() else "cpu"

# Load Stable Diffusion model (optimized for speed)
pipe = StableDiffusionPipeline.from_pretrained(
    "CompVis/stable-diffusion-v1-4",
    torch_dtype=torch.float16 if device == "cuda" else torch.float32  # Use half-precision on GPU
).to(device)


# Function to generate an image
def generate_image(prompt):
    """
    Generates an image based on the given text prompt using Stable Diffusion.

    Args:
        prompt (str): The text prompt for image generation.

    Returns:
        str: The file path of the generated image.
    """
    try:
        # Generate image
        image = pipe(prompt, height=512, width=512, guidance_scale=7.5).images[0]

        # Save image with a unique filename
        filename = f"{OUTPUT_DIR}/{uuid.uuid4()}.png"
        image.save(filename)

        return filename  # Return path of saved image

    except Exception as e:
        return f"Error: {str(e)}"
