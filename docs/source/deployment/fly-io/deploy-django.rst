Deploy Django
=============

.. title:: Django Deployment Guide for Fly.io
.. meta::
    :description: Learn how to deploy Django projects on Fly.io  
    :keywords: django on fly.io, django fly.io cloud, django fly.io deployment, fly.io cloud tools, deploy, ci-cd, deployment  

This page explains how to deploy a `Django <../../technologies/django/index.html>`__ project on `Fly.io <./index.html>`__, the popular deployment platform for developers. 

.. include::  /_templates/components/banner-top.rst

Framework Overview
------------------

Django is a high-level Python web framework that follows the model-template-view (MTV) architectural pattern. 
It implements the "batteries included" philosophy, providing robust built-in features for authentication, admin interface, ORM, and security. 

Django is particularly suited for data-driven applications, content management systems, and enterprise-grade web applications.

Deployment Configuration
------------------------

Project Structure
*****************

Standard Django application structure for deployment:

..	code-block:: bash

    ├── app/
    │   ├── __init__.py
    │   ├── asgi.py
    │   ├── settings/
    │   │   ├── __init__.py
    │   │   ├── base.py
    │   │   └── production.py
    │   ├── urls.py
    │   └── wsgi.py
    ├── manage.py
    ├── requirements.txt
    ├── Dockerfile
    ├── staticfiles/
    └── media/

### Essential Files Configuration

1. `requirements.txt`:

..	code-block:: text
    
    Django==5.0.0
    gunicorn==21.2.0
    psycopg2-binary==2.9.9
    whitenoise==6.6.0
    dj-database-url==2.1.0
    django-environ==0.11.2

2. `Dockerfile`:

..	code-block:: dockerfile


    FROM python:3.11-slim

    # Set environment variables
    ENV PYTHONDONTWRITEBYTECODE=1
    ENV PYTHONUNBUFFERED=1
    ENV DJANGO_SETTINGS_MODULE=app.settings.production

    # Set work directory
    WORKDIR /app

    # Install system dependencies
    RUN apt-get update && apt-get install -y \
        build-essential \
        libpq-dev \
        && rm -rf /var/lib/apt/lists/*

    # Install Python dependencies
    COPY requirements.txt .
    RUN pip install --no-cache-dir -r requirements.txt

    # Copy project
    COPY . .

    # Collect static files
    RUN python manage.py collectstatic --noinput

    # Run migrations
    RUN python manage.py makemigrations

    EXPOSE 8000

    # Start Gunicorn
    CMD ["gunicorn", "--bind", "0.0.0.0:8000", "app.wsgi:application"]


3. `app/settings/base.py`:

..	code-block:: python

    import os
    import environ

    env = environ.Env()

    # Read environment variables
    environ.Env.read_env()

    SECRET_KEY = env('DJANGO_SECRET_KEY')

    DEBUG = env.bool('DJANGO_DEBUG', False)

    ALLOWED_HOSTS = env.list('DJANGO_ALLOWED_HOSTS', default=['*'])

    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'whitenoise.runserver_nostatic',
        # Add your apps here
    ]

    MIDDLEWARE = [
        'django.middleware.security.SecurityMiddleware',
        'whitenoise.middleware.WhiteNoiseMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ]

    DATABASES = {
        'default': env.db('DATABASE_URL', default='sqlite:///db.sqlite3')
    }

    STATIC_URL = '/static/'
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


4. `app/settings/production.py`:

..	code-block:: python

    from .base import *

    DEBUG = False

    SECURE_SSL_REDIRECT = True
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True

    # HSTS settings
    SECURE_HSTS_SECONDS = 31536000
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True

5. `.dockerignore`:

..	code-block:: python

    *.pyc
    *.pyo
    *.mo
    *.db
    *.css.map
    *.egg-info
    *.sql.gz
    .cache
    .project
    .idea
    .pydevproject
    .idea/workspace.xml
    .DS_Store
    .git/
    .gitignore
    .env
    .venv/
    env/
    venv/
    ENV/
    staticfiles/
    media/

Fly.io Configuration
********************

1. `fly.toml`:

..	code-block:: toml

    app = "your-django-app"
    primary_region = "dfw"

    [build]
        dockerfile = "Dockerfile"

    [env]
        PORT = "8000"
        DJANGO_SETTINGS_MODULE = "app.settings.production"

    [http_service]
        internal_port = 8000
        force_https = true
        auto_stop_machines = true
        auto_start_machines = true
        min_machines_running = 1
        processes = ["app"]

    [[vm]]
        cpu_kind = "shared"
        cpus = 1
        memory_mb = 512

    [mounts]
        source = "django_media"
        destination = "/app/media"

    [deploy]
        release_command = "python manage.py migrate"


Deployment Process
------------------

1. Initialize Fly.io application:

..	code-block:: bash 

    fly launch

2. Configure environment variables:

..	code-block:: bash 

    fly secrets set DJANGO_SECRET_KEY="your-secret-key"
    fly secrets set DJANGO_DEBUG="False"
    fly secrets set DJANGO_ALLOWED_HOSTS=".fly.dev"

3. Create and attach PostgreSQL database:

..	code-block:: bash 

    fly postgres create
    fly postgres attach <database-name>

4. Deploy the application:

..	code-block:: bash 

    fly deploy

Database Management
-------------------

1. Run migrations:

..	code-block:: bash 

    fly ssh console -C "python manage.py migrate"

2. Create superuser:

..	code-block:: bash 

    fly ssh console -C "python manage.py createsuperuser"


Static Files and Media Storage
------------------------------

1. Configure WhiteNoise for static files:

..	code-block:: python

    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

2. For media files, configure volume storage:

..	code-block:: bash 

    fly volumes create django_media --size 1

Security Configuration
----------------------

1. Update `settings/production.py`:

..	code-block:: python

    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True

2. Configure CORS if needed:

..	code-block:: python

    CORS_ALLOWED_ORIGINS = [
        "https://your-domain.fly.dev",
    ]

Monitoring and Logging
----------------------

1. Configure Django logging:

..	code-block:: python

    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'handlers': {
            'console': {
                'class': 'logging.StreamHandler',
            },
        },
        'root': {
            'handlers': ['console'],
            'level': 'INFO',
        },
    }


2. Monitor application:

..	code-block:: bash 

    fly logs
    fly status

## Performance Optimization

1. Configure Gunicorn workers in `gunicorn.conf.py`:

..	code-block:: python

    import multiprocessing

    bind = "0.0.0.0:8000"
    workers = multiprocessing.cpu_count() * 2 + 1
    worker_class = "gthread"
    threads = 2
    max_requests = 1000
    max_requests_jitter = 50

2. Implement caching:

..	code-block:: python

    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.redis.RedisCache',
            'LOCATION': env('REDIS_URL'),
        }
    }

Health Checks
-------------

1. Create health check view:

..	code-block:: python

    # health/views.py
    from django.http import JsonResponse
    from django.db import connections
    from django.db.utils import OperationalError

    def health_check(request):
        try:
            connections['default'].ensure_connection()
            return JsonResponse({"status": "healthy"})
        except OperationalError:
            return JsonResponse({"status": "unhealthy"}, status=500)


2. Update `fly.toml`:

..	code-block:: toml

    [checks]
        [checks.health]
            port = 8000
            type = "http"
            interval = "15s"
            timeout = "2s"
            grace_period = "5s"
            method = "GET"
            path = "/health"

## Common Issues and Solutions

1. **Static Files Not Serving**
   - Verify STATIC_ROOT configuration
   - Ensure collectstatic runs in Dockerfile
   - Check WhiteNoise configuration

2. **Database Connectivity**
   - Verify DATABASE_URL environment variable
   - Check database instance status
   - Review connection pool settings

3. **Media Files**
   - Ensure volume is properly mounted
   - Check file permissions
   - Verify media URL configuration

This guide provides a comprehensive approach to deploying Django applications on Fly.io. Regular monitoring and maintenance are essential for optimal performance.

.. include::  /_templates/components/footer-links.rst
