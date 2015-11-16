# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0002_auto_20151116_1739'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='register_code',
            field=models.IntegerField(verbose_name='ID', serialize=False, primary_key=True),
        ),
    ]
