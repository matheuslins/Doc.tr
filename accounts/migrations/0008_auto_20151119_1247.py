# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20151119_1247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='allergy',
            field=models.TextField(verbose_name='Alergias', null=True, blank=True, max_length=100),
        ),
    ]
