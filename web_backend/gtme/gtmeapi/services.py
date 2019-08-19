import requests

from gtme.config import STEAM_API_KEY

STEAM_API_URL = "http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/"


def is_steamauth_valid(request):
    required_keys = ['openid.ns',
                     'openid.op_endpoint',
                     'openid.claimed_id',
                     'openid.identity',
                     'openid.return_to',
                     'openid.response_nonce',
                     'openid.assoc_handle',
                     'openid.signed',
                     'openid.sig']

    post_args = {
        'openid.mode': 'check_authentication',
    }

    for key in required_keys:
        if request.GET.get(key) is None:
            return False
        else:
            post_args[key] = request.GET.get(key)

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
