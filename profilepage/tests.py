from django.test import TestCase
from .models import Profile
from django.contrib.gis.geos import Point
from django.contrib.auth.models import User

class ProfileTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create()

    def test_can_create_profile(self):
         profile = User.objects.last().profile
