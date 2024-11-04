Static Files 
============

This page provides a comprehensive guide covering all aspects of Django static files management. Here are the key points to highlight:

- The guide covers both development and production configurations
- Shows multiple methods for overriding third-party static files
- Includes best practices for organization and performance
- Provides example configurations for popular deployment options

.. include::  /_templates/components/banner-top.rst

Basic Setup
-----------

Settings Configuration
**********************

.. code-block:: python

    # settings.py

    # Base directory for static files collection
    STATIC_URL = '/static/'
    STATIC_ROOT = BASE_DIR / 'staticfiles'  # Where collectstatic will collect files

    # Additional locations of static files
    STATICFILES_DIRS = [
        BASE_DIR / 'static',  # Your project's static files
    ]

    # Static file finders - how Django looks for static files
    STATICFILES_FINDERS = [
        'django.contrib.staticfiles.finders.FileSystemFinder',     # Looks in STATICFILES_DIRS
        'django.contrib.staticfiles.finders.AppDirectoriesFinder', # Looks in app/static/
    ]    


Project Structure
*****************

.. code-block:: bash

    myproject/
    ├── myproject/
    │   ├── settings.py
    │   └── urls.py
    ├── static/                  # Project-level static files
    │   ├── css/
    │   ├── js/
    │   └── images/
    ├── myapp/
    │   └── static/             # App-level static files
    │       └── myapp/          # Namespace to avoid conflicts
    │           ├── css/
    │           ├── js/
    │           └── images/
    └── staticfiles/            # Collected static files (production)


Development vs Production
-------------------------

Development
***********

.. code-block:: python 

    # settings/development.py
    DEBUG = True

    # Django's development server will automatically serve static files
    # No need to run collectstatic

Production
**********

.. code-block:: python 

    # settings/production.py
    DEBUG = False

    # Additional settings for production
    STATIC_ROOT = BASE_DIR / 'staticfiles'
    STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'

    # Optional: Configure compression and caching
    STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.CompressedManifestStaticFilesStorage'

Collecting Static Files
***********************

.. code-block:: bash

    # Collect all static files to STATIC_ROOT
    python manage.py collectstatic

    # Force collection even if files exist
    python manage.py collectstatic --clear --no-input


Overriding Third-Party Static Files
-----------------------------------

Method 1: Using STATICFILES_DIRS
********************************

.. code-block:: python 

    # settings.py
    STATICFILES_DIRS = [
        # Override specific files from third-party packages
        ('admin/css/base.css', '/path/to/your/custom/base.css'),
        # General static files directory
        BASE_DIR / 'static',
    ]    
    

Method 2: App-Level Override
****************************

.. code-block:: bash 

    myapp/
    └── static/
        └── third_party_app/  # Same name as the app you're overriding
            └── css/
                └── style.css  # File to override

Method 3: Using Template Loading Order
**************************************

.. code-block:: python 

    # settings.py
    INSTALLED_APPS = [
        'myapp',  # Your app first
        'third_party_app',  # Third-party app second
        # ... other apps
    ]

Using Static Files in Templates
-------------------------------

Template Tags
*************

.. code-block:: html 

    {% load static %}

    <!-- Basic usage -->
    <link href="{% static 'css/style.css' %}" rel="stylesheet">
    <img src="{% static 'images/logo.png' %}" alt="Logo">

    <!-- With variables -->
    <img src="{% static image_path %}" alt="{{ image_alt }}">     

Handling Missing Files
***********************

.. code-block:: python 

    # settings.py
    STATIC_URL = '/static/'
    STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'

    # Optional: Custom storage class for better error handling
    from django.contrib.staticfiles.storage import ManifestStaticFilesStorage

    class CustomManifestStaticFilesStorage(ManifestStaticFilesStorage):
        def hashed_name(self, name, content=None, filename=None):
            try:
                result = super().hashed_name(name, content, filename)
            except ValueError:
                # Return original name if hashing fails
                result = name
            return result

Serving Static Files in Production
----------------------------------

Using Whitenoise
****************

.. code-block:: python 

    # settings.py
    MIDDLEWARE = [
        # ...
        'whitenoise.middleware.WhiteNoiseMiddleware',
    ]

    # WhiteNoise configuration
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

    # Optional: Enable Brotli compression
    WHITENOISE_USE_FINDERS = True
    WHITENOISE_COMPRESSION_QUALITY = 100    


Using Nginx
***********

.. code-block:: nginx

    # nginx.conf
    server {
        # ...
        location /static/ {
            alias /path/to/your/staticfiles/;
            expires 30d;
            add_header Cache-Control "public, no-transform";
        }
    }     


Best Practices
--------------


Using Content Delivery Networks (CDN)
*************************************

.. code-block:: python 

    # settings.py
    # Use different static URLs based on environment
    if not DEBUG:
        STATIC_URL = 'https://your-cdn.com/static/'    

Organizing Static Files
***********************

.. code-block:: python 

    # Use namespaced folders to avoid conflicts
    STATICFILES_DIRS = [
        BASE_DIR / 'static' / 'common',  # Shared assets
        BASE_DIR / 'static' / 'vendor',  # Third-party assets
    ]

Cache Control
*************

.. code-block:: python 

    # settings.py
    AWS_S3_OBJECT_PARAMETERS = {  # If using S3
        'CacheControl': 'max-age=86400',
    }

    # Or in nginx
    location /static/ {
        expires max;
        add_header Cache-Control "public, no-transform";
    }    

.. include::  /_templates/components/footer-links.rst
