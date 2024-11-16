Admin Modernize 
===============

.. title:: Django Theme Modernize - Standalone Library for Ui and ADMIN Section     
.. meta::
    :description: Django Theme (UI and Admin Section) built on top of Modernize BS5 Design 
    :keywords: modernize design, django modernize, django material ui library, material dashboard modernize

Modern template for **Django Admin Section**, Auth Pages (registration included) crafted on top of **Modernize Dashboard**, an open-source `Bootstrap 5` design.

.. include::  /_templates/components/signin-invite.rst

Features 
--------

- Design: Modernize Bootstrap 5
- **Sections Covered**: 
    - `Admin Section`, reserved for `superusers`
    - `All pages` managed by `Django.contrib.AUTH`
    - `Registration` page
    - `Misc pages`: colors, icons, typography, blank-page 

.. image:: https://github.com/user-attachments/assets/afdb4417-1aa0-4cdd-9929-2f1efc7c18a4
   :alt: Django Modernize - open-source Django Admin Theme built on top of Modernize Design from AdminMart

Why **Django Modernize** 
*****************************

- Modern Bootstrap 5 Design
- Responsive Interface
- Minimal Template overriding
- Easy integration


Installation 
------------

.. code-block:: bash

    $ pip install django-admin-modernize
    // OR
    $ pip install git+https://github.com/app-generator/django-admin-modernize.git

Add **admin_modernize** application to the **INSTALLED_APPS Section** of your Django project **settings.py** file (note it should be before django.contrib.admin):

.. code-block:: python
    :caption: core/settings.py  

    INSTALLED_APPS = [
        ...
        'admin_modernize.apps.AdminModernizeConfig',
        'django.contrib.admin',
        ...
    ]

Add LOGIN_REDIRECT_URL and EMAIL_BACKEND of your Django project settings.py file:

.. code-block:: python
    :caption: core/settings.py  

    LOGIN_REDIRECT_URL = '/'
    # EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

Add **admin_modernize** routing in your Django Project **urls.py** file

.. code-block:: python

    from django.urls import path, include

    urlpatterns = [
        ...
        path('', include('admin_modernize.urls')),
    ]

Start the project now styled with the AdminLTE Design 

.. code-block:: bash
    :caption: Steps to start the project 

    python manage.py collectstatic
    python manage.py runserver # default port 8000    

Access the project in your preferred browser and the UI should be styled with the new design.

.. image:: https://github.com/user-attachments/assets/afdb4417-1aa0-4cdd-9929-2f1efc7c18a4
   :alt: Django Modernize - open-source Django Admin Theme built on top of Modernize Design from AdminMart

.. include::  /_templates/components/footer-links.rst
