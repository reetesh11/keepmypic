# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-23 20:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0007_auto_20161223_2043'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='thumbnail',
            name='photo',
        ),
        migrations.DeleteModel(
            name='Photo',
        ),
        migrations.DeleteModel(
            name='Thumbnail',
        ),
    ]