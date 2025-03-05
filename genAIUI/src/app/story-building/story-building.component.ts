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
  story_setting: string = '';
  story_conflict: string = '';
  story_resolution: string = '';
  story_dialogue: string = '';
  story_moral: string = '';

  constructor(private route: ActivatedRoute, private router: Router, private http: HttpClient) { }

  ngOnInit(): void {
    this.id = +this.route.snapshot.paramMap.get('id')!;
    console.log('Received ID:', this.id);
    // Fetch existing data if necessary
  }

  onUpdate() {
    const updatePayload = {
      story_character: this.story_character,
      story_setting: this.story_setting,
      story_conflict: this.story_conflict,
      story_resolution: this.story_resolution,
      story_dialogue: this.story_dialogue,
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
