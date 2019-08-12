import {Injectable} from '@angular/core';
import {ActivatedRouteSnapshot, CanActivate, Router, RouterStateSnapshot, UrlTree} from '@angular/router';
import {Observable} from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class UserLoggedInGuard implements CanActivate {

  isLoggedIn: boolean;

  constructor(private router: Router) {
    this.isLoggedIn = false; // Temp hack
  }

  canActivate(route: ActivatedRouteSnapshot, state: RouterStateSnapshot): boolean {
    if (this.isLoggedIn) {
      return true;
    } else {
      this.router.navigate(['/login']);
      return false;
    }

  }

}
