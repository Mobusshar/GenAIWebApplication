from diffusers import DiffusionPipeline
import torch
import os
import uuid
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

OUTPUT_DIR = "generated_images"
os.makedirs(OUTPUT_DIR, exist_ok=True)
logging.info(f"Output directory set to: {OUTPUT_DIR}")

# Load both base & refiner with increased timeout
logging.info("Loading base model...")
base = DiffusionPipeline.from_pretrained(
    "stabilityai/stable-diffusion-xl-base-1.0", 
    torch_dtype=torch.float16, 
    variant="fp16", 
    use_safetensors=True,
    timeout=600  # Increase timeout to 10 minutes
)
base.to("cuda")
logging.info("Base model loaded successfully.")

logging.info("Loading refiner model...")
refiner = DiffusionPipeline.from_pretrained(
    "stabilityai/stable-diffusion-xl-refiner-1.0",
    text_encoder_2=base.text_encoder_2,
    vae=base.vae,
    torch_dtype=torch.float16,
    use_safetensors=True,
    variant="fp16",
    timeout=600  # Increase timeout to 10 minutes
)
refiner.to("cuda")
logging.info("Refiner model loaded successfully.")

# Define how many steps and what % of steps to be run on each expert (80/20) here
n_steps = 40
high_noise_frac = 0.8

def generate_image(prompt):
    logging.info(f"Generating image for prompt: {prompt}")
    filename = f"{uuid.uuid4().hex}.png"
    output_path = os.path.join(OUTPUT_DIR, filename)
    logging.info(f"Output path set to: {output_path}")

    # Run both experts
    logging.info("Running base model...")
    image = base(
        prompt=prompt,
        num_inference_steps=n_steps,
        denoising_end=high_noise_frac,
        output_type="latent",
    ).images
    logging.info("Base model run completed.")

    logging.info("Running refiner model...")
    image = refiner(
        prompt=prompt,
        num_inference_steps=n_steps,
        denoising_start=high_noise_frac,
        image=image,
    ).images[0]
    logging.info("Refiner model run completed.")

    image.save(output_path)
    logging.info(f"Image saved to: {output_path}")
    return output_path
