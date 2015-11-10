# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('consult', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='consult',
            name='status',
        ),
        migrations.AlterField(
            model_name='doctor_consult',
            name='status',
            field=models.IntegerField(default=0, verbose_name='Situação', choices=[(0, 'Realizada'), (1, 'Pendente'), (2, 'Cancelada'), (3, 'Arquivada')], blank=True),
        ),
    ]
