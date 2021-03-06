# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-06-01 17:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ionibus', '0022_auto_20170601_1358'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='congregacao',
            name='evento',
        ),
        migrations.AddField(
            model_name='congregacao',
            name='circuito',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tasksCongregacao', to='ionibus.Circuito'),
        ),
        migrations.AlterField(
            model_name='eventos',
            name='circuito',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tasksEventos', to='ionibus.Circuito'),
        ),
        migrations.AlterField(
            model_name='eventos',
            name='local',
            field=models.CharField(blank=True, choices=[('01', 'Salão de Assembléias'), ('02', 'Ginásio Paulo Sarasate'), ('03', 'Estádio Castelão')], default='01', max_length=50, verbose_name='Local do Evento'),
        ),
    ]
