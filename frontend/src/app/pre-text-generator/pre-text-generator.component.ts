import { HttpClient } from '@angular/common/http';
import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { environment } from 'src/environments/environment';

@Component({
  selector: 'app-pre-text-generator',
  templateUrl: './pre-text-generator.component.html',
  styleUrls: ['./pre-text-generator.component.css']
})
export class PreTextGeneratorComponent {
  demo_name: string = '';
  demo_email: string = '';
  demo_academic: string = '';
  other_academic: string = ''; // For custom academic background
  isOtherAcademic: boolean = false; // Flag to show/hide "Other" input for academic background
  base_creativity_def: string = '';
  other_creativity: string = ''; // For custom creativity definition
  isOtherCreativity: boolean = false; // Flag to show/hide "Other" input for creativity definition
  base_creativity_conf: number = 0;
  base_creativity_freq: string = '';
  ai_used_before: boolean = false;
  ai_tools_list: string = '';
  ai_comfort: number = 0;
  ai_expectations: string = '';
  other_ai_expectations: string = ''; // For custom AI expectations
  isOtherAIExpectations: boolean = false; // Flag to show/hide "Other" input for AI expectations
  collab_conf: number = 0;
  collab_role: string = '';
  other_collab_role: string = ''; // For custom group work role
  isOtherCollabRole: boolean = false; // Flag to show/hide "Other" input for group work role
  collab_value: string = '';
  other_collab_value: string = ''; // For custom value of collaboration
  isOtherCollabValue: boolean = false; // Flag to show/hide "Other" input for value of collaboration

  constructor(private router: Router, private http: HttpClient) {}

  // Handle changes in the academic background dropdown
  onAcademicChange(event: Event): void {
    const selectedValue = (event.target as HTMLSelectElement).value;
    this.isOtherAcademic = selectedValue === 'Other';

    // Reset the academic background if "Other" is selected
    if (this.isOtherAcademic) {
      this.demo_academic = 'Other';
    }
  }

  // Update the academic background when "Other" input is provided
  updateAcademicBackground(): void {
    if (this.isOtherAcademic) {
      this.demo_academic = `Other - ${this.other_academic}`;
    }
  }

  // Handle changes in the creativity dropdown
  onCreativityChange(event: Event): void {
    const selectedValue = (event.target as HTMLSelectElement).value;
    this.isOtherCreativity = selectedValue === 'Other';

    // Reset the creativity definition if "Other" is selected
    if (this.isOtherCreativity) {
      this.base_creativity_def = 'Other';
    }
  }

  // Update the creativity definition when "Other" input is provided
  updateCreativityDefinition(): void {
    if (this.isOtherCreativity) {
      this.base_creativity_def = `Other - ${this.other_creativity}`;
    }
  }

  // Handle changes in the AI expectations dropdown
  onAIExpectationsChange(event: Event): void {
    const selectedValue = (event.target as HTMLSelectElement).value;
    this.isOtherAIExpectations = selectedValue === 'Other';

    // Reset the AI expectations if "Other" is selected
    if (this.isOtherAIExpectations) {
      this.ai_expectations = 'Other';
    }
  }

  // Update the AI expectations when "Other" input is provided
  updateAIExpectations(): void {
    if (this.isOtherAIExpectations) {
      this.ai_expectations = `Other - ${this.other_ai_expectations}`;
    }
  }

  // Handle changes in the group work role dropdown
  onCollabRoleChange(event: Event): void {
    const selectedValue = (event.target as HTMLSelectElement).value;
    this.isOtherCollabRole = selectedValue === 'Other';

    // Reset the group work role if "Other" is selected
    if (this.isOtherCollabRole) {
      this.collab_role = 'Other';
    }
  }

  // Update the group work role when "Other" input is provided
  updateCollabRole(): void {
    if (this.isOtherCollabRole) {
      this.collab_role = `Other - ${this.other_collab_role}`;
    }
  }

  // Handle changes in the value of collaboration dropdown
  onCollabValueChange(event: Event): void {
    const selectedValue = (event.target as HTMLSelectElement).value;
    this.isOtherCollabValue = selectedValue === 'Other';

    // Reset the value of collaboration if "Other" is selected
    if (this.isOtherCollabValue) {
      this.collab_value = 'Other';
    }
  }

  // Update the value of collaboration when "Other" input is provided
  updateCollabValue(): void {
    if (this.isOtherCollabValue) {
      this.collab_value = `Other - ${this.other_collab_value}`;
    }
  }

  // Validate all required fields before submission
  isFormValid(): boolean {
    return (
      this.demo_name.trim() !== '' &&
      this.demo_email.trim() !== '' &&
      this.demo_academic.trim() !== '' &&
      (!this.isOtherAcademic || this.other_academic.trim() !== '') &&
      this.base_creativity_def.trim() !== '' &&
      (!this.isOtherCreativity || this.other_creativity.trim() !== '') &&
      this.base_creativity_conf > 0 &&
      this.base_creativity_freq.trim() !== '' &&
      this.ai_comfort > 0 && // Validate AI comfort
      this.ai_expectations.trim() !== '' &&
      (!this.isOtherAIExpectations || this.other_ai_expectations.trim() !== '') &&
      this.collab_conf > 0 && // Validate collaboration confidence
      this.collab_role.trim() !== '' &&
      (!this.isOtherCollabRole || this.other_collab_role.trim() !== '') &&
      this.collab_value.trim() !== '' &&
      (!this.isOtherCollabValue || this.other_collab_value.trim() !== '')
    );
  }

  onSubmit() {
    if (!this.isFormValid()) {
      alert('Please fill out all required fields before proceeding.');
      return;
    }

    const requestPayload = {
      demo_name: this.demo_name,
      demo_email: this.demo_email,
      demo_academic: this.demo_academic,
      base_creativity_def: this.base_creativity_def,
      base_creativity_conf: this.base_creativity_conf,
      base_creativity_freq: this.base_creativity_freq,
      ai_used_before: this.ai_used_before,
      ai_tools_list: this.ai_tools_list,
      ai_comfort: this.ai_comfort,
      ai_expectations: this.ai_expectations,
      collab_conf: this.collab_conf,
      collab_role: this.collab_role,
      collab_value: this.collab_value
    };

    console.log('Request Payload:', requestPayload); // Log the request payload

    this.http.post<{ id: number }>(`${environment.apiUrl}/exercise1/save-pre-text`, requestPayload)
      .subscribe(
        response => {
          console.log('API Response:', response);
          if (response.id) {
            this.navigateToStoryBuilding(response.id);
          }
        },
        error => {
          console.error('API Error:', error);
          alert(`Error: ${error?.error?.error || 'Something went wrong while saving the pre-text data'}`);
        }
      );
  }

  navigateToStoryBuilding(id: number) {
    this.router.navigate(['/story-building', id]);
  }
}
