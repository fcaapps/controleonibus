# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-14 17:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ionibus', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='capitao',
            old_name='congregacao',
            new_name='id_congregacao',
        ),
        migrations.RenameField(
            model_name='passageiro',
            old_name='capitao',
            new_name='id_capitao',
        ),
        migrations.RenameField(
            model_name='passageiro',
            old_name='congregacao',
            new_name='id_congregacao',
        ),
        migrations.RenameField(
            model_name='responsavel',
            old_name='congregacao',
            new_name='id_congregacao',
        ),
    ]
