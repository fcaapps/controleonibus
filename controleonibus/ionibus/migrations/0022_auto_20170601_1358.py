# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-06-01 16:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ionibus', '0021_auto_20170601_1356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventos',
            name='local',
            field=models.CharField(blank=True, choices=[('01', 'Salão de Assembléias'), ('02', 'Paulo Sarasate'), ('03', 'Estádio Castelão')], default='01', max_length=50, verbose_name='Local do Evento'),
        ),
    ]
