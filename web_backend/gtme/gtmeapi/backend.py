import json

from gtme.gtmeapi.models import SteamUser
from gtme.gtmeapi.services import is_steamauth_valid


class SteamBackend:
    def authenticate(self, request, username=None, password=None, **kwargs):
        json_data = json.loads(request.body)

        if not is_steamauth_valid(json_data):
            return None

        claimedid = str(json_data['openid.claimed_id']).replace('https://steamcommunity.com/openid/id/', '')

        user = self.get_user(claimedid)

        if user is None:
            user = SteamUser.objects.create_user(steam64=claimedid)

        user.update_infos()

        return user

    def get_user(self, steam64):
        try:
            user = SteamUser.objects.get(steam64=steam64)
            return user
        except SteamUser.DoesNotExist:
            return None
