from rest_framework import viewsets
from rest_framework_gis import filters
from .models import Profile
from .serializers import ProfileSerializer
from django.utils import timezone

class ProfileViewSet(viewsets.ReadOnlyModelViewSet):
     bbox_filter_field = "location"
     filter_backends = (filters.InBBoxFilter,)
     queryset = Profile.objects.all()
     serializer_class = ProfileSerializer
