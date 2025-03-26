from flask import Blueprint, request, jsonify
from models.db.exercise1 import db, Exercise1
import logging
import requests

exercise1_bp = Blueprint('exercise1', __name__)

COLAB_API_URL = "https://7b3c-34-75-98-241.ngrok-free.app/chat"

@exercise1_bp.route('/save-pre-text', methods=['POST'])
def save_pre_text():
    data = request.json
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
        frustration=data.get('frustration', '').strip(),
        sadness=data.get('sadness', '').strip(),
        fear=data.get('fear', '').strip(),
        anger=data.get('anger', '').strip(),
        empathy=data.get('empathy', '').strip(),
        gratitude=data.get('gratitude', '').strip(),
        protectiveness=data.get('protectiveness', '').strip(),
        serenity=data.get('serenity', '').strip(),
        joy=data.get('joy', '').strip(),
        hope=data.get('hope', '').strip(),
        friendship=data.get('friendship', '').strip(),
        relief=data.get('relief', '').strip(),
        compassion=data.get('compassion', '').strip(),
        self_reflection=data.get('self_reflection', '').strip(),
        inspiration=data.get('inspiration', '').strip(),
        story_moral=data.get('story_moral', '').strip()
    )
    
    db.session.add(new_entry)
    db.session.commit()
    logging.info(f"Saved entry with ID: {new_entry.id}")
    return jsonify({"id": new_entry.id}), 201

@exercise1_bp.route('/update-story/<int:id>', methods=['PUT'])
def update_story(id):
    data = request.json
    logging.info(f"Received data for update: {data}")
    
    entry = db.session.get(Exercise1, id)
    
    if not entry:
        logging.error(f"Entry with ID {id} not found")
        return jsonify({"error": "Entry not found"}), 404
    
    entry.story_character = data.get('story_character', entry.story_character).strip()
    entry.frustration = data.get('frustration', entry.frustration).strip()
    entry.sadness = data.get('sadness', entry.sadness).strip()
    entry.fear = data.get('fear', entry.fear).strip()
    entry.anger = data.get('anger', entry.anger).strip()
    entry.empathy = data.get('empathy', entry.empathy).strip()
    entry.gratitude = data.get('gratitude', entry.gratitude).strip()
    entry.protectiveness = data.get('protectiveness', entry.protectiveness).strip()
    entry.serenity = data.get('serenity', entry.serenity).strip()
    entry.joy = data.get('joy', entry.joy).strip()
    entry.hope = data.get('hope', entry.hope).strip()
    entry.friendship = data.get('friendship', entry.friendship).strip()
    entry.relief = data.get('relief', entry.relief).strip()
    entry.compassion = data.get('compassion', entry.compassion).strip()
    entry.self_reflection = data.get('self_reflection', entry.self_reflection).strip()
    entry.inspiration = data.get('inspiration', entry.inspiration).strip()
    entry.story_moral = data.get('story_moral', entry.story_moral).strip()
    
    db.session.commit()
    logging.info(f"Updated entry with ID: {entry.id}")
    return jsonify({"message": "Entry updated successfully"}), 200

@exercise1_bp.route('/get-story/<int:id>', methods=['GET'])
def get_story(id):
    entry = db.session.get(Exercise1, id)
    
    if not entry:
        logging.error(f"Entry with ID {id} not found")
        return jsonify({"error": "Entry not found"}), 404
    
    story_data = {
        "story_character": entry.story_character,
        "frustration": entry.frustration,
        "sadness": entry.sadness,
        "fear": entry.fear,
        "anger": entry.anger,
        "empathy": entry.empathy,
        "gratitude": entry.gratitude,
        "protectiveness": entry.protectiveness,
        "serenity": entry.serenity,
        "joy": entry.joy,
        "hope": entry.hope,
        "friendship": entry.friendship,
        "relief": entry.relief,
        "compassion": entry.compassion,
        "self_reflection": entry.self_reflection,
        "inspiration": entry.inspiration,
        "story_moral": entry.story_moral
    }
    
    return jsonify(story_data), 200


@exercise1_bp.route('/update-post-exercise1/<int:id>', methods=['PUT'])
def update_post_exercise1(id):
    data = request.json
    logging.info(f"Received data for post-exercise1 update: {data}")
    
    entry = db.session.get(Exercise1, id)
    
    if not entry:
        logging.error(f"Entry with ID {id} not found")
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
    logging.info(f"Updated post-exercise1 entry with ID: {entry.id}")
    return jsonify({"message": "Post-exercise1 entry updated successfully"}), 200


@exercise1_bp.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.json
        prompt = data.get("prompt", "").strip()

        if not prompt:
            return jsonify({"error": "Prompt is required"}), 400
        
        # Forward the request to Google Colab
        response = requests.post(COLAB_API_URL, json={"prompt": prompt})

        return jsonify(response.json()), response.status_code
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