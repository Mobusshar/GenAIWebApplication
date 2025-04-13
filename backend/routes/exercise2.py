import logging
from flask import Blueprint, request, jsonify, send_from_directory, current_app
from models.db.exercise2 import db, Exercise2
import os
import requests
import json
import re
import base64
from dotenv import load_dotenv
from openai import OpenAI
from openai import OpenAIError
from jsonfinder import jsonfinder  # Import jsonfinder

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,  # Set the log level to DEBUG to capture all logs
    format="%(asctime)s - %(levelname)s - %(message)s",  # Format for log messages
    handlers=[
        logging.StreamHandler()  # Output logs to the terminal
    ]
)

# Load environment variables from .env file
load_dotenv()

# Access the OpenAI API key from the environment
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    raise ValueError("OpenAI API key is not set. Please add it to the .env file.")

exercise1_bp = Blueprint('exercise1', __name__)

client = OpenAI(api_key=OPENAI_API_KEY)  # Replace with your actual API key


exercise2_bp = Blueprint('exercise2', __name__)

@exercise2_bp.route("/pre-exercise2", methods=["POST"])
def create_pre_exercise_entry():
    """
    Create a new entry for Exercise 2 with pre-exercise values.
    """
    try:
        data = request.json

        # Extract pre-exercise values from the request
        pre_demo_name = data.get("pre_demo_name", "").strip()
        pre_demo_email = data.get("pre_demo_email", "").strip()
        pre_demo_academic = data.get("pre_demo_academic", "").strip()
        pre_creative_confidence = data.get("pre_creative_confidence")
        pre_creative_frequency = data.get("pre_creative_frequency")
        pre_creativity_meaning = data.get("pre_creativity_meaning", "").strip()
        pre_used_ai_tools = data.get("pre_used_ai_tools", False)
        pre_ai_tools_used = data.get("pre_ai_tools_used", "").strip()
        pre_ai_comfort = data.get("pre_ai_comfort")
        pre_ai_expectations = data.get("pre_ai_expectations", "").strip()
        pre_collab_confidence = data.get("pre_collab_confidence")
        pre_collab_role = data.get("pre_collab_role", "").strip()
        pre_collab_value = data.get("pre_collab_value", "").strip()

        # Validate required fields
        if not pre_demo_name or not pre_demo_email or not pre_demo_academic:
            return jsonify({"error": "Name, email, and academic background are required"}), 400

        # Create a new Exercise2 entry
        new_entry = Exercise2(
            pre_demo_name=pre_demo_name,
            pre_demo_email=pre_demo_email,
            pre_demo_academic=pre_demo_academic,
            pre_creative_confidence=pre_creative_confidence,
            pre_creative_frequency=pre_creative_frequency,
            pre_creativity_meaning=pre_creativity_meaning,
            pre_used_ai_tools=pre_used_ai_tools,
            pre_ai_tools_used=pre_ai_tools_used,
            pre_ai_comfort=pre_ai_comfort,
            pre_ai_expectations=pre_ai_expectations,
            pre_collab_confidence=pre_collab_confidence,
            pre_collab_role=pre_collab_role,
            pre_collab_value=pre_collab_value
        )

        # Add the entry to the database
        db.session.add(new_entry)
        db.session.commit()

        return jsonify({"message": "Pre-exercise entry created successfully", "id": new_entry.id}), 201

    except Exception as e:
        logging.error(f"Error creating pre-exercise entry: {str(e)}")
        return jsonify({"error": "Internal Server Error"}), 500

@exercise2_bp.route("/upload-sketch/<int:id>", methods=["PUT"])
def upload_sketch(id):
    """
    Upload a sketch image, save it to the server, rename it, and update the database.
    """
    try:
        # Check if a file is included in the request
        if 'file' not in request.files:
            return jsonify({"error": "No file part in the request"}), 400

        file = request.files['file']

        # Check if the file has a valid name
        if file.filename == '':
            return jsonify({"error": "No selected file"}), 400

        # Define the upload directory
        upload_dir = os.path.join(current_app.root_path, "user_sketch_images_before")
        os.makedirs(upload_dir, exist_ok=True)

        # Rename the file to <id>Sketch_before
        file_extension = os.path.splitext(file.filename)[1]
        new_filename = f"{id}_sketch_before{file_extension}"
        file_path = os.path.join(upload_dir, new_filename)

        # Save the file to the server
        file.save(file_path)

        # Update the database with the new file path
        entry = Exercise2.query.get(id)
        if not entry:
            return jsonify({"error": "Record not found"}), 404

        entry.sketch_upload_path_before = f"user_sketch_images_before/{new_filename}"
        db.session.commit()

        return jsonify({"message": "Sketch uploaded successfully", "filePath": entry.sketch_upload_path_before}), 200

    except Exception as e:
        logging.error(f"Error uploading sketch: {str(e)}")
        return jsonify({"error": "Internal Server Error"}), 500

@exercise2_bp.route("/upload-final-sketch/<int:id>", methods=["PUT"])
def upload_final_sketch(id):
    """
    Upload a final sketch image, save it to the server, rename it, and update the database.
    """
    try:
        # Check if a file is included in the request
        if 'file' not in request.files:
            return jsonify({"error": "No file part in the request"}), 400

        file = request.files['file']

        # Check if the file has a valid name
        if file.filename == '':
            return jsonify({"error": "No selected file"}), 400

        # Define the upload directory
        upload_dir = os.path.join(current_app.root_path, "user_sketch_images_final")
        os.makedirs(upload_dir, exist_ok=True)

        # Rename the file to <id>Sketch_after
        file_extension = os.path.splitext(file.filename)[1]
        new_filename = f"{id}_sketch_after{file_extension}"
        file_path = os.path.join(upload_dir, new_filename)

        # Save the file to the server
        file.save(file_path)

        # Update the database with the new file path
        entry = Exercise2.query.get(id)
        if not entry:
            return jsonify({"error": "Record not found"}), 404

        entry.sketch_upload_path_after = f"user_sketch_images_final/{new_filename}"
        db.session.commit()

        return jsonify({"message": "Final sketch uploaded successfully", "filePath": entry.sketch_upload_path_after}), 200

    except Exception as e:
        logging.error(f"Error uploading final sketch: {str(e)}")
        return jsonify({"error": "Internal Server Error"}), 500

@exercise2_bp.route("/update-products/<int:id>", methods=["PUT"])
def update_products(id):
    """
    Update product data and sketch path in the database.
    """
    try:
        data = request.json
        entry = Exercise2.query.get(id)
        if not entry:
            return jsonify({"error": "Record not found"}), 404

        # Update product fields
        entry.product1_name = data.get("product1_name", entry.product1_name)
        entry.product1_description = data.get("product1_description", entry.product1_description)
        entry.product1_suggested_euro = data.get("product1_suggested_euro", entry.product1_suggested_euro)
        entry.product2_name = data.get("product2_name", entry.product2_name)
        entry.product2_description = data.get("product2_description", entry.product2_description)
        entry.product2_suggested_euro = data.get("product2_suggested_euro", entry.product2_suggested_euro)
        entry.product3_name = data.get("product3_name", entry.product3_name)
        entry.product3_description = data.get("product3_description", entry.product3_description)
        entry.product3_suggested_euro = data.get("product3_suggested_euro", entry.product3_suggested_euro)

        db.session.commit()

        return jsonify({"message": "Product data and sketch updated successfully"}), 200

    except Exception as e:
        logging.error(f"Error updating product data: {str(e)}")
        return jsonify({"error": "Internal Server Error"}), 500

@exercise2_bp.route("/generate-ai-image/<int:id>", methods=["POST"])
def generate_ai_image(id):
    """
    Generate AI image and extract product details based on the uploaded sketch.
    """
    try:
        entry = Exercise2.query.get(id)
        if not entry:
            return jsonify({"error": "Record not found"}), 404

        # Validate sketch path
        sketch_path = entry.sketch_upload_path_before
        if not sketch_path:
            return jsonify({"error": "Sketch not found"}), 400

        full_sketch_path = os.path.join(current_app.root_path, sketch_path)
        if not os.path.exists(full_sketch_path):
            return jsonify({"error": "Sketch file not found"}), 404

        # Generate prompt from sketch using GPT-4 Vision
        try:
            prompt = generate_dalle_prompt_from_sketch(full_sketch_path, entry)
            logging.info(f"Generated DALL·E prompt: {prompt}")
        except Exception as e:
            logging.error(f"Error generating DALL·E prompt: {str(e)}")
            return jsonify({"error": "Failed to generate DALL·E prompt"}), 500

        # Generate AI image from prompt using DALL·E 3
        try:
            ai_image_dir = os.path.join(current_app.root_path, "ai_sketch_images")
            os.makedirs(ai_image_dir, exist_ok=True)
            ai_image_path = os.path.join(ai_image_dir, f"{id}_ai_generated.jpg")
            generate_image_with_dalle(prompt, ai_image_path)
            entry.ai_image_path = f"ai_sketch_images/{id}_ai_generated.jpg"
        except Exception as e:
            logging.error(f"Error generating AI image: {str(e)}")
            return jsonify({"error": "Failed to generate AI image"}), 500

        # Extract product details from AI image
        try:
            product_details = call_image_to_text_model(ai_image_path)

            # Save the extracted product details to the database
            entry.product1_ai_name = product_details["product1"]["name"]
            entry.product1_ai_description = product_details["product1"]["description"]
            entry.product1_ai_suggested_euro = product_details["product1"]["market_value_euro"]
            entry.product2_ai_name = product_details["product2"]["name"]
            entry.product2_ai_description = product_details["product2"]["description"]
            entry.product2_ai_suggested_euro = product_details["product2"]["market_value_euro"]
            entry.product3_ai_name = product_details["product3"]["name"]
            entry.product3_ai_description = product_details["product3"]["description"]
            entry.product3_ai_suggested_euro = product_details["product3"]["market_value_euro"]

            db.session.commit()

        except Exception as e:
            logging.error(f"Error extracting product details: {str(e)}")
            return jsonify({"error": "Failed to extract product details"}), 500

        return jsonify({
            "generatedImageUrl": entry.ai_image_path,
            "product1_ai_name": entry.product1_ai_name,
            "product1_ai_description": entry.product1_ai_description,
            "product1_ai_suggested_euro": entry.product1_ai_suggested_euro,
            "product2_ai_name": entry.product2_ai_name,
            "product2_ai_description": entry.product2_ai_description,
            "product2_ai_suggested_euro": entry.product2_ai_suggested_euro,
            "product3_ai_name": entry.product3_ai_name,
            "product3_ai_description": entry.product3_ai_description,
            "product3_ai_suggested_euro": entry.product3_ai_suggested_euro
        }), 200

    except Exception as e:
        logging.error(f"Error generating AI image: {str(e)}")
        return jsonify({"error": "Internal Server Error"}), 500

@exercise2_bp.route("/get-images-and-products/<int:id>", methods=["GET"])
def get_images_and_products(id):
    """
    Fetch the uploaded sketch, AI-generated image paths, and product details for a given ID.
    """
    try:
        entry = Exercise2.query.get(id)
        if not entry:
            return jsonify({"error": "Record not found"}), 404

        # Ensure the paths are correct
        sketch_path = f"/{entry.sketch_upload_path_before}"
        ai_image_path = f"/{entry.ai_image_path}"

        return jsonify({
            "uploaded": {
                "sketch_upload_path_before": sketch_path,
                "sketch_upload_path_after": entry.sketch_upload_path_after,
                "product1_name": entry.product1_name,
                "product1_description": entry.product1_description,
                "product1_suggested_euro": entry.product1_suggested_euro,
                "product2_name": entry.product2_name,
                "product2_description": entry.product2_description,
                "product2_suggested_euro": entry.product2_suggested_euro,
                "product3_name": entry.product3_name,
                "product3_description": entry.product3_description,
                "product3_suggested_euro": entry.product3_suggested_euro
            },
            "generated": {
                "ai_image_path": ai_image_path,
                "product1_ai_name": entry.product1_ai_name,
                "product1_ai_description": entry.product1_ai_description,
                "product1_ai_suggested_euro": entry.product1_ai_suggested_euro,
                "product2_ai_name": entry.product2_ai_name,
                "product2_ai_description": entry.product2_ai_description,
                "product2_ai_suggested_euro": entry.product2_ai_suggested_euro,
                "product3_ai_name": entry.product3_ai_name,
                "product3_ai_description": entry.product3_ai_description,
                "product3_ai_suggested_euro": entry.product3_ai_suggested_euro
            }
        }), 200

    except Exception as e:
        logging.error(f"Error fetching data: {str(e)}")
        return jsonify({"error": "Internal Server Error"}), 500


@exercise2_bp.route('/ai_sketch_images/<path:filename>', methods=['GET'])
def serve_ai_images(filename):
    """
    Serve AI-generated images from the ai_sketch_images directory.
    """
    ai_image_dir = os.path.join(current_app.root_path, 'ai_sketch_images')
    return send_from_directory(ai_image_dir, filename)


@exercise2_bp.route('/user_sketch_images_before/<path:filename>', methods=['GET'])
def serve_user_sketch_images(filename):
    """
    Serve user-uploaded sketch images from the user_sketch_images_before directory.
    """
    sketch_image_dir = os.path.join(current_app.root_path, 'user_sketch_images_before')
    return send_from_directory(sketch_image_dir, filename)


@exercise2_bp.route('/user_sketch_images_final/<path:filename>', methods=['GET'])
def serve_user_sketch_images_final(filename):
    """
    Serve user-uploaded final sketch images from the user_sketch_images_final directory.
    """
    sketch_image_dir = os.path.join(current_app.root_path, 'user_sketch_images_final')
    return send_from_directory(sketch_image_dir, filename)


@exercise2_bp.route("/post-exercise2-1/<int:id>", methods=["PUT"])
def update_post_exercise1(id):
    """
    Update post-exercise fields for Exercise 2.
    """
    try:
        data = request.json
        entry = Exercise2.query.get(id)
        if not entry:
            return jsonify({"error": "Record not found"}), 404

        # Update post-exercise fields
        entry.post_challenges_faced = data.get("post_challenges_faced", entry.post_challenges_faced)
        entry.post_most_engaging_part = data.get("post_most_engaging_part", entry.post_most_engaging_part)
        entry.post_most_difficult_part = data.get("post_most_difficult_part", entry.post_most_difficult_part)
        entry.post_ai_impact = data.get("post_ai_impact", entry.post_ai_impact)
        entry.post_revised_after_ai = data.get("post_revised_after_ai", entry.post_revised_after_ai)
        entry.post_revision_type = data.get("post_revision_type", entry.post_revision_type)
        entry.post_influenced_by_group = data.get("post_influenced_by_group", entry.post_influenced_by_group)
        entry.post_stuck_with_first_idea = data.get("post_stuck_with_first_idea", entry.post_stuck_with_first_idea)
        entry.post_ai_feedback_response = data.get("post_ai_feedback_response", entry.post_ai_feedback_response)
        entry.post_ai_made_more_appealing = data.get("post_ai_made_more_appealing", entry.post_ai_made_more_appealing)
        entry.post_description_influence = data.get("post_description_influence", entry.post_description_influence)
        entry.post_resistance_reason = data.get("post_resistance_reason", entry.post_resistance_reason)
        entry.post_familiarity_vs_innovation = data.get("post_familiarity_vs_innovation", entry.post_familiarity_vs_innovation)
        entry.post_ai_reinforce_or_challenge = data.get("post_ai_reinforce_or_challenge", entry.post_ai_reinforce_or_challenge)
        entry.post_experience_satisfaction = data.get("post_experience_satisfaction", entry.post_experience_satisfaction)
        entry.post_exercise_difficulty = data.get("post_exercise_difficulty", entry.post_exercise_difficulty)
        entry.post_creativity_boosted = data.get("post_creativity_boosted", entry.post_creativity_boosted)
        entry.post_exercise_enjoyment = data.get("post_exercise_enjoyment", entry.post_exercise_enjoyment)
        entry.post_exercise_improvements = data.get("post_exercise_improvements", entry.post_exercise_improvements)
        entry.post_ai_helpfulness = data.get("post_ai_helpfulness", entry.post_ai_helpfulness)
        entry.post_ai_modification_count = data.get("post_ai_modification_count", entry.post_ai_modification_count)
        entry.post_ai_refinement_strategy = data.get("post_ai_refinement_strategy", entry.post_ai_refinement_strategy)
        entry.post_final_output_contribution = data.get("post_final_output_contribution", entry.post_final_output_contribution)
        entry.post_ai_learning = data.get("post_ai_learning", entry.post_ai_learning)
        entry.post_peer_collab_value = data.get("post_peer_collab_value", entry.post_peer_collab_value)
        entry.post_peer_feedback_frequency = data.get("post_peer_feedback_frequency", entry.post_peer_feedback_frequency)
        entry.post_peer_collab_insight = data.get("post_peer_collab_insight", entry.post_peer_collab_insight)
        entry.post_confidence_after = data.get("post_confidence_after", entry.post_confidence_after)
        entry.post_skills_gained = data.get("post_skills_gained", entry.post_skills_gained)
        entry.post_future_ai_use_likelihood = data.get("post_future_ai_use_likelihood", entry.post_future_ai_use_likelihood)
        entry.post_confidence_change = data.get("post_confidence_change", entry.post_confidence_change)
        entry.post_ai_role = data.get("post_ai_role", entry.post_ai_role)
        entry.post_creative_challenges_preparation = data.get("post_creative_challenges_preparation", entry.post_creative_challenges_preparation)

        # Commit changes to the database
        db.session.commit()

        return jsonify({"message": "Post-exercise data updated successfully"}), 200

    except Exception as e:
        logging.error(f"Error updating post-exercise data: {str(e)}")
        return jsonify({"error": "Internal Server Error"}), 500


def generate_dalle_prompt_from_sketch(sketch_path, entry):
    """
    Generate a DALL·E prompt from a sketch and include product details from the database.
    If the API call fails, return a fallback prompt constructed from the product details.
    """
    try:
        # Read the sketch file and encode it as base64
        with open(sketch_path, "rb") as image_file:
            image_bytes = image_file.read()
            image_base64 = base64.b64encode(image_bytes).decode("utf-8")

        # Include product details in the prompt
        product_details_text = (
            f"Product 1: {entry.product1_name} - {entry.product1_description} (Suggested price: {entry.product1_suggested_euro} EUR)\n"
            f"Product 2: {entry.product2_name} - {entry.product2_description} (Suggested price: {entry.product2_suggested_euro} EUR)\n"
            f"Product 3: {entry.product3_name} - {entry.product3_description} (Suggested price: {entry.product3_suggested_euro} EUR)\n"
        )

        # Construct the primary prompt
        prompt_text = (
            "You are analyzing a sketch of a car interior that includes three distinct products. "
            "Your task is to write a vivid, high-quality prompt for generating an AI image using DALL·E 3. "
            "The generated image should be realistic, detailed, and match the perspective and point of view of the provided sketch. "
            "Ensure the image does not contain any text or labels. "
            "Focus on accurately representing the following three car interior products:\n"
            f"{product_details_text}\n"
            "Be creative and ensure the products are visually appealing and seamlessly integrated into the car interior design. "
            "The final image should look like a professional concept design for a luxury car interior."
        )

        # Attempt to generate the DALL·E prompt using GPT-4 Vision
        response = client.chat.completions.create(
            model="gpt-4-turbo",
            messages=[
                {
                    "role": "system",
                    "content": "You are an expert at creating DALL·E prompts from sketches."
                },
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": prompt_text
                        },
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/jpeg;base64,{image_base64}",
                                "detail": "high"
                            }
                        }
                    ]
                }
            ],
            max_tokens=800
        )

        # Return the generated prompt
        return response.choices[0].message.content.strip()

    except Exception as e:
        # Log the error and return the fallback prompt
        logging.error(f"Error generating DALL·E prompt: {str(e)}")
        logging.info("Returning fallback prompt.")

        # Construct the fallback prompt
        fallback_prompt = (
            "Fallback Prompt: Generate an AI image of a car interior based on the following product details:\n"
            f"{product_details_text}\n"
            "Ensure the image is realistic, detailed, and visually appealing, matching the perspective of a luxury car interior."
        )

        return fallback_prompt


def generate_image_with_dalle(prompt, output_path):
    """
    Generate an image using DALL·E 3. If the generation fails, serve a static fallback image.
    """
    try:
        # Attempt to generate the image using DALL·E
        response = client.images.generate(
            model="dall-e-3",
            prompt=prompt,
            size="1024x1024",
            quality="standard",
            n=1
        )

        # Extract the image URL from the response
        image_url = response.data[0].url
        if not image_url:
            raise Exception("No image URL returned from DALL·E")

        # Download the generated image
        image_response = requests.get(image_url)
        with open(output_path, "wb") as f:
            f.write(image_response.content)

    except Exception as e:
        logging.error(f"Error generating image with DALL·E: {str(e)}")

        # Serve a static fallback image
        static_fallback_path = os.path.join(current_app.root_path, "static", "DallEImages", "fallback_image.jpg")
        if not os.path.exists(static_fallback_path):
            logging.error("Fallback image not found. Please ensure 'fallback_image.jpg' exists in the 'static/DallEImages' directory.")
            raise Exception("Fallback image not found.")

        # Copy the fallback image to the output path
        with open(static_fallback_path, "rb") as fallback_file:
            with open(output_path, "wb") as output_file:
                output_file.write(fallback_file.read())
        logging.info(f"Served fallback image: {static_fallback_path}")


def call_image_to_text_model(image_path):
    """
    Use GPT-4 Vision to extract product details from an AI-generated image.
    """
    try:
        with open(image_path, "rb") as image_file:
            image_bytes = image_file.read()
            image_base64 = base64.b64encode(image_bytes).decode("utf-8")

        # Log the base64 string length for debugging
        logging.debug(f"Base64 image length: {len(image_base64)}")

        prompt = (
            "You are analyzing an image of a conceptual AI-generated car interior which has 3 products in it. "
            "Please extract and respond with a JSON object that includes three products in the following format:\n"
            "{\n"
            "  \"product1\": {\"name\": \"...\", \"description\": \"...\", \"market_value_euro\": 100},\n"
            "  \"product2\": {\"name\": \"...\", \"description\": \"...\", \"market_value_euro\": 200},\n"
            "  \"product3\": {\"name\": \"...\", \"description\": \"...\", \"market_value_euro\": 300}\n"
            "}\n"
            "Ensure the response is a valid JSON object and does not include any additional text or explanation."
        )

        response = client.chat.completions.create(
            model="gpt-4-turbo",
            messages=[
                {
                    "role": "system",
                    "content": "You are an AI that analyzes images of a car interior and extracts product data."
                },
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": prompt},
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/jpeg;base64,{image_base64}",
                                "detail": "high"
                            }
                        }
                    ]
                }
            ],
            max_tokens=1000
        )

        # Log the raw response for debugging
        logging.debug(f"Raw OpenAI API response: {response}")

        # Extract and parse the content
        content = response.choices[0].message.content.strip()
        logging.debug(f"Extracted content: {content}")

        # Validate and parse JSON
        try:
            parsed_content = json.loads(content)
            # Ensure the parsed content matches the expected structure
            if all(key in parsed_content for key in ["product1", "product2", "product3"]):
                return parsed_content
            else:
                raise ValueError("Response JSON does not match the expected structure.")
        except (json.JSONDecodeError, ValueError) as e:
            logging.warning(f"Initial JSON validation/parsing error: {str(e)}")
            # Attempt to find valid JSON using jsonfinder
            logging.debug("Attempting to extract JSON using jsonfinder...")
            matches = list(jsonfinder(content))
            for match in matches:
                try:
                    parsed_content = json.loads(match.json)
                    if all(key in parsed_content for key in ["product1", "product2", "product3"]):
                        logging.info("Valid JSON found using jsonfinder.")
                        return parsed_content
                except (json.JSONDecodeError, ValueError):
                    continue  # Try the next match

            logging.error("No valid JSON found using jsonfinder.")
            raise ValueError("No valid JSON found in the response.")

    except OpenAIError as e:
        logging.error(f"OpenAI API error: {str(e)}")
        raise

    except Exception as e:
        logging.error(f"Unexpected error: {str(e)}")
        raise

    # Fallback to default JSON if all else fails
    return {
        "product1": {"name": "Futuristic Steering Wheel", "description": "A high-tech steering wheel with integrated control systems and holographic displays", "market_value_euro": 450},
        "product2": {"name": "Interactive Dashboard Display", "description": "Advanced display with real-time vehicle analytics, navigation, and entertainment interfaces", "market_value_euro": 600},
        "product3": {"name": "Center Console Control Unit", "description": "Sophisticated center console featuring touch-sensitive controls and dynamic user interface for vehicle settings", "market_value_euro": 500}
    }
