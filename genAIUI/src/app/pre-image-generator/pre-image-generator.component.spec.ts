import { ComponentFixture, TestBed } from '@angular/core/testing';

import { PreImageGeneratorComponent } from './pre-image-generator.component';

describe('PreImageGeneratorComponent', () => {
  let component: PreImageGeneratorComponent;
  let fixture: ComponentFixture<PreImageGeneratorComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [PreImageGeneratorComponent]
    });
    fixture = TestBed.createComponent(PreImageGeneratorComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
