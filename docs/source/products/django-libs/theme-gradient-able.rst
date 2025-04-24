Admin Gradient
==============

.. title:: Django Theme Gradient Able  - Standalone Library for ADMIN Section and UI Pages     
.. meta::
    :description: Django Theme (UI and Admin Section) built on top of Gradient Able Design 
    :keywords: gradient able, gradient design, gradient able theme, django bootstrap, django gradient able, gradient able dashboard, gradient able django 

Modern template for **Django Admin Section**, Auth Pages (registration included) crafted on top of **Gradient Able Dashboard**, an open-source `Bootstrap` design.

- 👉 `Django Gradient Able </product/gradient-able/django/>`__ - Product that uses the library 
- 👉 `Django Gradient Able <https://django-gradient-able.appseed-srv1.com/>`__ - LIVE Demo

.. include::  /_templates/components/signin-invite.rst

Features 
--------

- Design: `Gradient Able </product/gradient-able/>`__ Bootstrap
- **Sections Covered**: 
    - `All pages` managed by `Django.contrib.AUTH`
    - `Registration` page
    - `Misc pages`: colors, icons, typography, blank-page 

.. image:: https://user-images.githubusercontent.com/51070104/171583187-c4ca1bef-b535-458e-9250-8d62ba1f5b30.png
   :alt: Django Gradient Able - open-source Django Admin Theme built on top of Gradient Able Dashboard Design 

Why **Django Admin Gradient** 
*****************************

- Modern Bootstrap Design
- `Responsive Interface`
- `Minimal Template` overriding
- `Easy integration`


Installation 
------------

.. code-block:: bash

    $ pip install django-admin-gradient
    // OR
    $ pip install git+https://github.com/app-generator/django-admin-gradient.git

Add **admin_gradient** application to the **INSTALLED_APPS Section** of your Django project **settings.py** file (note it should be before django.contrib.admin):

.. code-block:: python
    :caption: core/settings.py  

    INSTALLED_APPS = [
        ...
        'admin_gradient.apps.AdminGradientConfig',
        'django.contrib.admin',
        ...
    ]

Add LOGIN_REDIRECT_URL and EMAIL_BACKEND of your Django project settings.py file:

.. code-block:: python
    :caption: core/settings.py  

    LOGIN_REDIRECT_URL = '/'
    # EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

Add **admin_gradient** routing in your Django Project **urls.py** file

.. code-block:: python

    from django.urls import path, include

    urlpatterns = [
        ...
        path('', include('admin_gradient.urls')),
    ]

Start the project now styled with the AdminLTE Design 

.. code-block:: bash
    :caption: Steps to start the project 

    python manage.py collectstatic
    python manage.py runserver # default port 8000    

Access the project in your preferred browser and the UI should be styled with the new design.

.. image:: https://user-images.githubusercontent.com/51070104/171583187-c4ca1bef-b535-458e-9250-8d62ba1f5b30.png
   :alt: Django Gradient Able - open-source Django Admin Theme built on top of Gradient Able Dashboard Design 

.. include::  /_templates/components/generator-django.rst
        
.. include::  /_templates/components/footer-links.rst
