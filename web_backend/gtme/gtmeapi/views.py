from django.http import HttpResponse

from rest_framework.authentication import SessionAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes

from rest_framework.permissions import IsAuthenticated


def sample_view(request):
    current_user = request.user
    return HttpResponse(current_user.is_authenticated)
