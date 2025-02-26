import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SubmitExercise1Component } from './submit-exercise1.component';

describe('SubmitExercise1Component', () => {
  let component: SubmitExercise1Component;
  let fixture: ComponentFixture<SubmitExercise1Component>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [SubmitExercise1Component]
    });
    fixture = TestBed.createComponent(SubmitExercise1Component);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
