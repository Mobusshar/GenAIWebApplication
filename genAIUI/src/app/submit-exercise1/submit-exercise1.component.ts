import { Component } from '@angular/core';

@Component({
  selector: 'app-submit-exercise1',
  templateUrl: './submit-exercise1.component.html',
  styleUrls: ['./submit-exercise1.component.css']
})
export class SubmitExercise1Component {
  submitExercise1() {
    alert('Exercise 1 submitted!');
  }
}
