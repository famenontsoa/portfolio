# Generated by Django 3.2.16 on 2022-11-21 19:22

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profilepage', '0002_rename_userprofile_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='location',
            field=django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326),
        ),
    ]
