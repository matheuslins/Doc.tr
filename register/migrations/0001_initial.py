# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('consult', '0002_remove_consult_date_consult'),
    ]

    operations = [
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('name', models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='Nome do medicamento')),
            ],
            options={
                'verbose_name_plural': 'Medicamentos',
                'verbose_name': 'Medicamento',
            },
        ),
        migrations.CreateModel(
            name='Register',
            fields=[
                ('register_code', models.IntegerField(max_length=1, primary_key=True, default=0, serialize=False, verbose_name='ID')),
                ('about', models.TextField(blank=True, verbose_name='Mais informações')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
                ('slug', models.SlugField(max_length=150, verbose_name='Atalho')),
            ],
            options={
                'ordering': ['register_code'],
                'verbose_name_plural': 'Registros',
                'verbose_name': 'Registro',
            },
        ),
        migrations.CreateModel(
            name='Exams',
            fields=[
                ('register_ptr', models.OneToOneField(parent_link=True, auto_created=True, serialize=False, primary_key=True, to='register.Register')),
                ('result', models.TextField(max_length=50, null=True, blank=True, verbose_name='Resultado do Exame')),
            ],
            options={
                'verbose_name_plural': 'Exames',
                'verbose_name': 'Exame',
            },
            bases=('register.register',),
        ),
        migrations.CreateModel(
            name='Treatment',
            fields=[
                ('register_ptr', models.OneToOneField(parent_link=True, auto_created=True, serialize=False, primary_key=True, to='register.Register')),
                ('medicine', models.ForeignKey(blank=True, to='register.Medicine', verbose_name='Medicamento', null=True, related_name='medicine_Treatment')),
            ],
            options={
                'verbose_name_plural': 'Tratamentos',
                'verbose_name': 'Tratamento',
            },
            bases=('register.register',),
        ),
        migrations.AddField(
            model_name='register',
            name='consult',
            field=models.ForeignKey(to='consult.Consult', related_name='register_Consult', verbose_name='Consulta'),
        ),
    ]
