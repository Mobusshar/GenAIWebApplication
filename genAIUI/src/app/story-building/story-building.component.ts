import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { HttpClient } from '@angular/common/http';
import { environment } from 'src/environments/environment';

@Component({
  selector: 'app-story-building',
  templateUrl: './story-building.component.html',
  styleUrls: ['./story-building.component.css']
})
export class StoryBuildingComponent implements OnInit {
  id: number = 0;
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

  constructor(private route: ActivatedRoute, private router: Router, private http: HttpClient) { }

  ngOnInit(): void {
    this.id = +this.route.snapshot.paramMap.get('id')!;
    console.log('Received ID:', this.id);
    this.fetchStoryData();
  }

  fetchStoryData() {
    this.http.get<any>(`${environment.apiUrl}/get-story/${this.id}`)
      .subscribe(
        data => {
          if (data) {
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
          } else {
            console.log("No existing story data found.");
          }
        },
        error => {
          console.error("API Error:", error);
          alert(`Error: ${error?.error?.error || 'Something went wrong while fetching the story data'}`);
        }
      );
  }

  onUpdate() {
    const updatePayload = {
      story_character: this.story_character,
      frustration: this.frustration,
      sadness: this.sadness,
      fear: this.fear,
      anger: this.anger,
      empathy: this.empathy,
      gratitude: this.gratitude,
      protectiveness: this.protectiveness,
      serenity: this.serenity,
      joy: this.joy,
      hope: this.hope,
      friendship: this.friendship,
      relief: this.relief,
      compassion: this.compassion,
      self_reflection: this.self_reflection,
      inspiration: this.inspiration,
      story_moral: this.story_moral
    };

    console.log('Update Payload:', updatePayload); // Log the update payload

    this.http.put(`${environment.apiUrl}/update-story/${this.id}`, updatePayload)
      .subscribe(
        response => {
          console.log('API Response:', response);
          alert('Story updated successfully');
          this.navigateToTextGenerator(this.id); // Navigate to text generator page with the ID
        },
        error => {
          console.error('API Error:', error);
          alert(`Error: ${error?.error?.error || 'Something went wrong while updating the story'}`);
        }
      );
  }

  navigateToTextGenerator(id: number) {
    this.router.navigate(['/text-generator', id]);
  }
}
