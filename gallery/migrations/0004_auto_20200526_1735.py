# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-05-26 14:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0003_remove_galleryimage_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='galleryimage',
            name='location',
        ),
        migrations.DeleteModel(
            name='Location',
        ),
    ]