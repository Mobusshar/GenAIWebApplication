import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { ImageGeneratorComponent } from './image-generator/image-generator.component';
import { FormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';
import { LandingPageComponent } from './landing-page/landing-page.component';
import { PreTextGeneratorComponent } from './pre-text-generator/pre-text-generator.component';
import { TextGeneratorComponent } from './text-generator/text-generator.component';
import { SubmitExercise1Component } from './submit-exercise1/submit-exercise1.component';
import { PreImageGeneratorComponent } from './pre-image-generator/pre-image-generator.component';
import { SubmitExercise2Component } from './submit-exercise2/submit-exercise2.component';
import { HeaderComponent } from './header/header.component';
import { FooterComponent } from './footer/footer.component';
import { LayoutComponent } from './layout/layout.component';
import { StoryBuildingComponent } from './story-building/story-building.component';
import { ImageGenerator2Component } from './image-generator-2/image-generator-2.component';

@NgModule({
  declarations: [
    AppComponent,
    ImageGeneratorComponent,
    LandingPageComponent,
    PreTextGeneratorComponent,
    TextGeneratorComponent,
    SubmitExercise1Component,
    PreImageGeneratorComponent,
    SubmitExercise2Component,
    HeaderComponent,
    FooterComponent,
    LayoutComponent,
    StoryBuildingComponent,
    ImageGenerator2Component
  ],
  imports: [
    BrowserModule,
    FormsModule,
    HttpClientModule,
    AppRoutingModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
