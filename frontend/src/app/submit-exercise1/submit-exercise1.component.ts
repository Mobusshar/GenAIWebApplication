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
  exp_ai_biases: string = ''; // Concatenated AI biases
  exp_user_biases: string = ''; // Concatenated user biases
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

  // Bias options
  aiBiasOptions: string[] = [
    'May cause pessimistic thinking or resistance to new perspectives.',
    'Can lead to self-victimization and emotional exaggeration.',
    'Often irrational and exaggerated, leading to paranoia.',
    'Creates impulsive reactions and blame-shifting.',
    'Can be selective or manipulated based on personal biases.',
    'Sometimes romanticizes reality, ignoring struggles.',
    'May justify overprotective or exclusionary attitudes.',
    'Can dismiss real conflicts in favor of forced optimism.',
    'Can overlook negative realities and suppress struggles.',
    'Can lead to unrealistic expectations.',
    'Can create in-group favoritism or bias.',
    'Can downplay the severity of issues.',
    'May idealize emotions while neglecting complexities.',
    'Can become overly self-focused, losing objectivity.',
    'Can be influenced by social biases or personal agendas.'
  ];

  userBiasOptions: string[] = [...this.aiBiasOptions]; // Same options for user biases

  // Selected biases
  selectedAiBiases: string[] = [];
  selectedUserBiases: string[] = [];

  private apiUrl = environment.apiUrl;

  constructor(private http: HttpClient, private router: Router, private route: ActivatedRoute) {}

  ngOnInit(): void {
    this.id = +this.route.snapshot.paramMap.get('id')!;
    console.log('Received ID:', this.id);
    // Fetch existing data if necessary
  }

  // Handle AI Bias checkbox changes
  onAiBiasChange(event: Event, bias: string): void {
    const checkbox = event.target as HTMLInputElement;
    if (checkbox.checked) {
      this.selectedAiBiases.push(bias);
    } else {
      this.selectedAiBiases = this.selectedAiBiases.filter(item => item !== bias);
    }
  }

  // Handle User Bias checkbox changes
  onUserBiasChange(event: Event, bias: string): void {
    const checkbox = event.target as HTMLInputElement;
    if (checkbox.checked) {
      this.selectedUserBiases.push(bias);
    } else {
      this.selectedUserBiases = this.selectedUserBiases.filter(item => item !== bias);
    }
  }

  submitExercise1() {
    // Concatenate selected biases
    this.exp_ai_biases = this.selectedAiBiases.join(', ');
    this.exp_user_biases = this.selectedUserBiases.join(', ');

    const updatePayload = {
      exp_interest: this.exp_interest,
      exp_challenges: this.exp_challenges,
      exp_diff_ai_human: this.exp_diff_ai_human,
      exp_bias_ai_human: this.exp_bias_ai_human,
      exp_ai_biases: this.exp_ai_biases, // Concatenated AI biases
      exp_user_biases: this.exp_user_biases, // Concatenated user biases
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

    this.http.put(`${this.apiUrl}/exercise1/update-post-exercise1/${this.id}`, updatePayload)
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
