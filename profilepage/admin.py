from django.contrib.gis import admin
from .models import Profile

@admin.register(Profile)
class UserProfileAdmin(admin.OSMGeoAdmin):
    list_display = ('user', 'location')
