import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ContentGeneratorComponent } from './content-generator.component';

describe('ContentGeneratorComponent', () => {
  let component: ContentGeneratorComponent;
  let fixture: ComponentFixture<ContentGeneratorComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [ContentGeneratorComponent]
    });
    fixture = TestBed.createComponent(ContentGeneratorComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
