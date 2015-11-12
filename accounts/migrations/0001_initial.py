# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import accounts.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserU',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, verbose_name='last login', null=True)),
                ('is_superuser', models.BooleanField(help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status', default=False)),
                ('name', models.CharField(max_length=100, blank=True, verbose_name='name', null=True)),
                ('email', models.EmailField(unique=True, max_length=254, verbose_name='E-mail')),
                ('phone', models.CharField(max_length=100, blank=True, verbose_name='Telefone', null=True)),
                ('username', models.CharField(unique=True, max_length=100, verbose_name='name de Usuário')),
                ('birth_data', models.CharField(max_length=100, blank=True, verbose_name='Data de Nascimento')),
                ('sex', models.CharField(max_length=1, verbose_name='Sexo', default='Masculino', choices=[('M', 'Masculino'), ('F', 'Feminino')])),
                ('is_active', models.BooleanField(verbose_name='Está ativo?', default=True)),
                ('is_staff', models.BooleanField(verbose_name='É da equipe?', default=False)),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='Data de Entrada')),
            ],
            options={
                'verbose_name_plural': 'Usuários',
                'verbose_name': 'Usuário',
            },
            managers=[
                ('objects', accounts.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('useru_ptr', models.OneToOneField(to=settings.AUTH_USER_MODEL, serialize=False, auto_created=True, primary_key=True, parent_link=True)),
                ('crm', models.CharField(unique=True, max_length=100, verbose_name='CRM')),
            ],
            options={
                'verbose_name_plural': 'Médicos',
                'verbose_name': 'Médico',
            },
            bases=('accounts.useru',),
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('useru_ptr', models.OneToOneField(to=settings.AUTH_USER_MODEL, serialize=False, auto_created=True, primary_key=True, parent_link=True)),
            ],
            options={
                'verbose_name_plural': 'Pacientes',
                'verbose_name': 'Paciente',
            },
            bases=('accounts.useru',),
        ),
        migrations.AddField(
            model_name='useru',
            name='groups',
            field=models.ManyToManyField(related_name='user_set', to='auth.Group', verbose_name='groups', related_query_name='user', blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.'),
        ),
        migrations.AddField(
            model_name='useru',
            name='user_permissions',
            field=models.ManyToManyField(related_name='user_set', to='auth.Permission', verbose_name='user permissions', related_query_name='user', blank=True, help_text='Specific permissions for this user.'),
        ),
    ]
