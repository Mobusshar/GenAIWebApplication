import { HttpClient } from '@angular/common/http';
import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { environment } from 'src/environments/environment';

@Component({
  selector: 'app-pre-image-generator',
  templateUrl: './pre-image-generator.component.html',
  styleUrls: ['./pre-image-generator.component.css']
})
export class PreImageGeneratorComponent {
  pre_demo_name: string = '';
  pre_demo_email: string = '';
  pre_demo_academic: string = '';
  pre_creative_confidence: number = 0;
  pre_creative_frequency: number = 0;
  pre_creativity_meaning: string = '';
  pre_used_ai_tools: boolean = false;
  pre_ai_tools_used: string = '';
  pre_ai_comfort: number = 0;
  pre_ai_expectations: string = '';
  pre_collab_confidence: number = 0;
  pre_collab_role: string = '';
  pre_collab_value: string = '';

  constructor(private router: Router, private http: HttpClient) {}

  onSubmit() {
    const requestPayload = {
      pre_demo_name: this.pre_demo_name,
      pre_demo_email: this.pre_demo_email,
      pre_demo_academic: this.pre_demo_academic,
      pre_creative_confidence: this.pre_creative_confidence,
      pre_creative_frequency: this.pre_creative_frequency,
      pre_creativity_meaning: this.pre_creativity_meaning,
      pre_used_ai_tools: this.pre_used_ai_tools,
      pre_ai_tools_used: this.pre_ai_tools_used,
      pre_ai_comfort: this.pre_ai_comfort,
      pre_ai_expectations: this.pre_ai_expectations,
      pre_collab_confidence: this.pre_collab_confidence,
      pre_collab_role: this.pre_collab_role,
      pre_collab_value: this.pre_collab_value
    };

    console.log('Request Payload:', requestPayload); // Log the request payload

    this.http.post<{ id: number }>(`${environment.apiUrl}/exercise2/pre-exercise2`, requestPayload)
      .subscribe(
        response => {
          console.log('API Response:', response);
          if (response.id) {
            this.navigateToImageGenerator(response.id);
          }
        },
        error => {
          console.error('API Error:', error);
          alert(`Error: ${error?.error?.error || 'Something went wrong while saving the pre-exercise data'}`);
        }
      );
  }

  navigateToImageGenerator(id: number) {
    this.router.navigate(['/image-generator', id]);
  }
}
