DROP TABLE IF EXISTS exercise1;

CREATE TABLE exercise1 (
    id SERIAL PRIMARY KEY,

    -- Demographics & Baseline
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

    -- Collaboration & Experience
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

    -- AI-Specific Reflection
    ai_helpfulness INT,
    ai_iterations INT,
    ai_strategies TEXT,
    ai_contribution VARCHAR(50),
    ai_learnings TEXT,

    -- Post-Collab & Learning
    collab_value_post INT,
    collab_feedback VARCHAR(50),
    collab_new_ideas TEXT,
    learn_conf_post INT,
    learn_skills TEXT,
    learn_ai_future INT,

    -- Reflections
    reflect_creativity_change TEXT,
    reflect_human_ai_role TEXT,
    reflect_future_prep TEXT,

    -- Human Story Section
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

    -- AI Story Section
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

    -- Timestamp
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


select * from exercise1;

DROP TABLE IF EXISTS exercise2;

CREATE TABLE exercise2 (
    id SERIAL PRIMARY KEY,
    
    -- Pre-Exercise Demographics
    pre_demo_name VARCHAR(255),
    pre_demo_email VARCHAR(255),
    pre_demo_academic VARCHAR(255),

    -- Baseline Creativity
    pre_creative_confidence INT,
    pre_creative_frequency INT,
    pre_creativity_meaning VARCHAR(255),

    -- Familiarity with AI
    pre_used_ai_tools BOOLEAN,
    pre_ai_tools_used VARCHAR(255),
    pre_ai_comfort INT,
    pre_ai_expectations VARCHAR(255),

    -- Collaboration
    pre_collab_confidence INT,
    pre_collab_role VARCHAR(255),
    pre_collab_value VARCHAR(255),

    -- Post-Exercise Questions
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

    -- Exercise Experience
    post_experience_satisfaction INT,
    post_exercise_difficulty INT,
    post_creativity_boosted BOOLEAN,
    post_exercise_enjoyment VARCHAR(255),
    post_exercise_improvements VARCHAR(255),

    -- AI Usage
    post_ai_helpfulness INT,
    post_ai_modification_count INT,
    post_ai_refinement_strategy VARCHAR(255),
    post_final_output_contribution VARCHAR(255),
    post_ai_learning VARCHAR(255),

    -- Collaboration Reflection
    post_peer_collab_value INT,
    post_peer_feedback_frequency INT,
    post_peer_collab_insight TEXT,

    -- Learning Outcomes
    post_confidence_after INT,
    post_skills_gained VARCHAR(255),
    post_future_ai_use_likelihood INT,

    -- Reflection
    post_confidence_change VARCHAR(255),
    post_ai_role VARCHAR(255),
    post_creative_challenges_preparation VARCHAR(255),

    -- File Uploads
    sketch_upload_path_before VARCHAR(255),
    sketch_upload_path_after VARCHAR(255),
    ai_image_path VARCHAR(255),

    -- Product 1 Original
    product1_name VARCHAR(255),
    product1_description TEXT,
    product1_suggested_euro VARCHAR(255),

    -- Product 2 Original
    product2_name VARCHAR(255),
    product2_description TEXT,
    product2_suggested_euro VARCHAR(255),

    -- Product 3 Original
    product3_name VARCHAR(255),
    product3_description TEXT,
    product3_suggested_euro VARCHAR(255),

    -- Product 1 AI-Generated
    product1_ai_name VARCHAR(255),
    product1_ai_description TEXT,
    product1_ai_suggested_euro VARCHAR(255),

    -- Product 2 AI-Generated
    product2_ai_name VARCHAR(255),
    product2_ai_description TEXT,
    product2_ai_suggested_euro VARCHAR(255),

    -- Product 3 AI-Generated
    product3_ai_name VARCHAR(255),
    product3_ai_description TEXT,
    product3_ai_suggested_euro VARCHAR(255)
);

select * from exercise2;