import { Component } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-text-generator',
  templateUrl: './text-generator.component.html',
  styleUrls: ['./text-generator.component.css']
})
export class TextGeneratorComponent {
  constructor(private router: Router) {}

  navigateToSubmitExercise1() {
    this.router.navigate(['/submit-exercise1']);
  }
}
