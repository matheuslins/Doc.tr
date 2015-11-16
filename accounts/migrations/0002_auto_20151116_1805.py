# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0003_auto_20151116_1805'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Allergy',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('allergy_name', models.CharField(blank=True, verbose_name='Nome da Alergia', max_length=100, null=True)),
            ],
            options={
                'verbose_name_plural': 'Alergias',
                'verbose_name': 'Alergia',
            },
        ),
        migrations.AddField(
            model_name='patient',
            name='address',
            field=models.CharField(blank=True, verbose_name='Endereço', max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='blood_type',
            field=models.CharField(blank=True, verbose_name='Tipo Sanguíneo', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='clinical_condition',
            field=models.CharField(blank=True, verbose_name='Condições Clínicas', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='comment',
            field=models.TextField(verbose_name='Observações', blank=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='height',
            field=models.CharField(blank=True, verbose_name='Altura', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='medicine',
            field=models.ForeignKey(related_name='medicine_Patient', verbose_name='Medicamentos', null=True, blank=True, to='register.Medicine'),
        ),
        migrations.AddField(
            model_name='patient',
            name='weight',
            field=models.CharField(blank=True, verbose_name='Peso', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='allergy',
            field=models.ForeignKey(related_name='allergy_Patient', verbose_name='Medicamentos', null=True, blank=True, to='accounts.Allergy'),
        ),
    ]
