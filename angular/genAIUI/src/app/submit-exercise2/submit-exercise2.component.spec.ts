import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SubmitExercise2Component } from './submit-exercise2.component';

describe('SubmitExercise2Component', () => {
  let component: SubmitExercise2Component;
  let fixture: ComponentFixture<SubmitExercise2Component>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [SubmitExercise2Component]
    });
    fixture = TestBed.createComponent(SubmitExercise2Component);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
