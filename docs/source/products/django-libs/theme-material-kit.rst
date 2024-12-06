Material Kit
============

.. title:: Django Theme Material Kit - UI Library for Django with Material Design      
.. meta::
    :description: Django Ui Theme built on top of Material Kit Design 
    :keywords: material kit, material design, django material kit, django material theme, django material ui library, bootstrap material design  
 
Modern UI Library for **Django**, Auth Pages (registration included) crafted on top of **Material UI Kit**, an open-source `Bootstrap` design.

- 👉 `Django Material Kit </product/material-kit/django/>`__ - Product that uses the library 
- 👉 `Django Material Kit <https://django-mkit.onrender.com>`__ - LIVE Demo

.. include::  /_templates/components/signin-invite.rst

Features 
--------

- Design: `Material Kit </docs/templates/bootstrap/material-kit.html>`__ Bootstrap
- **Sections Covered**: 
    - `All pages` managed by `Django.contrib.AUTH`
    - `Registration` page
    - `Misc pages`: colors, icons, typography, blank-page 

.. image:: https://github.com/user-attachments/assets/d83d18dd-b147-4fcb-ba3a-cc4926c6d536
   :alt: Material Kit - open-source dashboard template provided by Creative-Tim 

Why **Django Material Kit** 
*****************************

- Modern Bootstrap 5 Design
- Responsive Interface
- Minimal Template overriding
- Easy integration


Installation 
------------

.. code-block:: bash

    $ pip install django-theme-material-kit
    // OR
    $ pip install git+https://github.com/app-generator/django-theme-material-kit.git

Add **theme_material_kit** application to the **INSTALLED_APPS Section** of your Django project **settings.py** file:

.. code-block:: python
    :caption: core/settings.py  

    INSTALLED_APPS = [
        "django.contrib.admin",
        "django.contrib.auth",
        "django.contrib.contenttypes",
        "django.contrib.sessions",
        "django.contrib.messages",
        "django.contrib.staticfiles",

        'theme_material_kit',          # <-- NEW 
    ]

Add LOGIN_REDIRECT_URL and EMAIL_BACKEND of your Django project settings.py file:

.. code-block:: python
    :caption: core/settings.py  

    LOGIN_REDIRECT_URL = '/'
    # EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

Add **theme_material_kit** routing in your Django Project **urls.py** file

.. code-block:: python

    from django.urls import path, include

    urlpatterns = [
        ...
        path('', include('theme_material_kit.urls')),  #  <-- NEW
    ]

Start the project now styled with the AdminLTE Design 

.. code-block:: bash
    :caption: Steps to start the project 

    python manage.py collectstatic
    python manage.py runserver # default port 8000    

Access the project in your preferred browser and the UI should be styled with the new design.

.. image:: https://github.com/user-attachments/assets/d83d18dd-b147-4fcb-ba3a-cc4926c6d536
   :alt: Material Kit - open-source dashboard template provided by Creative-Tim 

.. include::  /_templates/components/footer-links.rst
