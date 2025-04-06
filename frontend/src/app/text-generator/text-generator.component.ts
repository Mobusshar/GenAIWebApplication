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
  response: string = "";
  story_character: string = '';
  
  //ai_story_moral = 'Kindness is a reward';
  //ai_story_character = 'John';
  //ai_frustration = 'Frustration grew as the day went on.';
  //ai_sadness = 'Sadness overwhelmed him.';
  //ai_fear = 'Fear gripped him as he thought about losing his job.';
  //ai_anger = 'Anger erupted in his chest.';
  //ai_empathy = 'Empathy tugged at his heart.';
  //ai_gratitude = 'Gratitude filled her eyes.';
  //ai_protectiveness = 'He felt a sense of protectiveness.';
  //ai_serenity = 'Serenity washed over him.';
  //ai_joy = 'Joy filled his heart.';
  //ai_hope = 'Hope lit up his path.';
  //ai_friendship = 'Friendship blossomed in the workplace.';
  //ai_relief = 'Relief flooded his chest.';
  //ai_compassion = 'Compassion grew within him.';
  //ai_self_reflection = 'He reflected deeply on his experiences.';
  //ai_inspiration = 'Inspiration spread throughout the community.';


  // AI Story Variables
  ai_story_moral = '';
  ai_story_character = '';
  ai_frustration = '';
  ai_sadness = '';
  ai_fear = '';
  ai_anger = '';
  ai_empathy = '';
  ai_gratitude = '';
  ai_protectiveness = '';
  ai_serenity = '';
  ai_joy = '';
  ai_hope = '';
  ai_friendship = '';
  ai_relief = '';
  ai_compassion = '';
  ai_self_reflection = '';
  ai_inspiration = '';


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


  // Method to generate AI story
  generateAIStory() {
    this.http.get<any>(`${this.apiUrl}/exercise1/generate-ai-story`).subscribe(
      (response) => {
        // Update AI story variables with the response
        this.ai_story_moral = response.ai_story_moral;
        this.ai_story_character = response.ai_story_character;
        this.ai_frustration = response.ai_frustration;
        this.ai_sadness = response.ai_sadness;
        this.ai_fear = response.ai_fear;
        this.ai_anger = response.ai_anger;
        this.ai_empathy = response.ai_empathy;
        this.ai_gratitude = response.ai_gratitude;
        this.ai_protectiveness = response.ai_protectiveness;
        this.ai_serenity = response.ai_serenity;
        this.ai_joy = response.ai_joy;
        this.ai_hope = response.ai_hope;
        this.ai_friendship = response.ai_friendship;
        this.ai_relief = response.ai_relief;
        this.ai_compassion = response.ai_compassion;
        this.ai_self_reflection = response.ai_self_reflection;
        this.ai_inspiration = response.ai_inspiration;
      },
      (error) => {
        console.error('Error generating AI story:', error);
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

  navigateBack() {
    this.router.navigate(['/story-building', this.id]);
  }
  
  navigateToSubmitExercise1() {
    this.router.navigate(['/submit-exercise1', this.id]);
  }
}
