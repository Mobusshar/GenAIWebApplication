from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os
import logging
#from model import generate_image
from models import db, Exercise1

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend API access

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost/genai'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# Ensure generated images directory exists
GENERATED_IMAGES_DIR = "generated_images"
os.makedirs(GENERATED_IMAGES_DIR, exist_ok=True)

# Configure logging
logging.basicConfig(level=logging.INFO)

@app.route("/generate", methods=["POST"])
def generate():
    try:
        data = request.json
        name = data.get("name", "").strip()
        email = data.get("email", "").strip()
        studentid = data.get("studentid", "").strip()
        prompt = data.get("prompt", "").strip()

        if not prompt:
            return jsonify({"error": "Prompt is required"}), 400

        #image_path = generate_image(prompt)  # Generate image
        #if not image_path:
        #    return jsonify({"error": "Image generation failed"}), 500

        #image_url = f"/images/{os.path.basename(image_path)}"

        image_url = "/images/dummy.jpg"

        # Save the data to the database
        new_entry = Exercise1(name=name, email=email, studentid=studentid, prompt=prompt, image_url=image_url)
        db.session.add(new_entry)
        db.session.commit()

        return jsonify({"image_url": image_url}), 200

    except Exception as e:
        logging.error(f"Error generating image: {str(e)}")
        return jsonify({"error": "Internal Server Error"}), 500

@app.route("/images/<path:filename>")
def serve_generated_images(filename):
    """ Serve images safely from the generated images directory """
    safe_path = os.path.join(GENERATED_IMAGES_DIR, filename)

    if not os.path.exists(safe_path):
        return jsonify({"error": "File not found"}), 404

    return send_from_directory(GENERATED_IMAGES_DIR, filename)

@app.route('/images', methods=['GET'])
def list_images():
    images = os.listdir(GENERATED_IMAGES_DIR)
    image_urls = [f"/images/{image}" for image in images]
    return jsonify(image_urls)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(host="0.0.0.0", port=5000, debug=True)
