# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-15 00:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ionibus', '0005_auto_20170414_1845'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventos',
            name='circuito',
            field=models.CharField(blank=True, choices=[('CE01', 'CIRCUITO CE01'), ('CE02', 'CIRCUITO CE02'), ('CE03', 'CIRCUITO CE03'), ('CE04', 'CIRCUITO CE04'), ('CE05', 'CIRCUITO CE05'), ('CE06', 'CIRCUITO CE06'), ('CE07', 'CIRCUITO CE07'), ('CE08', 'CIRCUITO CE08'), ('CE09', 'CIRCUITO CE09'), ('CE10', 'CIRCUITO CE10'), ('CE11', 'CIRCUITO CE11'), ('CE12', 'CIRCUITO CE12'), ('CE13', 'CIRCUITO CE13'), ('CE14', 'CIRCUITO CE14'), ('CE15', 'CIRCUITO CE15'), ('CE16', 'CIRCUITO CE16'), ('CE17', 'CIRCUITO CE17'), ('CE18', 'CIRCUITO CE18')], max_length=4, verbose_name='Circuito'),
        ),
        migrations.AlterField(
            model_name='eventos',
            name='texto_base',
            field=models.CharField(blank=True, max_length=30, verbose_name='Texto Base'),
        ),
    ]
