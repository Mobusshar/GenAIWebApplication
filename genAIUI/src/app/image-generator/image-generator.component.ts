import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-image-generator',
  templateUrl: './image-generator.component.html',
  styleUrls: ['./image-generator.component.css']
})
export class ImageGeneratorComponent {
  prompt: string = ''; // Store prompt input
  images: string[] = []; // Initialize an empty array for images

  constructor(private http: HttpClient) {}

  generateImage() {
    console.log("Sending API request...");  // Debugging
    this.http.post<{ image_url: string }>('http://127.0.0.1:5000/generate', { prompt: this.prompt })
      .subscribe(
        response => {
          console.log("API Response:", response);  // Debugging
          this.images.push(response.image_url); // Add new image to list
        },
        error => {
          console.error("API Error:", error);
        }
      );
  }
}
