Tabler 
=======

.. title:: Django Theme Tabler  - Standalone library for Ui and ADMIN Section     
.. meta::
    :description: Django Theme (UI and Admin Section) built on top of Tabler Design    
    :keywords: django, django theme, django ui library, tabler, tabler django, tabler design  

**Django Theme tabler** is a standalone library for UI and Django ADMIN Section 

- 👉 `Django Tabler </docs/products/django/tabler/index.html>`__ - Product that uses the library 
- 👉 `Django Tabler <https://django-tabler.onrender.com/>`__ - LIVE Demo

.. include::  /_templates/components/signin-invite.rst


Installation 
------------

.. code-block:: bash

    pip install django-admin-tabler
    // OR 
    pip install git+https://github.com/app-generator/django-admin-tabler.git

Add **admin_adminlte** application to the **INSTALLED_APPS Section** of your Django project **settings.py** file (note it should be before django.contrib.admin):

.. code-block:: python
    :caption: core/settings.py  

    INSTALLED_APPS = [
        ...
        'admin_adminlte.apps.AdminTablerConfig',
        'django.contrib.admin',
        ...
    ]

Add LOGIN_REDIRECT_URL and EMAIL_BACKEND of your Django project settings.py file:

.. code-block:: python
    :caption: core/settings.py  

    LOGIN_REDIRECT_URL = '/'
    # EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

Add **admin_adminlte** routing in your Django Project **urls.py** file

.. code-block:: python

    from django.urls import path, include

    urlpatterns = [
        ...
        path('', include('admin_tabler.urls')),
    ]

Start the project now styled with the AdminLTE Design 

.. code-block:: bash
    :caption: Steps to start the project 

    python manage.py collectstatic
    python manage.py runserver # default port 8000    

Access the project in your preferred browser and the UI should be styled with the new design.

.. image:: https://github.com/user-attachments/assets/826e18b5-998d-41ec-b57b-35654c210a9b
   :alt: Homepage Django Tabler - open-source starter built on top of Tabler Design 

Resources
---------

- 👉 New to **AppSeed**? Join our 8k+ Community using GitHub `One-Click SignIN  </users/signin/>`__.
- 👉 ``Download`` `products </product/>`__ and start fast a new project 
- 👉 Bootstrap your startUp, MVP or Legacy project with a `custom development </custom-development/>`__  sprint
