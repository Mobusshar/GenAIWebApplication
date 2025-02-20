import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { environment } from '../../environments/environment';

@Component({
  selector: 'app-image-generator',
  templateUrl: './image-generator.component.html',
  styleUrls: ['./image-generator.component.css']
})
export class ImageGeneratorComponent implements OnInit {
  prompt: string = '';  // This will hold the user input
  images: string[] = []; // This array will store generated image URLs

  constructor(private http: HttpClient) {}

  ngOnInit() {
    this.loadImages();
  }

  generateImage() {
    if (!this.prompt.trim()) {
        alert("Please enter a prompt.");
        return;
    }

    console.log("Sending API request...");

    const requestPayload = { prompt: this.prompt }; // Prepare the request payload with the prompt

    // Send POST request to Flask backend
    this.http.post<{ image_url: string }>(`${environment.apiUrl}/generate`, requestPayload)
      .subscribe(
        response => {
          console.log("API Response:", response); 
          if (response.image_url) {
            this.images.unshift(`${environment.apiUrl}${response.image_url}`); // Add generated image URL to the beginning of the list
          }
        },
        error => {
          console.error("API Error:", error); // Log any error response from the API
          alert(`Error: ${error?.error?.error || 'Something went wrong while generating the image'}`);
        }
      );
  }

  loadImages() {
    this.http.get<string[]>(`${environment.apiUrl}/images`)
      .subscribe(
        images => {
          this.images = images.map(image => `${environment.apiUrl}${image}`);
        },
        error => {
          console.error("API Error:", error); // Log any error response from the API
        }
      );
  }

}
