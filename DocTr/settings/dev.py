#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Django settings for dev. """

from .common import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '-yut7rw%%a-gg^fq$2699*-r2(ze(=_8q$f7vkzaqt3xg7x#7='


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3',
    }
}

# Templates

TEMPLATE_DIRS = [
    os.path.join(BASE_DIR, 'templates'),
    BASE_DIR,
]

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
    BASE_DIR,
)


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['*']
