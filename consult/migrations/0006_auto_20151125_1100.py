# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('consult', '0005_auto_20151119_1105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consult',
            name='about',
            field=models.CharField(max_length=100, verbose_name='Mais informações', blank=True),
        ),
    ]
