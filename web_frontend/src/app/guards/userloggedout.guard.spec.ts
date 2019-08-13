import { TestBed, async, inject } from '@angular/core/testing';

import { UserLoggedOutGuard } from './userloggedout.guard';

describe('LoggedoutGuard', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [UserLoggedOutGuard]
    });
  });

  it('should ...', inject([UserLoggedOutGuard], (guard: UserLoggedOutGuard) => {
    expect(guard).toBeTruthy();
  }));
});
