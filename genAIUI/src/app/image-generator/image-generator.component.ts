import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-image-generator',
  templateUrl: './image-generator.component.html',
  styleUrls: ['./image-generator.component.css']
})
export class ImageGeneratorComponent {
  prompt: string = '';  
  images: string[] = []; 

  constructor(private http: HttpClient) {}

  generateImage() {
    if (!this.prompt) return;

    this.http.post<{ image_url: string }>("http://127.0.0.1:5000/generate", { prompt: this.prompt })
      .subscribe(response => {
        this.images.push(response.image_url); 
        this.prompt = ''; 
      }, error => {
        console.error("Error generating image:", error);
      });
  }
}
