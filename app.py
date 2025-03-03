from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os
import logging
#from models.image.sdxl import generate_image
from models.db.models import db, Exercise1
from models.text.qwen_model import load_qwen_model, generate_qwen_response
from transformers import pipeline, set_seed, AutoModelForCausalLM, AutoTokenizer
import torch

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

# Load models
tokenizer, qwen_model = load_qwen_model()

# Load Qwen2.5-14B model and tokenizer
# model_name = "Qwen/Qwen2.5-14B"
# model_name = "Qwen/Qwen2.5-1.5B"
# tokenizer = AutoTokenizer.from_pretrained(model_name)
# model = AutoModelForCausalLM.from_pretrained(model_name, torch_dtype=torch.float32).to("cpu")

# Load the GPT-2 model using pipeline
# generator = pipeline('text-generation', model='gpt2-xl')
# set_seed(42)

# Load the GPT-J model
# model_name = "EleutherAI/gpt-j-6B"
# model_name = "distilgpt2"
# model_name = "gpt2"
# model_name = "gpt2-xl"
# tokenizer = AutoTokenizer.from_pretrained(model_name)
# model = AutoModelForCausalLM.from_pretrained(model_name)

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


@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.json
        name = data.get("name", "").strip()
        email = data.get("email", "").strip()
        studentid = data.get("studentid", "").strip()
        prompt = data.get("prompt", "").strip()

        if not prompt:
            return jsonify({"error": "Prompt is required"}), 400

         # Tokenize input properly
        inputs = tokenizer(prompt, return_tensors="pt", truncation=True, max_length=512).to("cpu")

        response_text = generate_qwen_response(prompt, tokenizer, qwen_model)
        # response_text = tokenizer.decode(output[0], skip_special_tokens=True).strip()

        # Handle cases where response is empty or incorrect
        if not response_text.strip():
            return jsonify({"error": "No meaningful response generated. Try a different prompt."}), 400
        
        
        # Generate text using the pipeline
        # response = generator(prompt, max_length=200, num_return_sequences=1, pad_token_id=50256)
        # response_text = response[0]['generated_text']

        # Generate text using the Qwen2.5-14B model
        # inputs = tokenizer(prompt, return_tensors="pt").to("cpu")
        # output = model.generate(**inputs, max_length=200)
        # response_text = tokenizer.decode(output[0], skip_special_tokens=True)

        # Save the data to the database (optional)
        # new_entry = Exercise1(name=name, email=email, studentid=studentid, prompt=prompt, response=response_text)
        # db.session.add(new_entry)
        # db.session.commit()

        return jsonify({"response": response_text}), 200

    except Exception as e:
        logging.error(f"Error generating response: {str(e)}")
        return jsonify({"error": "Internal Server Error"}), 500



if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(host="0.0.0.0", port=5000, debug=True)
