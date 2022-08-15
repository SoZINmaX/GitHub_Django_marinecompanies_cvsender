import os
from invoke import task


@task
def run(ctx):
    print('Migrating db')
    ctx.run('./manage.py migrate')
    print('Collecting static')
    ctx.run('./manage.py collectstatic --noinput')

    cmd = ('uwsgi --http 0.0.0.0:8000 --master '
           '--module "django.core.wsgi:get_wsgi_application()" '
           '--processes 2 '
           '--offload-threads 4 '
           '--enable-threads '
           '--static-map /static=/static')

    if os.getenv('PY_AUTORELOAD'):
        cmd += ' --py-autoreload 1'
    else:
        cmd += ' --harakiri 30'
    ctx.run(cmd)