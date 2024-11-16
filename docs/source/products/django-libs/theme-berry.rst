Admin Berry 
============

.. title:: Django Theme Berry  - Standalone Library for Ui and ADMIN Section     
.. meta::
    :description: Django Theme (UI and Admin Section) built on top of Berry Dashboard Design 
    :keywords: berry, django berry, django theme bootstrap, django ui library, berry dashboard, berry django, berry design, bootstrap 5 design  

Modern template for **Django Admin Section**, Auth Pages (registration included) crafted on top of **Berry Dashboard**, an open-source `Bootstrap 5` design.

- 👉 `Django Berry </product/berry-dashboard/django/>`__ - Product that uses the library 
- 👉 `Django Berry <https://django-berry.onrender.com/>`__ - LIVE Demo

.. include::  /_templates/components/signin-invite.rst

Features 
--------

- Design: `Berry Dashboard </docs/templates/bootstrap/berry-dashboard.html>`__ Bootstrap 5
- **Sections Covered**: 
    - `Admin Section`, reserved for `superusers`
    - `All pages` managed by `Django.contrib.AUTH`
    - `Registration` page
    - `Misc pages`: colors, icons, typography, blank-page 

.. image:: https://user-images.githubusercontent.com/51070104/215728710-d1ee7fef-8153-402b-9741-371e1c01cd36.png
   :alt: Django Berry Dashboard - open-source Django Admin Theme built on top of Berry Dashboard Design 


Why **Django Admin Berry** 
***************************

- Modern Bootstrap Design
- Responsive Interface
- Minimal Template overriding
- Easy integration


Installation 
------------

.. code-block:: bash

    $ pip install django-admin-berry
    // OR
    $ pip install git+https://github.com/app-generator/django-admin-berry.git

Add **admin_berry** application to the **INSTALLED_APPS Section** of your Django project **settings.py** file (note it should be before django.contrib.admin):

.. code-block:: python
    :caption: core/settings.py  

    INSTALLED_APPS = [
        ...
        'admin_berry.apps.AdminBerryConfig',
        'django.contrib.admin',
        ...
    ]

Add LOGIN_REDIRECT_URL and EMAIL_BACKEND of your Django project settings.py file:

.. code-block:: python
    :caption: core/settings.py  

    LOGIN_REDIRECT_URL = '/'
    # EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

Add **admin_berry** routing in your Django Project **urls.py** file

.. code-block:: python

    from django.urls import path, include

    urlpatterns = [
        ...
        path('', include('admin_berry.urls')),
    ]

Start the project now styled with the AdminLTE Design 

.. code-block:: bash
    :caption: Steps to start the project 

    python manage.py collectstatic
    python manage.py runserver # default port 8000    

Access the project in your preferred browser and the UI should be styled with the new design.

.. image:: https://user-images.githubusercontent.com/51070104/215728710-d1ee7fef-8153-402b-9741-371e1c01cd36.png
   :alt: Django Berry Dashboard - open-source Django Admin Theme built on top of Berry Dashboard Design 

.. include::  /_templates/components/footer-links.rst
