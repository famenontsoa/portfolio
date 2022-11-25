from django import forms
from .models import Profile
import django.contrib.gis.forms as gis_forms

class ProfileForm(forms.ModelForm):
    location = gis_forms.PointField(
        srid=4326,
        widget= gis_forms.OSMWidget(
            attrs={'map_width': 400, 'map_height': 250, 'map_srid': 4326, 'default_zoom':0}))

    class Meta:
        model = Profile
        fields = ('user', 'phoneNumber', 'homeAddress', 'location')
