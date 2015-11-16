# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0003_auto_20151116_1805'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='treatment',
            name='medicine',
        ),
        migrations.AddField(
            model_name='treatment',
            name='medicine',
            field=models.ManyToManyField(null=True, verbose_name='Medicamento', blank=True, related_name='medicine_Treatment', to='register.Medicine'),
        ),
    ]
