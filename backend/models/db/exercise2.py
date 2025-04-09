from . import db

class Exercise2(db.Model):
    __tablename__ = 'exercise2'
    
    # Primary Key
    id = db.Column(db.Integer, primary_key=True)

    # Pre-Exercise Demographics
    pre_demo_name = db.Column(db.String(255))
    pre_demo_email = db.Column(db.String(255))
    pre_demo_academic = db.Column(db.String(255))

    # Baseline Creativity
    pre_creative_confidence = db.Column(db.Integer)
    pre_creative_frequency = db.Column(db.Integer)
    pre_creativity_meaning = db.Column(db.String(255))

    # Familiarity with AI
    pre_used_ai_tools = db.Column(db.Boolean)
    pre_ai_tools_used = db.Column(db.String(255))
    pre_ai_comfort = db.Column(db.Integer)
    pre_ai_expectations = db.Column(db.String(255))

    # Collaboration
    pre_collab_confidence = db.Column(db.Integer)
    pre_collab_role = db.Column(db.String(255))
    pre_collab_value = db.Column(db.String(255))

    # Post-Exercise Questions
    post_challenges_faced = db.Column(db.String(255))
    post_most_engaging_part = db.Column(db.String(255))
    post_most_difficult_part = db.Column(db.String(255))
    post_ai_impact = db.Column(db.String(255))
    post_revised_after_ai = db.Column(db.Boolean)
    post_revision_type = db.Column(db.String(255))
    post_influenced_by_group = db.Column(db.String(255))
    post_stuck_with_first_idea = db.Column(db.String(255))
    post_ai_feedback_response = db.Column(db.String(255))
    post_ai_made_more_appealing = db.Column(db.String(255))
    post_description_influence = db.Column(db.String(255))
    post_resistance_reason = db.Column(db.String(255))
    post_familiarity_vs_innovation = db.Column(db.String(255))
    post_ai_reinforce_or_challenge = db.Column(db.String(255))

    # Exercise Experience
    post_experience_satisfaction = db.Column(db.Integer)
    post_exercise_difficulty = db.Column(db.Integer)
    post_creativity_boosted = db.Column(db.Boolean)
    post_exercise_enjoyment = db.Column(db.String(255))
    post_exercise_improvements = db.Column(db.String(255))

    # AI Usage
    post_ai_helpfulness = db.Column(db.Integer)
    post_ai_modification_count = db.Column(db.Integer)
    post_ai_refinement_strategy = db.Column(db.String(255))
    post_final_output_contribution = db.Column(db.String(255))
    post_ai_learning = db.Column(db.String(255))

    # Collaboration Reflection
    post_peer_collab_value = db.Column(db.Integer)
    post_peer_feedback_frequency = db.Column(db.Integer)
    post_peer_collab_insight = db.Column(db.Text)

    # Learning Outcomes
    post_confidence_after = db.Column(db.Integer)
    post_skills_gained = db.Column(db.String(255))
    post_future_ai_use_likelihood = db.Column(db.Integer)

    # Reflection
    post_confidence_change = db.Column(db.String(255))
    post_ai_role = db.Column(db.String(255))
    post_creative_challenges_preparation = db.Column(db.String(255))

    # File Uploads
    sketch_upload_path_before = db.Column(db.String(255))
    sketch_upload_path_after = db.Column(db.String(255))
    ai_image_path = db.Column(db.String(255))

    # Product 1 Original
    product1_name = db.Column(db.String(255))
    product1_description = db.Column(db.Text)
    product1_suggested_euro = db.Column(db.String(255))

    # Product 2 Original
    product2_name = db.Column(db.String(255))
    product2_description = db.Column(db.Text)
    product2_suggested_euro = db.Column(db.String(255))

    # Product 3 Original
    product3_name = db.Column(db.String(255))
    product3_description = db.Column(db.Text)
    product3_suggested_euro = db.Column(db.String(255))

    # Product 1 AI-Generated
    product1_ai_name = db.Column(db.String(255))
    product1_ai_description = db.Column(db.Text)
    product1_ai_suggested_euro = db.Column(db.String(255))

    # Product 2 AI-Generated
    product2_ai_name = db.Column(db.String(255))
    product2_ai_description = db.Column(db.Text)
    product2_ai_suggested_euro = db.Column(db.String(255))

    # Product 3 AI-Generated
    product3_ai_name = db.Column(db.String(255))
    product3_ai_description = db.Column(db.Text)
    product3_ai_suggested_euro = db.Column(db.String(255))