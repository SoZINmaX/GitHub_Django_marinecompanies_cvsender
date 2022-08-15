from .settings import *
import os

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
CELERY_BROKER_URL = 'amqp://user:password@rabbitmq:5672/celery_tasks'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

STATIC_ROOT = '/static/'

SECRET_KEY = os.getenv('SECRET_KEY', 'django-insecure-8q867$0b(&2voe5o!_zh8)psj=o9+yz-b=q&+=*pdpo442$@)_')

# STATIC_URL = '/static/'
# STATIC_ROOT = '/static/'


# EMAIL_BACKEND = os.getenv('EMAIL_BACKEND', 'django.core.mail.backends.console.EmailBackend')
# EMAIL_HOST = os.getenv('EMAIL_HOST', 'aws-smtp.us-east-1.amazonaws.com')
# EMAIL_PORT = os.getenv('EMAIL_PORT', '465')
# EMAIL_USE_TLS = str(os.getenv('EMAIL_USE_TLS')).lower() in ('true', '1')
# EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER', '')
# EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD', '')

# CELERY_BROKER_URL = 'amqp://user:password@rabbitmq:5672/celery_tasks'