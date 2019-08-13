from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from gtme.gtmeapi import views

router = routers.DefaultRouter()

urlpatterns = [
    path('create_token/', views.create_token()),
    path('api/', include(router.urls)),
    path('accounts/', include('allauth.urls')),
    path('admin/', admin.site.urls),
]