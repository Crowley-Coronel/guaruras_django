# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-13 18:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alertas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='alerta',
            name='ubicacion',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]