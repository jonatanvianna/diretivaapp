# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-24 00:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diretiva', '0003_auto_20170924_0001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diretiva',
            name='date_closed',
            field=models.DateTimeField(null=True),
        ),
    ]
