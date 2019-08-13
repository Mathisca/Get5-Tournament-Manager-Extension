import { TestBed, async, inject } from '@angular/core/testing';

import { UserLoggedInGuard } from './userloggedin.guard';

describe('LoggedinGuard', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [UserLoggedInGuard]
    });
  });

  it('should ...', inject([UserLoggedInGuard], (guard: UserLoggedInGuard) => {
    expect(guard).toBeTruthy();
  }));
});
