# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('consult', '0006_auto_20151125_1100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consult',
            name='about',
            field=models.TextField(verbose_name='Mais informações', blank=True),
        ),
    ]
