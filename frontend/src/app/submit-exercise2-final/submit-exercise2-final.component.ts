import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { HttpClient } from '@angular/common/http';
import { environment } from 'src/environments/environment';

@Component({
  selector: 'app-submit-exercise2-final',
  templateUrl: './submit-exercise2-final.component.html',
  styleUrls: ['./submit-exercise2-final.component.css']
})
export class SubmitExercise2FinalComponent implements OnInit {
  id: string = '';

  // Final reflection form fields
  post_ai_helpfulness: number | null = null;
  post_ai_modification_count: number | null = null;
  post_ai_refinement_strategy: string = '';
  post_final_output_contribution: string = '';
  post_ai_learning: string = '';
  post_peer_collab_value: number | null = null;
  post_peer_feedback_frequency: number | null = null;
  post_peer_collab_insight: string = '';
  post_confidence_after: number | null = null;
  post_skills_gained: string = '';
  post_future_ai_use_likelihood: number | null = null;
  post_confidence_change: string = '';
  post_ai_role: string = '';
  post_creative_challenges_preparation: string = '';

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
      post_ai_helpfulness: this.post_ai_helpfulness,
      post_ai_modification_count: this.post_ai_modification_count,
      post_ai_refinement_strategy: this.post_ai_refinement_strategy,
      post_final_output_contribution: this.post_final_output_contribution,
      post_ai_learning: this.post_ai_learning,
      post_peer_collab_value: this.post_peer_collab_value,
      post_peer_feedback_frequency: this.post_peer_feedback_frequency,
      post_peer_collab_insight: this.post_peer_collab_insight,
      post_confidence_after: this.post_confidence_after,
      post_skills_gained: this.post_skills_gained,
      post_future_ai_use_likelihood: this.post_future_ai_use_likelihood,
      post_confidence_change: this.post_confidence_change,
      post_ai_role: this.post_ai_role,
      post_creative_challenges_preparation: this.post_creative_challenges_preparation
    };

    this.http.put<{ message: string }>(
      `${environment.apiUrl}/exercise2/post-exercise2-1/${this.id}`,
      requestPayload
    ).subscribe(
      response => {
        console.log('API Response:', response);
        // Show an alert before navigating
        alert('Your final reflection has been saved successfully!');
        this.router.navigate(['/']); // Redirect to a thank-you page or another route
      },
      error => {
        console.error('API Error:', error);
        alert(`Error: ${error?.error?.message || 'Something went wrong while submitting the final reflection data'}`);
      }
    );
  }
}
