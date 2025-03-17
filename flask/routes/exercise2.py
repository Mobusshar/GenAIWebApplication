from flask import Blueprint, request, jsonify, send_from_directory, current_app
from models.db.exercise2 import db, Exercise2
import os
import logging
import requests

exercise2_bp = Blueprint('exercise2', __name__)
COLAB_API_URL = "https://7b3c-34-75-98-241.ngrok-free.app/chat"

@exercise2_bp.route("/generate", methods=["POST"])
def generate():
    try:
        data = request.json
        name = data.get("name", "").strip()
        email = data.get("email", "").strip()
        studentid = data.get("studentid", "").strip()
        prompt = data.get("prompt", "").strip()

        if not prompt:
            return jsonify({"error": "Prompt is required"}), 400

        image_url = "/images/dummy.jpg"

        new_entry = Exercise2(name=name, email=email, studentid=studentid, prompt=prompt, image_url=image_url)
        db.session.add(new_entry)
        db.session.commit()

        return jsonify({"image_url": image_url}), 200

    except Exception as e:
        logging.error(f"Error generating image: {str(e)}")
        return jsonify({"error": "Internal Server Error"}), 500

@exercise2_bp.route("/images/<path:filename>")
def serve_generated_images(filename):
    safe_path = os.path.join(current_app.config['GENERATED_IMAGES_DIR'], filename)

    if not os.path.exists(safe_path):
        return jsonify({"error": "File not found"}), 404

    return send_from_directory(current_app.config['GENERATED_IMAGES_DIR'], filename)

@exercise2_bp.route('/images', methods=['GET'])
def list_images():
    images = os.listdir(current_app.config['GENERATED_IMAGES_DIR'])
    image_urls = [f"/images/{image}" for image in images]
    return jsonify(image_urls)

@exercise2_bp.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.json
        prompt = data.get("prompt", "").strip()

        if not prompt:
            return jsonify({"error": "Prompt is required"}), 400
        
        response = requests.post(COLAB_API_URL, json={"prompt": prompt})
        return jsonify(response.json()), response.status_code

    except Exception as e:
        logging.error(f"Error generating response: {str(e)}")
        return jsonify({"error": "Internal Server Error"}), 500