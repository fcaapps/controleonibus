# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-06-10 19:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ionibus', '0037_auto_20170610_1529'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lista_passageiros',
            name='onibus',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fk_onibus_a_lista_passageiros', to='ionibus.Onibus_assentos'),
        ),
    ]
