import requests

from gtme.config import STEAM_API_KEY

STEAM_API_URL = "http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/"


def is_steamauth_valid(request):
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

    return 'is_valid:true' in str(response.content)


def update_user_steam_info(user):
    requestParams = {
        "key": STEAM_API_KEY,
        "steamids": user.steam64
    }

    data = requests.get(STEAM_API_URL, requestParams).json()
    user.update_last_login()

    try:
        playerinfo = data['response']['players'][0]

        # List of possible keys returned by the api.
        # Some are removed as they are not stored in SteamUser
        keyList = [
            # 'steamid',
            # 'communityvisibilitystate',
            # 'profilestate',
            'personaname',
            # 'lastlogoff',
            # 'commentpermission',
            # 'profileurl',
            'avatar',
            'personastate',
            'realname',
            # 'primaryclanid',
            # 'timecreated',
            # 'gameextrainfo',
            # 'gameid',
            # 'gameserverip',
            'loccountrycode',
            # 'locstatecode',
            # 'loccityid',
        ]

        available_keys = set(keyList).intersection(playerinfo.keys())

        for key in available_keys:
            setattr(user, key, playerinfo[key])

    except IndexError:
        print("Can't find user info.")

    return user
