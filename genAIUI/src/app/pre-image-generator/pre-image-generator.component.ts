import { Component } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-pre-image-generator',
  templateUrl: './pre-image-generator.component.html',
  styleUrls: ['./pre-image-generator.component.css']
})
export class PreImageGeneratorComponent {
  constructor(private router: Router) {}

  navigateToImageGenerator() {
    this.router.navigate(['/image-generator']);
  }
}
