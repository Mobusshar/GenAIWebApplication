import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { environment } from 'src/environments/environment';
import { ActivatedRoute, Router } from '@angular/router';

@Component({
  selector: 'app-image-generator-2',
  templateUrl: './image-generator-2.component.html',
  styleUrls: ['./image-generator-2.component.css']
})
export class ImageGenerator2Component implements OnInit {
  id: number = 0;

  // Image paths
  uploadedImage: string | null = null;
  generatedImage: string | null = null;

  // Uploaded product details
  product1_name: string = '';
  product1_description: string = '';
  product1_suggested_euro: string = '';
  product2_name: string = '';
  product2_description: string = '';
  product2_suggested_euro: string = '';
  product3_name: string = '';
  product3_description: string = '';
  product3_suggested_euro: string = '';

  // AI-generated product details
  product1_ai_name: string = '';
  product1_ai_description: string = '';
  product1_ai_suggested_euro: string = '';
  product2_ai_name: string = '';
  product2_ai_description: string = '';
  product2_ai_suggested_euro: string = '';
  product3_ai_name: string = '';
  product3_ai_description: string = '';
  product3_ai_suggested_euro: string = '';

  // Final sketch file
  finalSketchFile: File | null = null;
  sketch_upload_path_after: string | null = null;

  constructor(private http: HttpClient, private router: Router, private route: ActivatedRoute) {}

  ngOnInit(): void {
    this.id = +this.route.snapshot.paramMap.get('id')!;
    this.loadImagesAndProducts();
  }

  // Fetch images and product details
  loadImagesAndProducts(): void {
    this.http.get<any>(`${environment.apiUrl}/exercise2/get-images-and-products/${this.id}`).subscribe(
      (response) => {
        // Uploaded Data
        this.uploadedImage = `${environment.apiUrl}/exercise2${response.uploaded.sketch_upload_path_before}`;
        this.product1_name = response.uploaded.product1_name;
        this.product1_description = response.uploaded.product1_description;
        this.product1_suggested_euro = response.uploaded.product1_suggested_euro;
        this.product2_name = response.uploaded.product2_name;
        this.product2_description = response.uploaded.product2_description;
        this.product2_suggested_euro = response.uploaded.product2_suggested_euro;
        this.product3_name = response.uploaded.product3_name;
        this.product3_description = response.uploaded.product3_description;
        this.product3_suggested_euro = response.uploaded.product3_suggested_euro;

        // AI-Generated Data
        this.generatedImage = `${environment.apiUrl}/exercise2${response.generated.ai_image_path}`;
        this.product1_ai_name = response.generated.product1_ai_name;
        this.product1_ai_description = response.generated.product1_ai_description;
        this.product1_ai_suggested_euro = response.generated.product1_ai_suggested_euro;
        this.product2_ai_name = response.generated.product2_ai_name;
        this.product2_ai_description = response.generated.product2_ai_description;
        this.product2_ai_suggested_euro = response.generated.product2_ai_suggested_euro;
        this.product3_ai_name = response.generated.product3_ai_name;
        this.product3_ai_description = response.generated.product3_ai_description;
        this.product3_ai_suggested_euro = response.generated.product3_ai_suggested_euro;

        console.log('Uploaded Image Path:', this.uploadedImage);
        console.log('Generated Image Path:', this.generatedImage);
      },
      (error) => {
        console.error('Error fetching data:', error);
        alert('Something went wrong while fetching the data.');
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

  // Handle file selection for the final sketch
  onFinalSketchSelected(event: Event): void {
    const input = event.target as HTMLInputElement;
    if (input.files && input.files[0]) {
      this.finalSketchFile = input.files[0];
    }
  }

  // Navigate to the submission page
  navigateToSubmitExercise2(): void {
    this.router.navigate(['/submit-exercise2', this.id]);
  }
}
