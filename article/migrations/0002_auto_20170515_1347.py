# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-15 13:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-date_time']},
        ),
    ]
