import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ChatbotAssistantComponent } from './chatbot-assistant.component';

describe('ChatbotAssistantComponent', () => {
  let component: ChatbotAssistantComponent;
  let fixture: ComponentFixture<ChatbotAssistantComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [ChatbotAssistantComponent]
    });
    fixture = TestBed.createComponent(ChatbotAssistantComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
