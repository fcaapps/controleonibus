# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-06-01 14:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ionibus', '0015_auto_20170601_1100'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eventos',
            name='parte',
        ),
        migrations.AlterField(
            model_name='eventos',
            name='circuito',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='ionibus.Circuito'),
        ),
    ]
