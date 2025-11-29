import { Component, Inject } from '@angular/core';
import { MatDialogModule, MAT_DIALOG_DATA } from '@angular/material/dialog';
import { MatProgressBarModule } from '@angular/material/progress-bar';


@Component({
  selector: 'app-predict-diaog',
  standalone: false,
  
  templateUrl: './predict-diaog.component.html',
  styleUrl: './predict-diaog.component.scss'
})
export class PredictDiaogComponent {
  constructor(
    @Inject(MAT_DIALOG_DATA) public data: {
      product: {
        name: string;
        id: number;
        sales: number;
        imageUrl: string;
      };
    }
  ) {}
}

