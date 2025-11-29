import { ComponentFixture, TestBed } from '@angular/core/testing';

import { PredictDiaogComponent } from './predict-diaog.component';

describe('PredictDiaogComponent', () => {
  let component: PredictDiaogComponent;
  let fixture: ComponentFixture<PredictDiaogComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [PredictDiaogComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(PredictDiaogComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
