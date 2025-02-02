import torch
from diffusers import StableDiffusionPipeline
import logging
import os


class ImageGenerator:
    def __init__(self):
        self.output_dir = "generated_images"
        os.makedirs(self.output_dir, exist_ok=True)
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.pipe = self._load_model()

    def _load_model(self):
        try:
            pipe = StableDiffusionPipeline.from_pretrained(
                "stabilityai/stable-diffusion-xl-base-1.0",
                torch_dtype=torch.float32,
                safety_checker=None
            ).to(self.device)
            logging.info("Model loaded successfully")
            return pipe
        except Exception as e:
            logging.error(f"Error loading model: {str(e)}")
            raise

    def generate_image(self, prompt):
        try:
            image = self.pipe(prompt).images[0]
            filename = f"{prompt[:20]}_{torch.rand(1).item():.4f}.png".replace(" ", "_")
            image_path = os.path.join(self.output_dir, filename)
            image.save(image_path)
            return filename
        except Exception as e:
            logging.error(f"Error generating image: {str(e)}")
            raise