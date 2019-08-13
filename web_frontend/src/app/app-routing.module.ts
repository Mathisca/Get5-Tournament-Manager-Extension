import {NgModule} from '@angular/core';
import {RouterModule, Routes} from '@angular/router';
import {DashboardComponent} from './components/dashboard/dashboard.component';
import {LoginComponent} from './components/login/login.component';
import {UserLoggedInGuard} from './guards/userloggedin.guard';
import {UserLoggedOutGuard} from './guards/userloggedout.guard';


const routes: Routes = [

  {
    path: 'dashboard',
    component: DashboardComponent,
    canActivate: [UserLoggedInGuard]
  },  {
    path: 'login',
    component: LoginComponent,
    canActivate: [UserLoggedOutGuard]
  },
  {path: '', redirectTo: '/dashboard', pathMatch: 'prefix'},
  {path: '**', redirectTo: ''}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule {
}
