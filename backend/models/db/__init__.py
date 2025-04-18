from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import inspect

db = SQLAlchemy()

def create_exercise1_table():
    """Create the exercise1 table if it doesn't exist."""
    engine = db.get_engine()
    table_name = "exercise1"

    # Use the public API to check if the table exists
    inspector = inspect(engine)
    if not inspector.has_table(table_name):
        print(f"Creating table: {table_name}")
        create_table_query = """
        CREATE TABLE exercise1 (
            id SERIAL PRIMARY KEY,
            demo_name VARCHAR(255),
            demo_email VARCHAR(255),
            demo_academic VARCHAR(255),
            base_creativity_conf INT,
            base_creativity_freq VARCHAR(50),
            base_creativity_def TEXT,
            ai_used_before BOOLEAN,
            ai_tools_list TEXT,
            ai_comfort INT,
            ai_expectations TEXT,
            collab_conf INT,
            collab_role VARCHAR(50),
            collab_value TEXT,
            exp_interest TEXT,
            exp_challenges TEXT,
            exp_diff_ai_human TEXT,
            exp_bias_ai_human TEXT,
            exp_ai_biases TEXT,
            exp_user_biases TEXT,
            exp_challenge_fairness TEXT,
            exp_message_change TEXT,
            exp_improve TEXT,
            exp_satisfaction INT,
            exp_challenge INT,
            exp_creativity_boost TEXT,
            exp_enjoyment TEXT,
            exp_improvements TEXT,
            ai_helpfulness INT,
            ai_iterations INT,
            ai_strategies TEXT,
            ai_contribution VARCHAR(50),
            ai_learnings TEXT,
            collab_value_post INT,
            collab_feedback VARCHAR(50),
            collab_new_ideas TEXT,
            learn_conf_post INT,
            learn_skills TEXT,
            learn_ai_future INT,
            reflect_creativity_change TEXT,
            reflect_human_ai_role TEXT,
            reflect_future_prep TEXT,
            story TEXT,
            story_character VARCHAR(255),
            frustration TEXT,
            sadness TEXT,
            fear TEXT,
            anger TEXT,
            empathy TEXT,
            gratitude TEXT,
            protectiveness TEXT,
            serenity TEXT,
            joy TEXT,
            hope TEXT,
            friendship TEXT,
            relief TEXT,
            compassion TEXT,
            self_reflection TEXT,
            inspiration TEXT,
            story_moral TEXT,
            ai_story TEXT,
            ai_story_character VARCHAR(255),
            ai_frustration TEXT,
            ai_sadness TEXT,
            ai_fear TEXT,
            ai_anger TEXT,
            ai_empathy TEXT,
            ai_gratitude TEXT,
            ai_protectiveness TEXT,
            ai_serenity TEXT,
            ai_joy TEXT,
            ai_hope TEXT,
            ai_friendship TEXT,
            ai_relief TEXT,
            ai_compassion TEXT,
            ai_self_reflection TEXT,
            ai_inspiration TEXT,
            ai_story_moral TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """
        with engine.connect() as connection:
            connection.execute(create_table_query)
        print(f"Table {table_name} created successfully.")
    else:
        print(f"Table {table_name} already exists.")

def create_exercise2_table():
    """Create the exercise2 table if it doesn't exist."""
    engine = db.get_engine()
    table_name = "exercise2"

    # Use the public API to check if the table exists
    inspector = inspect(engine)
    if not inspector.has_table(table_name):
        print(f"Creating table: {table_name}")
        create_table_query = """
        CREATE TABLE exercise2 (
            id SERIAL PRIMARY KEY,
            pre_demo_name VARCHAR(255),
            pre_demo_email VARCHAR(255),
            pre_demo_academic VARCHAR(255),
            pre_creative_confidence INT,
            pre_creative_frequency INT,
            pre_creativity_meaning VARCHAR(255),
            pre_used_ai_tools BOOLEAN,
            pre_ai_tools_used VARCHAR(255),
            pre_ai_comfort INT,
            pre_ai_expectations VARCHAR(255),
            pre_collab_confidence INT,
            pre_collab_role VARCHAR(255),
            pre_collab_value VARCHAR(255),
            post_challenges_faced VARCHAR(255),
            post_most_engaging_part VARCHAR(255),
            post_most_difficult_part VARCHAR(255),
            post_ai_impact VARCHAR(255),
            post_revised_after_ai BOOLEAN,
            post_revision_type VARCHAR(255),
            post_influenced_by_group VARCHAR(255),
            post_stuck_with_first_idea VARCHAR(255),
            post_ai_feedback_response VARCHAR(255),
            post_ai_made_more_appealing VARCHAR(255),
            post_description_influence VARCHAR(255),
            post_resistance_reason VARCHAR(255),
            post_familiarity_vs_innovation VARCHAR(255),
            post_ai_reinforce_or_challenge VARCHAR(255),
            post_experience_satisfaction INT,
            post_exercise_difficulty INT,
            post_creativity_boosted BOOLEAN,
            post_exercise_enjoyment VARCHAR(255),
            post_exercise_improvements VARCHAR(255),
            post_ai_helpfulness INT,
            post_ai_modification_count INT,
            post_ai_refinement_strategy VARCHAR(255),
            post_final_output_contribution VARCHAR(255),
            post_ai_learning VARCHAR(255),
            post_peer_collab_value INT,
            post_peer_feedback_frequency INT,
            post_peer_collab_insight TEXT,
            post_confidence_after INT,
            post_skills_gained VARCHAR(255),
            post_future_ai_use_likelihood INT,
            post_confidence_change VARCHAR(255),
            post_ai_role VARCHAR(255),
            post_creative_challenges_preparation VARCHAR(255),
            sketch_upload_path_before VARCHAR(255),
            sketch_upload_path_after VARCHAR(255),
            ai_image_path VARCHAR(255),
            product1_name VARCHAR(255),
            product1_description TEXT,
            product1_suggested_euro VARCHAR(255),
            product2_name VARCHAR(255),
            product2_description TEXT,
            product2_suggested_euro VARCHAR(255),
            product3_name VARCHAR(255),
            product3_description TEXT,
            product3_suggested_euro VARCHAR(255),
            product1_ai_name VARCHAR(255),
            product1_ai_description TEXT,
            product1_ai_suggested_euro VARCHAR(255),
            product2_ai_name VARCHAR(255),
            product2_ai_description TEXT,
            product2_ai_suggested_euro VARCHAR(255),
            product3_ai_name VARCHAR(255),
            product3_ai_description TEXT,
            product3_ai_suggested_euro VARCHAR(255)
        );
        """
        with engine.connect() as connection:
            connection.execute(create_table_query)
        print(f"Table {table_name} created successfully.")
    else:
        print(f"Table {table_name} already exists.")