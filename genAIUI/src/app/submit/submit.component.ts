import { Component, OnInit } from '@angular/core';
import { DataService } from '../shared/data.service';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-submit',
  templateUrl: './submit.component.html',
  styleUrls: ['./submit.component.css']
})
export class SubmitComponent implements OnInit {
  formData: any = {
    poq1: '',
    poq2: '',
    poq3: '',
    poq4: '',
    poq5: ''
  };

  constructor(private dataService: DataService, private http: HttpClient) {}

  ngOnInit() {
    this.formData = { ...this.dataService.getFormData(), ...this.formData };
  }

  submitForm() {
    this.http.post('/api/generate', this.formData).subscribe(response => {
      console.log('Form submitted successfully', response);
    }, error => {
      console.error('Error submitting form', error);
    });
  }
}
