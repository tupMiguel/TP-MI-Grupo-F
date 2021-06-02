import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { HomeComponent } from './pages/home/home.component';
import { GameComponent } from './pages/game/game.component';
import { RulesComponent } from './pages/rules/rules.component';
import { EditComponent } from './pages/edit/edit.component';
import { CredComponent } from './pages/cred/cred.component';

const routes: Routes = [
  { path: 'home', component: HomeComponent },
  { path: 'game', component: GameComponent },
  { path: 'rules', component:RulesComponent },
  { path: 'edit', component:EditComponent },
  { path: 'cred', component:CredComponent },
  { path: '**', redirectTo: '/home' }
];


@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
