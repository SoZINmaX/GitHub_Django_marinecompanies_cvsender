from .settings import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'djangodb_marinecv',
        'USER': 'postgres',
        'PASSWORD': '123',
        'HOST': 'db',
        'PORT': '5432',
        'ATOMIC_REQUESTS': True,
    }
}

# CELERY STUFF
CELERY_BROKER_URL = 'amqp://user:password@rabbitmq:5672/celery_tasks'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

STATIC_ROOT = '/static/'