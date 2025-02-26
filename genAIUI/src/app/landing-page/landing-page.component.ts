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
      this.router.navigate(['/image-generator']);
    } else {
      alert('Exercise 1 is not implemented yet.');
    }
  }
}
