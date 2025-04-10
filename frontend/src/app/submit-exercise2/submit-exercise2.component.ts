import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { HttpClient } from '@angular/common/http';
import { environment } from 'src/environments/environment';

@Component({
  selector: 'app-submit-exercise2',
  templateUrl: './submit-exercise2.component.html',
  styleUrls: ['./submit-exercise2.component.css']
})
export class SubmitExercise2Component implements OnInit {
  id: string = '';

  // 19 form fields
  post_challenges_faced: string = '';
  post_most_engaging_part: string = '';
  post_most_difficult_part: string = '';
  post_ai_impact: string = '';
  post_revised_after_ai: boolean | null = null;
  post_revision_type: string = '';
  post_influenced_by_group: string = '';
  post_stuck_with_first_idea: string = '';
  post_ai_feedback_response: string = '';
  post_ai_made_more_appealing: string = '';
  post_description_influence: string = '';
  post_resistance_reason: string = '';
  post_familiarity_vs_innovation: string = '';
  post_ai_reinforce_or_challenge: string = '';
  post_experience_satisfaction: number | null = null;
  post_exercise_difficulty: number | null = null;
  post_creativity_boosted: boolean | null = null;
  post_exercise_enjoyment: string = '';
  post_exercise_improvements: string = '';

  constructor(
    private route: ActivatedRoute,
    private router: Router,
    private http: HttpClient
  ) {}

  ngOnInit(): void {
    this.id = this.route.snapshot.paramMap.get('id') || '';
  }

  onSubmit(): void {
    const requestPayload = {
      post_challenges_faced: this.post_challenges_faced,
      post_most_engaging_part: this.post_most_engaging_part,
      post_most_difficult_part: this.post_most_difficult_part,
      post_ai_impact: this.post_ai_impact,
      post_revised_after_ai: this.post_revised_after_ai,
      post_revision_type: this.post_revision_type,
      post_influenced_by_group: this.post_influenced_by_group,
      post_stuck_with_first_idea: this.post_stuck_with_first_idea,
      post_ai_feedback_response: this.post_ai_feedback_response,
      post_ai_made_more_appealing: this.post_ai_made_more_appealing,
      post_description_influence: this.post_description_influence,
      post_resistance_reason: this.post_resistance_reason,
      post_familiarity_vs_innovation: this.post_familiarity_vs_innovation,
      post_ai_reinforce_or_challenge: this.post_ai_reinforce_or_challenge,
      post_experience_satisfaction: this.post_experience_satisfaction,
      post_exercise_difficulty: this.post_exercise_difficulty,
      post_creativity_boosted: this.post_creativity_boosted,
      post_exercise_enjoyment: this.post_exercise_enjoyment,
      post_exercise_improvements: this.post_exercise_improvements
    };

    this.http.put<{ message: string }>(
      `${environment.apiUrl}/exercise2/post-exercise2-1/${this.id}`,
      requestPayload
    ).subscribe(
      response => {
        console.log('API Response:', response);
        // Show an alert before navigating
        alert('Your data has been saved successfully!');
        this.router.navigate([`/submit-exercise2-final/${this.id}`]);
      },
      error => {
        console.error('API Error:', error);
        alert(`Error: ${error?.error?.message || 'Something went wrong while submitting the exercise data'}`);
      }
    );
  }
}
