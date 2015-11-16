# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='register_code',
            field=models.IntegerField(max_length=1, primary_key=True, verbose_name='ID', serialize=False),
        ),
    ]
