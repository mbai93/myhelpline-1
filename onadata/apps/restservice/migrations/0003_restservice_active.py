# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-02-06 08:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restservice', '0002_auto_20160524_0458'),
    ]

    operations = [
        migrations.AddField(
            model_name='restservice',
            name='active',
            field=models.BooleanField(default=True, verbose_name='Active'),
        ),
    ]
