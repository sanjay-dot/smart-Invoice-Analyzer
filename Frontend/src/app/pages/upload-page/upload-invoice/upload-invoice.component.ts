import { HttpClient, HttpEventType } from '@angular/common/http';
import { Component, ElementRef, ViewChild } from '@angular/core';
import { FormGroup, FormBuilder, Validators } from '@angular/forms';
import { ApiService } from '../../../api.service';

@Component({
  selector: 'app-upload-invoice',
  standalone: false,
  
  templateUrl: './upload-invoice.component.html',
  styleUrl: './upload-invoice.component.scss'
})
export class UploadInvoiceComponent {
  @ViewChild('fileInput') fileInput!: ElementRef<HTMLInputElement>;

  uploadForm: FormGroup; // FormControl for the file
  selectedFile: File | null = null; // To track the uploaded file
  dragging = false;
  uploadProgress: number = -1;


  constructor(private fb: FormBuilder, private http: HttpClient,private apiService: ApiService) {
    this.uploadForm = this.fb.group({
      file: [null, Validators.required],
    });
  }

  // Trigger file input's click event
  triggerFileUpload(): void {
    this.fileInput.nativeElement.click();
  }

  // Handle file selection via input
  onFileSelected(event: Event): void {
    const input = event.target as HTMLInputElement;

    if (input?.files && input.files.length > 0) {
      this.selectedFile = input.files[0];
      console.log('File selected:', this.selectedFile);
      this.uploadForm.patchValue({ file: this.selectedFile });
      this.uploadForm.get('file')?.updateValueAndValidity();
    }
  }

  // Handle drag-over event
  onDragOver(event: DragEvent): void {
    event.preventDefault();
    event.stopPropagation();
    this.dragging = true;
  }

  // Handle drag-leave event
  onDragLeave(event: DragEvent): void {
    event.preventDefault();
    event.stopPropagation();
    this.dragging = false;
  }

  // Handle file drop
  onFileDrop(event: DragEvent): void {
    event.preventDefault();
    event.stopPropagation();
    this.dragging = false;

    if (event.dataTransfer?.files && event.dataTransfer.files.length > 0) {
      this.selectedFile = event.dataTransfer.files[0];
      console.log('File dropped:', this.selectedFile);

      // Update FormControl with the dropped file
      this.uploadForm.patchValue({ file: this.selectedFile });
      this.uploadForm.get('file')?.updateValueAndValidity();
    }
  }

  // Remove the selected file
  removeFile(): void {
    this.selectedFile = null;
    this.uploadForm.patchValue({ file: null });
    this.uploadForm.get('file')?.updateValueAndValidity();
    console.log('File removed.');
  }
 
  // Handle file upload
  onUpload(): void {
    if (this.uploadForm.valid && this.selectedFile) {
      this.uploadProgress = 0; // Initialize progress
      const formData = new FormData();
      formData.append('file', this.selectedFile);
      console.log('Uploading file:', this.selectedFile);
      this.apiService.uploadFile(this.selectedFile).subscribe({
        next: (event) => {
          if (event.type === HttpEventType.UploadProgress && event.total) {
            this.uploadProgress = Math.round((100 * event.loaded) / event.total);
          } else if (event.type === HttpEventType.Response) {
            console.log('File uploaded successfully:', event.body);
            this.uploadProgress = -1; // Reset progress after success
          }
        },
        error: (error) => {
          console.error('File upload failed:', error);
          this.uploadProgress = -1; 
        },
      });
    } else {
      console.warn('Form is invalid or no file selected.');
    }
  }
}


