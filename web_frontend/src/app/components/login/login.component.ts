import {Component, OnInit} from '@angular/core';
import {AppConfigService} from '../../services/app-config.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})
export class LoginComponent implements OnInit {

  constructor(public config: AppConfigService) {


  }

  ngOnInit() {

  }

}
