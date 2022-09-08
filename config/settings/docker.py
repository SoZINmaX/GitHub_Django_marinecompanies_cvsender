from .settings import *
import os
from decouple import config

# DATABASE STUFF
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.getenv('POSTGRES_DB', 'djangodb_marinecv'),
        'USER': os.getenv('POSTGRES_USER', 'postgres'),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD', '123'),
        'HOST': os.getenv('POSTGRES_HOST', 'db'),
        'PORT': os.getenv('POSTGRES_PORT', '5432'),
        'ATOMIC_REQUESTS': True
    }
}

# CELERY STUFF
CELERY_BROKER_URL = config('CELERY_BROKER_URL')

# VOLUMES
MEDIA_URL = '/media/'
MEDIA_ROOT = '/media/'

STATIC_URL = '/static/'
STATIC_ROOT = '/static/'

# SECRET KEY
SECRET_KEY = config('DJANGO_SECRET_KEY')

# EMAIL STUFF
EMAIL_BACKEND = config('EMAIL_BACKEND')
EMAIL_HOST = config('EMAIL_HOST')
EMAIL_PORT = config('EMAIL_PORT')
EMAIL_USE_TLS = config('EMAIL_USE_TLS')
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')

