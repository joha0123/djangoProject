# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-15 11:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('offerStream', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='offer',
            old_name='storeFk',
            new_name='store',
        ),
        migrations.RenameField(
            model_name='store',
            old_name='adressFK',
            new_name='adress',
        ),
    ]
