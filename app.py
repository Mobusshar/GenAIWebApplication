from flask import Flask, render_template, request, jsonify, send_from_directory
from flask_cors import CORS
import os
from model import generate_image

app = Flask(__name__)
CORS(app)  # Enable CORS for API access

# Ensure generated images directory exists
GENERATED_IMAGES_DIR = "generated_images"
os.makedirs(GENERATED_IMAGES_DIR, exist_ok=True)

@app.route("/")
def home():
    # Get all previously generated images
    images = [f"/generated_images/{img}" for img in os.listdir(GENERATED_IMAGES_DIR) if img.endswith(('.png', '.jpg', '.jpeg'))]
    return render_template("index.html", images=images)

@app.route("/generate", methods=["POST"])
def generate():
    data = request.json
    prompt = data.get("prompt", "")

    if not prompt:
        return jsonify({"error": "Prompt is required"}), 400

    image_path = generate_image(prompt)  # Generate image
    filename = os.path.basename(image_path)

    return jsonify({"image_url": f"/generated_images/{filename}"}), 200

@app.route("/generated_images/<path:filename>")
def serve_generated_images(filename):
    return send_from_directory(GENERATED_IMAGES_DIR, filename)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
