import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { HttpClient } from '@angular/common/http';
import { environment } from '../../environments/environment';

@Component({
  selector: 'app-submit-exercise1',
  templateUrl: './submit-exercise1.component.html',
  styleUrls: ['./submit-exercise1.component.css']
})
export class SubmitExercise1Component implements OnInit {
  id: number = 0;
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

  private apiUrl = environment.apiUrl;

  constructor(private http: HttpClient, private router: Router, private route: ActivatedRoute) {}

  ngOnInit(): void {
    this.id = +this.route.snapshot.paramMap.get('id')!;
    console.log('Received ID:', this.id);
    // Fetch existing data if necessary
  }

  submitExercise1() {
    const updatePayload = {
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
      reflect_future_prep: this.reflect_future_prep
    };

    console.log('Update Payload:', updatePayload); // Log the update payload

    this.http.put(`${this.apiUrl}/update-post-exercise1/${this.id}`, updatePayload)
      .subscribe(
        response => {
          console.log('API Response:', response);
          alert('Exercise 1 submitted successfully');
            this.router.navigate(['/']); // Navigate to the homepage
        },
        error => {
          console.error('API Error:', error);
          alert(`Error: ${error?.error?.error || 'Something went wrong while submitting the exercise'}`);
        }
      );
  }
}
