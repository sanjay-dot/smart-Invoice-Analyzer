import { NgModule } from '@angular/core';
import { BrowserModule, provideClientHydration, withEventReplay } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { UploadInvoiceComponent } from './pages/upload-page/upload-invoice/upload-invoice.component';
import { HeaderPageComponent } from './shared-pages/header-page/header-page.component';
import { PgaeNotFoundComponent } from './shared-pages/page-not-found/pgae-not-found.component';
import { provideAnimationsAsync } from '@angular/platform-browser/animations/async';

import { FormsModule, ReactiveFormsModule } from '@angular/forms'; // Forms modules
import { HttpClientModule } from '@angular/common/http';
import { ListInvoiceComponent } from './pages/list-invoice/list-invoice.component'; // Import HttpClientModule
import { MatTableModule } from '@angular/material/table';
import { MatInputModule } from '@angular/material/input';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatPaginatorModule } from '@angular/material/paginator';
import { PredictDiaogComponent } from './pages/dialog/predict-diaog/predict-diaog.component';
import { MatDialogModule } from '@angular/material/dialog';
import { MatProgressBarModule } from '@angular/material/progress-bar';

@NgModule({
  declarations: [
    AppComponent,
    UploadInvoiceComponent,
    HeaderPageComponent,
    PgaeNotFoundComponent,
    ListInvoiceComponent,
    PredictDiaogComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    ReactiveFormsModule,
    HttpClientModule,
    MatTableModule,
    MatInputModule,
    MatFormFieldModule,
    MatPaginatorModule,
    MatDialogModule,
    MatProgressBarModule,
  ],
  providers: [
    provideClientHydration(withEventReplay()),
    provideAnimationsAsync(),
  ],
  bootstrap: [AppComponent],
})
export class AppModule {}
