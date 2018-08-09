# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-28 07:25
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('logger', '0047_dataview_deleted_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='dataview',
            name='deleted_by',
            field=models.ForeignKey(
                blank=True,
                default=None,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name='dataview_deleted_by',
                to=settings.AUTH_USER_MODEL),
        ),
    ]
