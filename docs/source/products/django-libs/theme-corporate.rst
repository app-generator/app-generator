Admin Corporate  
===============

.. title:: Django Theme Corporate Dashboard   - Standalone Library for Ui and ADMIN Section     
.. meta::
    :description: Django Theme (UI and Admin Section) built on top of Corporate Dashboard Design 
    :keywords: corporate ui bootstrap, corporate dashboard, django corporate ui, corporate django template, corporate django admin

Modern template for **Django Admin Section**, Auth Pages (registration included) crafted on top of **Corporate Dashboard**, an open-source `Bootstrap` design.

- 👉 `Django Corporate Dashboard </product/corporate-dashboard/django/>`__ - Product that uses the library 
- 👉 Get `Support </ticket/create/>`__ via Email and Discord

.. include::  /_templates/components/signin-invite.rst

Features 
--------

- Design: `Corporate Dashboard </docs/templates/bootstrap/corporate-dashboard.html>`__ Bootstrap
- **Sections Covered**: 
    - `Admin Section`, reserved for `superusers`
    - `All pages` managed by `Django.contrib.AUTH`
    - `Registration` page
    - `Misc pages`: colors, icons, typography, blank-page 

.. image:: https://github.com/user-attachments/assets/55f27009-2e46-433c-b2bc-4c0db1cd6c17
   :alt: Django Corporate Dashboard - open-source Django Admin Theme built on top of Black Dashboard Design from Creative-Tim

Why **Django Admin Corporate** 
******************************

- Modern Bootstrap Design
- Responsive Interface
- Minimal Template overriding
- Easy integration


Installation 
------------

.. code-block:: bash

    $ pip install django-admin-corporate
    // OR
    $ pip install git+https://github.com/app-generator/django-admin-corporate.git

Add **admin_corporate** application to the **INSTALLED_APPS Section** of your Django project **settings.py** file (note it should be before django.contrib.admin):

.. code-block:: python
    :caption: core/settings.py  

    INSTALLED_APPS = [
        ...
        'admin_corporate.apps.AdminCorporateConfig',
        'django.contrib.admin',
        ...
    ]

Add LOGIN_REDIRECT_URL and EMAIL_BACKEND of your Django project settings.py file:

.. code-block:: python
    :caption: core/settings.py  

    LOGIN_REDIRECT_URL = '/'
    # EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

Add **admin_corporate** routing in your Django Project **urls.py** file

.. code-block:: python

    from django.urls import path, include

    urlpatterns = [
        ...
        path('', include('admin_corporate.urls')),
    ]

Start the project now styled with the AdminLTE Design 

.. code-block:: bash
    :caption: Steps to start the project 

    python manage.py collectstatic
    python manage.py runserver # default port 8000    

Access the project in your preferred browser and the UI should be styled with the new design.

.. image:: https://github.com/user-attachments/assets/55f27009-2e46-433c-b2bc-4c0db1cd6c17
   :alt: Django Corporate Dashboard - open-source Django Admin Theme built on top of Black Dashboard Design from Creative-Tim

.. include::  /_templates/components/generator-django.rst
        
.. include::  /_templates/components/footer-links.rst
