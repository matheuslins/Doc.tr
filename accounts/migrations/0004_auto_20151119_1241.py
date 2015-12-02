# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20151119_1023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='blood_type',
            field=models.IntegerField(choices=[(0, 'A+'), (1, 'A-'), (2, 'B+'), (3, 'B-'), (4, 'AB+'), (5, 'AB-'), (6, 'O+'), (7, 'O-')], verbose_name='Tipo Sanguíneo', blank=True, null=True, default=1),
        ),
    ]
