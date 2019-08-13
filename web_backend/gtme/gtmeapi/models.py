from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.utils import timezone


class SteamManager(BaseUserManager):
    def create_user(self, steam64, **extra_fields):
        if not steam64:
            raise ValueError(_('Steam64 must be set'))
        user = self.model(steam64=steam64)
        user.save()
        return user

    def update_last_login(self, user):
        user.last_login = timezone.now()
        user.save()


class SteamUser(AbstractBaseUser):
    password = None
    steam64 = models.TextField('SteamID 64', unique=True)

    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(default=timezone.now)

    objects = SteamManager()

    USERNAME_FIELD = 'steam64'
    REQUIRED_FIELDS = []

    class Meta:
        app_label = "gtmeapi"
        db_table = "users"

    def __str__(self):
        return self.steam64
