# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('consult', '0002_auto_20151110_1556'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor_consult',
            name='status',
            field=models.IntegerField(verbose_name='Situação', blank=True, choices=[(0, 'Realizada'), (1, 'Pendente'), (2, 'Cancelada'), (3, 'Arquivada')], default=1),
        ),
    ]
