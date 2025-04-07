import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { environment } from 'src/environments/environment';
import { ActivatedRoute, Router } from '@angular/router';

@Component({
  selector: 'app-image-generator',
  templateUrl: './image-generator.component.html',
  styleUrls: ['./image-generator.component.css']
})
export class ImageGeneratorComponent implements OnInit{
  id: number = 0;

  product1: string = '';
  product1Name: string = '';
  product1Value: number | null = null;

  product2: string = '';
  product2Name: string = '';
  product2Value: number | null = null;

  product3: string = '';
  product3Name: string = '';
  product3Value: number | null = null;

  images: string[] = [];
  uploadedImage: string | ArrayBuffer | null = null;
  generatedImage: string | null = null;
  selectedFile: File | null = null;

  constructor(private http: HttpClient, private router: Router, private route: ActivatedRoute) {}

  ngOnInit(): void {
    this.id = +this.route.snapshot.paramMap.get('id')!;
    console.log('Received ID:', this.id);
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


  navigateToSubmitExercise2(): void {
    this.router.navigate(['/submit-exercise2', this.id]);
  }

  // Handle file selection
  onFileSelected(event: Event): void {
    const input = event.target as HTMLInputElement;
    if (input.files && input.files[0]) {
      this.selectedFile = input.files[0];

      // Preview the uploaded image
      const reader = new FileReader();
      reader.onload = (e) => {
        this.uploadedImage = e.target?.result ?? null;
      };
      reader.readAsDataURL(this.selectedFile);
    }
  }

  // Upload the sketch and call the DALL-E 2 API
  uploadSketch(): void {
    if (!this.selectedFile) {
      alert('Please upload a sketched image first.');
      return;
    }

    const formData = new FormData();
    formData.append('file', this.selectedFile);

    this.http.post<{ generatedImageUrl: string }>(`${environment.apiUrl}/generate-dalle-image`, formData)
      .subscribe(
        (response) => {
          this.generatedImage = response.generatedImageUrl;
        },
        (error) => {
          console.error('Error generating AI image:', error);
          alert('Something went wrong while generating the AI image.');
        }
      );
  }
}
