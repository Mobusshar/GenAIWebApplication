import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { ImageGeneratorComponent } from './image-generator/image-generator.component';
import { LandingPageComponent } from './landing-page/landing-page.component';

const routes: Routes = [
  { path: '', component: LandingPageComponent },
  { path: 'image-generator', component: ImageGeneratorComponent }
  //{ path: '', redirectTo: '/image-generator', pathMatch: 'full' }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
