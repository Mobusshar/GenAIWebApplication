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
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """
        with engine.connect() as connection:
            connection.execute(create_table_query)
        print(f"Table {table_name} created successfully.")
    else:
        print(f"Table {table_name} already exists.")