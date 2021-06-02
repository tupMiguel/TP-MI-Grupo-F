import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HomeComponent } from './pages/home/home.component';
import { NavbarComponent } from './components/shared/navbar/navbar.component';
import { GameComponent } from './pages/game/game.component';
import { RulesComponent } from './pages/rules/rules.component';
import { EditComponent } from './pages/edit/edit.component';
import { CredComponent } from './pages/cred/cred.component';


@NgModule({
  declarations: [
    AppComponent,
    HomeComponent,
    NavbarComponent,
    GameComponent,
    RulesComponent,
    EditComponent,
    CredComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
