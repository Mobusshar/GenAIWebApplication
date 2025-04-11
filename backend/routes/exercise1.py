from flask import Blueprint, request, jsonify
from models.db.exercise1 import db, Exercise1
import logging
import requests
import json
import re
import os
from dotenv import load_dotenv
from openai import OpenAI
from openai import OpenAIError

# Load environment variables from .env file
load_dotenv()

# Access the OpenAI API key from the environment
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    raise ValueError("OpenAI API key is not set. Please add it to the .env file.")

exercise1_bp = Blueprint('exercise1', __name__)

client = OpenAI(api_key=OPENAI_API_KEY)  # Replace with your actual API key
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
        collab_value=data.get('collab_value', '').strip()
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

    # Update individual fields
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

    # Concatenate the story dynamically
    entry.story = f"""
        {entry.story_character} was indeed a very hardworking man who put in all his efforts in all possible ways. Every morning he woke up early and got prepared for work meticulously to support his family most effectively. But unfortunately, things started going totally non-synchronized, one fine day.
        This particular morning, the alarm failed to ring, and therefore {entry.story_character} woke up late. In haste he got up and started living his daily life. He wore a shirt on which some coffee spilled and he got out just missing the usual bus. The rest of it was forced to be walked under a chilly and drizzling rain to get to work. {entry.story_character} noted how the rain fell and continued to match his steadily growing exasperation and sense of unluckiness. {entry.frustration}
        
        Thanks to the plethora of obstacles piling up in his life, he had exceeded that last point and went further. He had finally made it to work, only to continue discovering frustration. His computer failed him on an important assignment, and everyone else seemed too busy burning their bridges to offer assistance. Every tiny mishap continued accumulating, leaving him tired and muffling up the morale. {entry.story_character} heaved a frustrated sigh, staring at his screen, feeling utterly defeated by everything around him. {entry.sadness}
        
        Things couldn't get any worse, just as he thought. His boss calls him into the office. "{entry.story_character}, your work has been sloppy lately," said the boss coldly. He added, "If this continues, we may need to reconsider your position here." A sudden wave of fear gripped him. He had worked tireless days; now, one bad day could cost him everything. His hands trembled leaving the office; his heart was pounding. {entry.fear}
        
        At lunch hour, {entry.story_character} sat there alone, gripping a sandwich with white knuckle fingers. One coworker bumped into him; his food hit the floor. "Hey, watch it {entry.story_character}," the man dismissively muttered. That was the last straw. Anger erupted in {entry.story_character}'s chest. "Are you kidding me?!," he snapped, standing abruptly. But when he saw both men's shocked look, he bit his tongue and stormed out to seethe. {entry.anger}
        
        After a rough day at work, in busy streets {entry.story_character} walked home. There were thousands of things racing through his mind: frustration, worry, exhaustion, and everything too. It was then that he saw an elderly lady standing at a very crowded sidewalk. Cars rushed past, and she looked like she didn't have the courage to cross such a busy road. Although he was so much into his own trouble, somehow there was that tug he could feel within him to help. {entry.empathy}
        
        He did stop for a moment. "I am already having my worst day. Why even bother?" But this egoistic thought was removed from his mind. Something very deep was urging him forward. He went to her and said, "May I help you cross over the street?" The eyes of the woman brightened up instantaneously with an illumination associated with relief. "Oh, it would be a wonderful favor." He carefully took her across this street, protecting her from the flow of impatient rushing cars. When they reached just at the other side of the street, the woman squeezed his hand, saying, "You have a very kind heart, young man." {entry.gratitude} {entry.protectiveness}
        
        At that moment, for the first time in a long time, something inside {entry.story_character} changed. He found peace in this simple act of kindness to a stranger that would have been missing from his life for a while now. {entry.serenity}
        
        Later that night, {entry.story_character} reached home only to find an unexpected surprise lying on his doorstep: a tiny little package along with a handwritten note. The note written by the elderly lady acknowledged her heartfelt gratitude. Within that package was a pair of gloves with a simple message inscribed, "Kindness is a reward." {entry.story_character}'s eyes went wide as he read the note, and warmth began to swell in his chest. And for the first time that day, that was a smile of {entry.story_character}'s that could be described as genuine. {entry.joy}
        
        It has changed the entire scenario; most importantly, it brings some happiness and brightness. Even on a day that feels like it was filled with constant misfortunes, it feels great to have one's kindness appreciated and recognized. In the end, it just goes to show-and point out, really-that even on the worst days, such an act, no matter the proportion, can change everything. Inspired by the experience, he determined to keep helping others, though difficult his circumstances became. {entry.hope}
        
        The next morning came into play with the strangest of happenings. As he entered his work, he saw the coworker whom he had snapped at yesterday. It would have been easy to ignore him, but instead {entry.story_character} took a breath and said, "Hey... I'm sorry about yesterday." The man blinked at him in surprise, then laughed and said, "No worries, {entry.story_character}. I was in a bad mood, too." Then they shook hands, and for the first time ever, {entry.story_character} felt a sense of kinship with another human being in the workplace. {entry.friendship}
        
        Thus, {entry.story_character} was called again by his boss, only this time the tone was entirely different. "I've been watching you, {entry.story_character}. I see improvement. Keep it up." Relief flooded {entry.story_character}'s chest. He was convinced he might well be on the verge of losing everything; instead, there turned out to be a way forward. {entry.relief}
        
        He could feel the care for others in him-from within. He now knew how much people's suffering mirrored his own, and for the first time, he felt other people's suffering with a weight never felt before. {entry.compassion} He reflected on how he had judged people too early, not understanding that they had unseen burdens much like himself.
        
        He sat in silent deliberation, understanding what this harsh day really meant for him. He had thought that suffering hardship meant only pain but had now discovered the hidden meaning within. {entry.self_reflection} It had brought him under fire and had helped him to discover more deeply his understanding of himself and his environment.
        
        As a bright candle of hope, his story spread all over the community. People started thinking that no matter how wrong life seems at times, small acts of generosity and care could create ripples of change. The unlucky day for {entry.story_character} became a historic day-proving that every challenge has a chance to make this world a bit brighter. {entry.inspiration}
    """

    db.session.commit()
    logging.info(f"Updated entry with ID: {entry.id}")
    return jsonify({"message": "Entry updated successfully"}), 200

@exercise1_bp.route('/get-story/<int:id>', methods=['GET'])
def get_story(id):
    entry = db.session.get(Exercise1, id)
    
    if not entry:
        logging.error(f"Entry with ID {id} not found")
        return jsonify({"error": "Entry not found"}), 404
    
    # Include AI-generated values from the database
    story_data = {
        "story": entry.story,
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
        "story_moral": entry.story_moral,
        # Add AI-generated values
        "ai_story_character": entry.ai_story_character,
        "ai_frustration": entry.ai_frustration,
        "ai_sadness": entry.ai_sadness,
        "ai_fear": entry.ai_fear,
        "ai_anger": entry.ai_anger,
        "ai_empathy": entry.ai_empathy,
        "ai_gratitude": entry.ai_gratitude,
        "ai_protectiveness": entry.ai_protectiveness,
        "ai_serenity": entry.ai_serenity,
        "ai_joy": entry.ai_joy,
        "ai_hope": entry.ai_hope,
        "ai_friendship": entry.ai_friendship,
        "ai_relief": entry.ai_relief,
        "ai_compassion": entry.ai_compassion,
        "ai_self_reflection": entry.ai_self_reflection,
        "ai_inspiration": entry.ai_inspiration,
        "ai_story_moral": entry.ai_story_moral
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

    # Update individual fields
    entry.exp_interest = data.get('exp_interest', entry.exp_interest).strip()
    entry.exp_challenges = data.get('exp_challenges', entry.exp_challenges).strip()
    entry.exp_diff_ai_human = data.get('exp_diff_ai_human', entry.exp_diff_ai_human).strip()
    entry.exp_bias_ai_human = data.get('exp_bias_ai_human', entry.exp_bias_ai_human).strip()
    entry.exp_ai_biases = data.get('exp_ai_biases', entry.exp_ai_biases).strip()
    entry.exp_user_biases = data.get('exp_user_biases', entry.exp_user_biases).strip()
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

    # Commit changes to the database
    db.session.commit()
    logging.info(f"Updated post-exercise1 entry with ID: {entry.id}")
    return jsonify({"message": "Post-exercise1 entry updated successfully"}), 200


# Set to True if you want to use fallback mock data instead of calling OpenAI API
USE_MOCK_DATA = False

@exercise1_bp.route('/generate-ai-story/<int:id>', methods=['POST'])
def generate_ai_story(id):
    logging.info(f"Starting AI story generation for entry ID: {id}")
    
    story_text = """
        {{ ai_story_character }} was indeed a very hardworking man who put in all his efforts in all possible ways. Every morning he woke up early and got prepared for work meticulously to support his family most effectively. But unfortunately, things started going totally non-synchronized, one fine day.
        This particular morning, the alarm failed to ring, and therefore {{ ai_story_character }} woke up late. In haste he got up and started living his daily life. He wore a shirt on which some coffee spilled and he got out just missing the usual bus. The rest of it was forced to be walked under a chilly and drizzling rain to get to work. {{ ai_story_character }} noted how the rain fell and continued to match his steadily growing exasperation and sense of unluckiness. {{ ai_frustration }}
        
        Thanks to the plethora of obstacles piling up in his life, he had exceeded that last point and went further. He had finally made it to work, only to continue discovering frustration. His computer failed him on an important assignment, and everyone else seemed too busy burning their bridges to offer assistance. Every tiny mishap continued accumulating, leaving him tired and muffling up the morale. {{ ai_story_character }} heaved a frustrated sigh, staring at his screen, feeling utterly defeated by everything around him. {{ ai_sadness }}
        
        Things couldn't get any worse, just as he thought. His boss calls him into the office. "{{ ai_story_character }}, your work has been sloppy lately," said the boss coldly. He added, "If this continues, we may need to reconsider your position here." A sudden wave of fear gripped him. He had worked tireless days; now, one bad day could cost him everything. His hands trembled leaving the office; his heart was pounding. {{ ai_fear }}
        
        At lunch hour, {{ ai_story_character }} sat there alone, gripping a sandwich with white knuckle fingers. One coworker bumped into him; his food hit the floor. "Hey, watch it {{ ai_story_character }}," the man dismissively muttered. That was the last straw. Anger erupted in {{ ai_story_character }}'s chest. "Are you kidding me?!," he snapped, standing abruptly. But when he saw both men's shocked look, he bit his tongue and stormed out to seethe. {{ ai_anger }}
        
        After a rough day at work, in busy streets {{ ai_story_character }} walked home. There were thousands of things racing through his mind: frustration, worry, exhaustion, and everything too. It was then that he saw an elderly lady standing at a very crowded sidewalk. Cars rushed past, and she looked like she didn't have the courage to cross such a busy road. Although he was so much into his own trouble, somehow there was that tug he could feel within him to help. {{ ai_empathy }}
        
        He did stop for a moment. "I am already having my worst day. Why even bother?" But this egoistic thought was removed from his mind. Something very deep was urging him forward. He went to her and said, "May I help you cross over the street?" The eyes of the woman brightened up instantaneously with an illumination associated with relief. "Oh, it would be a wonderful favor." He carefully took her across this street, protecting her from the flow of impatient rushing cars. When they reached just at the other side of the street, the woman squeezed his hand, saying, "You have a very kind heart, young man." {{ ai_gratitude }} {{ ai_protectiveness }}
        
        At that moment, for the first time in a long time, something inside {{ ai_story_character }} changed. He found peace in this simple act of kindness to a stranger that would have been missing from his life for a while now. {{ ai_serenity }}
        
        Later that night, {{ ai_story_character }} reached home only to find an unexpected surprise lying on his doorstep: a tiny little package along with a handwritten note. The note written by the elderly lady acknowledged her heartfelt gratitude. Within that package was a pair of gloves with a simple message inscribed, "Kindness is a reward." {{ ai_story_character }}'s eyes went wide as he read the note, and warmth began to swell in his chest. And for the first time that day, that was a smile of {{ ai_story_character }}'s that could be described as genuine. {{ ai_joy }}
        
        It has changed the entire scenario; most importantly, it brings some happiness and brightness. Even on a day that feels like it was filled with constant misfortunes, it feels great to have one's kindness appreciated and recognized. In the end, it just goes to show-and point out, really-that even on the worst days, such an act, no matter the proportion, can change everything. Inspired by the experience, he determined to keep helping others, though difficult his circumstances became. {{ ai_hope }}
        
        The next morning came into play with the strangest of happenings. As he entered his work, he saw the coworker whom he had snapped at yesterday. It would have been easy to ignore him, but instead {{ ai_story_character }} took a breath and said, "Hey... I'm sorry about yesterday." The man blinked at him in surprise, then laughed and said, "No worries, {{ ai_story_character }}. I was in a bad mood, too." Then they shook hands, and for the first time ever, {{ ai_story_character }} felt a sense of kinship with another human being in the workplace. {{ ai_friendship }}
        
        Thus, {{ ai_story_character }} was called again by his boss, only this time the tone was entirely different. "I've been watching you, {{ ai_story_character }}. I see improvement. Keep it up." Relief flooded {{ ai_story_character }}'s chest. He was convinced he might well be on the verge of losing everything; instead, there turned out to be a way forward. {{ ai_relief }}
        
        He could feel the care for others in him-from within. He now knew how much people's suffering mirrored his own, and for the first time, he felt other people's suffering with a weight never felt before. {{ ai_compassion }} He reflected on how he had judged people too early, not understanding that they had unseen burdens much like himself.
        
        He sat in silent deliberation, understanding what this harsh day really meant for him. He had thought that suffering hardship meant only pain but had now discovered the hidden meaning within. {{ ai_self_reflection }} It had brought him under fire and had helped him to discover more deeply his understanding of himself and his environment.
        
        As a bright candle of hope, his story spread all over the community. People started thinking that no matter how wrong life seems at times, small acts of generosity and care could create ripples of change. The unlucky day for {{ ai_story_character }} became a historic day-proving that every challenge has a chance to make this world a bit brighter. {{ ai_inspiration }}
    """
    

    chatgpt_prompt = f"""
        Analyze the following story first and generate a JSON object with the following keys, each filled with one or two sentences extending the story:
        - ai_story_moral (one sentence only)
        - ai_story_character (ensure this is a **male** name)
        - ai_frustration 
        - ai_sadness 
        - ai_fear 
        - ai_anger 
        - ai_empathy 
        - ai_gratitude 
        - ai_protectiveness 
        - ai_serenity 
        - ai_joy
        - ai_hope 
        - ai_friendship 
        - ai_relief 
        - ai_compassion 
        - ai_self_reflection 
        - ai_inspiration

        Only return the JSON object. 
        Do not repeat anything from the story but only extend the feels in the key options.
        Try to be expressive with one or two long sentences and creative in the JSON object.
        Do not include any explanations or markdown formatting.
        Use pronouns as he/him in the outputs only. 
        Only use the name in the ai_story_character. 
        Do not use any other names in the JSON object.

        STORY:
        {story_text}
        """
    
    try:
        # Step 1: Fetch the database entry
        logging.info(f"Fetching database entry for ID: {id}")
        entry = db.session.get(Exercise1, id)
        if not entry:
            logging.error(f"Entry with ID {id} not found in the database")
            return jsonify({"error": "Entry not found"}), 404
        logging.info(f"Database entry found for ID: {id}")

        # Step 2: Generate AI story using mock data or OpenAI API
        if USE_MOCK_DATA:
            logging.info("Using mock data instead of OpenAI API")
            data = {
                "ai_story_character": "John",
                "ai_frustration": "He felt frustrated by the constant setbacks.",
                "ai_sadness": "He was saddened by the lack of support.",
                "ai_fear": "He feared losing his job.",
                "ai_anger": "He was angry at the unfair treatment.",
                "ai_empathy": "He empathized with a struggling coworker.",
                "ai_gratitude": "He was grateful for a kind gesture.",
                "ai_protectiveness": "He felt protective of his team.",
                "ai_serenity": "He found peace in helping others.",
                "ai_joy": "He experienced joy in small victories.",
                "ai_hope": "He hoped for a better future.",
                "ai_friendship": "He built a strong friendship with a colleague.",
                "ai_relief": "He felt relieved after resolving a conflict.",
                "ai_compassion": "He showed compassion to those in need.",
                "ai_self_reflection": "He reflected on his actions and grew stronger.",
                "ai_inspiration": "He inspired others to persevere.",
                "ai_story_moral": "Kindness and perseverance can overcome any challenge."
            }
        else:
            logging.info("Calling OpenAI API to generate the story")
            try:
                response = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "You are a helpful assistant."},
                        {"role": "user", "content": chatgpt_prompt}
                    ],
                    max_tokens=900,
                    temperature=0.7
                )
                logging.info("OpenAI API call successful")
                response_text = response.choices[0].message.content.strip()
                logging.debug(f"OpenAI response: {response_text}")
            except OpenAIError as api_error:
                logging.error(f"OpenAI API error: {api_error}")
                return jsonify({"error": "Failed to generate story: OpenAI quota or API error"}), 502

            # Step 3: Parse the JSON response
            try:
                data = json.loads(response_text)
                logging.info("Successfully parsed AI story JSON")
            except json.JSONDecodeError as e:
                logging.error(f"JSON parsing error: {e}")
                logging.error(f"Raw response: {response_text}")
                return jsonify({"error": "Failed to parse AI response as JSON"}), 500

        # Step 4: Update the database entry
        logging.info(f"Updating database entry for ID: {id}")
        entry.ai_story_character = data.get("ai_story_character", entry.ai_story_character)
        entry.ai_frustration = data.get("ai_frustration", entry.ai_frustration)
        entry.ai_sadness = data.get("ai_sadness", entry.ai_sadness)
        entry.ai_fear = data.get("ai_fear", entry.ai_fear)
        entry.ai_anger = data.get("ai_anger", entry.ai_anger)
        entry.ai_empathy = data.get("ai_empathy", entry.ai_empathy)
        entry.ai_gratitude = data.get("ai_gratitude", entry.ai_gratitude)
        entry.ai_protectiveness = data.get("ai_protectiveness", entry.ai_protectiveness)
        entry.ai_serenity = data.get("ai_serenity", entry.ai_serenity)
        entry.ai_joy = data.get("ai_joy", entry.ai_joy)
        entry.ai_hope = data.get("ai_hope", entry.ai_hope)
        entry.ai_friendship = data.get("ai_friendship", entry.ai_friendship)
        entry.ai_relief = data.get("ai_relief", entry.ai_relief)
        entry.ai_compassion = data.get("ai_compassion", entry.ai_compassion)
        entry.ai_self_reflection = data.get("ai_self_reflection", entry.ai_self_reflection)
        entry.ai_inspiration = data.get("ai_inspiration", entry.ai_inspiration)
        entry.ai_story_moral = data.get("ai_story_moral", entry.ai_story_moral)
        
        entry.ai_story = f"""
        {entry.ai_story_character} was indeed a very hardworking man who put in all his efforts in all possible ways. Every morning he woke up early and got prepared for work meticulously to support his family most effectively. But unfortunately, things started going totally non-synchronized, one fine day.
        This particular morning, the alarm failed to ring, and therefore {entry.ai_story_character} woke up late. In haste he got up and started living his daily life. He wore a shirt on which some coffee spilled and he got out just missing the usual bus. The rest of it was forced to be walked under a chilly and drizzling rain to get to work. {entry.ai_story_character} noted how the rain fell and continued to match his steadily growing exasperation and sense of unluckiness. {entry.ai_frustration}
        
        Thanks to the plethora of obstacles piling up in his life, he had exceeded that last point and went further. He had finally made it to work, only to continue discovering frustration. His computer failed him on an important assignment, and everyone else seemed too busy burning their bridges to offer assistance. Every tiny mishap continued accumulating, leaving him tired and muffling up the morale. {entry.ai_story_character} heaved a frustrated sigh, staring at his screen, feeling utterly defeated by everything around him. {entry.ai_sadness}
        
        Things couldn't get any worse, just as he thought. His boss calls him into the office. "{entry.ai_story_character}, your work has been sloppy lately," said the boss coldly. He added, "If this continues, we may need to reconsider your position here." A sudden wave of fear gripped him. He had worked tireless days; now, one bad day could cost him everything. His hands trembled leaving the office; his heart was pounding. {entry.ai_fear}
        
        At lunch hour, {entry.ai_story_character} sat there alone, gripping a sandwich with white knuckle fingers. One coworker bumped into him; his food hit the floor. "Hey, watch it {entry.ai_story_character}," the man dismissively muttered. That was the last straw. Anger erupted in {entry.ai_story_character}'s chest. "Are you kidding me?!," he snapped, standing abruptly. But when he saw both men's shocked look, he bit his tongue and stormed out to seethe. {entry.ai_anger}
        
        After a rough day at work, in busy streets {entry.ai_story_character} walked home. There were thousands of things racing through his mind: frustration, worry, exhaustion, and everything too. It was then that he saw an elderly lady standing at a very crowded sidewalk. Cars rushed past, and she looked like she didn't have the courage to cross such a busy road. Although he was so much into his own trouble, somehow there was that tug he could feel within him to help. {entry.ai_empathy}
        
        He did stop for a moment. "I am already having my worst day. Why even bother?" But this egoistic thought was removed from his mind. Something very deep was urging him forward. He went to her and said, "May I help you cross over the street?" The eyes of the woman brightened up instantaneously with an illumination associated with relief. "Oh, it would be a wonderful favor." He carefully took her across this street, protecting her from the flow of impatient rushing cars. When they reached just at the other side of the street, the woman squeezed his hand, saying, "You have a very kind heart, young man." {entry.ai_gratitude} {entry.ai_protectiveness}
        
        At that moment, for the first time in a long time, something inside {entry.ai_story_character} changed. He found peace in this simple act of kindness to a stranger that would have been missing from his life for a while now. {entry.ai_serenity}
        
        Later that night, {entry.ai_story_character} reached home only to find an unexpected surprise lying on his doorstep: a tiny little package along with a handwritten note. The note written by the elderly lady acknowledged her heartfelt gratitude. Within that package was a pair of gloves with a simple message inscribed, "Kindness is a reward." {entry.ai_story_character}'s eyes went wide as he read the note, and warmth began to swell in his chest. And for the first time that day, that was a smile of {entry.ai_story_character}'s that could be described as genuine. {entry.ai_joy}
        
        It has changed the entire scenario; most importantly, it brings some happiness and brightness. Even on a day that feels like it was filled with constant misfortunes, it feels great to have one's kindness appreciated and recognized. In the end, it just goes to show-and point out, really-that even on the worst days, such an act, no matter the proportion, can change everything. Inspired by the experience, he determined to keep helping others, though difficult his circumstances became. {entry.ai_hope}
        
        The next morning came into play with the strangest of happenings. As he entered his work, he saw the coworker whom he had snapped at yesterday. It would have been easy to ignore him, but instead {entry.ai_story_character} took a breath and said, "Hey... I'm sorry about yesterday." The man blinked at him in surprise, then laughed and said, "No worries, {entry.ai_story_character}. I was in a bad mood, too." Then they shook hands, and for the first time ever, {entry.ai_story_character} felt a sense of kinship with another human being in the workplace. {entry.ai_friendship}
        
        Thus, {entry.ai_story_character} was called again by his boss, only this time the tone was entirely different. "I've been watching you, {entry.ai_story_character}. I see improvement. Keep it up." Relief flooded {entry.ai_story_character}'s chest. He was convinced he might well be on the verge of losing everything; instead, there turned out to be a way forward. {entry.ai_relief}
        
        He could feel the care for others in him-from within. He now knew how much people's suffering mirrored his own, and for the first time, he felt other people's suffering with a weight never felt before. {entry.ai_compassion} He reflected on how he had judged people too early, not understanding that they had unseen burdens much like himself.
        
        He sat in silent deliberation, understanding what this harsh day really meant for him. He had thought that suffering hardship meant only pain but had now discovered the hidden meaning within. {entry.ai_self_reflection} It had brought him under fire and had helped him to discover more deeply his understanding of himself and his environment.
        
        As a bright candle of hope, his story spread all over the community. People started thinking that no matter how wrong life seems at times, small acts of generosity and care could create ripples of change. The unlucky day for {entry.ai_story_character} became a historic day-proving that every challenge has a chance to make this world a bit brighter. {entry.ai_inspiration}
    """

        # Step 5: Commit changes to the database
        try:
            db.session.commit()
            logging.info(f"Successfully updated database entry for ID: {id}")
        except Exception as db_error:
            logging.error(f"Database commit error: {db_error}")
            return jsonify({"error": "Database commit failed"}), 500

        # Step 6: Return success response
        logging.info(f"AI story generation and save completed for ID: {id}")
        return jsonify({"message": "AI story generated and saved successfully", "data": data}), 200

    except Exception as e:
        logging.error(f"Unexpected error during AI story generation: {str(e)}")
        return jsonify({"error": "Internal Server Error"}), 500

@exercise1_bp.route('/generate-ai-story', methods=['GET', 'POST'])
def generate_ai_story_without_id():
    story_text = """
        {{ ai_story_character }} was indeed a very hardworking man who put in all his efforts in all possible ways. Every morning he woke up early and got prepared for work meticulously to support his family most effectively. But unfortunately, things started going totally non-synchronized, one fine day.
        This particular morning, the alarm failed to ring, and therefore {{ ai_story_character }} woke up late. In haste he got up and started living his daily life. He wore a shirt on which some coffee spilled and he got out just missing the usual bus. The rest of it was forced to be walked under a chilly and drizzling rain to get to work. {{ ai_story_character }} noted how the rain fell and continued to match his steadily growing exasperation and sense of unluckiness. {{ ai_frustration }}
        
        Thanks to the plethora of obstacles piling up in his life, he had exceeded that last point and went further. He had finally made it to work, only to continue discovering frustration. His computer failed him on an important assignment, and everyone else seemed too busy burning their bridges to offer assistance. Every tiny mishap continued accumulating, leaving him tired and muffling up the morale. {{ ai_story_character }} heaved a frustrated sigh, staring at his screen, feeling utterly defeated by everything around him. {{ ai_sadness }}
        
        Things couldn't get any worse, just as he thought. His boss calls him into the office. "{{ ai_story_character }}, your work has been sloppy lately," said the boss coldly. He added, "If this continues, we may need to reconsider your position here." A sudden wave of fear gripped him. He had worked tireless days; now, one bad day could cost him everything. His hands trembled leaving the office; his heart was pounding. {{ ai_fear }}
        
        At lunch hour, {{ ai_story_character }} sat there alone, gripping a sandwich with white knuckle fingers. One coworker bumped into him; his food hit the floor. "Hey, watch it {{ ai_story_character }}," the man dismissively muttered. That was the last straw. Anger erupted in {{ ai_story_character }}'s chest. "Are you kidding me?!," he snapped, standing abruptly. But when he saw both men's shocked look, he bit his tongue and stormed out to seethe. {{ ai_anger }}
        
        After a rough day at work, in busy streets {{ ai_story_character }} walked home. There were thousands of things racing through his mind: frustration, worry, exhaustion, and everything too. It was then that he saw an elderly lady standing at a very crowded sidewalk. Cars rushed past, and she looked like she didn't have the courage to cross such a busy road. Although he was so much into his own trouble, somehow there was that tug he could feel within him to help. {{ ai_empathy }}
        
        He did stop for a moment. "I am already having my worst day. Why even bother?" But this egoistic thought was removed from his mind. Something very deep was urging him forward. He went to her and said, "May I help you cross over the street?" The eyes of the woman brightened up instantaneously with an illumination associated with relief. "Oh, it would be a wonderful favor." He carefully took her across this street, protecting her from the flow of impatient rushing cars. When they reached just at the other side of the street, the woman squeezed his hand, saying, "You have a very kind heart, young man." {{ ai_gratitude }} {{ ai_protectiveness }}
        
        At that moment, for the first time in a long time, something inside {{ ai_story_character }} changed. He found peace in this simple act of kindness to a stranger that would have been missing from his life for a while now. {{ ai_serenity }}
        
        Later that night, {{ ai_story_character }} reached home only to find an unexpected surprise lying on his doorstep: a tiny little package along with a handwritten note. The note written by the elderly lady acknowledged her heartfelt gratitude. Within that package was a pair of gloves with a simple message inscribed, "Kindness is a reward." {{ ai_story_character }}'s eyes went wide as he read the note, and warmth began to swell in his chest. And for the first time that day, that was a smile of {{ ai_story_character }}'s that could be described as genuine. {{ ai_joy }}
        
        It has changed the entire scenario; most importantly, it brings some happiness and brightness. Even on a day that feels like it was filled with constant misfortunes, it feels great to have one's kindness appreciated and recognized. In the end, it just goes to show-and point out, really-that even on the worst days, such an act, no matter the proportion, can change everything. Inspired by the experience, he determined to keep helping others, though difficult his circumstances became. {{ ai_hope }}
        
        The next morning came into play with the strangest of happenings. As he entered his work, he saw the coworker whom he had snapped at yesterday. It would have been easy to ignore him, but instead {{ ai_story_character }} took a breath and said, "Hey... I'm sorry about yesterday." The man blinked at him in surprise, then laughed and said, "No worries, {{ ai_story_character }}. I was in a bad mood, too." Then they shook hands, and for the first time ever, {{ ai_story_character }} felt a sense of kinship with another human being in the workplace. {{ ai_friendship }}
        
        Thus, {{ ai_story_character }} was called again by his boss, only this time the tone was entirely different. "I've been watching you, {{ ai_story_character }}. I see improvement. Keep it up." Relief flooded {{ ai_story_character }}'s chest. He was convinced he might well be on the verge of losing everything; instead, there turned out to be a way forward. {{ ai_relief }}
        
        He could feel the care for others in him-from within. He now knew how much people's suffering mirrored his own, and for the first time, he felt other people's suffering with a weight never felt before. {{ ai_compassion }} He reflected on how he had judged people too early, not understanding that they had unseen burdens much like himself.
        
        He sat in silent deliberation, understanding what this harsh day really meant for him. He had thought that suffering hardship meant only pain but had now discovered the hidden meaning within. {{ ai_self_reflection }} It had brought him under fire and had helped him to discover more deeply his understanding of himself and his environment.
        
        As a bright candle of hope, his story spread all over the community. People started thinking that no matter how wrong life seems at times, small acts of generosity and care could create ripples of change. The unlucky day for {{ ai_story_character }} became a historic day-proving that every challenge has a chance to make this world a bit brighter. {{ ai_inspiration }}
        """
    
    try:
        if request.method == 'GET':
            prompt = "Generate an AI story"
        else:
            data = request.json
            prompt = data.get("prompt", "").strip()

        if not prompt:
            return jsonify({"error": "Prompt is required"}), 400

        chatgpt_prompt = f"""
        Analyze the following story first and generate a JSON object with the following keys, each filled with one or two sentences extending the story:
        - ai_story_moral (one sentence only)
        - ai_story_character (ensure this is a **male** name)
        - ai_frustration 
        - ai_sadness 
        - ai_fear 
        - ai_anger 
        - ai_empathy 
        - ai_gratitude 
        - ai_protectiveness 
        - ai_serenity 
        - ai_joy
        - ai_hope 
        - ai_friendship 
        - ai_relief 
        - ai_compassion 
        - ai_self_reflection 
        - ai_inspiration

        Only return the JSON object. 
        Do not repeat anything from the story but only extend the feels in the key options.
        Try to be expressive with one or two long sentences and creative in the JSON object.
        Do not include any explanations or markdown formatting.
        Use pronouns as he/him in the outputs only. 
        Only use the name in the ai_story_character. 
        Do not use any other names in the JSON object.

        STORY:
        {story_text}
        """

        if USE_MOCK_DATA:
            logging.info("Using mock data instead of OpenAI API")
            response_text = json.dumps({
                "ai_story_moral": "Believe in yourself.",
                "ai_story_character": "A clever fox named Felix.",
                "ai_frustration": "Felix couldn’t outsmart a hunter.",
                "ai_sadness": "He lost his favorite hiding spot.",
                "ai_fear": "He feared being caught.",
                "ai_anger": "He was angry at his own mistake.",
                "ai_empathy": "He helped a scared rabbit.",
                "ai_gratitude": "He was grateful for his friend’s help.",
                "ai_protectiveness": "He guarded the forest animals.",
                "ai_serenity": "He meditated under the stars.",
                "ai_joy": "He played in the meadow.",
                "ai_hope": "He hoped for a safer forest.",
                "ai_friendship": "He bonded with a wise owl.",
                "ai_relief": "He narrowly escaped danger.",
                "ai_compassion": "He forgave the hunter.",
                "ai_self_reflection": "He realized he’s stronger with others.",
                "ai_inspiration": "He inspired animals to stand together."
            })
        else:
            try:
                response = client.chat.completions.create(
                    model="gpt-4-turbo",
                    messages=[
                        {"role": "system", "content": "You are a helpful assistant."},
                        {"role": "user", "content": chatgpt_prompt}
                    ],
                    max_tokens=900,
                    temperature=0.7
                )
            except OpenAIError as api_error:
                logging.error(f"OpenAI API error: {api_error}")
                return jsonify({"error": "Failed to generate story: OpenAI quota or API error"}), 502

            response_text = response.choices[0].message.content.strip()
            logging.debug(f"Raw OpenAI response: {repr(response_text)}")

            if not response_text:
                logging.error("Empty response from OpenAI")
                return jsonify({"error": "Empty response from OpenAI"}), 502

        try:
            # Attempt to extract JSON from markdown code block
            json_match = re.search(r'```json\s*(\{.*?\})\s*```', response_text, re.DOTALL)
            if json_match:
                json_str = json_match.group(1)
            else:
                json_str = response_text  # Try full text if no markdown found

            ai_story = json.loads(json_str)
        except json.JSONDecodeError as e:
            logging.error(f"JSON parsing error: {e}")
            logging.error(f"Raw response that caused error: {repr(response_text)}")
            return jsonify({
                "error": "Failed to parse AI response as JSON",
                "raw_response": response_text
            }), 500

        return jsonify(ai_story), 200

    except Exception as e:
        logging.error(f"Error generating AI story: {str(e)}")
        return jsonify({"error": "Internal Server Error"}), 500
