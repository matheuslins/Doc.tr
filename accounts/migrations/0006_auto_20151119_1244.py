# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20151119_1243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='clinical_condition',
            field=models.TextField(blank=True, max_length=100, null=True, verbose_name='Condições Clínicas'),
        ),
    ]
