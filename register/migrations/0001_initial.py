# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('consult', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Consult_Register',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('status', models.IntegerField(verbose_name='Situação', blank=True, choices=[(0, 'Realizada'), (1, 'Pendente'), (2, 'Cancelada'), (3, 'Arquivada')], default=1)),
                ('created_at', models.DateTimeField(verbose_name='Criado em', auto_now_add=True)),
                ('updated_at', models.DateTimeField(verbose_name='Atualizado em', auto_now=True)),
                ('consult', models.ForeignKey(verbose_name='Consulta', to='consult.Consult', related_name='consult_Consult_Register')),
            ],
            options={
                'verbose_name': 'Médico_Registro',
                'verbose_name_plural': 'Médicos_Registros',
            },
        ),
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(verbose_name='Nome do medicamento', max_length=50)),
            ],
            options={
                'verbose_name': 'Medicamento',
                'verbose_name_plural': 'Medicamentos',
            },
        ),
        migrations.CreateModel(
            name='Register',
            fields=[
                ('register_code', models.CharField(verbose_name='Código do Registro', primary_key=True, max_length=100, serialize=False, unique=True)),
                ('hospital', models.CharField(verbose_name='Hospital', max_length=50)),
                ('slug', models.SlugField(verbose_name='Atalho', max_length=150)),
                ('date_register', models.DateField(verbose_name='Data do Registro', null=True)),
                ('about', models.TextField(verbose_name='Mais informações', blank=True)),
                ('created_at', models.DateTimeField(verbose_name='Criado em', auto_now_add=True)),
                ('updated_at', models.DateTimeField(verbose_name='Atualizado em', auto_now=True)),
            ],
            options={
                'verbose_name': 'Registro',
                'verbose_name_plural': 'Registros',
                'ordering': ['slug'],
            },
        ),
        migrations.CreateModel(
            name='Exams',
            fields=[
                ('register_ptr', models.OneToOneField(primary_key=True, parent_link=True, serialize=False, to='register.Register', auto_created=True)),
                ('result', models.CharField(verbose_name='Resultado do Exame', max_length=50)),
            ],
            options={
                'verbose_name': 'Exame',
                'verbose_name_plural': 'Exames',
            },
            bases=('register.register',),
        ),
        migrations.CreateModel(
            name='Treatment',
            fields=[
                ('register_ptr', models.OneToOneField(primary_key=True, parent_link=True, serialize=False, to='register.Register', auto_created=True)),
                ('medicine', models.ForeignKey(verbose_name='Medicamento', to='register.Medicine', related_name='medicine_Treatment')),
            ],
            options={
                'verbose_name': 'Tratamento',
                'verbose_name_plural': 'Tratamentos',
            },
            bases=('register.register',),
        ),
        migrations.AddField(
            model_name='register',
            name='consult',
            field=models.ForeignKey(verbose_name='Consulta', to='consult.Consult', related_name='consult_Register'),
        ),
        migrations.AddField(
            model_name='consult_register',
            name='register',
            field=models.ForeignKey(verbose_name='Registro', to='register.Register', related_name='consult_register'),
        ),
        migrations.AlterUniqueTogether(
            name='consult_register',
            unique_together=set([('consult', 'register')]),
        ),
    ]
