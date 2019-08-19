from django.conf.urls import url
from django.urls import include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView

from gtme.gtmeapi import views

router = routers.DefaultRouter()
router.register(r'dumpaccount', views.DumpData, 'dump')

urlpatterns = [
    url('api/', include(router.urls)),
    url('token/auth', views.steam_auth, name='token_steam_auth'),
    url('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    url('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
