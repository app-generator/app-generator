Admin Material 
==============

.. title:: Django Theme Material Dashboard   - Standalone Library for Ui and ADMIN Section     
.. meta::
    :description: Django Theme (UI and Admin Section) built on top of Material Dashboard Design 
    :keywords: django bootstrap, django dark theme, django material ui library, material dashboard, django admin panel, material dashboard design, bootstrap 5 design  

Modern template for **Django Admin Section**, Auth Pages (registration included) crafted on top of **Material Dashboard**, an open-source `Bootstrap` design.

- 👉 `Django Material Dashboard </product/material-dashboard/django/>`__ - Product that uses the library 
- 👉 `Django Material Dashboard <https://django-material-dash2.onrender.com/>`__ - LIVE Demo

.. include::  /_templates/components/signin-invite.rst

Features 
--------

- Design: `Material Dashboard </docs/templates/bootstrap/material-dashboard.html>`__ Bootstrap
- **Sections Covered**: 
    - `Admin Section`, reserved for `superusers`
    - `All pages` managed by `Django.contrib.AUTH`
    - `Registration` page
    - `Misc pages`: colors, icons, typography, blank-page 

.. image:: https://github.com/user-attachments/assets/dba1a100-3309-400c-99bc-6ba707697509
   :alt: Django Material Dashboard - open-source Django Admin Theme built on top of Material Dashboard Design from Creative-Tim

Why **Django Admin Material** 
*****************************

- Modern Bootstrap Design
- Responsive Interface
- Minimal Template overriding
- Easy integration


Installation 
------------

.. code-block:: bash

    $ pip install django-admin-material-dashboard
    // OR
    $ pip install git+https://github.com/app-generator/django-admin-material-dashboard.git

Add **admin_material** application to the **INSTALLED_APPS Section** of your Django project **settings.py** file (note it should be before django.contrib.admin):

.. code-block:: python
    :caption: core/settings.py  

    INSTALLED_APPS = [
        ...
        'admin_material.apps.AdminMaterialDashboardConfig',
        'django.contrib.admin',
        ...
    ]

Add LOGIN_REDIRECT_URL and EMAIL_BACKEND of your Django project settings.py file:

.. code-block:: python
    :caption: core/settings.py  

    LOGIN_REDIRECT_URL = '/'
    # EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

Add **admin_material** routing in your Django Project **urls.py** file

.. code-block:: python

    from django.urls import path, include

    urlpatterns = [
        ...
        path('', include('admin_material.urls')),
    ]

Start the project now styled with the AdminLTE Design 

.. code-block:: bash
    :caption: Steps to start the project 

    python manage.py collectstatic
    python manage.py runserver # default port 8000    

Access the project in your preferred browser and the UI should be styled with the new design.

.. image:: https://github.com/user-attachments/assets/dba1a100-3309-400c-99bc-6ba707697509
   :alt: Django Material Dashboard - open-source Django Admin Theme built on top of Black Dashboard Design from Creative-Tim

.. include::  /_templates/components/generator-django.rst
        
.. include::  /_templates/components/footer-links.rst
