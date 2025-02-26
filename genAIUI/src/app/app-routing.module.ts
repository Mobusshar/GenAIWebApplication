import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { ImageGeneratorComponent } from './image-generator/image-generator.component';
import { LandingPageComponent } from './landing-page/landing-page.component';
import { PreTextGeneratorComponent } from './pre-text-generator/pre-text-generator.component';
import { TextGeneratorComponent } from './text-generator/text-generator.component';
import { SubmitExercise1Component } from './submit-exercise1/submit-exercise1.component';
import { SubmitExercise2Component } from './submit-exercise2/submit-exercise2.component';
import { PreImageGeneratorComponent } from './pre-image-generator/pre-image-generator.component';

const routes: Routes = [
  { path: '', component: LandingPageComponent },
  { path: 'image-generator', component: ImageGeneratorComponent },
  { path: 'pre-text-generator', component: PreTextGeneratorComponent },
  { path: 'text-generator', component: TextGeneratorComponent },
  { path: 'submit-exercise1', component: SubmitExercise1Component },
  { path: 'pre-image-generator', component: PreImageGeneratorComponent },
  { path: 'submit-exercise2', component: SubmitExercise2Component }
  //{ path: '', redirectTo: '/image-generator', pathMatch: 'full' }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
