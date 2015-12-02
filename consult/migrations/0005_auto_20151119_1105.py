# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20151119_1023'),
        ('consult', '0004_remove_doctor_consult_patient'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='consult',
            name='patient',
        ),
        migrations.AddField(
            model_name='doctor_consult',
            name='patient',
            field=models.ForeignKey(null=True, related_name='doctor_consult_Patient', blank=True, verbose_name='Paciente', to='accounts.Patient'),
        ),
    ]
