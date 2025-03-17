:og:description: Django Dynamic API - Open-Source Library 
:og:image: https://user-images.githubusercontent.com/51070104/197181145-f7458df7-23c3-4c14-bcb1-8e168882a104.jpg
:og:image:alt: A simple tool for coding Secure APIs on top of DRF and Django (open-source library) with minimal configuration effort

Django Dynamic API
==================

.. title:: Django Dynamic API - Open-Source Library 
.. meta::
    :description: A simple tool for coding Secure APIs on top of DRF and Django (open-source library) with minimal configuration effort
    :keywords: dynamic api, dynamic services, dynamic tool, django api generator

A simple tool for coding Secure APIs on top of DRF and Django (open-source library) with minimal configuration effort. Starters and services that uses the pattern:

- `Datta Able Django </product/datta-able/django/>`__ - Free Product that provides the `Dynamic API Demo <https://django-datta.onrender.com/api/product/>`__  
- `Django App Generator </tools/django-generator/>`__ - the service that include this option (PRO Users)

.. include::  /_templates/components/signin-invite.rst


Features
--------

- `API engine` provided by `DRF`
- Create, Update, Delete requests Secured by `JWT Tokens`
- `Minimal Configuration` (single line in config for each model)
- `Handles any model` defined across the project
- `CRUD` access logic:
    - `READ` is public (all items, get an item by ID)
    - `Mutating requests` are reserved for authenticated users 

.. figure:: https://user-images.githubusercontent.com/51070104/197181145-f7458df7-23c3-4c14-bcb1-8e168882a104.jpg
   :alt: A simple tool for coding Secure APIs on top of DRF and Django (open-source library)


How to use it
-------------

Step #1: Install the package
****************************

.. code-block:: shell
    
    $ pip install django-dynamic-api
    // OR
    $ pip install git+https://github.com/app-generator/django-dynamic-api.git


Step #2: Update Configuration
*****************************

.. code-block:: python 
    :caption: core/settings.py

    INSTALLED_APPS = [
        'django_dyn_api',            # Django Dynamic API  # <-- NEW
        'rest_framework',            # Include DRF         # <-- NEW 
        'rest_framework.authtoken',  # Include DRF Auth    # <-- NEW       


Step #3: - Enable Dynamic API for Model 
****************************************

.. code-block:: python 
    :caption: core/settings.py

    # Syntax: API_SLUG -> Import_PATH 
    DYNAMIC_API = {
        'books'  : "app1.models.Book",
    }

    # Used for authentication
    REST_FRAMEWORK = {
        'DEFAULT_AUTHENTICATION_CLASSES': [
            'rest_framework.authentication.SessionAuthentication',
            'rest_framework.authentication.TokenAuthentication',
        ],
    }


Step #4: - Migrate DB 
*********************

.. code-block:: shell

    $ python manage.py makemigrations
    $ python manage.py migrate


Step #5: - Update Routing 
*************************

.. code-block:: python 
    :caption: core/urls.py

    from django.contrib import admin
    from django.urls import path, include                        # <-- UPD: 'include` directive
    from rest_framework.authtoken.views import obtain_auth_token # <-- NEW

    urlpatterns = [
        path("admin/", admin.site.urls),
        path('', include('django_dyn_api.urls')),     # <-- NEW
        path('login/jwt/', view=obtain_auth_token),   # <-- NEW
    ]  


Step #7: - Use the API 
**********************

If the managed model is **Books**, the API interface is **/api/books/** and all CRUD methods are available. 

    NOTE: Note: for mutating requests, the `JWT Token` is provided by `http://localhost:8000/login/jwt/` route (the user should exist).

.. figure:: https://user-images.githubusercontent.com/51070104/197181265-eb648e27-e5cf-4f3c-b330-d000aba53c6a.jpg
   :alt: Django API Generator - POSTMAN Interface (open-source tool)   

.. include::  /_templates/components/footer-links.rst
