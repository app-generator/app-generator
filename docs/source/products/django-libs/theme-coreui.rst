Admin CoreUI 
============

.. title:: Django Theme CoreUI  - Standalone Library for Ui and ADMIN Section     
.. meta::
    :description: Django Theme (UI and Admin Section) built on top of CoreUI Dashboard Design 
    :keywords: coreui, django coreui, django theme bootstrap, django ui library, coreui dashboard, coreui django, coreui design, bootstrap 5 design  

Modern template for **Django Admin Section**, Auth Pages (registration included) crafted on top of **CoreUI Dashboard**, an open-source `Bootstrap 5` design.

- 👉 `Django CoreUI </product/coreui/django/>`__ - Product that uses the library 
- 👉 `Django CoreUI <https://django-coreui.appseed-srv1.com/>`__ - LIVE Demo

.. include::  /_templates/components/signin-invite.rst


Features 
--------

- Design: `CoreUI Dashboard </docs/templates/bootstrap/coreui.html>`__ Bootstrap 5
- **Sections Covered**: 
    - `Admin Section`, reserved for `superusers`
    - `All pages` managed by `Django.contrib.AUTH`
    - `Registration` page
    - `Misc pages`: colors, icons, typography, blank-page 


Why **Django Admin CoreUI** 
***************************

- Modern Bootstrap Design
- Responsive Interface
- Minimal Template overriding
- Easy integration


Installation 
------------

.. code-block:: bash

    $ pip install django-admin-coreui
    // OR
    $ pip install git+https://github.com/app-generator/django-admin-coreui.git

Add **admin_coreui** application to the **INSTALLED_APPS Section** of your Django project **settings.py** file (note it should be before django.contrib.admin):

.. code-block:: python
    :caption: core/settings.py  

    INSTALLED_APPS = [
        ...
        'admin_coreui.apps.AdminCoreuiConfig',
        'django.contrib.admin',
        ...
    ]

Add LOGIN_REDIRECT_URL and EMAIL_BACKEND of your Django project settings.py file:

.. code-block:: python
    :caption: core/settings.py  

    LOGIN_REDIRECT_URL = '/'
    # EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

Add **admin_coreui** routing in your Django Project **urls.py** file

.. code-block:: python

    from django.urls import path, include

    urlpatterns = [
        ...
        path('', include('admin_coreui.urls')),
    ]

Start the project now styled with the AdminLTE Design 

.. code-block:: bash
    :caption: Steps to start the project 

    python manage.py collectstatic
    python manage.py runserver # default port 8000    

Access the project in your preferred browser and the UI should be styled with the new design.

.. image:: https://user-images.githubusercontent.com/51070104/171336361-b125ca1d-8936-4f4a-b662-9e45ee25f404.png
   :alt: Django CoreUI Dashboard - open-source Django Admin Theme built on top of CoreUI Dashboard Design 

.. include::  /_templates/components/footer-links.rst
