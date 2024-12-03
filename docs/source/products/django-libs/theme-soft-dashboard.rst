Admin Soft
==========

.. title:: Django Theme Soft Dashboard   - Standalone Library for Ui and ADMIN Section     
.. meta::
    :description: Django Theme (UI and Admin Section) built on top of Soft Dashboard Design 
    :keywords: django bootstrap, django dark theme, django soft ui library, soft dashboard, dark dashboard django, soft dashboard design, bootstrap design  

Modern template for **Django Admin Section**, Auth Pages (registration included) crafted on top of **Soft Dashboard**, an open-source `Bootstrap` design.

- 👉 `Django Soft Dashboard </product/soft-ui-dashboard/django/>`__ - Product that uses the library 
- 👉 `Django Soft Dashboard <https://django-soft-dash.onrender.com/>`__ - LIVE Demo

.. include::  /_templates/components/signin-invite.rst

Features 
--------

- Design: `Soft UI Dashboard </docs/templates/bootstrap/soft-ui-dashboard.html>`__ Bootstrap
- **Sections Covered**: 
    - `Admin Section`, reserved for `superusers`
    - `All pages` managed by `Django.contrib.AUTH`
    - `Registration` page
    - `Misc pages`: colors, icons, typography, blank-page 

.. image:: https://github.com/user-attachments/assets/2dd7adf3-bf5f-4894-b585-3696e7a8606f
   :alt: Django Soft Dashboard - open-source Django Admin Theme built on top of Soft Dashboard Design from Creative-Tim

Why **Django Admin Soft** 
*************************

- Modern Bootstrap Design
- Responsive Interface
- Minimal Template overriding
- Easy integration


Installation 
------------

.. code-block:: bash

    $ pip install django-admin-soft-dashboard
    // OR
    $ pip install git+https://github.com/app-generator/django-admin-soft-dashboard.git

Add **admin_soft** application to the **INSTALLED_APPS Section** of your Django project **settings.py** file (note it should be before django.contrib.admin):

.. code-block:: python
    :caption: core/settings.py  

    INSTALLED_APPS = [
        ...
        'admin_soft.apps.AdminSoftDashboardConfig',
        'django.contrib.admin',
        ...
    ]

Add LOGIN_REDIRECT_URL and EMAIL_BACKEND of your Django project settings.py file:

.. code-block:: python
    :caption: core/settings.py  

    LOGIN_REDIRECT_URL = '/'
    # EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

Add **admin_soft** routing in your Django Project **urls.py** file

.. code-block:: python

    from django.urls import path, include

    urlpatterns = [
        ...
        path('', include('admin_soft.urls')),
    ]

Start the project now styled with the AdminLTE Design 

.. code-block:: bash
    :caption: Steps to start the project 

    python manage.py collectstatic
    python manage.py runserver # default port 8000    

Access the project in your preferred browser and the UI should be styled with the new design.

.. image:: https://github.com/user-attachments/assets/2dd7adf3-bf5f-4894-b585-3696e7a8606f
   :alt: Django Soft Dashboard - open-source Django Admin Theme built on top of Soft Dashboard Design from Creative-Tim

.. include::  /_templates/components/footer-links.rst
