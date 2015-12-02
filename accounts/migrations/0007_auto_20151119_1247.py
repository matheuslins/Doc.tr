# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20151119_1244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='allergy',
            field=models.CharField(max_length=100, verbose_name='Alergias', null=True, blank=True),
        ),
        migrations.DeleteModel(
            name='Allergy',
        ),
    ]
