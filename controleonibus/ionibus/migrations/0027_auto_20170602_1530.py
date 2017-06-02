# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-06-02 18:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ionibus', '0026_auto_20170602_1341'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='capitao',
            name='email',
        ),
        migrations.AlterField(
            model_name='responsavel',
            name='tipo',
            field=models.CharField(choices=[('EG', 'Encarregado Geral'), ('EC', 'Encarregado de Congregação'), ('EE', 'Encarregado do Evento'), ('AC', 'Ajudante de Congregação'), ('AE', 'Ajudante do Evento')], max_length=2, verbose_name='Tipo'),
        ),
    ]
