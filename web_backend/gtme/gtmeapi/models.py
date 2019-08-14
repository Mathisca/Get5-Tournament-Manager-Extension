from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils import timezone

from gtme.gtmeapi.services import update_user_steam_info


class SteamManager(BaseUserManager):
    def create_user(self, steam64, **extra_fields):
        if not steam64:
            raise ValueError('Steam64 must be set')

        user = self.model(steam64=steam64)
        user.save()
        return user


class SteamUser(AbstractBaseUser):
    password = None
    steam64 = models.TextField('SteamID 64', unique=True)

    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(default=timezone.now)

    # Steam API fields

    personaname = models.CharField("Display name", max_length=32, null=True)
    avatar = models.TextField("Avatar URL", null=True)
    personastate = models.IntegerField("User status", null=True)
    realname = models.TextField("User full name", null=True)
    loccountrycode = models.CharField("Coutry code", max_length=2, null=True)

    objects = SteamManager()

    USERNAME_FIELD = 'steam64'
    REQUIRED_FIELDS = []

    class Meta:
        app_label = "gtmeapi"
        db_table = "users"

    def __str__(self):
        return self.steam64

    def update_last_login(self):
        self.last_login = timezone.now()
        self.save()

    def update_infos(self):
        self.update_last_login()
        update_user_steam_info(self)
        self.save()
