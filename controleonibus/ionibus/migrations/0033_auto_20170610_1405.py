# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-06-10 17:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ionibus', '0032_auto_20170604_1206'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lista_passageiros',
            old_name='data_evento',
            new_name='data_arranjo',
        ),
    ]
