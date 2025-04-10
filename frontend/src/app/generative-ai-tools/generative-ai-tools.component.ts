import { Component } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-generative-ai-tools',
  templateUrl: './generative-ai-tools.component.html',
  styleUrls: ['./generative-ai-tools.component.css']
})
export class GenerativeAIToolsComponent {
  constructor(private router: Router) {}

  navigateToTool(tool: string): void {
    this.router.navigate([`/tools/${tool}`]); // Replace with actual routes for each tool
  }
}
