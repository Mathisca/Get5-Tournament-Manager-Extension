from django.contrib.auth.models import User
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_jwt.settings import api_settings

from gtme.gtmeapi.serializers import UserSerializer


def create_token(request):
    current_user = request.user
    if current_user.is_authenticated:
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(current_user)
        token = jwt_encode_handler(payload)

        return HttpResponse(token)
    return HttpResponse("NoAuth")


@api_view(['GET', 'POST'])
def get_account_data(request):
    if request.method == 'GET':
        serializer = UserSerializer(request.user, context={'request': request})
        return Response(serializer.data)