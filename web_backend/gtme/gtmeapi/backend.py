import requests

from gtme.gtmeapi.models import SteamUser


class SteamBackend:
    def authenticate(self, request, username=None, password=None, **kwargs):
        post_args = {
            'openid.assoc_handle': request.GET.get('openid.assoc_handle'),
            'openid.sig': request.GET.get('openid.sig'),
            'openid.ns': request.GET.get('openid.ns'),
            'openid.signed': request.GET.get('openid.signed'),
            'openid.mode': 'check_authentication'
        }

        openid_signed = request.GET.get('openid.signed').split(',')

        for param in openid_signed:
            val = 'openid.{}'.format(param)
            post_args[val] = request.GET.get(val)

        response = requests.post('https://steamcommunity.com/openid/login', data=post_args)

        if 'is_valid:true' in str(response.content):
            claimedid = str(request.GET.get('openid.claimed_id')).replace('https://steamcommunity.com/openid/id/', '')

            user = self.get_user(claimedid)
            if user is None:
                user = SteamUser.objects.create_user(steam64=claimedid)

            SteamUser.objects.update_last_login(user)

            return user
        else:
            return None

    def get_user(self, steam64):
        try:
            user = SteamUser.objects.get(steam64=steam64)
            return user
        except SteamUser.DoesNotExist:
            return None
