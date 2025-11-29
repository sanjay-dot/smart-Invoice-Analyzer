import { Component } from '@angular/core';
import { HeaderPageComponent } from './shared-pages/header-page/header-page.component';
@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  standalone: false,
  styleUrl: './app.component.scss'
})
export class AppComponent {
  title = 'InvoiceLens-Angular';
}
