# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Consult',
            fields=[
                ('consult_code', models.CharField(unique=True, max_length=100, verbose_name='Código da Consulta', primary_key=True, serialize=False)),
                ('consult_type', models.CharField(max_length=100, verbose_name='Tipo de Consulta')),
                ('hospital', models.CharField(max_length=50, verbose_name='Hospital')),
                ('slug', models.SlugField(max_length=150, verbose_name='Atalho')),
                ('date_consult', models.DateField(verbose_name='Data da Consulta', null=True)),
                ('about', models.TextField(blank=True, verbose_name='Mais informações')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
                ('doctor', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='consult_médico', verbose_name='Médico')),
                ('patient', models.ForeignKey(to='accounts.Patient', related_name='consult_paciente', verbose_name='Paciente', blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Consultas',
                'verbose_name': 'Consulta',
                'ordering': ['consult_type'],
            },
        ),
        migrations.CreateModel(
            name='Doctor_consult',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('status', models.IntegerField(blank=True, verbose_name='Situação', default=1, choices=[(0, 'Realizada'), (1, 'Pendente'), (2, 'Cancelada'), (3, 'Arquivada')])),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
                ('consult', models.ForeignKey(to='consult.Consult', related_name='doctor_consult', verbose_name='Consulta')),
                ('doctor', models.ForeignKey(to='accounts.Doctor', related_name='doctor_consult', verbose_name='Médico')),
            ],
            options={
                'verbose_name_plural': 'Médicos_Consultas',
                'verbose_name': 'Médico_Consulta',
            },
        ),
        migrations.AlterUniqueTogether(
            name='doctor_consult',
            unique_together=set([('doctor', 'consult')]),
        ),
    ]
