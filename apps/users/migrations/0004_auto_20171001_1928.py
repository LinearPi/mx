# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-10-01 19:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20171001_1737'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='gender',
            field=models.CharField(choices=[('male', '男'), ('famale', '女')], default='famale', max_length=6),
        ),
    ]
