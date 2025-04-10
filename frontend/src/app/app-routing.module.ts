import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { ImageGeneratorComponent } from './image-generator/image-generator.component';
import { LandingPageComponent } from './landing-page/landing-page.component';
import { PreTextGeneratorComponent } from './pre-text-generator/pre-text-generator.component';
import { TextGeneratorComponent } from './text-generator/text-generator.component';
import { SubmitExercise1Component } from './submit-exercise1/submit-exercise1.component';
import { SubmitExercise2Component } from './submit-exercise2/submit-exercise2.component';
import { PreImageGeneratorComponent } from './pre-image-generator/pre-image-generator.component';
import { LayoutComponent } from './layout/layout.component';
import { StoryBuildingComponent } from './story-building/story-building.component';
import { ImageGenerator2Component } from './image-generator-2/image-generator-2.component';
import { SubmitExercise2FinalComponent } from './submit-exercise2-final/submit-exercise2-final.component';
import { GenerativeAiToolsComponent } from './generative-ai-tools/generative-ai-tools.component';

const routes: Routes = [
  {
    path: '',
    component: LayoutComponent,
    children: [
      { path: '', component: LandingPageComponent },
      { path: 'image-generator/:id', component: ImageGeneratorComponent },
      { path: 'pre-text-generator', component: PreTextGeneratorComponent },
      { path: 'story-building/:id', component: StoryBuildingComponent },
      { path: 'text-generator/:id', component: TextGeneratorComponent },
      { path: 'submit-exercise1/:id', component: SubmitExercise1Component },
      { path: 'pre-image-generator', component: PreImageGeneratorComponent },
      { path: 'image-generator-2/:id', component: ImageGenerator2Component },
      { path: 'submit-exercise2/:id', component: SubmitExercise2Component },
      { path: 'submit-exercise2-final/:id', component: SubmitExercise2FinalComponent },
      { path: 'generative-ai-tools', component: GenerativeAiToolsComponent }
      //{ path: '', redirectTo: '/image-generator', pathMatch: 'full' }
    ]
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
