import { Component } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-pre-text-generator',
  templateUrl: './pre-text-generator.component.html',
  styleUrls: ['./pre-text-generator.component.css']
})
export class PreTextGeneratorComponent {
  constructor(private router: Router) {}

  navigateToTextGenerator() {
    this.router.navigate(['/text-generator']);
  }
}
