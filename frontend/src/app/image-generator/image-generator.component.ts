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
  finalSketchFile: File | null = null;

  constructor(private http: HttpClient, private router: Router, private route: ActivatedRoute) {}

  ngOnInit(): void {
    this.id = +this.route.snapshot.paramMap.get('id')!;
    console.log('Received ID:', this.id);
  }

  // Method to handle file selection
  onFileSelected(event: Event): void {
    const input = event.target as HTMLInputElement;
    if (input.files && input.files[0]) {
      this.selectedFile = input.files[0];
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

    this.http.put<{ filePath: string }>(`${environment.apiUrl}/exercise2/upload-sketch/${this.id}`, formData)
      .subscribe(
        (response) => {
          this.sketch_upload_path_before = response.filePath; // Save the file path returned by the backend
          alert('Sketch uploaded and updated successfully.');
        },
        (error) => {
          console.error('Error uploading sketch:', error);
          alert('Something went wrong while uploading the sketch.');
        }
      );
  }

  // Handle file selection for the final sketch
  onFinalSketchSelected(event: Event): void {
    const input = event.target as HTMLInputElement;
    if (input.files && input.files[0]) {
      this.finalSketchFile = input.files[0];
    }
  }

  // Method to generate the AI image
  generateAIImage(): void {
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
          this.ai_image_path = response.generatedImageUrl; // Save the AI image path
          alert('AI image generated successfully.');
        },
        (error) => {
          console.error('Error generating AI image:', error);
          alert('Something went wrong while generating the AI image.');
        }
      );
  }

  // Method to generate AI image with product data and update the fields
  generateAIImageWithProducts(): void {
    const payload = {
      id: this.id, // Include the ID to update the existing record
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

          alert('AI image and product data updated successfully.');
        },
        (error) => {
          console.error('Error updating AI image and product data:', error);
          alert('Something went wrong while updating the AI image and product data.');
        }
      );
  }

  // Upload the final sketch
  uploadFinalSketch(): void {
    if (!this.finalSketchFile) {
      alert('Please select a file to upload.');
      return;
    }

    const formData = new FormData();
    formData.append('file', this.finalSketchFile);

    // Use the `id` to specify which record to update
    this.http.put<{ filePath: string }>(`${environment.apiUrl}/exercise2/upload-final-sketch/${this.id}`, formData)
      .subscribe(
        (response) => {
          this.sketch_upload_path_after = response.filePath; // Save the file path returned by the backend
          alert('Final sketch uploaded and updated successfully.');
        },
        (error) => {
          console.error('Error uploading final sketch:', error);
          alert('Something went wrong while uploading the final sketch.');
        }
      );
  }

  // Save all data to the backend
  updateExercise2(): void {
    const payload = {
      id: this.id,
      sketch_upload_path_before: this.sketch_upload_path_before,
      sketch_upload_path_after: this.sketch_upload_path_after,
      ai_image_path: this.ai_image_path,
      product1_name: this.product1_name,
      product1_description: this.product1_description,
      product1_suggested_euro: this.product1_suggested_euro,
      product2_name: this.product2_name,
      product2_description: this.product2_description,
      product2_suggested_euro: this.product2_suggested_euro,
      product3_name: this.product3_name,
      product3_description: this.product3_description,
      product3_suggested_euro: this.product3_suggested_euro,
      product1_ai_name: this.product1_ai_name,
      product1_ai_description: this.product1_ai_description,
      product1_ai_suggested_euro: this.product1_ai_suggested_euro,
      product2_ai_name: this.product2_ai_name,
      product2_ai_description: this.product2_ai_description,
      product2_ai_suggested_euro: this.product2_ai_suggested_euro,
      product3_ai_name: this.product3_ai_name,
      product3_ai_description: this.product3_ai_description,
      product3_ai_suggested_euro: this.product3_ai_suggested_euro
    };

    this.http.put(`${environment.apiUrl}/exercise2/update`, payload)
      .subscribe(
        () => {
          alert('Exercise 2 data updated successfully.');
          this.navigateToImageGenerator2();
        },
        (error) => {
          console.error('Error updating Exercise 2:', error);
          alert('Something went wrong while updating Exercise 2.');
        }
      );
  }

  // Navigate to Image Generator 2
  navigateToImageGenerator2(): void {
    this.router.navigate(['/image-generator-2', this.id]);
  }
}
