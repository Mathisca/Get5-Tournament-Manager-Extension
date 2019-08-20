import {Injectable} from '@angular/core';
import {HttpClient, HttpParams, HttpUrlEncodingCodec} from '@angular/common/http';
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

      const loginParam = {};

      for (const param in queryParams) {
        loginParam[param] = (queryParams[param]);

      }

      this.http.post(this.config.settings.apiRoot + '/token/auth',
        loginParam
      )
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
