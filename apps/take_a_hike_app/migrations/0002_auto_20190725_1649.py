# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-07-25 16:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('take_a_hike_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='hikers',
            field=models.ManyToManyField(null=True, related_name='trips', to='take_a_hike_app.User'),
        ),
    ]