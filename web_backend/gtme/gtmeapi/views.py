from django.contrib.auth import authenticate
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework_jwt.settings import api_settings

from gtme.gtmeapi.models import SteamUser
from gtme.gtmeapi.serializers import SteamSerializer


class DumpData(ViewSet):
    def list(self, request, format=None):
        user = SteamUser.objects.filter(steam64=request.user.steam64)[0]
        serializer = SteamSerializer(user, many=False)
        return Response(serializer.data)


def steam_auth(request):
    user = authenticate(request)

    if user is None:
        return HttpResponse("can't verify your identity")

    jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
    jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

    payload = jwt_payload_handler(user)
    token = jwt_encode_handler(payload)

    return HttpResponse("Your claimed id is " + str(user.steam64) + " is confirmed. JWT token : " + str(token))
