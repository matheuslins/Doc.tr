# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_passwordreset'),
    ]

    operations = [
        migrations.AddField(
            model_name='useru',
            name='image',
            field=models.ImageField(null=True, verbose_name='Imagem', blank=True, upload_to='accounts/images'),
        ),
    ]
