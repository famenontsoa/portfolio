from rest_framework_gis.serializers import GeoFeatureModelSerializer
from rest_framework import serializers
from .models import Profile

class ProfileSerializer(GeoFeatureModelSerializer):
    username = serializers.CharField(read_only=True, source="user.username")

    class Meta:
         fields = ("id", "username", "homeAddress", "phoneNumber", "published_date")
         geo_field = "location"
         model = Profile
