# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('consult', '0003_auto_20151119_1030'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor_consult',
            name='patient',
        ),
    ]
