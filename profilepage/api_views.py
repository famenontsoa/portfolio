from rest_framework import viewsets
from rest_framework_gis import filters
from profilepage.models import Profile
from profilepage.serializers import ProfileSerializer
from django.utils import timezone

class ProfileViewSet(viewsets.ReadOnlyModelViewSet):
     bbox_filter_field = "location"
     filter_backends = (filters.InBBoxFilter,)
     queryset = Profile.objects.filter(published_date__lte=timezone.now())
     serializer_class = ProfileSerializer
