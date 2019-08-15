from gtme.gtmeapi.models import SteamUser


class SteamBackend:
    def authenticate(self, request, username=None, password=None, **kwargs):
        # if not is_steamauth_valid(request):
        #   return None

        claimedid = str(request.GET.get('openid.claimed_id')).replace('https://steamcommunity.com/openid/id/', '')

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
