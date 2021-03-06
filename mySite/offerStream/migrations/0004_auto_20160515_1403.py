# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-15 12:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('offerStream', '0003_auto_20160515_1357'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='store',
            name='adress',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='offerStream.Adress'),
        ),
    ]
