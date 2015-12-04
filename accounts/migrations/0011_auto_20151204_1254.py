# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_useru_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useru',
            name='birth_data',
            field=models.CharField(blank=True, null=True, verbose_name='Data de Nascimento', max_length=100),
        ),
        migrations.AlterField(
            model_name='useru',
            name='sex',
            field=models.CharField(blank=True, choices=[('M', 'Masculino'), ('F', 'Feminino')], verbose_name='Sexo', default='Masculino', max_length=1),
        ),
    ]
