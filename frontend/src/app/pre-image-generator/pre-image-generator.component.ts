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
      collab_value: this.collab_value
    };

    console.log('Request Payload:', requestPayload); // Log the request payload

    this.http.post<{ id: number }>(`${environment.apiUrl}/exercise1/save-pre-text`, requestPayload)
      .subscribe(
        response => {
          console.log('API Response:', response);
          if (response.id) {
            this.navigateToImageGenerator(response.id);
          }
        },
        error => {
          console.error('API Error:', error);
          alert(`Error: ${error?.error?.error || 'Something went wrong while saving the pre-text data'}`);
        }
      );
  }

  navigateToImageGenerator(id: number) {
    this.router.navigate(['/image-generator', id]);
  }
}
