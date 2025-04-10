import { Component } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-landing-page',
  templateUrl: './landing-page.component.html',
  styleUrls: ['./landing-page.component.css']
})
export class LandingPageComponent {
  constructor(private router: Router) {}

  navigateToExercise(exercise: number) {
    if (exercise === 2) {
      this.router.navigate(['/pre-image-generator']);
    } else if (exercise === 1) {
      this.router.navigate(['/pre-text-generator']);
    } else {
      alert('Exercise not implemented yet.');
    }
  }

  navigateToGenerativeAITools(): void {
    this.router.navigate(['/generative-ai-tools']); // Replace with the actual route for the Generative AI Tools page
  }
}
