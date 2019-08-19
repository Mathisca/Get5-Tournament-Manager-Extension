import json

from django.contrib.auth import authenticate
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework_simplejwt.tokens import RefreshToken

from gtme.gtmeapi.models import SteamUser
from gtme.gtmeapi.serializers import SteamSerializer


class DumpData(ViewSet):
    def list(self, request, format=None):
        user = SteamUser.objects.filter(steam64=request.user.steam64)[0]
        serializer = SteamSerializer(user, many=False)
        return Response(serializer.data)


# def refresh_token(request):
# return HttpResponse("access: "+str(AccessToken.))

def steam_auth(request):
    user = authenticate(request)

    if user is None:
        return HttpResponse('Unable to confirm identity', status=401)

    refresh = RefreshToken.for_user(user)

    return HttpResponse(json.dumps({
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }))
