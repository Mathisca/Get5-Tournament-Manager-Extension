import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { AuthcheckComponent } from './authcheck.component';

describe('AuthcheckComponent', () => {
  let component: AuthcheckComponent;
  let fixture: ComponentFixture<AuthcheckComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ AuthcheckComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(AuthcheckComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
