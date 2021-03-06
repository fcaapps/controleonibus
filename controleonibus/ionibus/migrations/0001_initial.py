# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-14 17:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Capitao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('congregacao', models.IntegerField(verbose_name='Congregação')),
                ('telefone1', models.CharField(max_length=30, verbose_name='Telefone 1')),
                ('telefone2', models.CharField(max_length=30, verbose_name='Telefone 2')),
                ('email', models.CharField(max_length=100, verbose_name='E-mail')),
                ('foto', models.ImageField(blank=True, null=True, upload_to='ionibus/images', verbose_name='Imagem')),
                ('criado_em', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('atualizado_em', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
            ],
        ),
        migrations.CreateModel(
            name='Congregacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('coordenador', models.CharField(max_length=50, verbose_name='Coordenador')),
                ('tel_coordenador', models.CharField(max_length=30, verbose_name='Telefone Coordenador')),
                ('email_coordenador', models.CharField(max_length=100, verbose_name='E-mail')),
                ('criado_em', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('atualizado_em', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
            ],
        ),
        migrations.CreateModel(
            name='Eventos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=2, verbose_name='Tipo')),
                ('data_evento', models.DateField(blank=True, null=True, verbose_name='Data do Evento')),
                ('texto_base', models.CharField(max_length=30, verbose_name='Texto Base')),
                ('criado_em', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('atualizado_em', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
            ],
        ),
        migrations.CreateModel(
            name='Passageiro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('congregacao', models.IntegerField(verbose_name='Congregação')),
                ('rg_cpf', models.CharField(max_length=30, verbose_name='RG/CPF')),
                ('capitao', models.IntegerField(verbose_name='Capitão')),
                ('crianca_colo', models.CharField(max_length=1, verbose_name='Criança de Colo')),
                ('observacao', models.TextField(blank=True, verbose_name='Criança de Colo')),
                ('criado_em', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('atualizado_em', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
            ],
        ),
        migrations.CreateModel(
            name='Responsavel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('tipo', models.CharField(max_length=2, verbose_name='Tipo')),
                ('congregacao', models.IntegerField(verbose_name='Congregação')),
                ('email', models.CharField(max_length=100, verbose_name='E-mail')),
                ('telefone', models.CharField(max_length=30, verbose_name='Telefone')),
                ('foto', models.ImageField(blank=True, null=True, upload_to='ionibus/images', verbose_name='Imagem')),
                ('criado_em', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('atualizado_em', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
            ],
        ),
    ]
