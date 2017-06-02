# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-06-01 14:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ionibus', '0014_auto_20170601_1056'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventos',
            name='parte',
            field=models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B')], max_length=1, verbose_name='Parte'),
        ),
        migrations.AlterField(
            model_name='eventos',
            name='circuito',
            field=models.CharField(blank=True, choices=[('CE01', 'CE01'), ('CE02', 'CE02'), ('CE03', 'CE03'), ('CE04', 'CE04'), ('CE05', 'CE05'), ('CE06', 'CE06'), ('CE07', 'CE07'), ('CE08', 'CE08'), ('CE09', 'CE09'), ('CE10', 'CE10'), ('CE11', 'CE11'), ('CE12', 'CE12'), ('CE13', 'CE13'), ('CE14', 'CE14'), ('CE15', 'CE15'), ('CE16', 'CE16'), ('CE17', 'CE17'), ('CE18', 'CE18')], max_length=4, verbose_name='Circuito'),
        ),
    ]