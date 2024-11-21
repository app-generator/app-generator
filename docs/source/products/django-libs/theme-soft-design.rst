Soft Design
===========

.. title:: Django Soft Design - UI Library for Django with Soft UI Design      
.. meta::
    :description: Django Ui Theme built on top of Soft UI Design 
    :keywords: soft ui desgin, soft design, django soft design, django soft ui theme, django soft ui library, bootstrap soft design  
 
Modern UI Library for **Django**, Auth Pages (registration included) crafted on top of **Soft UI Design**, an open-source `Bootstrap` design.

- 👉 `Django Soft Design </product/soft-ui-design/django/>`__ - Product that uses the library 
- 👉 `Django Soft Design <https://django-soft-ui-free.appseed-srv1.com/>`__ - LIVE Demo

.. include::  /_templates/components/signin-invite.rst

Features 
--------

- Design: `Soft UI Design </docs/templates/bootstrap/soft-ui-design.html>`__ Bootstrap
- **Sections Covered**: 
    - `All pages` managed by `Django.contrib.AUTH`
    - `Registration` page
    - `Misc pages`: colors, icons, typography, blank-page 

.. image:: https://github.com/user-attachments/assets/ce56cfce-5194-4409-af80-097fc4492589
   :alt: Soft UI Design - open-source UI Kit template provided by Creative-Tim 

Why **Django Material Kit** 
*****************************

- Modern Bootstrap 5 Design
- Responsive Interface
- Minimal Template overriding
- Easy integration


Installation 
------------

.. code-block:: bash

    $ pip install django-theme-soft-design
    // OR
    $ pip install git+https://github.com/app-generator/django-theme-soft-design.git

Add **theme_soft_design** application to the **INSTALLED_APPS Section** of your Django project **settings.py** file:

.. code-block:: python
    :caption: core/settings.py  

    INSTALLED_APPS = [
        "django.contrib.admin",
        "django.contrib.auth",
        "django.contrib.contenttypes",
        "django.contrib.sessions",
        "django.contrib.messages",
        "django.contrib.staticfiles",

        'theme_soft_design',          # <-- NEW 
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
        path('', include('theme_soft_design.urls')),  #  <-- NEW
    ]

Start the project now styled with the AdminLTE Design 

.. code-block:: bash
    :caption: Steps to start the project 

    python manage.py collectstatic
    python manage.py runserver # default port 8000    

Access the project in your preferred browser and the UI should be styled with the new design.

.. image:: https://github.com/user-attachments/assets/ce56cfce-5194-4409-af80-097fc4492589
   :alt: Soft UI Design - open-source UI Kit template provided by Creative-Tim 

.. include::  /_templates/components/footer-links.rst
