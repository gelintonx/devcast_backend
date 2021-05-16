from .base import *

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'devcast_db',
        'USER': 'devcast',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '5432',

    }
}