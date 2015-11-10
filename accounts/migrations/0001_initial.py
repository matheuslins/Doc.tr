# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import accounts.models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserU',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, verbose_name='last login', null=True)),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('name', models.CharField(max_length=100, blank=True, verbose_name='name', null=True)),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='E-mail')),
                ('phone', models.CharField(max_length=100, blank=True, verbose_name='Telefone', null=True)),
                ('username', models.CharField(max_length=100, unique=True, verbose_name='name de Usuário')),
                ('birth_data', models.CharField(max_length=100, blank=True, verbose_name='Data de Nascimento')),
                ('sex', models.CharField(max_length=1, default='Masculino', choices=[('M', 'Masculino'), ('F', 'Feminino')], verbose_name='Sexo')),
                ('is_active', models.BooleanField(default=True, verbose_name='Está ativo?')),
                ('is_staff', models.BooleanField(default=False, verbose_name='É da equipe?')),
                ('date_joined', models.DateTimeField(verbose_name='Data de Entrada', auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Usuário',
                'verbose_name_plural': 'Usuários',
            },
            managers=[
                ('objects', accounts.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('useru_ptr', models.OneToOneField(to=settings.AUTH_USER_MODEL, primary_key=True, serialize=False, auto_created=True, parent_link=True)),
                ('crm', models.CharField(max_length=100, unique=True, verbose_name='CRM')),
            ],
            options={
                'verbose_name': 'Médico',
                'verbose_name_plural': 'Médicos',
            },
            bases=('accounts.useru',),
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('useru_ptr', models.OneToOneField(to=settings.AUTH_USER_MODEL, primary_key=True, serialize=False, auto_created=True, parent_link=True)),
            ],
            options={
                'verbose_name': 'Paciente',
                'verbose_name_plural': 'Pacientes',
            },
            bases=('accounts.useru',),
        ),
        migrations.AddField(
            model_name='useru',
            name='groups',
            field=models.ManyToManyField(to='auth.Group', help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', blank=True, related_name='user_set', related_query_name='user', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='useru',
            name='user_permissions',
            field=models.ManyToManyField(to='auth.Permission', help_text='Specific permissions for this user.', blank=True, related_name='user_set', related_query_name='user', verbose_name='user permissions'),
        ),
    ]
