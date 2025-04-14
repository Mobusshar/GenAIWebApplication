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
  ai_story = '';


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
  story: string = '';
  private apiUrl = environment.apiUrl;
  isLoading: boolean = false;

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

          // Map manually entered fields
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
          this.story = data.story;

          // Map AI-generated fields
          this.ai_story_character = data.ai_story_character;
          this.ai_frustration = data.ai_frustration;
          this.ai_sadness = data.ai_sadness;
          this.ai_fear = data.ai_fear;
          this.ai_anger = data.ai_anger;
          this.ai_empathy = data.ai_empathy;
          this.ai_gratitude = data.ai_gratitude;
          this.ai_protectiveness = data.ai_protectiveness;
          this.ai_serenity = data.ai_serenity;
          this.ai_joy = data.ai_joy;
          this.ai_hope = data.ai_hope;
          this.ai_friendship = data.ai_friendship;
          this.ai_relief = data.ai_relief;
          this.ai_compassion = data.ai_compassion;
          this.ai_self_reflection = data.ai_self_reflection;
          this.ai_inspiration = data.ai_inspiration;
          this.ai_story_moral = data.ai_story_moral;
          this.ai_story = data.ai_story;
        },
        error => {
          console.error("API Error:", error);
          alert(`Error: ${error?.error?.error || 'Something went wrong while fetching the story data'}`);
        }
      );
  }

  // Method to generate AI story
  generateAIStory() {
    if (!this.id) {
        alert("Invalid ID. Please ensure the ID is provided.");
        return;
    }

    this.isLoading = true; // Set loading state to true
    this.http.post<any>(`${this.apiUrl}/exercise1/generate-ai-story/${this.id}`, {}).subscribe(
        (response) => {
            console.log("Generated AI Story Response:", response);

            if (response && response.data) {
                const aiStory = response.data;

                // Update AI story variables with the response
                this.ai_story_moral = aiStory.ai_story_moral;
                this.ai_story_character = aiStory.ai_story_character;
                this.ai_frustration = aiStory.ai_frustration;
                this.ai_sadness = aiStory.ai_sadness;
                this.ai_fear = aiStory.ai_fear;
                this.ai_anger = aiStory.ai_anger;
                this.ai_empathy = aiStory.ai_empathy;
                this.ai_gratitude = aiStory.ai_gratitude;
                this.ai_protectiveness = aiStory.ai_protectiveness;
                this.ai_serenity = aiStory.ai_serenity;
                this.ai_joy = aiStory.ai_joy;
                this.ai_hope = aiStory.ai_hope;
                this.ai_friendship = aiStory.ai_friendship;
                this.ai_relief = aiStory.ai_relief;
                this.ai_compassion = aiStory.ai_compassion;
                this.ai_self_reflection = aiStory.ai_self_reflection;
                this.ai_inspiration = aiStory.ai_inspiration;
                this.ai_story = aiStory.ai_story;

                alert("AI story generated and saved successfully!");
            } else {
                console.error("Invalid response structure:", response);
                alert("Error: Invalid response structure from the server.");
            }
            this.isLoading = false; // Reset loading state
        },
        (error) => {
            console.error("Error generating AI story:", error);
            alert(`Error: ${error?.error?.error || 'Something went wrong while generating the AI story'}`);
            this.isLoading = false; // Reset loading state
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
