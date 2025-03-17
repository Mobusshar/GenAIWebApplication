import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { ActivatedRoute, Router } from '@angular/router';
import { environment } from '../../environments/environment';

@Component({
  selector: 'app-text-generator',
  templateUrl: './text-generator.component.html',
  styleUrls: ['./text-generator.component.css']
})
export class TextGeneratorComponent implements OnInit {
  id: number = 0;
  prompt: string = '';
  response: string = 'This is a dummy response to show how the AI generated story will look like. The story will be dynamically generated based on the prompt provided by the user.';
  story_character: string = '';
  
  frustration: string = '';
  sadness: string = '';
  fear: string = '';
  anger: string = '';
  empathy: string = '';
  gratitude: string = '';
  protectiveness: string = '';
  serenity: string = '';
  joy: string = '';
  hope: string = '';
  friendship: string = '';
  relief: string = '';
  compassion: string = '';
  self_reflection: string = '';
  inspiration: string = '';
  story_moral: string = '';
  private apiUrl = environment.apiUrl;

  constructor(private http: HttpClient, private router: Router, private route: ActivatedRoute) {}

  ngOnInit(): void {
    this.id = +this.route.snapshot.paramMap.get('id')!;
    console.log('Received ID:', this.id);
    this.fetchStoryData();
  }

  fetchStoryData() {
    this.http.get<any>(`${this.apiUrl}/exercise1/get-story/${this.id}`)
      .subscribe(
        data => {
          console.log("Fetched Story Data:", data);
          this.story_character = data.story_character;
          this.frustration = data.frustration;
          this.sadness = data.sadness;
          this.fear = data.fear;
          this.anger = data.anger;
          this.empathy = data.empathy;
          this.gratitude = data.gratitude;
          this.protectiveness = data.protectiveness;
          this.serenity = data.serenity;
          this.joy = data.joy;
          this.hope = data.hope;
          this.friendship = data.friendship;
          this.relief = data.relief;
          this.compassion = data.compassion;
          this.self_reflection = data.self_reflection;
          this.inspiration = data.inspiration;
          this.story_moral = data.story_moral;
        },
        error => {
          console.error("API Error:", error);
          alert(`Error: ${error?.error?.error || 'Something went wrong while fetching the story data'}`);
        }
      );
  }

  sendMessage() {
    if (!this.prompt.trim()) {
      alert("Please enter a prompt.");
      return;
    }

    console.log("Sending API request...");

    const requestPayload = {
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
