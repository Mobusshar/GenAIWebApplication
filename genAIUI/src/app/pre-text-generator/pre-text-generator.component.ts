import { HttpClient } from '@angular/common/http';
import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { environment } from 'src/environments/environment';

@Component({
  selector: 'app-pre-text-generator',
  templateUrl: './pre-text-generator.component.html',
  styleUrls: ['./pre-text-generator.component.css']
})
export class PreTextGeneratorComponent {
  demo_name: string = '';
  demo_email: string = '';
  demo_academic: string = '';
  base_creativity_conf: number = 0;
  base_creativity_freq: string = '';
  base_creativity_def: string = '';
  ai_used_before: boolean = false;
  ai_tools_list: string = '';
  ai_comfort: number = 0;
  ai_expectations: string = '';
  collab_conf: number = 0;
  collab_role: string = '';
  collab_value: string = '';
  exp_interest: string = '';
  exp_challenges: string = '';
  exp_diff_ai_human: string = '';
  exp_bias_ai_human: string = '';
  exp_challenge_fairness: string = '';
  exp_message_change: string = '';
  exp_improve: string = '';
  exp_satisfaction: number = 0;
  exp_challenge: number = 0;
  exp_creativity_boost: string = '';
  exp_enjoyment: string = '';
  exp_improvements: string = '';
  ai_helpfulness: number = 0;
  ai_iterations: number = 0;
  ai_strategies: string = '';
  ai_contribution: string = '';
  ai_learnings: string = '';
  collab_value_post: number = 0;
  collab_feedback: string = '';
  collab_new_ideas: string = '';
  learn_conf_post: number = 0;
  learn_skills: string = '';
  learn_ai_future: number = 0;
  reflect_creativity_change: string = '';
  reflect_human_ai_role: string = '';
  reflect_future_prep: string = '';
  story_character: string = '';
  story_setting: string = '';
  story_conflict: string = '';
  story_resolution: string = '';
  story_dialogue: string = '';
  story_moral: string = '';

  constructor(private router: Router, private http: HttpClient) {}

  onSubmit() {
    const requestPayload = {
      demo_name: this.demo_name,
      demo_email: this.demo_email,
      demo_academic: this.demo_academic,
      base_creativity_conf: this.base_creativity_conf,
      base_creativity_freq: this.base_creativity_freq,
      base_creativity_def: this.base_creativity_def,
      ai_used_before: this.ai_used_before,
      ai_tools_list: this.ai_tools_list,
      ai_comfort: this.ai_comfort,
      ai_expectations: this.ai_expectations,
      collab_conf: this.collab_conf,
      collab_role: this.collab_role,
      collab_value: this.collab_value,
      exp_interest: this.exp_interest,
      exp_challenges: this.exp_challenges,
      exp_diff_ai_human: this.exp_diff_ai_human,
      exp_bias_ai_human: this.exp_bias_ai_human,
      exp_challenge_fairness: this.exp_challenge_fairness,
      exp_message_change: this.exp_message_change,
      exp_improve: this.exp_improve,
      exp_satisfaction: this.exp_satisfaction,
      exp_challenge: this.exp_challenge,
      exp_creativity_boost: this.exp_creativity_boost,
      exp_enjoyment: this.exp_enjoyment,
      exp_improvements: this.exp_improvements,
      ai_helpfulness: this.ai_helpfulness,
      ai_iterations: this.ai_iterations,
      ai_strategies: this.ai_strategies,
      ai_contribution: this.ai_contribution,
      ai_learnings: this.ai_learnings,
      collab_value_post: this.collab_value_post,
      collab_feedback: this.collab_feedback,
      collab_new_ideas: this.collab_new_ideas,
      learn_conf_post: this.learn_conf_post,
      learn_skills: this.learn_skills,
      learn_ai_future: this.learn_ai_future,
      reflect_creativity_change: this.reflect_creativity_change,
      reflect_human_ai_role: this.reflect_human_ai_role,
      reflect_future_prep: this.reflect_future_prep,
      story_character: this.story_character,
      story_setting: this.story_setting,
      story_conflict: this.story_conflict,
      story_resolution: this.story_resolution,
      story_dialogue: this.story_dialogue,
      story_moral: this.story_moral
    };

    console.log('Request Payload:', requestPayload); // Log the request payload

    this.http.post<{ id: number }>(`${environment.apiUrl}/save-pre-text`, requestPayload)
      .subscribe(
        response => {
          console.log('API Response:', response);
          if (response.id) {
            this.navigateToTextGenerator(response.id);
          }
        },
        error => {
          console.error('API Error:', error);
          alert(`Error: ${error?.error?.error || 'Something went wrong while saving the pre-text data'}`);
        }
      );
  }

  navigateToTextGenerator(id: number) {
    this.router.navigate(['/text-generator', id]);
  }
}
