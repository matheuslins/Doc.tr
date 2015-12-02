# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20151119_1241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='blood_type',
            field=models.IntegerField(null=True, choices=[(0, 'A+'), (1, 'A-'), (2, 'B+'), (3, 'B-'), (4, 'AB+'), (5, 'AB-'), (6, 'O+'), (7, 'O-')], blank=True, verbose_name='Tipo Sanguíneo'),
        ),
    ]
