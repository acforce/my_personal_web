# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-19 21:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weblog', '0003_auto_20160819_2122'),
    ]

    operations = [
        migrations.RenameField(
            model_name='entry',
            old_name='mod_date',
            new_name='mod_time',
        ),
    ]
