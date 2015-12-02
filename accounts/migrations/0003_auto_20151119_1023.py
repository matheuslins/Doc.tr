# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20151116_1805'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='allergy',
            field=models.ForeignKey(to='accounts.Allergy', related_name='allergy_Patient', blank=True, null=True, verbose_name='Alergias'),
        ),
    ]
