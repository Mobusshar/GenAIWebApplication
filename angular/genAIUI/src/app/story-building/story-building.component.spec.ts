import { ComponentFixture, TestBed } from '@angular/core/testing';

import { StoryBuildingComponent } from './story-building.component';

describe('StoryBuildingComponent', () => {
  let component: StoryBuildingComponent;
  let fixture: ComponentFixture<StoryBuildingComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [StoryBuildingComponent]
    });
    fixture = TestBed.createComponent(StoryBuildingComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
