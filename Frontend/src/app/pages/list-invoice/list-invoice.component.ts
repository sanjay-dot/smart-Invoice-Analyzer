import { Component, ViewChild } from '@angular/core';
import { MatPaginator } from '@angular/material/paginator';
import { MatSort } from '@angular/material/sort';
import { MatTableDataSource } from '@angular/material/table';
import {
  MAT_DIALOG_DATA,
  MatDialog,
  MatDialogActions,
  MatDialogClose,
  MatDialogContent,
  MatDialogRef,
  MatDialogTitle,
} from '@angular/material/dialog';
import { PredictDiaogComponent } from '../dialog/predict-diaog/predict-diaog.component';

export interface FileData {
  id: number;
  filename: string;
  uploaded_on: string;
}

const ELEMENT_DATA: FileData[] = [
  { id: 1, filename: 'Invoice_001.zip', uploaded_on: '2025-01-20' },
  { id: 2, filename: 'Invoice_002.zip', uploaded_on: '2025-01-21' },
  { id: 3, filename: 'Invoice_003.zip', uploaded_on: '2025-01-22' },
  { id: 4, filename: 'Invoice_004.zip', uploaded_on: '2025-01-23' },
  { id: 5, filename: 'Invoice_005.zip', uploaded_on: '2025-01-24' },
  { id: 6, filename: 'Invoice_006.zip', uploaded_on: '2025-01-25' },
  { id: 7, filename: 'Invoice_007.zip', uploaded_on: '2025-01-26' },
  { id: 8, filename: 'Invoice_008.zip', uploaded_on: '2025-01-27' },
  { id: 9, filename: 'Invoice_009.zip', uploaded_on: '2025-01-28' },
  { id: 10, filename: 'Invoice_010.zip', uploaded_on: '2025-01-29' },
];

@Component({
  selector: 'app-list-invoice',
  standalone: false,
  
  templateUrl: './list-invoice.component.html',
  styleUrl: './list-invoice.component.scss'
})

export class ListInvoiceComponent {
  constructor(private dialog: MatDialog) {}

  displayedColumns = ['id', 'filename', 'uploaded_on', 'actions'];
  dataSource = new MatTableDataSource(ELEMENT_DATA);
  // dataSource = ELEMENT_DATA;
  @ViewChild(MatPaginator) paginator!: MatPaginator;
  @ViewChild(MatSort) sort!: MatSort;



  ngAfterViewInit() {
    setTimeout(() => {
      this.dataSource.paginator = this.paginator;
      this.dataSource.sort = this.sort;
      this.paginator.length = ELEMENT_DATA.length;
    });
  }

  applyFilter(event: Event) {
    const filterValue = (event.target as HTMLInputElement).value;
    this.dataSource.filter = filterValue.trim().toLowerCase();
  }

  /**
   * Function to Predict
   */
predict(row: FileData) {
  const data = {
    product: {
      name: "Off-White - Nehru Jacket",
      sales: 27,
      imageUrl: "https://upload.wikimedia.org/wikipedia/commons/thumb/f/fc/Nehru_Jacket.jpg/220px-Nehru_Jacket.jpg"
    }
  };
  const dialogRef = this.dialog.open(PredictDiaogComponent, {
    data: data,
    width: '600px',
    height: '400px',
    disableClose: true,
    autoFocus: true
  });

  dialogRef.afterClosed().subscribe((result: any) => {
    if (result) {
      // Handle the result from the dialog if needed
    }
  });
}


  /**
   * Function to Analyze
   */
  analyze(row: FileData): void {
    const dashboardUrl = 'https://app.powerbi.com/view?r=eyJrIjoiZDgzNjMzZTAtYjFkYi00YjYzLTlkMmMtMmZkNzEzM2ExOTdhIiwidCI6IjM2NDliMmFmLWIxMTUtNDFlOC1iM2ZkLWMzNzVhZTJiNmY0OSJ9';
    window.open(dashboardUrl, '_blank');
  }
  
  
  
}

