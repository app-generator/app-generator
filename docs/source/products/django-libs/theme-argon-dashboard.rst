Admin Argon  
===========

.. title:: Django Theme Argon Dashboard   - Standalone Library for Ui and ADMIN Section     
.. meta::
    :description: Django Theme (UI and Admin Section) built on top of Argon Dashboard Design 
    :keywords: django bootstrap, django dark theme, django argon ui library, argon dashboard, dark dashboard django, argon dashboard design, bootstrap design  

Modern template for **Django Admin Section**, Auth Pages (registration included) crafted on top of **Argon Dashboard**, an open-source `Bootstrap` design.

- 👉 `Django Argon Dashboard </product/argon-dashboard/django/>`__ - Product that uses the library 
- 👉 `Django Argon Dashboard <https://django-argon-dash2.onrender.com/>`__ - LIVE Demo

.. include::  /_templates/components/signin-invite.rst

Features 
--------

- Design: `Argon Dashboard </docs/templates/bootstrap/argon-dashboard.html>`__ Bootstrap
- **Sections Covered**: 
    - `Admin Section`, reserved for `superusers`
    - `All pages` managed by `Django.contrib.AUTH`
    - `Registration` page
    - `Misc pages`: colors, icons, typography, blank-page 

.. image:: https://user-images.githubusercontent.com/51070104/215804889-94eba681-8262-41a3-8e57-7d5b12dcc209.png
   :alt: Django Argon Dashboard - open-source Django Admin Theme built on top of Black Dashboard Design from Creative-Tim

Why **Django Admin Argon** 
*****************************

- Modern Bootstrap Design
- Responsive Interface
- Minimal Template overriding
- Easy integration


Installation 
------------

.. code-block:: bash

    $ pip install django-admin-argon-dashboard
    // OR
    $ pip install git+https://github.com/app-generator/django-admin-argon-dashboard.git

Add **admin_argon** application to the **INSTALLED_APPS Section** of your Django project **settings.py** file (note it should be before django.contrib.admin):

.. code-block:: python
    :caption: core/settings.py  

    INSTALLED_APPS = [
        ...
        'admin_argon.apps.AdminArgonConfig',
        'django.contrib.admin',
        ...
    ]

Add LOGIN_REDIRECT_URL and EMAIL_BACKEND of your Django project settings.py file:

.. code-block:: python
    :caption: core/settings.py  

    LOGIN_REDIRECT_URL = '/'
    # EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

Add **admin_argon** routing in your Django Project **urls.py** file

.. code-block:: python

    from django.urls import path, include

    urlpatterns = [
        ...
        path('', include('admin_argon.urls')),
    ]

Start the project now styled with the AdminLTE Design 

.. code-block:: bash
    :caption: Steps to start the project 

    python manage.py collectstatic
    python manage.py runserver # default port 8000    

Access the project in your preferred browser and the UI should be styled with the new design.

.. image:: https://user-images.githubusercontent.com/51070104/215804889-94eba681-8262-41a3-8e57-7d5b12dcc209.png
   :alt: Django Argon Dashboard - open-source Django Admin Theme built on top of Black Dashboard Design from Creative-Tim

.. include::  /_templates/components/generator-django.rst
        
.. include::  /_templates/components/footer-links.rst
