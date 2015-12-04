# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0005_auto_20151119_1023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='consult',
            field=models.ForeignKey(to='consult.Doctor_consult', related_name='register_Consult', verbose_name='Consulta'),
        ),
    ]
