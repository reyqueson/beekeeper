# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-08-27 05:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aws', '0015_auto_20180827_1042'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='descriptor',
        ),
    ]
