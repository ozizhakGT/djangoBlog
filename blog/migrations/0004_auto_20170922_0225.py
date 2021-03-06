# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-09-21 23:25
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20170921_2335'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='approve_comment',
            new_name='approved_comment',
        ),
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 9, 21, 23, 25, 5, 118556, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
