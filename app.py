from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os
import logging
from model import generate_image

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend API access

# Ensure generated images directory exists
GENERATED_IMAGES_DIR = "generated_images"
os.makedirs(GENERATED_IMAGES_DIR, exist_ok=True)

# Configure logging
logging.basicConfig(level=logging.INFO)


@app.route("/generate", methods=["POST"])
def generate():
    try:
        data = request.json
        prompt = data.get("prompt", "").strip()

        if not prompt:
            return jsonify({"error": "Prompt is required"}), 400


        image_path = generate_image(prompt)  # Generate image
        if not image_path:
            return jsonify({"error": "Image generation failed"}), 500

        return jsonify({"image_url": f"/static/{image_path}"}), 200

    except Exception as e:
        logging.error(f"Error generating image: {str(e)}")
        return jsonify({"error": "Internal Server Error"}), 500


@app.route("/static/<path:filename>")
def serve_generated_images(filename):
    """ Serve images safely from the generated images directory """
    safe_path = os.path.join(GENERATED_IMAGES_DIR, filename)

    if not os.path.exists(safe_path):
        return jsonify({"error": "File not found"}), 404

    return send_from_directory(GENERATED_IMAGES_DIR, filename)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
