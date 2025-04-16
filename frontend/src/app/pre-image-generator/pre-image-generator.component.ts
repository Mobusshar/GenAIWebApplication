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

  constructor(private router: Router, private http: HttpClient) {}

  onSubmit() {
    const requestPayload = {
      pre_demo_name: this.pre_demo_name
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
