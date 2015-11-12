# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='medicine',
            name='id',
        ),
        migrations.AlterField(
            model_name='medicine',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Nome do medicamento', primary_key=True, serialize=False),
        ),
    ]
