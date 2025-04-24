`Datta Able </product/datta-able/>`__ Library
=============================================

.. title:: Django Theme Datta Able  - Standalone Library for ADMIN Section and UI Pages     
.. meta::
    :description: Django Theme (UI and Admin Section) built on top of Datta Able Design 
    :keywords: django bootstrap, django theme bootstrap, django datta able, datta able dashboard, datta able django, datta able design, bootstrap design  

Modern template for **Django Admin Section**, Auth Pages (registration included) crafted on top of **Datta Able Dashboard**, an open-source `Bootstrap` design.

- 👉 `Django Datta Able </product/datta-able/django/>`__ - Product that uses the library 
- 👉 `Django Datta Able <https://django-datta-able.appseed-srv1.com/>`__ - LIVE Demo

.. include::  /_templates/components/signin-invite.rst

Features 
--------

- Design: `Datta Able </product/datta-able/>`__ Bootstrap
- **Sections Covered**: 
    - `All pages` managed by `Django.contrib.AUTH`
    - `Registration` page
    - `Misc pages`: colors, icons, typography, blank-page 

.. image:: https://user-images.githubusercontent.com/51070104/176118649-7233ffbc-6118-4f56-8cda-baa81d256877.png
   :alt: Django Datta Able - open-source Django Admin Theme built on top of Datta Able Dashboard Design 

Why **Django Admin Datta** 
**************************

- Modern Bootstrap Design
- `Responsive Interface`
- `Minimal Template` overriding
- `Easy integration`


Installation 
------------

.. code-block:: bash

    $ pip install django-admin-datta
    // OR
    $ pip install git+https://github.com/app-generator/django-admin-datta.git

Add **admin_datta** application to the **INSTALLED_APPS Section** of your Django project **settings.py** file (note it should be before django.contrib.admin):

.. code-block:: python
    :caption: core/settings.py  

    INSTALLED_APPS = [
        ...
        'admin_datta.apps.AdminDattaConfig',
        'django.contrib.admin',
        ...
    ]

Add LOGIN_REDIRECT_URL and EMAIL_BACKEND of your Django project settings.py file:

.. code-block:: python
    :caption: core/settings.py  

    LOGIN_REDIRECT_URL = '/'
    # EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

Add **admin_datta** routing in your Django Project **urls.py** file

.. code-block:: python

    from django.urls import path, include

    urlpatterns = [
        ...
        path('', include('admin_datta.urls')),
    ]

Start the project now styled with the AdminLTE Design 

.. code-block:: bash
    :caption: Steps to start the project 

    python manage.py collectstatic
    python manage.py runserver # default port 8000    

Access the project in your preferred browser and the UI should be styled with the new design.

.. image:: https://user-images.githubusercontent.com/51070104/176118649-7233ffbc-6118-4f56-8cda-baa81d256877.png
   :alt: Django Datta Able - open-source Django Admin Theme built on top of Datta Able Dashboard Design 

.. include::  /_templates/components/generator-django.rst
        
.. include::  /_templates/components/footer-links.rst
