
from django.test import TestCase
from .models import Profile
from django.contrib.gis.geos import Point
from django.contrib.auth.models import User

class ProfileTestCase(TestCase):
    @classmethod
    def setUpTestData(self):
        user1 = User.objects.create(username="sara",password="kjhjkh")
        user1.profile.homeAddress = "NYC"
        user1.save()

    def test_can_create_profile(self):
        user = User.objects.last()
        self.assertEqual(user.profile.homeAddress, "NYC")
