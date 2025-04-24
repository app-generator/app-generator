`Volt Dashboard </product/volt-dashboard/>`__ Library 
=====================================================

.. title:: Django Theme Volt  - Standalone Library for Ui and ADMIN Section     
.. meta::
    :description: Django Theme (UI and Admin Section) built on top of Volt Dashboard Design 
    :keywords: django bootstrap 5, django theme bootstrap, django ui library, volt dashboard, volt django, volt design, bootstrap 5 design  

Modern template for **Django Admin Section**, Auth Pages (registration included) crafted on top of **Volt Dashboard**, an open-source `Bootstrap 5` design.

- 👉 `Django Volt Dashboard </product/volt-dashboard/django/>`__ - Product that uses the library 
- 👉 `Django Volt Dashboard <https://django-volt.onrender.com/>`__ - LIVE Demo

.. include::  /_templates/components/signin-invite.rst

Features 
--------

- Design: `Volt Dashboard </product/volt-dashboard/>`__ Bootstrap 5
- **Sections Covered**: 
    - `All pages` managed by `Django.contrib.AUTH`
    - `Registration` page
    - `Misc pages`: colors, icons, typography, blank-page 

.. image:: https://user-images.githubusercontent.com/51070104/168843604-b026fd94-5969-4be7-81ac-5887cf0958e5.png
   :alt: Django Volt Dashboard - open-source Django Admin Theme built on top of Volt Dashboard Design 
   
Why **Django Admin Volt** 
*************************

- Modern Bootstrap 5 Design
- Responsive Interface
- Minimal Template overriding
- Easy integration


Installation 
------------

.. code-block:: bash

    $ pip install django-admin-volt
    // OR
    $ pip install git+https://github.com/app-generator/django-admin-volt.git

Add **admin_volt** application to the **INSTALLED_APPS Section** of your Django project **settings.py** file (note it should be before django.contrib.admin):

.. code-block:: python
    :caption: core/settings.py  

    INSTALLED_APPS = [
        ...
        'admin_volt.apps.AdminVoltConfig',
        'django.contrib.admin',
        ...
    ]

Add LOGIN_REDIRECT_URL and EMAIL_BACKEND of your Django project settings.py file:

.. code-block:: python
    :caption: core/settings.py  

    LOGIN_REDIRECT_URL = '/'
    # EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

Add **admin_volt** routing in your Django Project **urls.py** file

.. code-block:: python

    from django.urls import path, include

    urlpatterns = [
        ...
        path('', include('admin_volt.urls')),
    ]

Start the project now styled with the AdminLTE Design 

.. code-block:: bash
    :caption: Steps to start the project 

    python manage.py collectstatic
    python manage.py runserver # default port 8000    

Access the project in your preferred browser and the UI should be styled with the new design.

.. image:: https://user-images.githubusercontent.com/51070104/168843604-b026fd94-5969-4be7-81ac-5887cf0958e5.png
   :alt: Django Volt Dashboard - open-source Django Admin Theme built on top of Volt Dashboard Design 

.. include::  /_templates/components/generator-django.rst
        
.. include::  /_templates/components/footer-links.rst
