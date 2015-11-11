# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('consult', '0003_auto_20151110_1556'),
    ]

    operations = [
        migrations.CreateModel(
            name='Consult_Register',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('status', models.IntegerField(choices=[(0, 'Realizada'), (1, 'Pendente'), (2, 'Cancelada'), (3, 'Arquivada')], verbose_name='Situação', blank=True, default=1)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated_at', models.DateTimeField(verbose_name='Atualizado em', auto_now=True)),
                ('consult', models.ForeignKey(verbose_name='Consulta', related_name='consult_Consult_Register', to='consult.Consult')),
            ],
            options={
                'verbose_name': 'Médico_Registro',
                'verbose_name_plural': 'Médicos_Registros',
            },
        ),
        migrations.CreateModel(
            name='Register',
            fields=[
                ('register_code', models.CharField(verbose_name='Código do Registro', unique=True, serialize=False, max_length=100, primary_key=True)),
                ('register_type', models.CharField(verbose_name='Tipo do Registro', max_length=100)),
                ('hospital', models.CharField(verbose_name='Hospital', max_length=50)),
                ('slug', models.SlugField(verbose_name='Atalho', max_length=150)),
                ('date_register', models.DateField(verbose_name='Data do Registro', null=True)),
                ('about', models.TextField(verbose_name='Mais informações', blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated_at', models.DateTimeField(verbose_name='Atualizado em', auto_now=True)),
                ('consult', models.ForeignKey(verbose_name='Consulta', related_name='consult_Register', to='consult.Consult')),
            ],
            options={
                'verbose_name': 'Registro',
                'verbose_name_plural': 'Registros',
                'ordering': ['register_type'],
            },
        ),
        migrations.AddField(
            model_name='consult_register',
            name='register',
            field=models.ForeignKey(verbose_name='Registro', related_name='consult_register', to='register.Register'),
        ),
        migrations.AlterUniqueTogether(
            name='consult_register',
            unique_together=set([('consult', 'register')]),
        ),
    ]
