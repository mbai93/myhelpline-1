# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-09-12 18:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helpline', '0012_hotdesk_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='case',
            name='status',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
    ]
