# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20151119_1023'),
        ('consult', '0002_remove_consult_date_consult'),
    ]

    operations = [
        migrations.AddField(
            model_name='consult',
            name='date_consult',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Data que está marcada a Consulta', null=True),
        ),
        migrations.AddField(
            model_name='doctor_consult',
            name='patient',
            field=models.ForeignKey(verbose_name='Paciente', related_name='doctor_consult_Patient', to='accounts.Patient', null=True),
        ),
        migrations.AlterField(
            model_name='doctor_consult',
            name='consult',
            field=models.ForeignKey(verbose_name='Consulta', related_name='doctor_consult_Consult', to='consult.Consult'),
        ),
        migrations.AlterField(
            model_name='doctor_consult',
            name='doctor',
            field=models.ForeignKey(verbose_name='Médico', related_name='doctor_consult_Doctor', to='accounts.Doctor'),
        ),
    ]
