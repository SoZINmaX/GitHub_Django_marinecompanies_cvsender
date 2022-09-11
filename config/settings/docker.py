from .settings import *
from decouple import config

# DATABASE STUFF

NAME=config('POSTGRES_DB')
USER=config('POSTGRES_USER')
PASSWORD=config('POSTGRES_PASSWORD')
HOST=config('POSTGRES_HOST')
PORT=config('POSTGRES_PORT')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': NAME,
        'USER': USER,
        'PASSWORD': PASSWORD,
        'HOST': HOST,
        'PORT': PORT,
        'ATOMIC_REQUESTS': True
    }
}

# CELERY STUFF
CELERY_BROKER_URL = config('CELERY_BROKER_URL')
# CELERY_BROKER_URL = config('CELERY_BROKER_URL')
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

