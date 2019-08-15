from django.urls import path, include
from rest_framework import routers

from gtme.gtmeapi import views

router = routers.DefaultRouter()
router.register(r'dumpaccount', views.DumpData, 'dump')

urlpatterns = [
    path('api/', include(router.urls)),
    path('auth/', views.steam_auth),
    path('refresh/', views.refresh_token),
]
