import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SubmitExercise2FinalComponent } from './submit-exercise2-final.component';

describe('SubmitExercise2FinalComponent', () => {
  let component: SubmitExercise2FinalComponent;
  let fixture: ComponentFixture<SubmitExercise2FinalComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [SubmitExercise2FinalComponent]
    });
    fixture = TestBed.createComponent(SubmitExercise2FinalComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
