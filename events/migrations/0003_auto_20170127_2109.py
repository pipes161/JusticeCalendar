# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-01-28 02:09
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_auto_20170127_2056'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='start',
        ),
        migrations.AddField(
            model_name='event',
            name='start_day',
            field=models.DateField(db_index=True, default=datetime.date(2017, 1, 28)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='start_time',
            field=models.TimeField(db_index=True, default=datetime.time(2, 9, 11, 955349)),
            preserve_default=False,
        ),
    ]
