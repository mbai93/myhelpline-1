# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-19 08:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logger', '0022_auto_20160418_0518'),
    ]

    operations = [
        migrations.AlterField(
            model_name='widget',
            name='column',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='widget',
            name='group_by',
            field=models.CharField(blank=True, default=None, max_length=255,
                                   null=True),
        ),
    ]
