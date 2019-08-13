from rest_framework import serializers

from gtme.gtmeapi.models import SteamUser


class SteamSerializer(serializers.ModelSerializer):
    class Meta:
        model = SteamUser
        fields = '__all__'
