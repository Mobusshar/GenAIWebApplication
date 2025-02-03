import { Component } from '@angular/core';
import { ImageService } from '../services/image.service';

@Component({
  selector: 'app-image-generator',
  templateUrl: './image-generator.component.html',
  styleUrls: ['./image-generator.component.scss']
})
export class ImageGeneratorComponent {
  prompt: string = '';
  images: string[] = [];

  constructor(private imageService: ImageService) {}

  generateImage() {
    this.imageService.generateImage(this.prompt).subscribe(response => {
      this.images.push(response.image_url);
    });
  }
}
