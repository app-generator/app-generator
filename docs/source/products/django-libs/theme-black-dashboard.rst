Admin Black
===========

.. title:: Django Theme Black Dashboard   - Standalone Library for Ui and ADMIN Section     
.. meta::
    :description: Django Theme (UI and Admin Section) built on top of Black Dashboard Design 
    :keywords: django bootstrap, django dark theme, django black ui library, black dashboard, dark dashboard django, black dashboard design, bootstrap design  

Modern template for **Django Admin Section**, Auth Pages (registration included) crafted on top of **Black Dashboard**, an open-source `Bootstrap` design.

- 👉 `Django Black Dashboard </product/black-dashboard/django/>`__ - Product that uses the library 
- 👉 `Django Black Dashboard <https://django-black-dashboard.appseed-srv1.com/>`__ - LIVE Demo

.. include::  /_templates/components/signin-invite.rst

Features 
--------

- Design: `Black Dashboard </docs/templates/bootstrap/black-dashboard.html>`__ Bootstrap
- **Sections Covered**: 
    - `Admin Section`, reserved for `superusers`
    - `All pages` managed by `Django.contrib.AUTH`
    - `Registration` page
    - `Misc pages`: colors, icons, typography, blank-page 

.. image:: https://user-images.githubusercontent.com/51070104/196730732-dda1794b-93ce-48cb-bc5c-182411495512.png
   :alt: Django Black Dashboard - open-source Django Admin Theme built on top of Black Dashboard Design from Creative-Tim

Why **Django Black Material** 
*****************************

- Modern Bootstrap Design
- Responsive Interface
- Minimal Template overriding
- Easy integration


Installation 
------------

.. code-block:: bash

    $ pip install django-admin-black
    // OR
    $ pip install git+https://github.com/app-generator/django-admin-black.git

Add **admin_black** application to the **INSTALLED_APPS Section** of your Django project **settings.py** file (note it should be before django.contrib.admin):

.. code-block:: python
    :caption: core/settings.py  

    INSTALLED_APPS = [
        ...
        'admin_black.apps.AdminBlackConfig',
        'django.contrib.admin',
        ...
    ]

Add LOGIN_REDIRECT_URL and EMAIL_BACKEND of your Django project settings.py file:

.. code-block:: python
    :caption: core/settings.py  

    LOGIN_REDIRECT_URL = '/'
    # EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

Add **admin_black** routing in your Django Project **urls.py** file

.. code-block:: python

    from django.urls import path, include

    urlpatterns = [
        ...
        path('', include('admin_black.urls')),
    ]

Start the project now styled with the AdminLTE Design 

.. code-block:: bash
    :caption: Steps to start the project 

    python manage.py collectstatic
    python manage.py runserver # default port 8000    

Access the project in your preferred browser and the UI should be styled with the new design.

.. image:: https://user-images.githubusercontent.com/51070104/196730732-dda1794b-93ce-48cb-bc5c-182411495512.png
   :alt: Django Black Dashboard - open-source Django Admin Theme built on top of Black Dashboard Design from Creative-Tim

.. include::  /_templates/components/footer-links.rst
