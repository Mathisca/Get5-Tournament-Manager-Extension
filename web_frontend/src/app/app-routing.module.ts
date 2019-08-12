import {NgModule} from '@angular/core';
import {RouterModule, Routes} from '@angular/router';
import {DashboardComponent} from './dashboard/dashboard.component';
import {LoginComponent} from './login/login.component';
import {UserLoggedInGuard} from './auth/userloggedin.guard';
import {UserLoggedOutGuard} from './auth/userloggedout.guard';


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
