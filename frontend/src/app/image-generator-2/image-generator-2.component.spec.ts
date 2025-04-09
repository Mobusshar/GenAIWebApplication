import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ImageGenerator2Component } from './image-generator-2.component';

describe('ImageGenerator2Component', () => {
  let component: ImageGenerator2Component;
  let fixture: ComponentFixture<ImageGenerator2Component>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [ImageGenerator2Component]
    });
    fixture = TestBed.createComponent(ImageGenerator2Component);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
