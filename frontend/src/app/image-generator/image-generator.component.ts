import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { environment } from 'src/environments/environment';
import { ActivatedRoute, Router } from '@angular/router';

@Component({
  selector: 'app-image-generator',
  templateUrl: './image-generator.component.html',
  styleUrls: ['./image-generator.component.css']
})
export class ImageGeneratorComponent implements OnInit {
  id: number = 0;

  // Product fields
  product1_name: string = '';
  product1_description: string = '';
  product1_suggested_euro: string = '';

  product2_name: string = '';
  product2_description: string = '';
  product2_suggested_euro: string = '';

  product3_name: string = '';
  product3_description: string = '';
  product3_suggested_euro: string = '';

  // AI-generated product fields
  product1_ai_name: string = '';
  product1_ai_description: string = '';
  product1_ai_suggested_euro: string = '';

  product2_ai_name: string = '';
  product2_ai_description: string = '';
  product2_ai_suggested_euro: string = '';

  product3_ai_name: string = '';
  product3_ai_description: string = '';
  product3_ai_suggested_euro: string = '';

  // Image paths
  sketch_upload_path_before: string | null = null;
  sketch_upload_path_after: string | null = null;
  ai_image_path: string | null = null;

  uploadedImage: string | ArrayBuffer | null = null;
  generatedImage: string | null = null;
  selectedFile: File | null = null;

  // Loading and generation state
  isLoading: boolean = false;
  isGenerated: boolean = false; // Flag to show "View Results" button

  constructor(private http: HttpClient, private router: Router, private route: ActivatedRoute) {}

  ngOnInit(): void {
    this.id = +this.route.snapshot.paramMap.get('id')!;
    console.log('Received ID:', this.id);
  }

  // Method to handle file selection and automatically upload
  onFileSelected(event: Event): void {
    const input = event.target as HTMLInputElement;
    if (input.files && input.files[0]) {
      this.selectedFile = input.files[0];
      this.uploadSketch(); // Automatically call the upload function
    }
  }

  // Method to upload the sketch and update the file name in the backend
  uploadSketch(): void {
    if (!this.selectedFile) {
      alert('Please select a file to upload.');
      return;
    }

    const formData = new FormData();
    formData.append('file', this.selectedFile);

    this.isLoading = true; // Show loading spinner

    this.http.put<{ filePath: string }>(`${environment.apiUrl}/exercise2/upload-sketch/${this.id}`, formData)
      .subscribe(
        (response) => {
          this.sketch_upload_path_before = response.filePath; // Save the file path returned by the backend
          alert('Sketch uploaded and updated successfully.');
          this.isLoading = false; // Hide loading spinner
        },
        (error) => {
          console.error('Error uploading sketch:', error);
          alert('Something went wrong while uploading the sketch.');
          this.isLoading = false; // Hide loading spinner
        }
      );
  }

  // Method to generate AI image with product data and update the fields
  generateAIImageWithProducts(): void {
    const payload = {
      id: this.id,
      product1_name: this.product1_name,
      product1_description: this.product1_description,
      product1_suggested_euro: this.product1_suggested_euro,
      product2_name: this.product2_name,
      product2_description: this.product2_description,
      product2_suggested_euro: this.product2_suggested_euro,
      product3_name: this.product3_name,
      product3_description: this.product3_description,
      product3_suggested_euro: this.product3_suggested_euro
    };

    this.isLoading = true;

    this.http.put<{
      generatedImageUrl: string,
      product1_ai_name: string,
      product1_ai_description: string,
      product1_ai_suggested_euro: string,
      product2_ai_name: string,
      product2_ai_description: string,
      product2_ai_suggested_euro: string,
      product3_ai_name: string,
      product3_ai_description: string,
      product3_ai_suggested_euro: string
    }>(`${environment.apiUrl}/exercise2/update-products/${this.id}`, payload)
      .subscribe(
        (response) => {
          // Update the AI-generated image path
          this.generatedImage = response.generatedImageUrl;
          this.ai_image_path = response.generatedImageUrl;

          // Update the AI-generated product fields
          this.product1_ai_name = response.product1_ai_name;
          this.product1_ai_description = response.product1_ai_description;
          this.product1_ai_suggested_euro = response.product1_ai_suggested_euro;

          this.product2_ai_name = response.product2_ai_name;
          this.product2_ai_description = response.product2_ai_description;
          this.product2_ai_suggested_euro = response.product2_ai_suggested_euro;

          this.product3_ai_name = response.product3_ai_name;
          this.product3_ai_description = response.product3_ai_description;
          this.product3_ai_suggested_euro = response.product3_ai_suggested_euro;

          this.isLoading = false;
          this.isGenerated = true; // Show "View Results" button
          alert('AI image and product data updated successfully.');
        },
        (error) => {
          console.error('Error:', error);
          this.isLoading = false;

          // Display specific error messages based on the backend response
          if (error.error && error.error.error) {
            alert(`Error: ${error.error.error}`);
          } else {
            alert('Something went wrong while updating the AI image and product data.');
          }
        }
      );
  }

  // Navigate to Image Generator 2
  navigateToImageGenerator2(): void {
    this.router.navigate(['/image-generator-2', this.id]);
  }
}
