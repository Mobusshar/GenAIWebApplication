import { ComponentFixture, TestBed } from '@angular/core/testing';

import { TextSummarizerComponent } from './text-summarizer.component';

describe('TextSummarizerComponent', () => {
  let component: TextSummarizerComponent;
  let fixture: ComponentFixture<TextSummarizerComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [TextSummarizerComponent]
    });
    fixture = TestBed.createComponent(TextSummarizerComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
