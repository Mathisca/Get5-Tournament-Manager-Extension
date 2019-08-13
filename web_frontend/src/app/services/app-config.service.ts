import {Injectable} from '@angular/core';
import {AppConfigModel} from '../models/app-config-model';
import {HttpClient} from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class AppConfigService {

   settings: AppConfigModel;

  constructor(private http: HttpClient) {
  }

  load() {
    const jsonFile = `assets/config.json`;
    return new Promise<void>((resolve, reject) => {
      this.http.get(jsonFile).toPromise().then((response: AppConfigModel) => {
        this.settings = response as AppConfigModel;
        resolve();
      }).catch((response: any) => {
        reject(`Could not load file '${jsonFile}': ${JSON.stringify(response)}`);
      });
    });
  }
}
