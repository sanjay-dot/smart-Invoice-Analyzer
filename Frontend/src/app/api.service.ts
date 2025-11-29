import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders, HttpParams } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class ApiService {
  private readonly baseUrl = 'http://localhost:5000/api/v1';

  constructor(private http: HttpClient) {}

  /**
   * Upload a file to the Python backend.
   * @param file The file to be uploaded.
   * @returns Observable<any>
   */
  uploadFile(file: File): Observable<any> {
    const formData = new FormData();
    formData.append('file', file);

    return this.http.post(`${this.baseUrl}/invoices-upload`, formData, {
      reportProgress: true,
      observe: 'events',
    });
  }

  /**
   * Fetch the list of uploaded files from the Python backend.
   * @returns Observable<any>
   */
  getUploadedFiles(): Observable<any> {
    return this.http.get(`${this.baseUrl}/files`);
  }

  /**
   * Delete a file by its ID.
   * @param fileId The ID of the file to delete.
   * @returns Observable<any>
   */
  deleteFile(fileId: string): Observable<any> {
    return this.http.delete(`${this.baseUrl}/files/${fileId}`);
  }
}
