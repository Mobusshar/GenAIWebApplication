from flask import Blueprint, request, jsonify, send_from_directory, current_app
from models.db.exercise2 import db, Exercise2
import os
import logging
import requests

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