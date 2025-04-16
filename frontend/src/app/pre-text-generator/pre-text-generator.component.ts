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
  
  constructor(private router: Router, private http: HttpClient) {}


  // Validate all required fields before submission
  isFormValid(): boolean {
    return (
      this.demo_name.trim() !== ''
    );
  }

  onSubmit() {
    if (!this.isFormValid()) {
      alert('Please fill out all required fields before proceeding.');
      return;
    }

    const requestPayload = {
      demo_name: this.demo_name
    };

    console.log('Request Payload:', requestPayload); // Log the request payload

    this.http.post<{ id: number }>(`${environment.apiUrl}/exercise1/save-pre-text`, requestPayload)
      .subscribe(
        response => {
          console.log('API Response:', response);
          if (response.id) {
            this.navigateToStoryBuilding(response.id);
          }
        },
        error => {
          console.error('API Error:', error);
          alert(`Error: ${error?.error?.error || 'Something went wrong while saving the pre-text data'}`);
        }
      );
  }

  navigateToStoryBuilding(id: number) {
    this.router.navigate(['/story-building', id]);
  }
}
