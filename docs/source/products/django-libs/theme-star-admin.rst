Star Admin Library
==================

.. title:: Django Theme StarAdmin  - Standalone library for Ui and ADMIN Section     
.. meta::
    :description: Django Theme (UI and Admin Section) built on top of StarAdmin Design    
    :keywords: django, django theme, django ui library, starAdmin, starAdmin django, starAdmin design  

**Django StarAdmin** is a standalone library for UI and Django ADMIN Section.

.. include::  /_templates/components/signin-invite.rst

Features 
--------

- Design: `Star Admin </docs/templates/bootstrap/staradmin.html>`__ Bootstrap
- **Sections Covered**: 
    - `Admin Section`, reserved for `superusers`
    - `All pages` managed by `Django.contrib.AUTH`
    - `Registration` page
    - `Misc pages`: colors, icons, typography, blank-page 

.. image:: https://user-images.githubusercontent.com/51070104/168732392-51748c85-f2c2-45ad-978c-2b64e52292e2.png
   :alt: Homepage Django StarAdmin - open-source starter built on top of StarAdmin Design 

Why **Django StarAdmin** 
***************************

- Modern Bootstrap Design
- Responsive Interface
- Minimal Template overriding
- Easy integration


Installation 
------------

.. code-block:: bash

    pip install django-admin-star
    // OR 
    pip install git+https://github.com/app-generator/django-admin-star.git

Add **admin_star** application to the **INSTALLED_APPS Section** of your Django project **settings.py** file (note it should be before django.contrib.admin):

.. code-block:: python
    :caption: core/settings.py  

    INSTALLED_APPS = [
        ...
        'admin_star.apps.AdminStarConfig',
        'django.contrib.admin',
        ...
    ]

Add LOGIN_REDIRECT_URL and EMAIL_BACKEND of your Django project settings.py file:

.. code-block:: python
    :caption: core/settings.py  

    LOGIN_REDIRECT_URL = '/'
    # EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

Add **admin_star** routing in your Django Project **urls.py** file

.. code-block:: python

    from django.urls import path, include

    urlpatterns = [
        ...
        path('', include('admin_star.urls')),
    ]

Start the project now styled with the AdminLTE Design 

.. code-block:: bash
    :caption: Steps to start the project 

    python manage.py collectstatic
    python manage.py runserver # default port 8000    

Access the project in your preferred browser and the UI should be styled with the new design.

.. image:: https://user-images.githubusercontent.com/51070104/168732392-51748c85-f2c2-45ad-978c-2b64e52292e2.png
   :alt: Homepage Django StarAdmin - open-source starter built on top of StarAdmin Design 

.. include::  /_templates/components/generator-django.rst
        
.. include::  /_templates/components/footer-links.rst

