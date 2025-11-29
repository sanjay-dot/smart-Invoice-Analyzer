import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { UploadInvoiceComponent } from './pages/upload-page/upload-invoice/upload-invoice.component';

const routes: Routes = [
  { path: '', component: UploadInvoiceComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
