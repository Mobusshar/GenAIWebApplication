import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { ActivatedRoute, Router } from '@angular/router';
import { environment } from '../../environments/environment';

@Component({
  selector: 'app-text-generator',
  templateUrl: './text-generator.component.html',
  styleUrls: ['./text-generator.component.css']
})
export class TextGeneratorComponent {
  id: number = 0;
  name: string = '';
  email: string = '';
  studentid: string = '';
  prompt: string = '';
  response: string = '';
  private apiUrl = environment.apiUrl;

  constructor(private http: HttpClient, private router: Router, private route: ActivatedRoute) {}

  ngOnInit(): void {
    this.id = +this.route.snapshot.paramMap.get('id')!;
    console.log('Received ID:', this.id);
    // Add your logic to handle the ID and fetch data if necessary
  }

  sendMessage() {
    if (!this.prompt.trim()) {
      alert("Please enter a prompt.");
      return;
    }

    console.log("Sending API request...");

    const requestPayload = { 
      name: this.name,
      email: this.email,
      studentid: this.studentid,
      prompt: this.prompt 
    }; // Prepare the request payload with the additional fields

    // Send POST request to Flask backend
    this.http.post<{ response: string }>(`${this.apiUrl}/chat`, requestPayload)
      .subscribe(
        response => {
          console.log("API Response:", response); 
          this.response = response.response;
        },
        error => {
          console.error("API Error:", error); // Log any error response from the API
          alert(`Error: ${error?.error?.error || 'Something went wrong while generating the response'}`);
        }
      );
  }

  navigateToSubmitExercise1() {
    this.router.navigate(['/submit-exercise1', this.id]);
  }
}
