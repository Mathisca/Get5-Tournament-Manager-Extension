import {Injectable} from '@angular/core';
import {ActivatedRouteSnapshot, CanActivate, Router, RouterStateSnapshot, UrlTree} from '@angular/router';
import {Observable} from 'rxjs';
import {UserLoggedInGuard} from './userloggedin.guard';

@Injectable({
  providedIn: 'root'
})
export class UserLoggedOutGuard implements CanActivate {
  isLoggedIn: boolean;

  constructor(private router: Router) {
    this.isLoggedIn = false; // Temp hack
  }

  canActivate(route: ActivatedRouteSnapshot, state: RouterStateSnapshot): boolean {
    return !this.isLoggedIn;
  }
}
