from django.contrib.gis.db import models
from django.contrib.gis.geos import Point
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    homeAddress = models.CharField(max_length=100)
    phoneNumber = PhoneNumberField(null=False, blank=False, unique=True)
    location = models.PointField(default=Point(0,0, srid=4326))
    published_date = models.DateTimeField(blank=True, null=True)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    def __str__(self):
        return self.user.username
