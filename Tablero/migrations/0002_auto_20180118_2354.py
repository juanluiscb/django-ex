# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-19 05:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Tablero', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='encuentro',
            name='equipo1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Equipo1', to='Tablero.Equipo', verbose_name='Equipo1'),
        ),
        migrations.AlterField(
            model_name='encuentro',
            name='equipo2',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Equipo2', to='Tablero.Equipo', verbose_name='Equipo2'),
        ),
    ]
