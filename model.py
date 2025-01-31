import torch
from diffusers import StableDiffusionPipeline
import os
from datetime import datetime

# Load the model (this will download it if not already present)
pipe = StableDiffusionPipeline.from_pretrained("CompVis/stable-diffusion-v1-4")
pipe.to("cuda" if torch.cuda.is_available() else "cpu")

GENERATED_IMAGES_DIR = "generated_images"

def generate_image(prompt):
    """Generates an image from a given text prompt using Stable Diffusion."""
    image = pipe(prompt).images[0]

    filename = f"{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
    filepath = os.path.join(GENERATED_IMAGES_DIR, filename)
    image.save(filepath)

    return filename  # Return filename to serve it later
