# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-10-02 09:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_auto_20171002_0920'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='course_org',
        ),
    ]
