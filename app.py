from flask import Flask, render_template, request, jsonify, send_from_directory
from flask_cors import CORS
from model import ImageGenerator
import os

app = Flask(__name__)
CORS(app)
generator = ImageGenerator()
output_dir = "generated_images"


def get_existing_images():
    images = []
    try:
        for filename in os.listdir(output_dir):
            if filename.endswith(".png"):
                images.append(f"/images/{filename}")
    except Exception as e:
        app.logger.error(f"Error reading images: {str(e)}")
    return images


@app.route("/")
def index():
    return render_template("index.html", images=get_existing_images())


@app.route("/generate", methods=["POST"])
def generate():
    try:
        data = request.get_json()
        prompt = data.get("prompt", "").strip()

        if not prompt:
            return jsonify({"error": "Please enter a prompt"}), 400

        filename = generator.generate_image(prompt)
        return jsonify({"image_url": f"/images/{filename}"})

    except Exception as e:
        app.logger.error(f"Generation error: {str(e)}")
        return jsonify({"error": str(e)}), 500


@app.route("/images/<filename>")
def serve_image(filename):
    return send_from_directory(output_dir, filename)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)