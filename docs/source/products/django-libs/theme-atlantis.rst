Admin Atlantis 
==============

.. title:: Django Theme Atlantis  - Standalone Library for Ui and ADMIN Section     
.. meta::
    :description: Django Theme (UI and Admin Section) built on top of Atlantis Dashboard Design 
    :keywords: atlantis, django atlantis, django theme bootstrap, django ui library, atlantis dashboard, atlantis django, atlantis design, bootstrap 5 design  

Modern template for **Django Admin Section**, Auth Pages (registration included) crafted on top of **Atlantis Dashboard**, an open-source `Bootstrap` design.

- 👉 `Django Atlantis </product/atlantis-dark/django/>`__ - Product that uses the library 
- 👉 `Django Atlantis <https://django-atlantis-dark.appseed-srv1.com/>`__ - LIVE Demo

.. include::  /_templates/components/signin-invite.rst

Features 
--------

- Design: Atlantis Dashboard (Bootstrap) 
- **Sections Covered**: 
    - `Admin Section`, reserved for `superusers`
    - `All pages` managed by `Django.contrib.AUTH`
    - `Registration` page
    - `Misc pages`: colors, icons, typography, blank-page 

.. image:: https://user-images.githubusercontent.com/51070104/172799909-4cbc8eed-fdde-4408-ab61-123f235212d0.png
   :alt: Django Atlantis Dashboard - open-source Django Admin Theme built on top of Atlantis Dashboard Design 


Why **Django Admin Atlantis** 
*****************************

- Modern Bootstrap Design
- Responsive Interface
- Minimal Template overriding
- Easy integration


Installation 
------------

.. code-block:: bash

    $ pip install django-admin-atlantis
    // OR
    $ pip install git+https://github.com/app-generator/django-admin-atlantis.git

Add **admin_atlantis** application to the **INSTALLED_APPS Section** of your Django project **settings.py** file (note it should be before django.contrib.admin):

.. code-block:: python
    :caption: core/settings.py  

    INSTALLED_APPS = [
        ...
        'admin_atlantis.apps.AdminAtlantisConfig',
        'django.contrib.admin',
        ...
    ]

Add LOGIN_REDIRECT_URL and EMAIL_BACKEND of your Django project settings.py file:

.. code-block:: python
    :caption: core/settings.py  

    LOGIN_REDIRECT_URL = '/'
    # EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

Add **admin_atlantis** routing in your Django Project **urls.py** file

.. code-block:: python

    from django.urls import path, include

    urlpatterns = [
        ...
        path('', include('admin_atlantis.urls')),
    ]

Start the project now styled with the AdminLTE Design 

.. code-block:: bash
    :caption: Steps to start the project 

    python manage.py collectstatic
    python manage.py runserver # default port 8000    

Access the project in your preferred browser and the UI should be styled with the new design.

.. image:: https://user-images.githubusercontent.com/51070104/172799909-4cbc8eed-fdde-4408-ab61-123f235212d0.png
   :alt: Django Atlantis Dashboard - open-source Django Admin Theme built on top of Atlantis Dashboard Design 

.. include::  /_templates/components/footer-links.rst
