# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-06-02 19:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ionibus', '0029_auto_20170602_1611'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passageiro',
            name='capitao',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fk_cap_Passageiro', to='ionibus.Capitao'),
        ),
    ]
