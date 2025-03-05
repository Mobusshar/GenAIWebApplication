from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os
import logging
#from models.image.sdxl import generate_image
from models.db.exercise1 import db, Exercise1
from models.db.exercise2 import db, Exercise2
#from models.text.qwen_model import load_qwen_model, generate_qwen_response
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
# tokenizer, qwen_model = load_qwen_model()

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
        new_entry = Exercise2(name=name, email=email, studentid=studentid, prompt=prompt, image_url=image_url)
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
# working this block
         # Tokenize input properly
        #inputs = tokenizer(prompt, return_tensors="pt", truncation=True, max_length=512).to("cpu")

        #response_text = generate_qwen_response(prompt, tokenizer, qwen_model)
        # response_text = tokenizer.decode(output[0], skip_special_tokens=True).strip()

        # Handle cases where response is empty or incorrect
        #if not response_text.strip():
        #    return jsonify({"error": "No meaningful response generated. Try a different prompt."}), 400
        
# unlock till here
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

        #return jsonify({"response": response_text}), 200

    except Exception as e:
        logging.error(f"Error generating response: {str(e)}")
        return jsonify({"error": "Internal Server Error"}), 500


@app.route('/save-pre-text', methods=['POST'])
def save_pre_text():
    data = request.json
    #app.logger.info(f"Received data: {data}")
    
    new_entry = Exercise1(
        demo_name=data.get('demo_name', '').strip(),
        demo_email=data.get('demo_email', '').strip(),
        demo_academic=data.get('demo_academic', '').strip(),
        base_creativity_conf=data.get('base_creativity_conf', 0),
        base_creativity_freq=data.get('base_creativity_freq', '').strip(),
        base_creativity_def=data.get('base_creativity_def', '').strip(),
        ai_used_before=data.get('ai_used_before', False),
        ai_tools_list=data.get('ai_tools_list', '').strip(),
        ai_comfort=data.get('ai_comfort', 0),
        ai_expectations=data.get('ai_expectations', '').strip(),
        collab_conf=data.get('collab_conf', 0),
        collab_role=data.get('collab_role', '').strip(),
        collab_value=data.get('collab_value', '').strip(),
        exp_interest=data.get('exp_interest', '').strip(),
        exp_challenges=data.get('exp_challenges', '').strip(),
        exp_diff_ai_human=data.get('exp_diff_ai_human', '').strip(),
        exp_bias_ai_human=data.get('exp_bias_ai_human', '').strip(),
        exp_challenge_fairness=data.get('exp_challenge_fairness', '').strip(),
        exp_message_change=data.get('exp_message_change', '').strip(),
        exp_improve=data.get('exp_improve', '').strip(),
        exp_satisfaction=data.get('exp_satisfaction', 0),
        exp_challenge=data.get('exp_challenge', 0),
        exp_creativity_boost=data.get('exp_creativity_boost', '').strip(),
        exp_enjoyment=data.get('exp_enjoyment', '').strip(),
        exp_improvements=data.get('exp_improvements', '').strip(),
        ai_helpfulness=data.get('ai_helpfulness', 0),
        ai_iterations=data.get('ai_iterations', 0),
        ai_strategies=data.get('ai_strategies', '').strip(),
        ai_contribution=data.get('ai_contribution', '').strip(),
        ai_learnings=data.get('ai_learnings', '').strip(),
        collab_value_post=data.get('collab_value_post', 0),
        collab_feedback=data.get('collab_feedback', '').strip(),
        collab_new_ideas=data.get('collab_new_ideas', '').strip(),
        learn_conf_post=data.get('learn_conf_post', 0),
        learn_skills=data.get('learn_skills', '').strip(),
        learn_ai_future=data.get('learn_ai_future', 0),
        reflect_creativity_change=data.get('reflect_creativity_change', '').strip(),
        reflect_human_ai_role=data.get('reflect_human_ai_role', '').strip(),
        reflect_future_prep=data.get('reflect_future_prep', '').strip(),
        story_character=data.get('story_character', '').strip(),
        story_setting=data.get('story_setting', '').strip(),
        story_conflict=data.get('story_conflict', '').strip(),
        story_resolution=data.get('story_resolution', '').strip(),
        story_dialogue=data.get('story_dialogue', '').strip(),
        story_moral=data.get('story_moral', '').strip()
    )
    
    db.session.add(new_entry)
    db.session.commit()
    app.logger.info(f"Saved entry with ID: {new_entry.id}")
    return jsonify({"id": new_entry.id}), 201

@app.route('/update-story/<int:id>', methods=['PUT'])
def update_story(id):
    data = request.json
    app.logger.info(f"Received data for update: {data}")
    
    # Use Session.get() instead of Query.get()
    entry = db.session.get(Exercise1, id)
    
    if not entry:
        app.logger.error(f"Entry with ID {id} not found")
        return jsonify({"error": "Entry not found"}), 404
    
    entry.story_character = data.get('story_character', entry.story_character).strip()
    entry.story_setting = data.get('story_setting', entry.story_setting).strip()
    entry.story_conflict = data.get('story_conflict', entry.story_conflict).strip()
    entry.story_resolution = data.get('story_resolution', entry.story_resolution).strip()
    entry.story_dialogue = data.get('story_dialogue', entry.story_dialogue).strip()
    entry.story_moral = data.get('story_moral', entry.story_moral).strip()
    
    db.session.commit()
    app.logger.info(f"Updated entry with ID: {entry.id}")
    return jsonify({"message": "Entry updated successfully"}), 200

@app.route('/update-post-exercise1/<int:id>', methods=['PUT'])
def update_post_exercise1(id):
    data = request.json
    app.logger.info(f"Received data for post-exercise1 update: {data}")
    
    entry = db.session.get(Exercise1, id)
    
    if not entry:
        app.logger.error(f"Entry with ID {id} not found")
        return jsonify({"error": "Entry not found"}), 404
    
    entry.exp_interest = data.get('exp_interest', entry.exp_interest).strip()
    entry.exp_challenges = data.get('exp_challenges', entry.exp_challenges).strip()
    entry.exp_diff_ai_human = data.get('exp_diff_ai_human', entry.exp_diff_ai_human).strip()
    entry.exp_bias_ai_human = data.get('exp_bias_ai_human', entry.exp_bias_ai_human).strip()
    entry.exp_challenge_fairness = data.get('exp_challenge_fairness', entry.exp_challenge_fairness).strip()
    entry.exp_message_change = data.get('exp_message_change', entry.exp_message_change).strip()
    entry.exp_improve = data.get('exp_improve', entry.exp_improve).strip()
    entry.exp_satisfaction = data.get('exp_satisfaction', entry.exp_satisfaction)
    entry.exp_challenge = data.get('exp_challenge', entry.exp_challenge)
    entry.exp_creativity_boost = data.get('exp_creativity_boost', entry.exp_creativity_boost).strip()
    entry.exp_enjoyment = data.get('exp_enjoyment', entry.exp_enjoyment).strip()
    entry.exp_improvements = data.get('exp_improvements', entry.exp_improvements).strip()
    entry.ai_helpfulness = data.get('ai_helpfulness', entry.ai_helpfulness)
    entry.ai_iterations = data.get('ai_iterations', entry.ai_iterations)
    entry.ai_strategies = data.get('ai_strategies', entry.ai_strategies).strip()
    entry.ai_contribution = data.get('ai_contribution', entry.ai_contribution).strip()
    entry.ai_learnings = data.get('ai_learnings', entry.ai_learnings).strip()
    entry.collab_value_post = data.get('collab_value_post', entry.collab_value_post)
    entry.collab_feedback = data.get('collab_feedback', entry.collab_feedback).strip()
    entry.collab_new_ideas = data.get('collab_new_ideas', entry.collab_new_ideas).strip()
    entry.learn_conf_post = data.get('learn_conf_post', entry.learn_conf_post)
    entry.learn_skills = data.get('learn_skills', entry.learn_skills).strip()
    entry.learn_ai_future = data.get('learn_ai_future', entry.learn_ai_future)
    entry.reflect_creativity_change = data.get('reflect_creativity_change', entry.reflect_creativity_change).strip()
    entry.reflect_human_ai_role = data.get('reflect_human_ai_role', entry.reflect_human_ai_role).strip()
    entry.reflect_future_prep = data.get('reflect_future_prep', entry.reflect_future_prep).strip()
    
    db.session.commit()
    app.logger.info(f"Updated post-exercise1 entry with ID: {entry.id}")
    return jsonify({"message": "Post-exercise1 entry updated successfully"}), 200

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(host="0.0.0.0", port=5000, debug=True)
