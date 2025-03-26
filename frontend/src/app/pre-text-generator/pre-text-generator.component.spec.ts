import { ComponentFixture, TestBed } from '@angular/core/testing';

import { PreTextGeneratorComponent } from './pre-text-generator.component';

describe('PreTextGeneratorComponent', () => {
  let component: PreTextGeneratorComponent;
  let fixture: ComponentFixture<PreTextGeneratorComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [PreTextGeneratorComponent]
    });
    fixture = TestBed.createComponent(PreTextGeneratorComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
