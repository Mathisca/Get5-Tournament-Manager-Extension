import {Component, OnInit} from '@angular/core';
import {AuthService} from '../../services/auth.service';
import {ActivatedRoute} from '@angular/router';

@Component({
  selector: 'app-authcheck',
  templateUrl: './authcheck.component.html',
  styleUrls: ['./authcheck.component.scss']
})
export class AuthcheckComponent implements OnInit {

  constructor(public auth: AuthService, private route: ActivatedRoute) {
  }

  ngOnInit() {
    this.auth.authUser(this.route);
  }

}
