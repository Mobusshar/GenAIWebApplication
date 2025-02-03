import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ImageService {
  private apiUrl = 'http://127.0.0.1:5000/generate';

  constructor(private http: HttpClient) {}

  generateImage(prompt: string): Observable<any> {
    return this.http.post<any>(this.apiUrl, { prompt });
  }
}
