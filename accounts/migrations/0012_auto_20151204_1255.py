# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_auto_20151204_1254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='comment',
            field=models.TextField(null=True, blank=True, verbose_name='Observações'),
        ),
    ]
