import {Injectable} from '@angular/core';
import {HttpClient, HttpParams} from '@angular/common/http';
import {ActivatedRoute} from '@angular/router';
import {AppConfigService} from './app-config.service';

@Injectable({
  providedIn: 'root'
})
export class AuthService {

  constructor(private http: HttpClient, public config: AppConfigService) {
  }

  public authUser(route: ActivatedRoute) {
    const reqParams = new HttpParams();
    route.queryParams.subscribe(queryParams => {
      this.http.get(this.config.settings.apiRoot + '/token/auth', {
        params: queryParams, // TODO encode params
        observe: 'response'
      })
        .toPromise()
        .then(response => {
          console.log(response);
        })
        .catch(console.log);
    });
  }

  public getAccessToken(): string {
    return localStorage.getItem('accessToken');
  }

  public getRefreshToken(): string {
    return localStorage.getItem('refreshToken');
  }

  // public isAuthenticated(): boolean {
  //   const token = this.getToken();
  //   return tokenNotExpired(null, token);
  // }

}
