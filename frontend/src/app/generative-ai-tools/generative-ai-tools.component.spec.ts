import { ComponentFixture, TestBed } from '@angular/core/testing';

import { GenerativeAiToolsComponent } from './generative-ai-tools.component';

describe('GenerativeAiToolsComponent', () => {
  let component: GenerativeAiToolsComponent;
  let fixture: ComponentFixture<GenerativeAiToolsComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [GenerativeAiToolsComponent]
    });
    fixture = TestBed.createComponent(GenerativeAiToolsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
