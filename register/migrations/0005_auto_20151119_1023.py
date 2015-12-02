# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0004_auto_20151116_1825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='treatment',
            name='medicine',
            field=models.ManyToManyField(to='register.Medicine', related_name='medicine_Treatment', verbose_name='Medicamento', blank=True),
        ),
    ]
