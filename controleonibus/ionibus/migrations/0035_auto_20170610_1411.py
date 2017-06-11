# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-06-10 17:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ionibus', '0034_remove_lista_passageiros_evento'),
    ]

    operations = [
        migrations.AddField(
            model_name='lista_passageiros',
            name='evento',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fk_eve_lista_passageiros', to='ionibus.Eventos'),
        ),
        migrations.AlterField(
            model_name='lista_passageiros',
            name='data_arranjo',
            field=models.DateField(blank=True, null=True, verbose_name='Data do Arranjo'),
        ),
    ]
